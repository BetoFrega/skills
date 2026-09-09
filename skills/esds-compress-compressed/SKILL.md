---
name: esds-compress-compressed
description: Self-compressed ESDS. Use for ESDS compression or dense semantic payloads of state changes, architectural decisions, outcomes, and blockers.
---

input=text; transform=ESDS
strip={grammar,stop_words,conversational_framing,narrative,repetition}
preserve={negation,conditions,scope,temporal_order}
retain_only={state_deltas,architectural_decisions,deterministic_outcomes,blockers}
retain_dependencies={identifiers,interpretive_constraints}
encode=DSL|KV|logic_triples; example=Event(X)->StateDelta(Y)
identifiers=consistent; relations=explicit+source_supported
invented(causality|certainty)=forbidden
decided != proposed; verified != pending

recency -> specificity
age -> recursive_abstraction(exponentially_growing_windows)
window_axis=source_time; missing_dates -> source_order
n=input_events; historical_token_target=O(log(n)); independent_facts -> guarantee=false
active_decisions|unresolved_blockers -> preserve(regardless_of_age)

validate=source_support(each_relation)+preserved(current_state,decision_scope,blocker_status)
output=semantic_payload_only; introduction|commentary|markdown_fences|closing=exclude
retained_facts=empty -> output={}
