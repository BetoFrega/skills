# Boundaries and transitional architecture

Read when decomposing an application or replacing a capability behind a new boundary.

## Justify the boundary

Compare forces for separation with forces for keeping components together. Separation can improve functional cohesion, independent change, scaling, fault isolation, security, or extensibility. Shared transactions, workflow coordination, code, and data relationships can make separation costly. Investigate actual requirements rather than speculative future needs.

Trace a representative operation across the proposed boundary. Identify synchronous calls, shared storage, libraries, coordinated releases, and failure propagation. State which dependencies remain and whether they permit the agreed autonomy. A new deployment unit can still depend on another unit for every operation or release.

Compare a larger cohesive unit, preparatory decoupling, and the proposed extraction when these are viable. For example, separating a backoffice can enable independent releases, but shared schema changes may still require coordinated deployment. Explain the constraint and how the proposed sequence addresses it.

## Design the intermediate architecture

Consider **Branch by Abstraction** for replacement inside the same process: introduce a stable interface, place old and new implementations behind it, and select the active implementation under controlled activation. Extraction into a separate service is a distinct decision.

Choose temporary adapters, model translation, routing, or synchronization that reduce transition risk. For each selected mechanism, define its purpose, owning team, operating and maintenance cost, and observable removal condition. Include construction and removal in the plan. Assess temporary dependencies as well as the destination architecture.

Boundary design is ready when its benefit, remaining coupling, intermediate states, operational ownership, and removal conditions are explicit enough to implement the next slice.

## Basis

[The Hard Parts, chapter 7](https://www.thoughtworks.com/content/dam/thoughtworks/documents/books/bk_software_architecture_hard_parts_ch7_en.pdf), [Branch by Abstraction](https://samnewman.io/patterns/architectural/branch-by-abstraction/), and [Transitional Architecture](https://martinfowler.com/articles/patterns-legacy-displacement/transitional-architecture.html).
