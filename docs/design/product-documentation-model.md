# Product documentation model

Agreed design from the product-owner interview, updated on 2026-10-06.
This document preserves agreed needs and process boundaries. The implementation uses
[consolidate](../../skills/consolidate/SKILL.md) for canonical knowledge,
[plan-increment](../../skills/plan-increment/SKILL.md) for selected work, and
[review-learnings](../../skills/review-learnings/SKILL.md) for learning feedback.
Standard setup owns configuration; skill references own operational authoring and
maintenance rules.
A dedicated learning-review skill gathers and reviews learning across work items,
using grilling for consequential choices and consolidate for canonical persistence.
[Next steps](../../skills/next-steps/SKILL.md) owns completion guidance and points to
the applicable continuation, including learning review.
For source rationale or comparisons with other methods, consult the [research note](../research/product-business-decision-practices.md).

## Purpose and adaptability

Maintain explicit product knowledge that supports product-owner decisions and agent execution across sessions: intent, capabilities, behavior, business rules, delivery, exposure, and decision history. AIFSD requires greater coverage and standardization than reliance on a team's tacit knowledge.

Standardize meanings, authority, traceability, and relevant behavioral coverage. Adapt hierarchy, formats, workflow, depth, and maintenance cadence to each product through the setup below.

The starting hierarchy is **product areas → capabilities → functionalities**. Group by domain behavior and meaningful outcomes, adapting depth to the product. Roles, segments, and jobs provide additional views of the same records.

## Product-owner needs

Maintain a durable canonical product knowledge space, independently of the lifetime
of work items in the ticket tracker. It must support these needs:

- Understand approved product behavior, its actors, jobs, rules, value, and cost,
  with delivery and audience exposure distinguishable from approved intent.
- Organize features into meaningful families and navigate their relationships,
  adapting the hierarchy and views to the product.
- Keep ideas, hypotheses, and draft functionalities discoverable in the canonical
  space, with detail proportional to their maturity. Canonical location identifies
  where knowledge belongs; approval status identifies which choices are accepted.
- Support discovery and maturation through problems, actors, alternatives, value,
  cost, hypotheses, research, experiments, and evidence as relevant. A raw idea can
  remain a short note; richer investigation does not impose a fixed sequence of
  stages or mandatory completeness on every idea.
- Slice features into usable end-to-end increments with identifiable scope,
  acceptance, dependencies, and exposure controls, preserving the feature contract.
- Organize executable work in the configured ticket tracker and trace work items
  to the product knowledge and increments they implement, change, or investigate.
- Include bounded research, discovery, prototyping, experiments, implementation,
  and maintenance in that work. Each item has a concrete action, scope, expected
  output, and completion criteria; learning work does not require an approved
  feature commitment.
- Follow the relationships from product knowledge to work and from work evidence
  back to supported delivery and exposure observations.
- Return supported learning, changes of direction, and redefinitions to canonical
  knowledge, including their effects on related features, slices, and pending work.
- Ground product grilling in the relevant canonical knowledge before interviewing
  the user, retaining settled choices and investigating consequential uncertainty.
- Bound discussion and delivery planning to the next increment or explicitly
  selected set of increments. Preserve future ideas and uncertainties without
  expanding the present interview or ticket scope to the whole functionality.

These needs govern workflow design. Consolidate product-documentation responsibilities
into consolidate. Use contextual grilling to clarify selected increments and
plan-increment to organize vertical delivery and executable tracker work within that
selection. Technical preparation is proportional to execution needs: consolidate
routes durable architecture choices to ADRs and scoped technical specs to the tracker
when useful. Resolve consequential execution gaps before readiness; leave routine
implementation choices to execution.

## Working on selected increments

For a new functionality or a change to an existing one, use the following process
without imposing a universal sequence of mandatory artifacts:

1. **Read the relevant context.** Grill-with-docs resolves the configured domain
   vocabulary, functionality records, shared rules, decisions, evidence, existing
   increments, and relevant technical constraints. Read context needed to understand
   the change and its consequences rather than the entire product knowledge base.
2. **Clarify the selected increments.** Establish the next increment or set being
   considered and ask about consequential uncertainty within that scope. Use the
   interview stopping check below to assess whether the knowledge is sufficient to
   formulate a consistent vertical slice. Keep later possibilities and uncertainties
   explicitly deferred. Account for a cross-cutting question when it actually affects
   the selected work.
3. **Consolidate the agreed knowledge.** Consolidate updates
   approved product decisions and affected contracts in their canonical destination,
   and routes relevant technical decisions to the appropriate records. Use ADRs when
   an architectural choice warrants one. A scoped technical spec in the configured
   tracker remains an available work artifact for technical approach, constraints,
   and validation; it references product authority instead of duplicating that contract.
   Preserve vocabulary through the configured glossary and verify persisted records.
4. **Plan the selected delivery.** Plan-increment develops
   vertical delivery and executable work only for the increments selected now. Carry
   the agreed product and technical references, acceptance, dependencies, and exposure
   controls. A selected increment can require multiple tickets. Reflect newly agreed
   increment definitions through the canonical writer; identify a necessary scope
   change for the user instead of silently adding future functionality to the plan.

The canonical space can describe more than the selected work. A feature record,
future proposal, or unresolved question is not an instruction to generate its tickets.
Retain confirmed choices during discussion and consolidate the affected records at
the agreed handoff. Subsequent learning and redefinitions return through the same
canonical authority.

### Interview stopping check

For product increment interviews, the next step is being able to formulate a
consistent vertical slice. The agent proposes ending grilling when the available
context and confirmed choices support a usable end-to-end outcome, bounded scope,
acceptance, and the material prerequisites needed to define that slice. This is a
knowledge-sufficiency check for slice planning, not a requirement to finish the
technical design or decompose all implementation tickets during the interview.

Explain the candidate outcome and why the knowledge is sufficient. Keep consequential
uncertainties visible; a question blocks closure when its answer is needed to make
the proposed slice consistent. Visiting the whole functionality's decision tree is
not the completion criterion.

The user can accept the proposed closure, disagree and identify what is missing, or
choose to continue toward the next slice. Recompute the interview scope from that
choice, retain settled decisions, and apply the same sufficiency check to any added
slice. Further slicing is an explicit continuation rather than an automatic expansion
to all future functionality. On accepted closure, carry the confirmed knowledge and
selected scope into consolidation and delivery planning, with deferred questions
identified separately.

### When evidence is missing

First consult the available documentation, code, observations, and other relevant
sources. Quick factual checks can remain within the interview session. Ask the user
to resolve product choices rather than facts the agent can retrieve.

When a factual uncertainty blocks a consistent slice and needs further investigation,
propose ending the interview with bounded discovery work. Specify the question,
scope, method, expected evidence or output, and completion criterion. This is an
executable investigation, distinguishable from a product delivery slice. Carry it
into work planning within the existing publication and execution authority.

Prefer a smaller delivery scope instead when it still preserves relevant progress
toward the user's goal. Record the deferred uncertainty and its implications. Keeping
the interview open is suitable for quick checks; longer investigations use the
bounded discovery handoff.

Return the investigation's supported findings to canonical knowledge and use them
when resuming the product discussion. Preserve confirmed choices and resolve the
remaining consequential questions for the selected slice.

## Documentation functions

| Function | Purpose |
| --- | --- |
| Product catalogue | Current product capabilities and sufficiently defined proposals, with behavior, audiences, value, cost, delivery, and exposure. |
| Domain vocabulary | Terms and definitions used consistently by the other records. |
| Shared rules | Constraints that apply across functionalities, referenced from the affected records. |
| Product direction | Current audiences, problems, value proposition, strategy, principles, and objectives. |
| Decision records | Choices, authority, context, alternatives, rationale, consequences, and later supersession. |
| Evidence and discovery | Research, hypotheses, experiments, and observed results. Raw ideas remain here until sufficiently defined for the catalogue. |
| Pitches | Proposed changes worth evaluating as investments, with problem, appetite, solution, risks, and exclusions as appropriate. |
| Delivery slices, change specs, and tickets | Work derived from the applicable product knowledge; slices identify usable end-to-end increments, with links to the work and evidence needed to deliver them. |

These functions may share native objects. Choose formats and workflow steps appropriate to the change; use pitches for investment decisions that warrant them.

## Catalogue identity and granularity

A functionality represents a recognizable outcome an actor can achieve, with relevant conditions and rules. Separate functionalities when actor outcomes or behavioral contracts differ materially; use delivery slices for increments of the same functionality. Preserve stable identity through ordinary evolution and link material changes to their rationale.

Distinguish **roles**, which express responsibilities and permissions, from **segments**, which express different needs and contexts. A functionality may serve multiple roles, segments, and jobs without duplicating its canonical record.

Each functionality record is the canonical source for its specific behavior and rules; shared rules have their own authoritative records. Keep proposals distinguishable from the consolidated contract. Document revisions remain in native version history; genuine decision records capture substantive choices and rationale. The executable [record format](../../skills/consolidate/references/record-format.md) owns consolidation, changelog limits, the template, and the worked example.

## Vertical delivery slices

A [delivery slice](../../CONTEXT.md) reduces the scope of an increment while retaining
a usable end-to-end outcome across the necessary layers. The functionality remains
the authority for its behavior; slices reference the rules and scenarios they cover.

Give every slice a stable identity and a reference to its functionality. Start with
identifiable sections within the functionality record. Use related records when they
improve individual maintenance or queries across functionalities. Standard setup maps
the representation to the selected destination; a subpage is one possible mapping.
Retain identifiers and relationships when that representation changes.

Capture the slice's usable result, scope and covered rules, its own acceptance
criteria, dependencies, exposure control, and links to specs, tickets, and verification
evidence. Generally use a dedicated flag to control its exposure, while documenting
the actual control relationships. Keep implementation, deployment, authorized release,
observed exposure, and flag observations independently accessible for each slice.

A slice can require several tickets. Size the slice by a coherent deliverable outcome
and the tickets by the work needed to produce it. The slicing workflow defines those
increments; consolidate owns their configured representation and maintenance.

Use [grilling](../../skills/grilling/SKILL.md) to resolve consequential uncertainty
about the selected increments: their boundaries, usable outcomes, acceptance,
dependencies, and exposure. Start from the functionality contract and settled choices.
The interview tree is bounded by the selected work, with later branches explicitly
deferred. Record settled choices as the interview progresses; keep unresolved
alternatives identifiable as proposals.

The focused delivery-planning stage develops the selected vertical delivery and
executable tickets. The agent-callable canonical writer owns the increment records
and their maintenance; it can be reached by interview and planning workflows without
duplicating their rules or expanding their scope. The
[delivery-slice requirements](../../skills/consolidate/references/delivery-slices.md)
define the operational record format, template, example, and completion checks to
incorporate under the canonical-record entry.

## Functionality record content

Map this content to native properties, sections, links, or associated objects. Preserve each meaning as independently accessible information. Adapt field names and organization, cover the relevant content, and identify meaningful unknowns.

| Information | Meaning |
| --- | --- |
| Identity and organization | Stable reference, title, parent capability or area, related functionalities, and applicable product scope. |
| Product decision state | Whether this is current approved product behavior or a proposal; authority, acceptance evidence, and effective timing where relevant. |
| User roles | Actors' responsibilities, permissions, and applicable conditions. |
| User segments | Contexts or groups with materially different needs. |
| Job to be done | Situation, need, and desired progress. |
| User story | Actor, desired outcome, and reason for seeking it. |
| Expected behavior | Domain outcomes, permissions, business states and transitions, conditions, invariants, limits, exceptions, and positive and negative scenarios sufficient for implementation and validation. |
| User value | Benefit in the relevant segment and job context, with rationale and supporting evidence. |
| User cost | Time, effort, obligations, monetary expense, friction, or risk in that context. |
| Business value | Expected contribution to business outcomes, with material audience differences identified. |
| Business cost | Build investment, operation, support, opportunity cost, and other relevant burdens. |
| Implementation | Behavior constructed and validated, with scenario coverage and verification gaps. |
| Deployment | Presence of the change in particular environments, linked to revision or equivalent provider evidence when available. |
| Authorized release | Approved audiences, conditions, rollout bounds, and conditions for advancement or reversal. See delivery semantics below for flag authority. |
| Observed exposure | Availability for particular audiences and conditions, including gradual exposure where applicable. |
| Feature flag observations | Relevant controls, observed configuration and targeting, source references, and observation time. See delivery semantics below for interpretation. |
| Evidence and maintenance | Sources, observation dates, coverage, responsible maintenance process, unresolved questions, and identified discrepancies. |
| Traceability | Applicable decisions, shared rules, research, pitches, work records, and verification evidence. |

Explain value and cost qualitatively in material segment/job contexts, adding supported measurements. Label estimates, hypotheses, and observed outcomes distinctly. Retain the rationale behind comparative scores. Evaluate relevant contexts rather than every possible role/segment/job combination.

Interaction sketches may express intent. Label them as illustrative and replaceable, and state binding outcomes and rules in expected behavior so the illustration leaves implementation choices open.

## Delivery and release semantics

Implementation, deployment, release, and exposure evolve independently. Adapt provider labels while retaining these dimensions and audience-specific observations.

When flags are used, verify their relationships: a functionality may depend on multiple controls, and a control may affect multiple functionalities. Configuration and targeting describe the control; observed behavior demonstrates availability and correctness for an audience.

Agents may operate flags within an authorized release plan, including its advancement and reversal conditions. Use existing session authorization within its scope; obtain corresponding authority for changes beyond it. Record the approved plan and observed configuration as distinct information.

## Agent maintenance

Agents maintain documentation during related implementation, deployment, and release work and through periodic reconciliation. Setup determines sources, cadence, coverage, and access for each product. Reconciliation accounts for external changes and stale or missing updates.

1. **Locate authority.** Read project conventions, applicable product decisions and release plans, and affected records. Resolve local or external configuration through the standard setup's location rules. Identify missing conventions for the user to resolve through standard setup; retain settled choices. Complete when the update scope, destinations, and existing authorization are identified; identify any unresolved authority needed for dependent changes.
2. **Observe sources.** Read the relevant implementation, deployment, availability, and flag sources. Complete when every relevant source has dated observations with references and coverage, or an identified access gap. Preserve earlier dated evidence and mark current uncertainty or staleness where a source is unavailable.
3. **Reconcile records.** Account for each affected functionality, shared rule, delivery dimension, and exposure scope. Reflect approved behavior changes with their rationale; record discrepancies and unresolved decisions explicitly. Complete when every affected item has a supported update or an identified gap.
4. **Verify persistence.** Write in the configured representation, then read back the affected records and relationships. Successful completion requires verified changes and links. Report partial and unverifiable effects with the affected records and remaining work identified.

## Learning feedback

Use canonical knowledge as both context for work and the destination for what the
work establishes. Review learning across relevant work items when their combined
results may change product understanding, direction, or priorities. Adapt the review
scope and triggers to the product rather than requiring a fixed ceremony.

By default, next-steps recommends a learning review when supported results contradict
an important hypothesis, change scope or direction, call for redefining a product
rule, or materially affect related functionalities. Judge relevance against the
current canonical knowledge and work scope. Standard setup may additionally configure
periodic review points for the product. This recommendation does not require a full
review after every ticket; factual delivery and flag maintenance continues during work.

1. **Gather evidence.** Resolve the applicable canonical records and review scope.
   Collect relevant work results, experiments, verification, user feedback, and
   confirmed decisions with source references and coverage; identify missing evidence.
2. **Synthesize learning.** Consolidate repeated findings, contradictions, and
   consequences. Distinguish observations, interpretations, hypotheses, proposals,
   and accepted decisions; retain meaningful uncertainty and contrary evidence.
3. **Grill consequential choices.** Use grilling to resolve changes of direction,
   redefinitions, and unresolved product choices against the existing knowledge.
   Reuse approvals within their scope. Evidence or implementation alone does not
   authorize a new product contract. Supported factual maintenance can proceed
   without a new interview when it introduces no unresolved product choice.
4. **Update affected knowledge.** Use consolidate to incorporate supported evidence and
   accepted changes into the configured canonical records. Account for related
   features, slices, shared rules, and pending work; route work changes through
   plan-increment within the applicable authorization. Preserve unresolved proposals
   explicitly. Consolidate living records instead of narrating their revision history.
5. **Verify the feedback.** Read back affected records and relationships. Complete
   when each material finding has a supported canonical update, a reason it requires
   no change, or an explicit unresolved question or access gap.

Provide this review as a dedicated skill, complementing factual maintenance during
work. It owns evidence gathering, synthesis, and grilling, and delegates canonical
product persistence to consolidate. Reuse the authoritative authoring and maintenance
rules rather than creating a competing format or a second canonical writer.
Review-learnings owns this review; next-steps owns completion guidance.

For product interviews, grill-with-docs must obtain the relevant canonical contracts,
decisions, proposals, and evidence through grilling before the first product question.
It follows configured authority through consolidate.
Domain modeling maintains vocabulary in its configured glossary; architecture choices
use the applicable ADR workflow. These records remain connected to the product
knowledge they inform.

## Completion and continuation

Extend next-steps as the shared completion guidance for implementation, discovery,
experiments, and documentation work. Existing execution skills consult it at the
appropriate end of their work. Ship-main retains its Git delivery scope and consults
the same guidance; learning and documentation work can end without Git delivery.

Resolve the current goal, canonical references, work relationships, and applicable
completion criteria before recommending a continuation. Distinguish outstanding
requirements for the current work from subsequent learning review or successor work.
Use supported evidence to identify delivery or documentation gaps, relevant learning
to review, and ready successors within the agreed priorities and dependencies.
Apply the learning-review triggers above and the product's configured review points.

An explicit next-steps request remains informational. When consulted during execution,
complete remaining authorized work before the final report and identify blocked
actions precisely. Recommendations alone do not authorize new work, product choices,
release operations, or publications. Existing authorization remains usable within its
scope. Keep concrete execution in the relevant skills and canonical product updates
in consolidate, without adding a separate completion entry point.

## Project setup and canonical destination

The existing `setup-beto-frega-skills` owns this configuration as part of the user's standard setup. The consolidate skill consumes it and identifies gaps. Keep setup procedures in plain references under standard setup, independently of the product knowledge routes. Read established conventions and retain settled choices. Ask for missing decisions only. Configure the following using operations verified for the selected systems:

1. **Map authority and representation.** Choose arbitrary canonical destinations and concrete locations; map content, objects, states, history, links, and navigation to their native representation. Complete when each documentation function in the project's scope has an authoritative location and applicable representation.
2. **Adapt product conventions.** Record hierarchy, granularity, terminology, audiences, decision authority, effective timing, and permitted release operations. Complete when product-specific conventions preserve the meanings defined above.
3. **Establish maintenance.** Identify observation sources, read/write capabilities, update triggers, reconciliation cadence, coverage, and responsibility. Complete when the maintenance mechanism and its actual availability are recorded, with unavailable operations and access gaps identified.

Select integrations after destinations are chosen. When direct writing is unavailable, prepare a clearly identified draft or manual transfer in the agreed format. Keep working copies subordinate to the configured authority.

### Configuration outside the repository

Support configuration files inside the repository, outside it, or across both. External configuration enables work on third-party repositories while leaving their tracked files untouched. Configuration placement and canonical documentation destinations are separate decisions; a personal configuration may point to the product's existing shared catalogue.

Bind external configuration to the project and its applicable contexts. Resolve relative references against their containing document. Make it discoverable through a supplied task reference, personal instructions actually loaded by the agent, or an approved repository pointer; file creation alone does not establish automatic discovery. Pass the relevant configuration reference to delegated agents. Preserve applicable repository instructions and resolve consequential conflicts through the normal instruction hierarchy.

Use [the standard setup's location rules](../../skills/setup-beto-frega-skills/references/project-configuration.md) for setup and consuming skills. Preserve declared destinations; an unreadable replacement is an explicit gap. Creating repository instruction files or symlinks is optional in the external mode.

## Product knowledge and work entry points

Use one model-invoked consolidate skill that users and other skills can reach for
canonical product knowledge. It creates, revises, reads, and reconciles records,
including existing functionalities, ideas, discovery, decisions, and delivery slices.
Its `SKILL.md` resolves intent and project conventions, selects references, and states
common completion rules. Its description exposes the distinct invocation branches.
It also routes relevant technical decisions to ADRs or scoped technical work records
when appropriate.

Use plan-increment for selected delivery planning and
executable tracker work. It consumes canonical
references, preserves scope and acceptance, and owns execution decomposition,
dependencies, readiness, and work-item publication. Preserve the configured destinations
for both entries; Spaces is a project choice rather than a universal provider.
Select the increments in scope before decomposing work; broader feature documentation
does not authorize a broader delivery plan.

Use progressive disclosure through plain reference files within each entry. Define an explicit reading trigger for each reference and keep each rule authoritative in one place. Group and split references according to their consumers; the following are product-knowledge routing responsibilities, not a fixed file count or mandatory process sequence:

| Branch | Read when |
| --- | --- |
| Catalogue | Finding product capabilities or creating and updating functionality behavior, audiences, jobs, value, and cost. |
| Delivery slices | Recording or maintaining usable feature increments, acceptance, dependencies, exposure strategy, and their delivery evidence. |
| Product context | Maintaining direction, shared rules, vocabulary references, or research and experiment evidence. |
| Decisions | Recording an approved choice, preserving its rationale, or identifying the contracts affected by a change. |
| Proposals | Preparing a sufficiently defined product proposal or an investment pitch. |
| Technical work | Routing architecture choices to ADRs or preparing a scoped technical spec in the tracker when useful. |
| Reconciliation | Updating implementation, deployment, release, exposure, and flag observations or detecting documentation drift. |

Combine branches when needed: an approved decision may require decision recording, a catalogue change, and reconciliation. Complete the affected operation and verify its result; selecting references alone is not completion. Preserve project-specific formats and workflows through their configuration.

Standard setup records destinations, representation, conventions, and maintenance;
consolidate reads that configuration before its applicable routes. Missing configuration
does not authorize autonomous invocation of the explicit-only setup. Decision recording
can reuse the product routes and existing architecture-decision handling. Redirect
product readers and maintainers to consolidate, including grilling, domain modeling,
decision recording, architecture decisions, implementation, review, and Git delivery.
Existing records retain their identity and approved content through the consolidation.
