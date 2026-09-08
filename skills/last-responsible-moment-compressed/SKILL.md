---
name: last-responsible-moment-compressed
description: ESDS-compressed Last Responsible Moment. Apply to ongoing work to curb overplanning, premature commitment, or risky deferral.
---

scope=current_workflow; restart=false; expansion=false
priority=learning_before_commitment; preserve=options+delivery
inputs={next_increment,reversibility,delay_cost,expected_learning,lead_time}

required(progress|verifiable_behavior) OR delay(disproportionate_cost|risk|important_option_loss) -> DECIDE_NOW
uncertainty(invalidates_approach) -> INVESTIGATE_NOW(code|docs|measurements|minimal_experiment); definitive_commitment=unnecessary
needs_progress AND cheap_reversal AND preserves_important_options AND delegated_authority -> PROVISIONAL(simplest); invented_requirements|business_rules=forbidden
choice_unnecessary AND acceptable_delay_cost -> DEFER; upcoming_learning=favors_deferral; record={question,reason,observable_trigger}; reserve_lead_time={investigate,implement,validate}

DEFER -> defer(dependent_branches) EXCEPT independently_relevant_risks
out_of_scope != future_commitment
evidence > preference_questions
needs_user -> one_decision+recommendation+why_now
YAGNI=changeability; speculative(abstractions|config|infrastructure)=exclude
importance != irreversibility; defer(solution) != defer(investigation)
records=existing_docs; distinguish={decision,hypothesis,deferral}; retain=continuity_relevant; exhaustive_inventory|ADR_per_pending_issue=exclude
new_evidence -> reassess(commitments,triggers)

ready(next_increment)=clear AND executable AND verifiable AND no_hidden_business_assumptions AND no_unaddressed_material_risks
ready -> STOP(deliberation); PROCEED(existing_authorization)
planning_target=ready(next_increment); exhaustive_decision_tree=false
communicate=relevant_adjustments|blockers; extra_planning_ceremony=false
