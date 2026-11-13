# Optional multi-agent execution — user opt-in, not default

**The main agent remains accountable.** A swarm is a productivity option, not a quality guarantee. Parallel agents commonly **increase total tokens**, even if they reduce elapsed time. Never invoke a subagent, \`/swarm\`, \`/teamwork\`, delegated coding agent, or paid agent team without an explicit user opt-in for this task.

## Eligibility check (cheap)

Offer the choice **once**, only when all are true:
- At least **two independent, meaningful workstreams** exist (e.g. read-only backend contract audit and existing-UI review, or tests on a separate isolated fixture).
- The host exposes an actual subagent/swarm tool; don't invent capabilities.
- Dependencies, integration, costs, and merge conflict risks have been considered.
- The user hasn't already approved/refused this approach for the task.

A simple bug fix, small page update, single tightly coupled flow, or task without suitable tooling stays **single-agent by default**. If another mandatory question (especially stack choice) is unresolved, ask that first, then the optional choice only if still appropriate.

Suggested **single, direct question**: *"Pekerjaan ini bisa dibagi menjadi audit backend dan audit UI. Mau saya gunakan subagent/agent swarm agar bisa paralel, atau tetap satu agent yang lebih hemat token?"* Include that parallel workers may use more aggregate tokens. If user says **no**, continue solo without revisiting. If user says **yes** but no tool is available, explain and use a single agent—do not simulate worker output or invent execution logs.

## Tool selection (capability, not host branding)

- **Antigravity CLI (\`agy\`):** \`/swarm <task>\` is documented; \`/teamwork <task>\` is plan-dependent. Only recommend/use when present in this session and the user approved. Interactive slash commands are entered *inside* AGY, not as \`agy skills ...\` shell subcommands.
- **Other coding agents:** use their actual delegation/subagent mechanism if exposed in the current session, otherwise single-agent. Never assume feature parity across Codex, Claude, Gemini, or ChatGPT. No fake agent teams.
- **Agent's own explicit tools** take precedence over shell prompt tricks. Respect permissions, rate limits, quota and costs. User consent to parallelism is **not** permission for deployment, destructive tests or unattended security-sensitive actions.

## Efficient coordination after approval

1. **Freeze a short shared context:** task, approved stack, UI contract source, repo SHA, test acceptance, off-limits files. Send this once—not a transcript, full README or repeated file dumps.
2. **Partition by stable, non-overlapping ownership.** Read-only discovery can be parallel. If workers write code, grant disjoint files/modules or separate worktrees, never the same files. Avoid two workers redesigning the same screen.
3. **Use minimum necessary workers** (typically two) and limit each to one bounded result; no swarm-of-swarms, recursive delegation or redundant design exploration.
4. Require each worker to return **only:** \`files inspected/changed\`, 3 highest-impact findings, actual tests run, evidence paths, unresolved blockers. Keep results short (target <= 200 words/workstream). Link to actual artifacts instead of quoting whole logs.
5. **Main agent integrates and owns QA:** reconcile decisions against one approved design contract, run one combined build/test, inspect live browser flow, review diff and merge conflicts.
6. If parallel output diverges, pick based on evidence/contract, not voting or model taste. Do not claim a token saving or a speedup without measuring before/after.

## Execution examples

Suitable: inspector A maps backend authorization and data; inspector B audits existing UI and assets; coordinator resolves contract and implements the approved direction.

Unsuitable: workers each generating a fresh frontend from the same prompt, workers independently inventing a brand, several agents editing shared layout/tokens, or duplicate full-repository scans.

**Success = verified integrated product**, not a report that many agents were spawned.
