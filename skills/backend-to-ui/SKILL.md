---
name: backend-to-ui
description: Build, redesign, audit or improve a real product frontend using its existing stack or actual backend contracts. Use for existing frontend, frontend-only, full-stack and backend-to-UI work; preserve brand and behavior, prevent generic AI templates, verify interactions in a live browser, and optionally offer subagent parallelism.
license: MIT
metadata:
  version: "1.5.0"
---

# Backend to UI

Create a useful product interface **from the real user's task**, never from the host agent's preferred UI aesthetic. The model and agent host have **zero design authority**. Preserve the existing stack, brand, data, architecture and working user flows unless the user explicitly requests a change.

## Load only what the task needs

When this skill is invoked, actually read this file; installation alone does not prove activation. Use **progressive disclosure** to reduce token use: for frontend edits read [stack selection](references/stack-selection.md) and [design contract](references/design-contract.md). Then read only task-relevant references: [existing frontend](references/existing-frontend.md), [backend data](references/data.md), [performance](references/performance.md), [design](references/design.md), [stacks](references/stacks.md), [visual review](references/visual-review.md) or [verification](references/verify.md). [Product cases](references/cases.md) are contrasts, **not copyable templates**.

Follow [lean workflow](references/lean-workflow.md): inspect relevant routes/files once, maintain a short task ledger, avoid duplicate analysis and redundant full-repo reads, reuse project tools, run focused checks before expensive checks, and report evidence briefly. **Do not sacrifice data security or functional testing for token savings.**

## Mandatory frontend stack gate

Before implementation or redesign, require an explicit frontend-stack choice or explicit authorization to reuse the already-detected stack. Otherwise **ask one direct question** and do not edit frontend files until answered. **Never silently fall back to native HTML**, React, Vue or anything else. A read-only audit needs no stack approval. See [stack-selection.md](references/stack-selection.md).

## Design authority and anti-slop

Current explicit user request → user-approved project `UI_CONTRACT.json` → observed existing brand/components/tokens → product evidence → domain conventions. Agent preferences are not evidence.

If `UI_CONTRACT.json` exists, read it before UI changes. If not, preserve existing design sources; for a *substantial new design*, record a source-backed `provisional` contract when useful, not a forced JSON document for a small fix. An `approved` contract requires explicit user approval; an `observed` direction comes from actual project files. Validate recorded provenance using `scripts/check_contract.py` when available. See [design-contract.md](references/design-contract.md).

For a **new** direction compare **two materially different compositions** by user workflow and information hierarchy, not color swaps. Reuse an existing approved composition for small changes. Reject fake KPIs, card spam, decoration hiding the main task, nonfunctional controls and interchangeable dashboard shells. Gradients/cards/bright colors can be correct when justified by the product, not as automatic defaults.

## Optional parallel execution — ask, don't assume

If the host **actually supports subagents/swarm** and a task has at least two independent workstreams, **offer a single optional question**: *"Mau saya gunakan subagent/agent swarm agar beberapa pekerjaan berjalan paralel, atau tetap satu agent yang lebih hemat token?"* Explain that parallelism can use **more total tokens**, although it may finish sooner. Do not launch or imply any subagent without explicit opt-in. Don't ask for trivial/tightly coupled tasks or when the host has no tool. Resolve any mandatory stack question first. If declined, continue alone; don't ask again. Follow [parallel-work.md](references/parallel-work.md) for isolated ownership, short context packets and one coordinator. On AGY CLI, `/swarm` and plan-dependent `/teamwork` exist **inside AGY**, not as generic shell subcommands.

## Work cycle

1. **Inspect.** Choose audit-only, existing frontend, frontend-only, backend-only or integration mode. Inspect only relevant routes, components, design tokens, state, auth, permissions, fixtures, tests and the primary user flow. Don't scan unrelated code without reason.
2. **Understand.** Identify user, device, primary job and **product mode** (operate, explore, play, create, read, persuade). Separate observed, inferred and unknown facts; define the first meaningful action.
3. **Map.** Document the smallest preservation/data map: existing route/role/state boundaries, real backend handlers and response/error shapes where available, or actual local state for frontend-only work. No invented APIs, metrics or permissions.
4. **Plan for speed.** Choose backend → transport → state → render, or local state → render. Apply pagination, request deduplication/race safety, bounded rendering and caching only where relevant. Avoid needless dependencies and multiple data owners.
5. **Art direct.** Reuse approved visual identity. If the user requested a new direction, compare the competing compositions, select one using evidence, choose task-driven hierarchy, density, typography, assets and motion. Don't default to a generic SaaS layout.
6. **Build.** Make the smallest correct changes in the authorized stack and existing components. Complete visible interactions, accessible semantics, mobile/touch paths, loading/empty/error/retry/validation and mutation feedback as applicable.
7. **Test, critique, fix.** Run affected code tests, then use an **actual live browser or DevTools** when available: Playwright, CDP/Chrome DevTools, browser agent or existing browser plugin. Follow [live-browser.md](references/live-browser.md). Exercise the user journey, inspect console/network failures and **actual rendered desktop and mobile screenshots**; fix stop-ship issues and retest. For native apps use native UI tools. If unavailable, explicitly mark live testing **unverified**—never invent traces or screenshots.
8. **Deliver.** Briefly state changed files, preserved behavior, design source/status, real tests/viewport evidence, performance observations and unverified gaps. Claim activation, host compatibility or token savings only when actually verified.

## Stop-ship criteria

- **Stack:** no frontend edits before the mandatory choice; no surprise replatforming.
- **Brand:** no agent-designed replacement for a user-approved identity.
- **Backend:** displayed data/actions are real or clearly labeled fixture; enforce real permissions.
- **Experience:** dominant product task visible and appropriately sized; no fake UI functionality.
- **Quality:** severe product-fit, accessibility, interaction, responsiveness or visual composition defects require correction, not just recoloring.
- **Evidence:** passing build or contract validation is **not** live browser QA or proof of aesthetic quality.

## Reporting contract (keep concise)

Before edits: `mode · selected stack/consent · primary task · preservation constraints · design source`. After edits: `changed files · working flows · checks actually run · rendered evidence · unverified`. Don't produce a long strategy memo for a small fix.

## Host check

Antigravity CLI executable is `agy`, not `gemini`. For AGY/IDE install discovery and skill activation, see [host-compatibility.md](references/host-compatibility.md). From a cloned repository, `python3 skills/backend-to-ui/scripts/doctor.py --host antigravity-cli --strict` verifies files on disk, **not** activation inside AGY.
