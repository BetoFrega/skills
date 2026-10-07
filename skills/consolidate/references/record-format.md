# Living record format

Read this before writing or consolidating catalogue records, shared rules, direction,
proposals, or current delivery observations. Adapt headings, language, properties,
and linked objects to the configured destination while retaining these invariants.

## Consolidate the current contract

Write the latest approved contract in direct, present-tense language. Identify
proposals and accepted future-effective rules separately, with their timing.
Keep approval authority and source references in compact metadata or evidence fields.
The reader must understand each applicable rule without reconstructing an interview.

After an accepted change, rewrite the affected rule and reconcile related sections,
examples, summaries, open questions, and records. Replace superseded wording in place.
Several saves implementing one decision still produce one consolidated result.

Document revision history belongs to the destination's native versions, commits, or
audit history. Historical narratives of document changes are prohibited in the living
record, including dedicated history sections, footnotes, appendices, and comments
used as substitute logs. Earlier values, question numbers, rejected answers, and
reopened-choice stories remain recoverable through native history.

Current rationale may explain a rule's purpose or value. A genuine
[decision record](decisions.md) may describe a substantive choice and its rationale;
it is not an edit log. Dated observations relevant to a current discrepancy remain
evidence, with their scope and uncertainty.

## Optional final changelog

Use a changelog only for substantial changes to outcomes, material rules, permissions,
commercial terms, scope, or availability. Formatting, wording, links, routine
observations, and minor clarifications do not qualify. A new record needs no creation
entry. Omit the section when no qualifying change needs a summary.

When used:

- Put it at the end of the document, after all other content.
- Keep at most five recent entries, newest first; earlier entries remain in native history.
- Use one plain-text bullet on one logical line per substantial change or coordinated
  change set: `YYYY-MM-DD — <what changed>`.
- Limit each entry to 20 words. Count whitespace-separated tokens after the bullet
  marker, including the date. Count before saving and shorten any entry over the limit.
- State the change alone. Keep explanations, approval details, question references,
  and comparisons with earlier values out of the entry.
- Combine repeated saves of the same change into one entry. Readbacks do not add entries.

## Template and example

For a functionality, adapt the [template](../assets/functionality-template.md).
Read the [worked example](functionality-example.md) when establishing a representation
or consolidating a record that accumulated interview notes. The example uses fictional
decisions; copy its organization, not its product rules or evidence.

Use equivalent native fields when the project already has a representation. Keep
user value, user cost, business value, and business cost independently accessible,
along with implementation, deployment, authorized release, observed exposure, and
flag observations. Mark relevant unknowns with reasons; omit irrelevant template
sections instead of leaving empty scaffolding. Split materially different actor
outcomes into identifiable records or sections according to the product's granularity.

## Completion checks

Check the saved document as a whole:

- Applicable rules and examples agree with the latest accepted choices and timing.
- Titles, summaries, and open questions reflect the consolidated content.
- Revision history and interview narration are absent from the document.
- Actors, jobs, behavior, the four value/cost meanings, and delivery dimensions are
  independently accessible where relevant, including identified knowledge gaps.
- Any changelog is final, qualifies as substantial, has at most five entries, and
  every entry fits the word limit.

Successful persistence alone does not satisfy these checks.
