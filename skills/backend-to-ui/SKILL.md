---
name: backend-to-ui
description: Build, audit or redesign real product frontends using approved stacks and real backend contracts. Preserve brand and interactions, reject generic AI templates, verify live browser flows, and optionally offer user-approved subagents.
license: MIT
metadata:
  version: "1.6.0"
---

# Backend to UI

Design for **this product**, not the model's usual UI. User instructions, brand, real content and task come first. Model taste has **zero design authority**.

## English-only agent communication

Use **English for all agent-facing questions, option labels, recommendations, progress, reviews, summaries and subagent instructions.** Never switch language because of an example in a reference. Preserve exact commands, symbols and errors. The *application UI's locale* still follows the user's specification and existing project localization; do not translate it automatically.

## Progressive disclosure and token efficiency

Read this entrypoint on invocation; installation alone does not prove activation. For UI edits, consult [stack-selection.md](references/stack-selection.md) and [design-contract.md](references/design-contract.md). Open only task-relevant guides: [existing-frontend.md](references/existing-frontend.md), [data.md](references/data.md), [performance.md](references/performance.md), [stacks.md](references/stacks.md), [design.md](references/design.md), [visual-review.md](references/visual-review.md), [live-browser.md](references/live-browser.md), [verify.md](references/verify.md) and [cases.md](references/cases.md). Cases contrast product types; never copy their look.

Follow [lean-workflow.md](references/lean-workflow.md): inspect relevant files once, use concise technical English, summarize errors instead of dumping logs, avoid duplicate plans/scans, and stop after verified acceptance. Caveman-style *short replies* do not compress input or reasoning. **No claimed token savings without measured AGY usage**; see [token-measurement.md](references/token-measurement.md).

## Mandatory frontend stack gate

If the stack is explicitly chosen or the user explicitly authorizes reuse of the unambiguous existing stack, proceed. Otherwise **ask one direct question** and **do not create or edit frontend implementation files until answered**. Read-only audits are exempt. **Never silently fall back to native HTML**, React or another preferred stack. Recommend the **smallest justified stack**: a CSS-tilted 3D card does not automatically require Next.js, Three.js or Framer Motion. Never bundle libraries as a single "recommended stack" without task evidence.

## Product-specific anti-slop

Preserve observed project brand/tokens; use an existing `UI_CONTRACT.json` where present. Creating one is optional for small changes. A design is `approved` only with user evidence, `observed` when supported by project files, otherwise `provisional`. For a new visual direction, compare **two materially different compositions** in flow/hierarchy; reusing an approved direction needs no new alternatives.

The primary task or product object must dominate the screen. Make **product-specific proportions, content and actions**, not a reusable hero + metrics + card grid. Fake KPIs, decorative 3D, inactive buttons, arbitrary neon and tiny core objects are stop-ship findings. Evaluate actual browser output, not code aesthetics alone. See [design.md](references/design.md) and [visual-review.md](references/visual-review.md).

## Optional agent swarm — ask only when justified

If **two independent workstreams** and an actual host subagent tool exist, **after** resolving the stack question, the agent may ask: "This task has independent workstreams. Would you prefer parallel subagents (possibly faster, higher total token use) or a single agent (lower overhead)?" This is **explicit opt-in**. **Never ask it for a single card/page, tightly coupled task or small fix.** Never display it alongside another unresolved question; **if declined**, proceed solo. Do not invent agent capabilities. See [parallel-work.md](references/parallel-work.md).

## Work cycle

1. **Inspect.** Identify audit, existing frontend, backend-only or integration mode. Read affected routes, components, assets, auth/permissions, state and tests; skip irrelevant files.
2. **Understand.** Identify real users, device, defining object/action and **product mode** (operate, explore, play, create, read, persuade). Separate facts from assumptions.
3. **Map.** Preserve working routes, components, localized copy, design tokens and permissions. Map actual backend operations, or genuine local state; never invent API features.
4. **Plan for speed.** Trace data → state → render, avoid redundant queries, request races, unbounded DOM and dependencies without benefit.
5. **Art direct.** Choose or reuse product-backed composition, typography, density, imagery and interactions; reject default agent layouts.
6. **Build.** Make scoped changes in the authorized stack; complete accessible and responsive user flows, loading, empty, error, retry and mutation states as applicable.
7. **Test, critique, fix.** Run relevant tests and **actual live browser** checks (DevTools, Playwright or available browser agent); inspect actions, network/console and **actual rendered desktop and mobile screenshots**. Fix failures; if tooling is unavailable, mark visual QA **unverified**.
8. **Deliver.** Brief English summary: changed files, preserved flows, functional checks, real render evidence, risks. No fictitious agent activation or benchmarks.

## Hard gates and reporting

- Stack consent, real data/permissions, task-first composition, functional controls and screenshot evidence are mandatory when applicable. Build passing != visually ready.
- Before edits: `mode | stack approval | primary task | preserved constraints`.
- After edits: `changed files | verified flow | screenshots/tests | unverified`.
- Keep code/docs precise; do not sacrifice security, accessibility or necessary clarity for brevity.

## Host guidance

AGY uses `agy`; interactive `/skills` checks activation. In AGY, `/context` lists the tokens loaded from Skill files. For separate headless tasks the terminal JSON `usage` is real session telemetry, **not skill-only cost**. See [host-compatibility.md](references/host-compatibility.md) and [token-measurement.md](references/token-measurement.md).
