# Keep It Lean

Build only what the current increment needs, and leave the design easy to change
when the next need arrives.

- **YAGNI.** Add no abstraction, pattern, framework, configuration, option, or
  dependency that no current requirement uses.
- **Last Responsible Moment.** Commit when progress or verifiable behavior needs the
  choice, or when delay would lose an important option. Until then, preserve
  changeability instead of guessing.
- **Evolutionary Architecture.** Lean is not careless. Keep seams where change is
  already evident, so the next requirement extends the design instead of rewriting it.
- **Minimize the diff.** Make the smallest change that solves the problem. Fewer lines
  beat elegant boilerplate.
- **Consolidate decisions.** Make each choice in one place and pass its result along,
  rather than repeating the choice where it is used.
- **No premature optimization.** Optimize after a measurement shows the need.
