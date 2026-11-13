# Optional parallel work — only with explicit user opt-in

**Default: one agent.** Swarms often reduce wall-clock time while increasing **aggregate token use** (may **increase total tokens**) and coordination overhead. Never invoke a subagent, `/swarm`, delegated agent or agent team without permission for **this** task.

## Eligibility

Offer a choice **only when** the host exposes real delegation tools, the task has at least two independent substantial workstreams, and concurrent work avoids blocking dependencies. A single card/landing page, small bug, or one tightly coupled feature **does not qualify**. Resolve the mandatory frontend-stack question **first**. Do **not** show the two questions in the same turn. If there is no independent work, skip the swarm question entirely.

**English-only option:**

> This task has independent workstreams. Would you prefer parallel subagents (possibly faster but more total tokens) or one agent (lower overhead)?

If declined, proceed single-agent without repeating the offer. If accepted but the host lacks tools, explain briefly and work alone; never simulate a swarm.

## Per-host use

- AGY: `/swarm <task>` and potentially plan-dependent `/teamwork <task>` **inside interactive AGY**, if available. No assumption that the current session supports them.
- Codex, Claude or other hosts: use **only their actual exposed subagent tools**, not made-up commands.
- Do not automatically install plugins, spawn extra paid agents, alter permissions, or deploy anything under the guise of parallelism.

## After approval

1. Delegate to the **minimum useful** workers (normally two); freeze project commit, approved stack, design contract, constraints and acceptance criteria.
2. Divide independent read-only research or disjoint file ownership. Avoid overlapping edits to app shell, styling tokens or the same route.
3. Send only scoped paths, task and acceptance tests; not entire transcripts, dependencies or unrelated source files.
4. Each worker returns brief results: relevant files, up to three findings, evidence paths, actual tests, blockers. Target <=200 English words per worker.
5. **Main agent integrates and owns QA**, reviews diffs, resolves contract conflicts, runs combined tests and verifies live browser behavior. Do not declare success because workers finished.
6. Record actual tokens/time for A/B comparison if available; never claim swarm saved tokens without measurements.

Suitable: one worker audits API permissions, another audits existing UI, coordinator owns fixes. Unsuitable: two agents independently generating different designs for one Pokémon card.
