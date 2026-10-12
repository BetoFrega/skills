import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import MagicMock, patch


script = Path(__file__).resolve().parents[1] / "scripts" / "pricing_cache.py"
spec = importlib.util.spec_from_file_location("pricing_cache", script)
cache = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cache)

SOURCE = """#### Token rates
Standard speed, credits per million tokens.
<table><thead><tr><th>Credits per 1M tokens</th><th>Input Tokens</th>
<th>Cached input tokens</th><th>Output Tokens</th></tr></thead><tbody>
<tr><td>GPT-6.1 Sol</td><td>50 credits</td><td>2.5 credits</td><td>250 credits</td></tr>
<tr><td>GPT-6 Astra</td><td>250 credits</td><td>25 credits</td><td>1,250 credits</td></tr>
<tr><td>Daybreak Blue</td><td>100 credits</td><td>10 credits</td><td>500 credits</td></tr>
<tr><td>GPT-Image-2 (text)</td><td>125 credits</td><td>31.25 credits</td><td>250 credits</td></tr>
</tbody></table>
### Another section
"""

ANTHROPIC_SOURCE = """## Model pricing

| Model | Base input tokens | 5m cache writes | 1h cache writes | Cache hits and refreshes | Output tokens |
| :---- | :---------------- | :-------------- | :-------------- | :----------------------- | :------------ |
| Claude Fable 5.1 | $10 / MTok | $12.50 / MTok | $20 / MTok | $0.25 / MTok<sup>1</sup> | $50 / MTok |
| Claude Mythos 5.1 ([limited availability](https://example.test)) | $10 / MTok | $12.50 / MTok | $20 / MTok | $0.25 / MTok<sup>1</sup> | $50 / MTok |
| Claude Opus 5.5 | $4 / MTok | $5 / MTok | $8 / MTok | $0.20 / MTok<sup>2</sup> | $20 / MTok |
| Claude Opus 4.1 ([retired, except on Bedrock](https://example.test)) | $15 / MTok | $18.75 / MTok | $30 / MTok | $1.50 / MTok | $75 / MTok |
| Claude Haiku 5.5 (for prompts up to 100,000 tokens) | $0.10 / MTok | $0.125 / MTok | $0.20 / MTok | $0.01 / MTok | $0.50 / MTok |
| Claude Haiku 5.5 (for prompts over 100,000 tokens) | $0.50 / MTok | $0.625 / MTok | $1 / MTok | $0.05 / MTok | $2.50 / MTok |

## Cloud platform pricing

| Model | Base input tokens | 5m cache writes | 1h cache writes | Cache hits and refreshes | Output tokens |
| Claude Opus 5.5 | $9 / MTok | $9 / MTok | $9 / MTok | $9 / MTok | $9 / MTok |
"""


def card(provider="openai", surface="codex_paid_credits"):
    return {"provider": provider, "billing_surface": surface, "speed_mode": "standard",
            "unit": "credits_per_million_tokens", "source_url": "https://example.test/rates",
            "checked_at": "2026-01-01T00:00:00+00:00",
            "models": {"gpt-6.1-sol": {"input": 50, "cached_input": 2.5, "output": 250}}}


class PricingCacheTest(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "prices.json"
        self.original = {"schema_version": 1, "rate_cards": [card()]}
        self.path.write_text(json.dumps(self.original))

    def response(self, source=SOURCE):
        response = MagicMock()
        response.__enter__.return_value.read.return_value = source.encode()
        return response

    def test_extracts_model_ids_and_numeric_rates(self):
        rates = cache.parse_rates(SOURCE)
        self.assertEqual(rates["gpt-6.1-sol"]["cached_input"], 2.5)
        self.assertEqual(rates["gpt-6-astra"]["output"], 1250)
        self.assertEqual(rates["gpt-daybreak-blue-latest"]["input"], 100)
        self.assertEqual(len(rates), 3)

    def test_changed_source_shape_or_units_are_rejected(self):
        for source in (SOURCE.replace("Standard speed", "Fast speed"),
                       SOURCE.replace("Output Tokens", "Other Tokens"),
                       SOURCE.replace("2.5 credits", "2.5 dollars"),
                       SOURCE.replace("</table>", ""),
                       SOURCE.replace("1,250 credits", "1,25 credits")):
            with self.subTest(source=source), self.assertRaises(ValueError):
                cache.parse_rates(source)

    def test_extracts_active_claude_api_rates(self):
        rates = cache.parse_anthropic_rates(ANTHROPIC_SOURCE)
        self.assertEqual(list(rates), ["claude-fable-5-1", "claude-mythos-5-1", "claude-opus-5-5", "claude-haiku-5-5"])
        self.assertEqual(rates["claude-fable-5-1"], {"input": 10, "cache_write_5m": 12.5, "cache_write_1h": 20,
                                                     "cached_input": 0.25, "output": 50})
        self.assertEqual(rates["claude-haiku-5-5"]["output"], 0.5)

    def test_changed_claude_source_shape_or_units_are_rejected(self):
        for source in (ANTHROPIC_SOURCE.replace("## Model pricing", "## Prices"),
                       ANTHROPIC_SOURCE.replace("Output tokens |\n| :", "Other tokens |\n| :"),
                       ANTHROPIC_SOURCE.replace("| $4 / MTok |", "| $4 / KTok |"),
                       ANTHROPIC_SOURCE.replace("Claude Opus 5.5 | $4", "Opus Next | $4"),
                       ANTHROPIC_SOURCE.replace("Claude Mythos 5.1", "Claude Fable 5.1")):
            with self.subTest(source=source), self.assertRaises(ValueError):
                cache.parse_anthropic_rates(source)

    def test_claude_refresh_replaces_only_its_rate_card(self):
        with patch.object(cache, "urlopen", return_value=self.response(ANTHROPIC_SOURCE)):
            result = cache.refresh(self.path, "anthropic")
        updated = cache.load_cache(self.path)
        self.assertEqual(result["model_count"], 4)
        self.assertEqual(updated["rate_cards"][0], card())
        self.assertEqual(updated["rate_cards"][1]["unit"], "usd_per_million_tokens")
        self.assertEqual(updated["rate_cards"][1]["source_url"], cache.ANTHROPIC_SOURCE_URL)

    def test_cli_refreshes_every_source_by_default(self):
        sources = {cache.SOURCE_URL: SOURCE, cache.ANTHROPIC_SOURCE_URL: ANTHROPIC_SOURCE}
        respond = lambda request, timeout: self.response(sources[request.full_url])
        with patch.object(cache, "urlopen", side_effect=respond), \
             patch.object(cache.sys, "argv", ["pricing_cache.py", "--cache", str(self.path), "refresh"]), \
             patch("builtins.print"):
            self.assertEqual(cache.main(), 0)
        providers = [item["provider"] for item in cache.load_cache(self.path)["rate_cards"]]
        self.assertEqual(sorted(providers), ["anthropic", "openai"])

    def test_show_is_offline_and_reports_unknown_models(self):
        with patch.object(cache, "urlopen", side_effect=AssertionError("Network access")) as network:
            result = cache.show(self.path, ["gpt-6.1-sol", "unknown-model"])
        network.assert_not_called()
        self.assertEqual(list(result["rate_card"]["models"]), ["gpt-6.1-sol"])
        self.assertEqual(result["missing_models"], ["unknown-model"])

    def test_refresh_replaces_only_its_rate_card(self):
        other = card(provider="another-provider", surface="api_usd")
        self.original["rate_cards"].append(other)
        self.path.write_text(json.dumps(self.original))
        with patch.object(cache, "urlopen", return_value=self.response()):
            result = cache.refresh(self.path)
        updated = cache.load_cache(self.path)
        self.assertEqual(result["model_count"], 3)
        self.assertEqual(updated["rate_cards"][0], other)
        self.assertEqual(updated["rate_cards"][1]["source_url"], cache.SOURCE_URL)
        self.assertEqual(list(self.path.parent.iterdir()), [self.path])

    def test_download_or_parse_failure_preserves_existing_cache(self):
        original_bytes = self.path.read_bytes()
        for failure in (OSError("Offline"), None):
            with self.subTest(failure=failure):
                response = self.response(SOURCE.replace("credits per million", "dollars per thousand"))
                with patch.object(cache, "urlopen", side_effect=failure, return_value=response):
                    with self.assertRaises((OSError, ValueError)):
                        cache.refresh(self.path)
                self.assertEqual(self.path.read_bytes(), original_bytes)

    def test_failed_atomic_replace_preserves_cache_and_cleans_temporary_file(self):
        original_bytes = self.path.read_bytes()
        with patch.object(cache, "urlopen", return_value=self.response()), \
             patch.object(cache.os, "replace", side_effect=OSError("Write failed")):
            with self.assertRaises(OSError):
                cache.refresh(self.path)
        self.assertEqual(self.path.read_bytes(), original_bytes)
        self.assertEqual(list(self.path.parent.iterdir()), [self.path])

    def test_refresh_repairs_malformed_or_incompatible_cache_with_a_backup(self):
        incompatible = card()
        incompatible["unit"] = "usd_per_million_tokens"
        raw_card = json.dumps({"schema_version": 1, "rate_cards": [incompatible]}).encode()
        for raw in (b"{broken json", b'{"schema_version":2,"rate_cards":[]}', raw_card):
            with self.subTest(raw=raw):
                self.path.write_bytes(raw)
                with patch.object(cache, "urlopen", return_value=self.response()):
                    result = cache.refresh(self.path)
                self.assertEqual(cache.show(self.path, ["gpt-6.1-sol"])["missing_models"], [])
                self.assertEqual(Path(result["backup"]).read_bytes(), raw)

    def test_refresh_repairs_target_card_and_preserves_other_valid_cards(self):
        other = card(provider="another-provider", surface="api_usd")
        broken = card()
        broken["models"]["gpt-6.1-sol"]["input"] = -1
        self.path.write_text(json.dumps({"schema_version": 1, "rate_cards": [broken, other]}))
        original_bytes = self.path.read_bytes()
        with patch.object(cache, "urlopen", return_value=self.response()):
            result = cache.refresh(self.path)
        self.assertEqual(cache.load_cache(self.path)["rate_cards"][0], other)
        self.assertEqual(Path(result["backup"]).read_bytes(), original_bytes)
        self.assertEqual(cache.show(self.path, ["gpt-6.1-sol"])["rate_card"]["models"]["gpt-6.1-sol"]["input"], 50)

    def test_failed_download_preserves_corrupt_cache_without_creating_a_backup(self):
        self.path.write_bytes(b"{broken json")
        for failure in (OSError("Offline"), None):
            with self.subTest(failure=failure):
                response = self.response(SOURCE.replace("Standard speed", "Fast speed"))
                with patch.object(cache, "urlopen", side_effect=failure, return_value=response):
                    with self.assertRaises((OSError, ValueError)):
                        cache.refresh(self.path)
                self.assertEqual(self.path.read_bytes(), b"{broken json")
                self.assertEqual(list(self.path.parent.iterdir()), [self.path])

    def test_incompatible_or_corrupt_cache_is_rejected(self):
        for value in (-1, True, float("nan"), "50"):
            with self.subTest(value=value):
                self.original["rate_cards"][0]["models"]["gpt-6.1-sol"]["input"] = value
                self.path.write_text(json.dumps(self.original))
                with self.assertRaises(ValueError):
                    cache.show(self.path, [])
        self.original["rate_cards"] = [card(), card()]
        self.path.write_text(json.dumps(self.original))
        with self.assertRaises(ValueError):
            cache.show(self.path, [])


if __name__ == "__main__":
    unittest.main()
