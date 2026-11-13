---
name: backend-to-ui
description: Turn existing backend routes, APIs, models, page props and business rules into complete, fast, accessible, distinctive frontends for any stack. Use for backend-only projects, redesigns, data-heavy UIs and one-shot implementation. Includes context-first art direction, anti-generic design critique, real-data integration and visual verification.
license: MIT
metadata:
  version: "1.2.0"
---

# Backend to UI

Turn **what the backend supports** into **what people need and want to use**. A technically correct interface that looks interchangeable, wastes the viewport, or misunderstands its product is unfinished.

## How to work

One request should run end-to-end when the repository and tools permit, **after the required frontend stack is selected**. Do not stop at a plan or mockup. Keep the existing stack, auth and brand. Ask only about true blockers or high-risk changes **except the mandatory frontend stack decision below**; label reasonable product assumptions instead of inventing facts.

## Mandatory frontend stack gate (before editing UI files)

If implementation or redesign is requested, read [stack decision policy](references/stack-selection.md) **before changing frontend code**.

- If the user explicitly names a frontend stack (including plain/native HTML/CSS/JS), use it unless incompatible with hard repository constraints; explain any conflict.
- If the user explicitly authorizes **reuse of the existing frontend stack** and one is reliably detected, proceed with that stack.
- If no stack is specified or authorized, **ask one direct question**. If the repo uses Vue + Inertia, for example: "I found Vue + Inertia. Should I continue with it, or use another frontend stack?" If no frontend is present: "Which frontend stack should I use?"
- **Do not create or modify frontend implementation files before the answer. Never silently fall back to native HTML/CSS/JavaScript, React, Vue or any other framework.** Backend language, a JSON endpoint, and a package manager alone are not frontend-stack consent.
- A read-only audit may proceed without this question; ask before subsequently implementing changes. Once the stack is confirmed, perform remaining steps autonomously and only ask again for a genuine blocker.

**One-shot** means one request can complete the implementation when the stack decision is already resolved; it does not override this explicit user-choice gate.

1. **Inspect.** Verify the frontend stack gate, then read routes/handlers, schemas, tests, permissions, response shapes, pagination, errors, existing screens, assets, style tokens and product docs. Read [data contracts](references/data.md). Never invent actions, roles, KPI values or endpoints.
2. **Understand.** Identify the real user, job, device, environment, emotional expectation and **product mode**: operate, explore, play, create, read or persuade. Separate observed facts from assumptions. Do not infer the information architecture from database table names. Read [design direction](references/design.md).
3. **Map.** Link each principal user task and visible action to an existing authorized handler, fields, states and recovery flow. Preserve SSR, native, Inertia, GraphQL or other idioms already used; no automatic React/REST rewrite.
4. **Plan for speed.** Trace database → serializer → transport → UI state → rendered view. Plan bounded payloads, pagination, cache scope, request deduplication, cancellation/race safety and efficient list rendering. Read [performance](references/performance.md).
5. **Art direct.** Before writing layout code, briefly consider **two materially different compositions** appropriate to the product; select one and state the rationale in the work. Define the dominant subject or task, visual hierarchy, density, typography, color roles, assets and motion. Be specific to the domain, not a default dashboard skin. See [product examples](references/cases.md). Never use large blank desktop margins to hide a phone-sized UI unless that presentation is explicitly the product.
6. **Build.** Implement the main user flow and its real states. Give the primary interaction an appropriate share of screen space and visual prominence. Make controls legible and functional; provide loading, empty, error, retry, validation, permission and mutation states where relevant. Do not add decorative complexity in place of useful content.
7. **Test, critique, fix.** Run available tests and inspect **actual rendered desktop and mobile screenshots** (plus an intermediate width when possible). Apply [visual review gates](references/visual-review.md) and [functional verification](references/verify.md). If a serious gate fails, **change the design and review again**; do not stop at a CSS tweak or report success based only on a passing build. Test real data timing and request races. If render tools are unavailable, report visual QA as unverified rather than asserting it passed.
8. **Deliver.** Describe what the user can do, real contracts used, the chosen design rationale, notable visual correction(s), performance controls, tests actually run and outstanding risks. Documentation proportional to the project; no required paperwork for its own sake.

## Hard gates

- **Stack truth:** explicit choice or explicit reuse authorization is required before frontend implementation; detected stack alone is not permission. Never default to native HTML.
- **Backend truth:** no fabricated data, fake functionality, hidden authorization bypasses or unsafe client-side assumptions.
- **Product truth:** screen hierarchy must express the product's defining action or subject. A playful game, a dense operations queue and a medical record must not receive the same page shell.
- **Composition truth:** do not ship a tiny central app surrounded by unused desktop canvas, uniform card grids, repeated pill badges or layers of chrome unless they genuinely serve the task.
- **Craft truth:** typography, proportion, assets, spacing, color and motion must form one coherent direction. Avoid gradient/glass/neon/rounded-card defaults; these are allowed only when supported by the product's visual world and executed with care.
- **Interaction truth:** all visible affordances work; important events have feedback; motion respects reduced-motion preferences and performance.
- **Evidence truth:** screenshot critique requires a screenshot, performance claims require measurements, live API claims require live requests. One-shot means one user prompt, **not** one unreviewed visual pass.

## References (read when needed)

- [stack-selection.md](references/stack-selection.md) — mandatory stack choice and one-shot behavior
- [data.md](references/data.md) — real contracts, permissions, state handling
- [performance.md](references/performance.md) — efficient data pipeline, rendering, cache and races
- [design.md](references/design.md) — product modes and evidence-based visual direction
- [cases.md](references/cases.md) — contextual examples including arcade, operations and reading
- [visual-review.md](references/visual-review.md) — stop-ship visual gates and screenshot iteration
- [stacks.md](references/stacks.md) — stack-specific integration choices
- [verify.md](references/verify.md) — functional and evidence-based acceptance tests

## Example trigger

> Use backend-to-ui to build or improve this project's frontend. Understand its users and backend first. Create a distinctive interface, keep real data fast, inspect screenshots, fix generic design, and test the working flows.
