# Product documentation model

Agreed design from the product-owner interview, updated on 2026-10-04.
The executable workflow is [product-documentation](../../skills/product-documentation/SKILL.md); this document preserves the agreed design. Consult it for the model's rationale and implementation scope. Standard setup owns configuration; the skill's references own the operational authoring and maintenance rules.
For source rationale or comparisons with other methods, consult the [research note](../research/product-business-decision-practices.md).

## Purpose and adaptability

Maintain explicit product knowledge that supports product-owner decisions and agent execution across sessions: intent, capabilities, behavior, business rules, delivery, exposure, and decision history. AIFSD requires greater coverage and standardization than reliance on a team's tacit knowledge.

Standardize meanings, authority, traceability, and relevant behavioral coverage. Adapt hierarchy, formats, workflow, depth, and maintenance cadence to each product through the setup below.

The starting hierarchy is **product areas → capabilities → functionalities**. Group by domain behavior and meaningful outcomes, adapting depth to the product. Roles, segments, and jobs provide additional views of the same records.

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
| Delivery scopes, change specs, and tickets | Work derived from the applicable product knowledge; scopes track integrated parts that can be completed independently. |

These functions may share native objects. Choose formats and workflow steps appropriate to the change; use pitches for investment decisions that warrant them.

## Catalogue identity and granularity

A functionality represents a recognizable outcome an actor can achieve, with relevant conditions and rules. Separate functionalities when outcomes, rules, or independent delivery differ materially. Preserve stable identity through ordinary evolution and link material changes to their rationale.

Distinguish **roles**, which express responsibilities and permissions, from **segments**, which express different needs and contexts. A functionality may serve multiple roles, segments, and jobs without duplicating its canonical record.

Each functionality record is the canonical source for its specific behavior and rules; shared rules have their own authoritative records. Keep proposals distinguishable from the current contract, and preserve historical rationale through decision links and available record history.

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

## Project setup and canonical destination

The existing `setup-beto-frega-skills` owns this configuration as part of the user's standard setup. The product-documentation skill consumes it and identifies gaps. Keep setup procedures in plain references under standard setup, independently of the product skill's operating routes. Read established conventions and retain settled choices. Ask for missing decisions only. Configure the following using operations verified for the selected systems:

1. **Map authority and representation.** Choose arbitrary canonical destinations and concrete locations; map content, objects, states, history, links, and navigation to their native representation. Complete when each documentation function in the project's scope has an authoritative location and applicable representation.
2. **Adapt product conventions.** Record hierarchy, granularity, terminology, audiences, decision authority, effective timing, and permitted release operations. Complete when product-specific conventions preserve the meanings defined above.
3. **Establish maintenance.** Identify observation sources, read/write capabilities, update triggers, reconciliation cadence, coverage, and responsibility. Complete when the maintenance mechanism and its actual availability are recorded, with unavailable operations and access gaps identified.

Select integrations after destinations are chosen. When direct writing is unavailable, prepare a clearly identified draft or manual transfer in the agreed format. Keep working copies subordinate to the configured authority.

### Configuration outside the repository

Support configuration files inside the repository, outside it, or across both. External configuration enables work on third-party repositories while leaving their tracked files untouched. Configuration placement and canonical documentation destinations are separate decisions; a personal configuration may point to the product's existing shared catalogue.

Bind external configuration to the project and its applicable contexts. Resolve relative references against their containing document. Make it discoverable through a supplied task reference, personal instructions actually loaded by the agent, or an approved repository pointer; file creation alone does not establish automatic discovery. Pass the relevant configuration reference to delegated agents. Preserve applicable repository instructions and resolve consequential conflicts through the normal instruction hierarchy.

Use [the standard setup's location rules](../../skills/setup-beto-frega-skills/references/project-configuration.md) for setup and consuming skills. Preserve declared destinations; an unreadable replacement is an explicit gap. Creating repository instruction files or symlinks is optional in the external mode.

## Single skill with internal routing

Provide one model-invoked product-documentation skill that users and other skills can reach. Its `SKILL.md` resolves task intent and project conventions, selects applicable references, and states the common completion rules. Its description exposes the distinct invocation branches.

Use progressive disclosure through plain reference files within that skill. Define an explicit reading trigger for each reference and keep each rule authoritative in one place. Group and split references according to their consumers; the following are routing responsibilities, not a fixed file count or mandatory process sequence:

| Branch | Read when |
| --- | --- |
| Catalogue | Finding product capabilities or creating and updating functionality behavior, audiences, jobs, value, and cost. |
| Product context | Maintaining direction, shared rules, vocabulary references, or research and experiment evidence. |
| Decisions | Recording an approved choice, preserving its rationale, or identifying the contracts affected by a change. |
| Proposals | Preparing a sufficiently defined product proposal or an investment pitch. |
| Reconciliation | Updating implementation, deployment, release, exposure, and flag observations or detecting documentation drift. |

Combine branches when needed: an approved decision may require decision recording, a catalogue change, and reconciliation. Complete the affected operation and verify its result; selecting references alone is not completion. Preserve project-specific formats and workflows through their configuration.

Standard setup records destinations, representation, conventions, and maintenance; the product skill reads that configuration before its applicable routes. Missing configuration does not authorize autonomous invocation of the explicit-only setup. Decision recording can reuse the product routes and existing architecture-decision handling. When discovery, domain modeling, specs, or tickets depend on product behavior, their instructions must point agents to this entry and the configured authority.
