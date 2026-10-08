# Logic Prototype

Build a shareable demo to answer one question about business logic, state transitions, or data shape. For appearance questions, use [UI.md](UI.md). Follow the shared [prototype rules](SKILL.md).

1. **State the question.** Before coding, identify the model and question in a visible introductory paragraph at the top of the demo.
2. **Isolate the logic.** Choose the representation that fits the question. Keep a small, portable module in one inline `<script>`, independent of DOM and event handlers; the page calls its public interface.
3. **Build one self-contained HTML file.** Use plain inline HTML/CSS/JS, runnable by opening the file, without frameworks, bundlers, or servers. Write labels and explanations in domain language for non-developers. Use static, restrained styling: clear typography, generous spacing, one accent colour.

   Present these in order:

   - Title and the question being explored.
   - Full relevant state as labeled fields, updated after every action.
   - Always-available free-play buttons, one per action.
   - Guided scenarios in tabs: normal, tricky, and invalid cases. Explain each situation and what to observe. Starting a scenario resets to known state; ordered action buttons execute each step and advance the walkthrough.

4. **Hand over and capture.** Open or share the file; adapt actions/scenarios to feedback. Once the question is answered, record the verdict and capture under the shared rules: validated logic goes into the real module; the HTML shell remains rerunnable on the throwaway branch, outside main.

Use in-memory state unless persistence is the question; then use the shared rules' scratch storage.
