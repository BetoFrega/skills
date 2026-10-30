# Subtract Before You Add

When evolving a system, remove complexity first, then build on the simpler base.

Make simplification a continual investment. Leave the design slightly simpler and more
capable, behind the same or a smaller surface than you found.

- Sequence removal before construction: delete dead code, obsolete adapters, redundant
  validators, and stale references before adding the new part.
- **Simplify again in the same change.** A new part may grow while you find its
  shape. Once it works and before delivery, merge the duplicates it created, remove
  its scaffolding, and delete the code it made redundant.
- Cut before you polish. Reach the minimum before investing in quality.
- Design for observed usage.
- Simplify instructions as well as code: remove redundant rules, excessive templates,
  and stub references with no novel content.
