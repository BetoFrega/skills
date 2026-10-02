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

The initial source covers Codex Standard paid-credit rates. API charges, included
subscription limits, other speed modes, and negotiated rates have separate billing
bases. Compare configurations within the same rate card.

## Refresh explicitly

```sh
python3 scripts/pricing_cache.py refresh
```

The script downloads the [official Markdown source](https://learn.chatgpt.com/docs/pricing.md),
extracts the Standard credit table without a model call, and atomically replaces that
rate card. It preserves other rate cards and retains the existing cache on download
or parsing failure. The command reports a compact result rather than the source page.

For a corrupt or incompatible cache, a successful refresh saves the original bytes
in a `.bak` file beside the cache and rebuilds the target card. It retains other valid
rate cards when the version 1 container can be read, and reports the backup path.

The source is documentation, not a dedicated pricing API. A changed heading, table,
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
`credits_per_million_tokens`. Other cards can be maintained explicitly from their
own authoritative sources. Availability, capability, and supported effort remain
facts of the execution environment.
