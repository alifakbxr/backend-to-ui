---
name: backend-to-ui
description: Turn existing backends, APIs, server routes, database-backed endpoints, Inertia props, GraphQL, RPC or realtime contracts into complete, fast, accessible, human-centered frontends. Use when building UI from backend-only code, connecting frontend to real data, redesigning a full-stack app, fixing slow data-heavy screens, or implementing a working frontend in one prompt. Works with any tech stack.
license: MIT
metadata:
  version: "1.0.0"
---

# Backend to UI

Transform **what the backend can do** into **what people need to do**. Make a usable product, not a JSON viewer or a generic dashboard.

## How to work

One user request = one end-to-end execution when the repository and tools allow it. Do not stop after producing a plan or a mockup. Respect the user's scope and existing code. Ask only for genuinely blocking information or irreversible/high-risk changes; otherwise make conservative assumptions and name them.

1. **Inspect.** Identify stack, architecture, actual routes and handlers, auth/permissions, payload shapes, pagination, validation, failure semantics, existing frontend, and repository conventions. Read [contracts](references/data.md) before wiring data. Never invent unsupported CRUD, roles, charts, metrics or APIs.
2. **Understand.** From names, workflows, and product evidence, infer the user's job, device, vocabulary and most important action. Distinguish observed facts from assumptions. Read [design](references/design.md). Choose a visual language appropriate for the domain, not an automatic "AI SaaS" aesthetic. Existing brand and components take precedence.
3. **Map.** Connect each important user task to an endpoint/handler, authorization, request/response field, UI state, and recovery path. Favor direct, idiomatic integration: Inertia page props where they exist, SSR/templates where appropriate, native patterns on mobile; do not force REST + React.
4. **Plan for speed.** Before building large screens, define data volume, who filters/sorts, page/cursor strategy, N+1 avoidance, payload projection, concurrency, caching scope, reactive ownership, and failure behavior. Read [performance](references/performance.md). Never solve a server-scale problem with an enormous browser array.
5. **Build.** Implement the top user task all the way through. Include loading, empty, error, retry, unauthorized/forbidden, validation, and mutation state where applicable. Provide natural copy, keyboard controls, responsive layout, accessible semantics, and real interactions. Use current project's libraries and architecture unless there is a demonstrable reason not to.
6. **Test, critique, fix.** Run real available tests/builds and inspect actual UI if browser/device tools exist. Test cancellation/races, failed and slow requests, long lists, permissions, and small screens. Review whether the interface fits its users; make at least one substantive correction where warranted. Read [verification](references/verify.md). Never call fixtures "live" or target budgets "measurements".
7. **Deliver.** Summarize changed files, working user flows, real endpoints, safeguards for performance, tests run, unverified areas, and follow-up risks. Create lightweight design/contract notes only when they clarify maintenance; no mandatory documentation ceremony.

## Non-negotiables

- **Backend truth.** Every displayed value or action is backed by a real field/operation or explicitly labeled demo data. Never bypass permission checks.
- **User truth.** Information architecture comes from tasks, not the names of database tables. Clarity before decoration.
- **Speed truth.** No unbounded list DOM, unconditional full-database downloads, uncontrolled request fanout, duplicate request storms, stale search results, cross-tenant cache leaks, or expensive transformations on every render.
- **Design truth.** No default gradient hero, glass cards, ornamental blobs, fake KPIs, infinite badge lists, or oversized headings used to disguise thin content. A screen must feel right for this exact product.
- **Evidence truth.** Test claims require execution. Report tool/network limits honestly. One-shot means one *request*, not skipping analysis or QA.

## References (read only as needed)

- [data.md](references/data.md): inspect backend + contract-to-UI + auth/mutations
- [performance.md](references/performance.md): API/client data pipeline, pagination, race safety, budgets
- [design.md](references/design.md): human context, visual system, anti-slop critique
- [stacks.md](references/stacks.md): idioms across server, SPA, native, realtime stacks
- [verify.md](references/verify.md): UI, functional, security, performance and acceptance tests

## Example trigger

> Use backend-to-ui. Build the frontend for this repository from the existing backend. Keep all current business logic. Make the UI appropriate to its users, fast with real data, and test it.
