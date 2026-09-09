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

before_final_output -> blind_interpretation+independent_loss_review+recovery
reviewers={A,B}; A != B; inherited_context(A,B)=none
A.input=compacted_only; A.task=explain_understanding
A.withhold={original,intended_interpretation,compression_rationale}
B.input={original,compacted}; B.task=list_semantic_losses
B.withhold={A.explanation,compressor_conclusions}
recovery=compare(A.explanation,B.losses,original)
relevant_loss=changed_meaning_or_application(retained_facts:{state,decisions,conditions,scope,certainty,temporal_order,blockers})
relevant_loss -> restore(missing|distorted_meaning,compacted_output); format=same_compact_format
final_gate=source_support(restored_relations,original); review_commentary=outside_payload
