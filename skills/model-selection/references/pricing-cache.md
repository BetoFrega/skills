# Pricing cache

`~/.agents/model-pricing.json` is the shared local price snapshot. Selection reads
it; maintenance updates it only when the user explicitly requests setup, repair, or
refresh. A missing file, unknown model, or old timestamp leaves pricing uncertain
and work continues with a suitable configuration.

## Read locally

Run from this skill's directory, resolving its installed location from the environment:

```sh
python3 scripts/pricing_cache.py show gpt-6.1-sol gpt-5.6-terra
```

`show` performs no network requests and emits only matching cached rates, their
provenance, and missing model names. Reuse the snapshot for child assignments.
This command selects the Codex Standard card only. Read the JSON snapshot directly
for other providers' cards.

Built-in sources cover Codex Standard paid-credit rates and Claude API standard
rates. Included subscription limits, other speed modes, and negotiated rates have
separate billing bases. Compare configurations within the same rate card.

## Refresh explicitly

```sh
python3 scripts/pricing_cache.py refresh
```

The script downloads each built-in official Markdown source, extracts its table
without a model call, and atomically replaces that rate card: the
[Codex pricing](https://learn.chatgpt.com/docs/pricing.md) Standard credit table and
the [Claude API pricing](https://platform.claude.com/docs/en/about-claude/pricing)
model table. Pass `openai` or `anthropic` to refresh one source. Each source succeeds
or fails independently; a failure retains that card, preserves other rate cards, and
makes the command exit nonzero. The command reports one compact line per source.

For a corrupt or incompatible cache, a successful refresh saves the original bytes
in a `.bak` file beside the cache and rebuilds the target card. It retains other valid
rate cards when the version 1 container can be read, and reports the backup path.

The sources are documentation pages without a pricing API. A changed heading, table,
or unit requires repairing the parser against the official source before retrying.
Use an agent for that repair when interpretation is needed; routine extraction runs
as a script.

## Structure

Schema version 1 contains a `rate_cards` array. Each card has:

- `provider`, `billing_surface`, `speed_mode`, and `unit` identifying comparable rates;
- `source_url` and `checked_at` recording provenance;
- `models`, keyed by execution model ID, with numeric `input`, `cached_input`, and
  `output` prices per million tokens. Output includes billed reasoning tokens.

The built-in refresher writes `openai` / `codex_paid_credits` / `standard` /
`credits_per_million_tokens` and `anthropic` / `claude_api` / `standard` /
`usd_per_million_tokens`. Other cards can be maintained explicitly from their own
authoritative sources. Availability, capability, and supported effort remain
facts of the execution environment.

The Anthropic `claude_api` / `standard` card uses `usd_per_million_tokens` and model
IDs such as `claude-fable-5-1` and `claude-opus-5-5`, derived from the official
model names. `cached_input` is the cache-read price; `cache_write_5m` and
`cache_write_1h` capture the distinct write rates. Retired models are skipped, and
models with prompt-length tiers keep only the base tier. These are standard global
API rates; Claude subscription costs and Codex credits differ. Account for cache writes
when estimating API costs.
