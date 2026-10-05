# Issue tracker: local Markdown

Choose the issue and spec storage root during setup. The repository default is
`.scratch/<feature>/`; use an external storage root when selected. Configuration
placement and work-record placement are separate choices.

Recommended layout:

```text
.scratch/<feature>/spec.md
.scratch/<feature>/issues/01-<slug>.md
```

Use one file per issue. Record status and categories near the top and append discussion
under a `## Comments` heading. The generated configuration must define its actual
naming, metadata, linking, blocking, and publish/fetch conventions.
