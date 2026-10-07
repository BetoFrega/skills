# Product documentation validation

Historical validation on 2026-10-04 of the original product-documentation skill,
whose canonical authoring responsibility now lives in consolidate. This exercise
does not validate the subsequent workflow changes. See the agreed
[product-documentation model](../design/product-documentation-model.md) and
[skill entry](../../skills/consolidate/SKILL.md).
The [workflow validation](product-workflow.md) covers the newer entrypoints and boundaries.

## Scope

The authoring agent exercised the instructions using synthetic project records and
observations in a temporary workspace. Configuration and canonical records lived
outside a separate mock third-party repository. The native representation was an
object collection stored in JSON, with its property mapping declared in the external
configuration. No live provider, flag service, scheduler, or production product was
involved. This was an author-run exercise, not an independent agent evaluation.

## Scenarios and observed results

| Scenario | Result |
| --- | --- |
| External configuration and native representation | Relative entry/configuration/record pointers resolved to the external collection. Record writes left the mock repository unchanged, verified by file hashes. |
| Shaped proposal and raw idea | The waiting-list proposal entered the catalogue as proposed behavior and linked to its pitch. Approval of a three-day experiment did not establish permanent release authority. The unrelated raw idea remained in discovery. |
| Separate value and cost | User value, user cost, business value, and business cost stayed separate. Unknown support cost remained unknown, and illustrative interaction intent remained nonbinding. |
| Accepted decision with future effect | A sixty-minute reservation decision effective on 2026-11-01 preserved the current thirty-minute contract, predecessor rationale, and two-way history links. |
| Deployment and partial exposure | Implementation evidence and deployment evidence stayed separate. A successful probe for one identity did not become a population availability claim. |
| Flag drift | Observed targeting of 50% remained distinct from the authorized maximum of 20%. The discrepancy was recorded without changing the release plan or operational flag source. |
| Unavailable observation and maintenance | An inaccessible safety flag retained its previous observation date and an explicit freshness gap. A planned weekly cadence remained inactive because no scheduler existed. |
| Wrong project and unavailable replacement | A mismatched project entry and an unreadable declared configuration produced gaps without creating fallback repository configuration. |
| Incomplete catalogue relationship | The absent parent capability remained a named gap rather than an invented authoritative record. |

Sixteen assertions passed over saved state, authority, history, evidence, and filesystem
effects. Readback covered the created proposal, proposed functionality, accepted
decision, and updated current functionality and predecessor decision.

## Integration review

The setup owns configuration locations and product conventions, with references to
the product skill's content requirements. Product writing and reconciliation stay in
one agent-callable skill with five progressively disclosed routes. Existing explicit
invocation policies remain intact.

Decision recording, domain modeling, grilling, specs, tickets, implementation, reviews,
and Git delivery reference the appropriate product authority. Work records retain
canonical contract and scenario links. The local-ticket consumer uses the configured
work-record location, including external locations. Readiness accounts for unresolved
product choices; approved work scope alone does not silently approve product policy.

Repository discovery uses a relative link to the canonical skill directory. Persistent
discovery of an individual product's external configuration and actual recurring
maintenance still depend on that product's selected setup and verified mechanism.

## Structural and package checks

- The new product skill and revised standard setup passed skill frontmatter validation.
- The package builder validated all 49 skills and their references and verified the
  candidate archive's contents. The candidate contains uncommitted workspace changes;
  it is not a published release.
- All 20 existing package/release-preparation tests passed after new source files were
  included in the Git index used by the builder.
- Repository discovery points relatively to `skills/product-documentation`; link
  resolution and the literal relative target were verified.
- Product documentation allows implicit invocation. Setup and decision recording keep
  explicit invocation; domain modeling retains its existing default implicit policy.
- Markdown references and whitespace checks passed. Provider authentication and live
  product maintenance were outside this validation scope.
