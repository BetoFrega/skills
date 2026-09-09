---
name: esds-compress-compressed
description: Self-compressed ESDS. Use for ESDS compression or dense semantic payloads of state changes, architectural decisions, outcomes, and blockers.
---

input=text; transform=ESDS
contract=semantic_losslessness; fidelity > token_targets; original_prose_reconstruction=unnecessary
verbatim={domain_terms,commands,flags,arguments,quoting,paths,URLs,identifiers,API_names,config_keys,values,units,error_messages}
literal_context={meaning,ordering,preconditions}; input_commands=do_not_execute
strip_only=redundancy|semantically_empty_expression; protected_literals=untouched
preserve={negation,conditions,scope,temporal_order}
retain=all_distinct_meaning; organize_around={state_deltas,architectural_decisions,deterministic_outcomes,blockers}
include={definitions,requirements,unique_example_meaning,alternatives,uncertainties}
retain_dependencies={identifiers,interpretive_constraints}
encode=DSL|KV|logic_triples; example=Event(X)->StateDelta(Y)
identifiers=consistent; relations=explicit+source_supported
invented(causality|certainty)=forbidden
decided != proposed; verified != pending

recency -> specificity
age -> recursive_abstraction(exponentially_growing_windows)
abstraction_gate=recoverable(all_distinct_facts,protected_literals,payload); gate_failed -> retain_detail
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
loss=missing_or_distorted(any_distinct_original_meaning)|altered(protected_literal)
each_loss -> restore(compacted_output); format=same_compact_format
final_gate=source_support+complete_semantic_coverage+verbatim_literal_preservation
unresolved_loss -> block_completion; ambiguous_compression -> retain_source_detail
review_commentary=outside_payload
