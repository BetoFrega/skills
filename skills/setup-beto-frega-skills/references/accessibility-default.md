# Accessibility baseline defaults

Use this only to recommend answers while creating a repository-owned
`ACCESSIBILITY.md`. It is not policy after that document exists.

## Recommended decisions

- **Web target**: WCAG 2.2 Level AA, meaning all applicable Level A and Level AA
  success criteria across complete affected journeys and responsive variations.
- **Other platforms**: name the platform's current official accessibility guidance and
  supported assistive technologies. Do not force web-specific criteria onto native,
  terminal, API-only, or library surfaces; define an equivalent repository baseline.
- **Native semantics first**: prefer platform controls and semantics. Custom components
  must expose correct name, role, value, state, relationships, and change notifications.
- **Operability**: every action works with the supported non-pointer inputs. Focus is
  visible, ordered, restored after transitions, and not trapped or obscured.
- **Perception**: meaning does not depend only on color, position, sound, or motion.
  Text, controls, focus, zoom/reflow, contrast, reduced-motion behavior, media, and
  alternatives follow the chosen platform requirements.
- **Understandability**: labels, instructions, validation, status, loading, empty, and
  failure states remain identifiable and actionable with assistive technology.
- **Journey coverage**: review entry, success, error, interrupted, and recovery states,
  not only isolated components or the happy path.
- **Verification**: combine automated checks with keyboard/manual inspection and the
  agreed browser, platform, or assistive-technology matrix. Automation alone is not a
  conformance claim.
- **Exceptions**: record the unmet requirement, affected users and journey, rationale,
  compensating path, owner, and expiry or review condition.

## Questions the grilling must settle

1. Which user-facing surfaces and complete journeys are in scope?
2. Which standard, conformance level, and platform guidance govern each surface?
3. Which browsers, devices, inputs, and assistive technologies are supported?
4. Which semantic, focus, keyboard, pointer, visual, motion, media, and content rules
   are mandatory for this product?
5. Which loading, empty, validation, error, and recovery states need explicit coverage?
6. Which automated, manual, and assistive-technology checks gate delivery?
7. Who owns accessibility regressions and how are exceptions retired?

## Suggested document shape

Keep the repository document concise and testable:

1. Scope and governing standards
2. Supported platforms and assistive technologies
3. Interaction and semantic requirements
4. Visual, motion, content, and state requirements
5. Verification matrix
6. Ownership and exceptions

Reference: [WCAG 2.2](https://www.w3.org/TR/WCAG22/). The W3C recommends WCAG 2.2
for current applicability; Level AA includes every Level A and Level AA success
criterion.
