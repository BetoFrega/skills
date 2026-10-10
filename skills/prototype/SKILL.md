---
name: prototype
description: Prototype a state model, business logic, or UI with throwaway code that answers a design question.
---

# Prototype

Identify the question and completion criterion. For product questions, read canonical
contracts/evidence through [consolidate](../consolidate/SKILL.md), including external
configuration. Technical or interaction success establishes no product rule or release.

## Pick a branch

- Logic/state model → [LOGIC.md](LOGIC.md): one shareable HTML file with free-play
  actions and tabbed walkthroughs, usable by a non-developer.
- Appearance → [UI.md](UI.md): distinct variants on one route, selectable through a
  URL parameter and floating bottom bar.

Infer from prompt/code or ask when ambiguous. If the user is unreachable, prefer
logic for backend modules and UI for pages/components; state the assumption at the
prototype's top.

## Rules that apply to both

1. **Throwaway:** place code beside its intended module/page, named as a prototype.
   Temporary UI routes follow existing project routing conventions.
2. **Runnable:** UI starts with one project-task-runner command; logic opens as one
   HTML file.
3. **In-memory:** if persistence is the question, use scratch database/file storage
   clearly named "PROTOTYPE, wipe me".
4. **Minimal:** no tests, abstractions, or error handling beyond runnable behavior.
5. **Visible state:** show full relevant state after each logic action or UI switch.
6. **Capture:** integrate validated decisions in real code. Commit the complete
   rerunnable prototype as a primary source on a throwaway branch outside main;
   link that branch from the implementation issue. Record question/verdict in the
   issue or commit. Main retains only validated decisions.

Return supported learning and accepted choices through consolidate within existing
documentation authority, preserving unresolved proposals/evidence limits. Use
[next steps](../next-steps/SKILL.md) for completion, meaningful learning review, or
ready continuation; feature delivery and follow-up work retain their own scope.
