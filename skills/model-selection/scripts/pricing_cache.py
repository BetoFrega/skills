#!/usr/bin/env python3
"""Read local model prices or explicitly refresh Codex Standard credit rates."""

import argparse
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from html.parser import HTMLParser
import json
import math
import os
from pathlib import Path
import re
import sys
import tempfile
from urllib.request import Request, urlopen


SOURCE_URL = "https://learn.chatgpt.com/docs/pricing.md"
DEFAULT_CACHE = Path.home() / ".agents" / "model-pricing.json"
CARD_KEY = ("openai", "codex_paid_credits", "standard")


class Table(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows = []
        self.row = []
        self.cell = None

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.row = []
        elif tag in ("td", "th"):
            self.cell = []

    def handle_data(self, data):
        if self.cell is not None:
            self.cell.append(data)

    def handle_endtag(self, tag):
        if tag in ("td", "th") and self.cell is not None:
            self.row.append(" ".join("".join(self.cell).split()))
            self.cell = None
        elif tag == "tr":
            self.rows.append(self.row)


def parse_rates(markdown):
    heading = re.search(r"(?m)^#### Token rates\s*$", markdown)
    if heading is None:
        raise ValueError("Official token-rate heading was not found")
    section = markdown[heading.end():]
    section = re.split(r"(?m)^#{1,4} ", section, maxsplit=1)[0]
    if "Standard speed" not in section or "credits per million" not in section:
        raise ValueError("Expected Standard credit-rate units were not found")
    tables = re.findall(r"<table\b[^>]*>.*?</table>", section, re.S)
    if len(tables) != 1:
        raise ValueError("Expected one complete token-rate table")
    table = Table()
    table.feed(tables[0])
    expected_header = ["Credits per 1M tokens", "Input Tokens", "Cached input tokens", "Output Tokens"]
    if not table.rows or table.rows[0] != expected_header:
        raise ValueError("Official credit-rate columns changed")
    models = {}
    for row in table.rows[1:]:
        if not row:
            continue
        label = row[0]
        if label in ("Daybreak Blue", "Daybreak Red"):
            model = "gpt-daybreak-" + label.split()[1].lower() + "-latest"
        elif re.fullmatch(r"GPT-[A-Za-z0-9.-]+(?: [A-Za-z0-9]+)*", label):
            model = label.lower().replace(" ", "-")
        else:
            continue
        if len(row) != 4 or model in models:
            raise ValueError("Incomplete or duplicate model rate row: " + label)
        rates = {}
        for key, cell in zip(("input", "cached_input", "output"), row[1:]):
            match = re.fullmatch(r"(\d+(?:\.\d+)?|\d{1,3}(?:,\d{3})+(?:\.\d+)?) credits", cell)
            if match is None:
                raise ValueError("Invalid credit rate: " + cell)
            value = Decimal(match.group(1).replace(",", ""))
            rates[key] = float(value)
        models[model] = rates
    if not models:
        raise ValueError("No model rates were extracted")
    return models


def load_cache(path):
    return validate_cache(json.loads(path.read_text()))


def validate_cache(data):
    if not isinstance(data, dict) or data.get("schema_version") != 1 or not isinstance(data.get("rate_cards"), list):
        raise ValueError("Unsupported pricing cache structure")
    seen = set()
    for card in data["rate_cards"]:
        if not isinstance(card, dict):
            raise ValueError("Invalid rate card")
        for field in ("provider", "billing_surface", "speed_mode", "unit", "source_url", "checked_at"):
            if not isinstance(card.get(field), str) or not card[field]:
                raise ValueError("Missing rate-card field: " + field)
        timestamp = datetime.fromisoformat(card["checked_at"].replace("Z", "+00:00"))
        if timestamp.tzinfo is None:
            raise ValueError("checked_at must include its timezone")
        key = key_for(card)
        if key == CARD_KEY and card["unit"] != "credits_per_million_tokens":
            raise ValueError("Codex credit-rate units are incompatible")
        if key in seen:
            raise ValueError("Duplicate rate card")
        seen.add(key)
        if not isinstance(card.get("models"), dict) or not card["models"]:
            raise ValueError("A rate card must contain model rates")
        for model, rates in card["models"].items():
            if not model or not isinstance(rates, dict):
                raise ValueError("Invalid model rates")
            for field in ("input", "cached_input", "output"):
                value = rates.get(field)
                if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
                    raise ValueError("Invalid numeric rate for " + model + ": " + field)
    return data


def key_for(card):
    return tuple(card.get(key) for key in ("provider", "billing_surface", "speed_mode"))


def prepare_refresh(path):
    empty = {"schema_version": 1, "rate_cards": []}
    if not path.exists():
        return empty, None
    raw = path.read_bytes()
    parsed = None
    try:
        parsed = json.loads(raw)
        return validate_cache(parsed), None
    except (ValueError, TypeError, KeyError, OverflowError):
        recovered = empty
        if isinstance(parsed, dict) and parsed.get("schema_version") == 1 and isinstance(parsed.get("rate_cards"), list):
            recovered = dict(parsed, rate_cards=[])
            seen = set()
            for item in parsed["rate_cards"]:
                try:
                    validate_cache({"schema_version": 1, "rate_cards": [item]})
                except (ValueError, TypeError, KeyError, OverflowError):
                    continue
                key = key_for(item)
                if key != CARD_KEY and key not in seen:
                    recovered["rate_cards"].append(item)
                    seen.add(key)
        return recovered, raw


def refresh(path):
    request = Request(SOURCE_URL, headers={"User-Agent": "model-selection-cache/1.0"})
    with urlopen(request, timeout=30) as response:
        models = parse_rates(response.read().decode("utf-8"))
    card = dict(zip(("provider", "billing_surface", "speed_mode"), CARD_KEY))
    card.update(unit="credits_per_million_tokens", source_url=SOURCE_URL,
                checked_at=datetime.now(timezone.utc).isoformat(), models=models)
    data, invalid_bytes = prepare_refresh(path)
    data["rate_cards"] = [item for item in data["rate_cards"] if key_for(item) != CARD_KEY] + [card]
    validate_cache(data)
    content = json.dumps(data, indent=2, allow_nan=False) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    backup = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", dir=path.parent, encoding="utf-8", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(content)
        if invalid_bytes is not None:
            with tempfile.NamedTemporaryFile(mode="wb", dir=path.parent, prefix=path.name + ".invalid-",
                                             suffix=".bak", delete=False) as handle:
                backup = Path(handle.name)
                handle.write(invalid_bytes)
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()
    result = {"cache": str(path), "checked_at": card["checked_at"], "model_count": len(models)}
    if backup is not None:
        result["backup"] = str(backup)
    return result


def show(path, model_names):
    data = load_cache(path)
    cards = [card for card in data["rate_cards"] if key_for(card) == CARD_KEY]
    if len(cards) != 1:
        raise ValueError("Expected one Codex Standard credit-rate card")
    card = dict(cards[0])
    rates = card["models"]
    selected = model_names or list(rates)
    card["models"] = {model: rates[model] for model in selected if model in rates}
    return {"rate_card": card, "missing_models": [model for model in selected if model not in rates]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("refresh", help="Explicitly download and update the Standard credit-rate card")
    read = commands.add_parser("show", help="Read cached rates without network access")
    read.add_argument("models", nargs="*")
    args = parser.parse_args()
    try:
        path = args.cache.expanduser()
        result = refresh(path) if args.command == "refresh" else show(path, args.models)
        print(json.dumps(result, separators=(",", ":"), allow_nan=False))
    except (OSError, ValueError, KeyError, TypeError, InvalidOperation) as error:
        print("Pricing cache: " + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
