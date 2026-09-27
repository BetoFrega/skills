# Scream tests for unknown consumers

Read before proposing or operating a retirement-discovery experiment. A scream test supplements the consumer inventory when remaining dependencies are uncertain.

## Choose and explain the experiment

Explain the concrete effect to the user and establish its explicitly accepted operational scope. Temporary consumer interruption may be a deliberate exception to default continuity for this experiment; that exception does not extend to ordinary rollout.

- **Reversible disablement:** put the legacy capability behind a control flag, disable it, observe usage and reports, and restore it when an affected consumer emerges. Define exposure scope, observation conditions, restoration signals, and the restoration mechanism.
- **Consumer-controlled deprecation opt-in:** clearly state in the response that the legacy capability is being removed and require an explicit consumer-supplied deprecation acknowledgement for temporary continued access. Explain the acknowledgement and how to contact the migration team so consumers can restore access while coordinating migration. This changes availability policy, not normal authentication or authorization.

## Prepare and observe

Define signals that reveal consumers, how to identify their owners, and what triggers restoration or temporary access. Verify the restoration or opt-in path before the experiment. Observe within the agreed scope and apply its response conditions.

Carry each newly discovered consumer into the inventory and migration plan. Include continued deprecation opt-in usage in retirement evidence. Absence of complaints alone is not proof that all consumers migrated.

The experiment is accounted for when discovered consumers have an explicit disposition, accepted responses were executed, and remaining uncertainty is visible in retirement criteria. This evidence informs the final retirement decision; it does not itself establish completed migration.
