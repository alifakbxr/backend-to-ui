# Lean execution — minimize context and tool calls without sacrificing evidence

**Goal:** reduce **unnecessary** token consumption and redundant work, not the amount of verification required by the task. Parallel workers may be faster in elapsed time but often cost **more** aggregate tokens.

## Progressive disclosure

- **Skill discovery:** metadata describes *when* to invoke this skill; load this file first.
- **Always-required references** on implementation: stack-selection, design-contract. Then load only **relevant** sections for the task; avoid reading all case studies, stack guides and testing manuals indiscriminately.
- **Existing project:** inspect route/component entry points, relevant tests, local tokens and data owner first. Targeted \`rg\`/file globs before deep reads; avoid dumping the entire repo, giant logs, lock files, binary files or all endpoints.
- Preserve a **tiny task ledger**: authorized stack; task; affected paths; existing UX identity; data source; acceptance criteria; risk. Update on meaningful discoveries, not on every tool call. Don't repeatedly summarize the same facts to the user.

## Risk-aware execution lane

| Lane | Choose when | Minimum work |
| --- | --- | --- |
| Audit-only | User asked to inspect, no edit | Scoped reads → prioritized, source-backed findings; no contract writes |
| Targeted fix | Small bug/copy/style change, no new design world | Existing tokens/stack → minimal patch → focused test; live browser if UI behavior/render changes |
| Feature | New flow or moderate screen changes | Map relevant contracts → implement → affected tests → browser interaction + viewport check |
| Full redesign | Product layout/identity or multi-screen rewrite requested | Preserve map → design alternatives + contract → incremental implementation → cross-screen live QA |
| Backend-only | Build UI from real backend | Stack consent → relevant handlers/data → real UI flow → validation and browser testing |

Do not turn a button-label fix into a research paper, design-system rewrite or a fresh \`UI_CONTRACT.json\`. Do not skip interaction checks for a stateful UI because the patch is small.

## One-pass approach

1. **Read** just enough code to identify the true data and component boundary; batch relevant files rather than reopening them repeatedly.
2. **Decide** scope, risk, contract/brand reuse and tests once. Don't generate several long plans or multiple new docs unless required.
3. **Change** the smallest correct set of files. Reuse installed dependencies; avoid new frameworks, duplicate state sources and deep generic abstractions.
4. **Check** fast targeted tests first; if a relevant failure appears, fix it before running heavier checks.
5. **Live verify** the changed user journey using existing browser/DevTools tool when available; inspect screenshots once after changes, repeat *only for corrections*.
6. **Conclude** in a short evidence-oriented summary. Report missing checks accurately; never claim savings, speed, or quality without measurement.

## Delegation cost control

Use [parallel-work.md](parallel-work.md) only **after explicit opt-in**. Don't spawn agents to decide whether spawning agents is helpful. Delegate isolated work with short file-based briefs; require small summaries with artifact paths. One coordinator owns final integration and testing.

## Hard constraints

- Don't drop the mandatory **stack choice** question when required.
- Don't truncate security/permission checks to save tokens.
- Don't infer design approval from model preference or a stale screenshot.
- Don't force users to approve a long form or create persistent files for trivial work.
- If tool/browser environment is unavailable, do not simulate it.
