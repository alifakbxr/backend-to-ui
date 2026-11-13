# Lean workflow — token cost without quality loss

Borrow Caveman's **concise, exact output** principle, not its stylized broken English. Shorter replies reduce visible output tokens; they do **not** compress reasoning, input, tool schemas or repository files. Never claim a reduction without measured usage. See [token-measurement.md](token-measurement.md).

## Progressive disclosure and input control

- Load SKILL.md first; open only task-relevant references and source paths. Do not load every skill reference by default.
- Inspect relevant route/component files, state owners and tests. Use targeted file search and bounded line ranges, not repeated recursive dumps.
- Summarize tool output without losing precise errors, paths, failing assertions or important API/permission data. For long logs show first root error + concise context; retain a path to the full log for recovery.
- Avoid rereading unchanged files and reproducing full code in chat. Use a tiny working ledger: stack, task, affected files, brand source, constraints, acceptance.
- Do not install Caveman, proxy tools, tokenizers, browser plugins, or convert skill text to images automatically. Those tools have setup and validation costs; use them only when available and justified.

## Work lanes

| Lane | Minimum evidence |
| --- | --- |
| Read-only audit | Scoped source evidence, ranked findings; no implementation or contract writes |
| Targeted fix (small fix) | Minimal patch + focused regression; browser only if visual/interaction behavior changed |
| Feature | Real contract map, affected tests, primary browser flow, relevant states |
| Full redesign | Product-specific design directions, approved/observed brand, multi-screen render and interaction QA |
| Backend-only | Explicit stack consent, real handlers/data, main flow, failure and auth checks |

## Execution budget

1. Read relevant source once; record the data and UI boundary.
2. Make one scoped implementation plan, not multiple speculative essays.
3. Patch the smallest correct surface, preserving existing dependencies and working behavior.
4. Run focused tests, then required broader tests only for cross-cutting changes.
5. Inspect real browser output and user interactions if relevant; re-capture screenshots after corrections, not for every CSS tweak.
6. Deliver a short English report: changed files, actual checks and remaining risks; no decorative narration.

**Do not shorten** code, commands, permission reviews, warnings, or errors to the point of ambiguity. No fabricated evidence or claims about total tokens.

## Subagent economics

Read [parallel-work.md](parallel-work.md) **only when two independent workstreams and an exposed host tool make it relevant**. User opt-in is required. Each worker adds initialization, context and reconciliation cost; fewer elapsed minutes does not prove fewer tokens.
