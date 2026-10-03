# Coordinate a Decision Set

Create an index of activated decision IDs, their classes and subtypes, prerequisites, current stage,
packet revision, agent assignments, additional-decider budget, and disposition.
Use a durable task-local record for a large set so resuming preserves completed
work and budgets. A new process or batch directory never resets a decision's budget.

Distinguish prerequisites that require an accepted choice from those that require
verified implementation. Group mutually dependent choices into one material decision,
or ask the user to resolve the dependency if grouping would expand the activated set.

Read [prepare.md](prepare.md) for each eligible decision whose prerequisites are
settled. Independent decisions may advance concurrently. Each keeps its own packet,
reports, verification appendix, and judgment; each reference applies to that
decision's current stage. Complete a stage before loading its next instructions.

## Dispatch ready work

Select native agents or a CLI adapter based on the tools and model configurations
actually available. CLI processes have their own sessions; native-agent slot limits
and account/provider throughput limits are distinct constraints. Set a positive
global concurrency cap consistent with the environment and existing user constraints.
Check current capability rather than promising dozens of simultaneous live sessions.

Apply `model-selection` independently to every ready assignment, using that role's
unresolved reasoning and evidence. Keep the initial pair independent per decision.
Give every judge only its own decision's reports and checked evidence; sharing a
batch does not make another decision's context admissible.

For CLI work, prepare a manifest of ready assignments under the selected adapter and
use [dispatch.py](../scripts/dispatch.py). A manifest is one bounded wave of jobs;
finish or reconcile it before starting another wave so the global cap holds. The
runner executes assigned roles and collects artifacts. The coordinator interprets
reports and routes each decision under its current stage's reference.

Continue eligible work while another decision waits for user input. Mark that
decision `awaiting_user` and hold only its dependents. Present each escalated decision
with its own evidence and recommendation, preserving the majority-challenge branch.

## Execute and resume

The coordinator executes accepted choices under existing authorization. Serialize
changes that share resources or affect another decision's premises. Before executing,
check that the candidate's packet revision and prerequisite choices remain current.
A material change invalidates the old judgment; record it and return to the user if
the decision's remaining budget cannot support a fresh valid evaluation.

Reuse completed artifacts when resuming. Reconcile failed, timed-out, or uncertain
dispatches by their recorded IDs and statuses; do not silently launch replacements.

**Complete when:** every activated decision is accepted with its actual execution
status, awaiting a specified user choice, or blocked by a named prerequisite or
execution failure. Report these dispositions without treating pending choices as
approved or failed execution as verified implementation.
