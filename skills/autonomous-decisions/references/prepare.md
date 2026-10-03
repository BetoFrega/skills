# Prepare the Decision

Resolve the explicitly activated decision set. If it is unspecified, ask which
decisions the user means before running deliberation. A request to include every
decision in the task expands eligibility, while preserving the standing rules.
Handle separate decisions separately; settle prerequisites before dependent choices.

Select one eligible unresolved decision and create its packet:

- Decision ID, class and material subtype, question, authorized scope, and desired
  outcome. Identify each determinant component when the decision mixes classes.
- Existing execution authorization and its origin in the task; identify absent
  permissions explicitly.
- Criteria for comparing alternatives and any known viable options.
- Previous directions, established values, and other binding constraints, each
  with its origin in user instructions or trusted project guidance.
- Necessary project context, current evidence, and authorized read-only tools and
  resources. Include source excerpts or observed results, source locations, and
  revision or observation time where freshness matters.
- A distinction between verified facts, inferences, and unresolved claims.
- Remaining uncertainties, with no preferred answer supplied by the coordinator.

User preferences and values come from their actual instructions and trusted
guidance. Preserve the origin of a constraint so a discovered disagreement can be
recognized as a user decision rather than silently resolved by agents.

Apply `model-selection` independently to each initial decider assignment. Record
its model, effort, and role-specific rationale. Select later assignments when their
stage is ready, using the evidence and unresolved reasoning available then.

Initialize a per-decision record with the packet, agent IDs and configurations,
reports, verification findings, and `additional_decider_used: false`. Keep this in
task context unless an existing task convention calls for a persistent record.

**Complete when:** the decision belongs to the activated set, passes the standing
rules, the packet contains the context needed for an independent choice, and the
initial decider assignments have recorded configurations and rationales.
Then read [deliberate.md](deliberate.md).
