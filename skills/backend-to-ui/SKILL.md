---
name: backend-to-ui
description: Turn existing backend routes, APIs, models, page props and business rules into complete, fast, accessible, distinctive frontends for any stack. Use for backend-only projects, redesigns, data-heavy UIs and one-shot implementation. Includes context-first art direction, anti-generic design critique, real-data integration and visual verification.
license: MIT
metadata:
  version: "1.1.0"
---

# Backend to UI

Turn **what the backend supports** into **what people need and want to use**. A technically correct interface that looks interchangeable, wastes the viewport, or misunderstands its product is unfinished.

## How to work

One request should run end-to-end when the repository and tools permit. Do not stop at a plan or design mockup. Keep the existing stack, auth and brand. Ask only about blockers or high-risk changes; label reasonable assumptions instead of inventing facts.

1. **Inspect.** Read routes/handlers, schemas, tests, permissions, response shapes, pagination, errors, existing screens, assets, style tokens and product docs. Read [data contracts](references/data.md). Never invent actions, roles, KPI values or endpoints.
2. **Understand.** Identify the real user, job, device, environment, emotional expectation and **product mode**: operate, explore, play, create, read or persuade. Separate observed facts from assumptions. Do not infer the information architecture from database table names. Read [design direction](references/design.md).
3. **Map.** Link each principal user task and visible action to an existing authorized handler, fields, states and recovery flow. Preserve SSR, native, Inertia, GraphQL or other idioms already used; no automatic React/REST rewrite.
4. **Plan for speed.** Trace database → serializer → transport → UI state → rendered view. Plan bounded payloads, pagination, cache scope, request deduplication, cancellation/race safety and efficient list rendering. Read [performance](references/performance.md).
5. **Art direct.** Before writing layout code, briefly consider **two materially different compositions** appropriate to the product; select one and state the rationale in the work. Define the dominant subject or task, visual hierarchy, density, typography, color roles, assets and motion. Be specific to the domain, not a default dashboard skin. See [product examples](references/cases.md). Never use large blank desktop margins to hide a phone-sized UI unless that presentation is explicitly the product.
6. **Build.** Implement the main user flow and its real states. Give the primary interaction an appropriate share of screen space and visual prominence. Make controls legible and functional; provide loading, empty, error, retry, validation, permission and mutation states where relevant. Do not add decorative complexity in place of useful content.
7. **Test, critique, fix.** Run available tests and inspect **actual rendered desktop and mobile screenshots** (plus an intermediate width when possible). Apply [visual review gates](references/visual-review.md) and [functional verification](references/verify.md). If a serious gate fails, **change the design and review again**; do not stop at a CSS tweak or report success based only on a passing build. Test real data timing and request races. If render tools are unavailable, report visual QA as unverified rather than asserting it passed.
8. **Deliver.** Describe what the user can do, real contracts used, the chosen design rationale, notable visual correction(s), performance controls, tests actually run and outstanding risks. Documentation proportional to the project; no required paperwork for its own sake.

## Hard gates

- **Backend truth:** no fabricated data, fake functionality, hidden authorization bypasses or unsafe client-side assumptions.
- **Product truth:** screen hierarchy must express the product's defining action or subject. A playful game, a dense operations queue and a medical record must not receive the same page shell.
- **Composition truth:** do not ship a tiny central app surrounded by unused desktop canvas, uniform card grids, repeated pill badges or layers of chrome unless they genuinely serve the task.
- **Craft truth:** typography, proportion, assets, spacing, color and motion must form one coherent direction. Avoid gradient/glass/neon/rounded-card defaults; these are allowed only when supported by the product's visual world and executed with care.
- **Interaction truth:** all visible affordances work; important events have feedback; motion respects reduced-motion preferences and performance.
- **Evidence truth:** screenshot critique requires a screenshot, performance claims require measurements, live API claims require live requests. One-shot means one user prompt, **not** one unreviewed visual pass.

## References (read when needed)

- [data.md](references/data.md) — real contracts, permissions, state handling
- [performance.md](references/performance.md) — efficient data pipeline, rendering, cache and races
- [design.md](references/design.md) — product modes and evidence-based visual direction
- [cases.md](references/cases.md) — contextual examples including arcade, operations and reading
- [visual-review.md](references/visual-review.md) — stop-ship visual gates and screenshot iteration
- [stacks.md](references/stacks.md) — stack-specific integration choices
- [verify.md](references/verify.md) — functional and evidence-based acceptance tests

## Example trigger

> Use backend-to-ui to build or improve this project's frontend. Understand its users and backend first. Create a distinctive interface, keep real data fast, inspect screenshots, fix generic design, and test the working flows.
