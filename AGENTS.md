<!-- @bufferapp/cli skill — managed -->
!buffer context
<!-- /@bufferapp/cli skill — managed -->

## Language

Write all skill content in English, including frontmatter descriptions, headings, instructions, and examples. Apply this rule when creating or editing skills in this repository. Respond to the user in their preferred language.

## Portable paths

Use repository-relative paths in maintained instructions and examples. Scripts must
discover the repository root from their own location or Git metadata rather than
hardcode a user's home, checkout name, or absolute checkout path. Resolve standard
user installation directories through the environment or `Path.home()`. Create
cross-directory symlinks with relative targets calculated from their actual locations.
