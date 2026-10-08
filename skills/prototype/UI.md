# UI Prototype

Explore appearance through radically different variants on one route. For logic or state questions, use [LOGIC.md](LOGIC.md). Follow the shared [prototype rules](SKILL.md).

## Build

State the question and plan in one line. Default to three variants; cap at five.

Prefer an existing host page, including for new sections, cards, or flow steps. Preserve its data fetching, route params, authentication, and surrounding app context; swap only the relevant rendering. When no sensible host exists, create an obviously named throwaway prototype route using project routing conventions.

Use the page's available data and existing component/styling system. Give variants clear exported component names. Each must differ in layout, information hierarchy, and primary affordance; redo similar drafts. Share components only where each variant retains structural freedom. Keep interactions read-only or stub mutations.

Select variants through the shareable, reload-stable `?variant=` URL parameter, updated through the project's router.

## Switcher

Use one shared component, located with shared UI, fixed at bottom-center and visually distinct from the evaluated design:

- Previous/next arrows cycle with wraparound.
- Label shows the current key and its name when available.
- Keyboard left/right arrows cycle except while an input, textarea, or contenteditable element has focus.
- Hide the switcher in production builds.

Give the user the URL and variant keys; allow combining parts from different variants.

## Capture and integrate

Record the selected design and why. Capture the complete variants and switcher on a throwaway branch as a primary source, following the shared prototype rules.

Rewrite the accepted design to production standards in its existing host or a real new route. Main retains the accepted implementation; remove losing variants, the switcher, and any temporary route.
