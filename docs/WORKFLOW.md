# Engineering workflow and acceptance criteria

This document explains the intent behind the short `SKILL.md`. It is not a universal implementation recipe; the agent must follow the target repository's architecture and user needs.

## 1. Context comes before appearance

Collect evidence from README, user journeys, route names, existing wording, policy classes, tests and existing screens. State who uses the product and what a successful task looks like. Avoid transferring a generic SaaS layout to an unrelated domain.

## 2. Trace the real data path

Inspect database/query → backend handler → serialization/page props → transport → client data owner → render. For each important view, trace where values come from and which operations are authorized. Identify query filters, pagination, validation, errors and lifecycle behaviors. Reject fantasy KPIs and unsupported buttons.

## 3. Keep work near its owner

Prefer query-side filtering/aggregation/pagination for large data; limit payload shape; avoid N+1; add request deduplication and race protection where necessary; scope private caching to authenticated identity and tenant; avoid whole-list rendering. Choose idiomatic techniques for the current framework, rather than imposing a one-size-fits-all client cache.

## 4. Implement end-to-end

Ship the primary workflow before decoration. For each screen account for success, empty, loading, timeout, forbidden, validation, rate limits and recoverable failure where relevant. Use accessible inputs, keyboard control, correct focus, clear status copy and responsive layouts. No inert actions.

## 5. Review with evidence

Tests should exercise the real flows, not only compilation. When available, inspect the rendered desktop/mobile UI, measure network and rendering bottlenecks, and test rapid searching, long records, failed requests, pagination and permissions. Report which checks were performed and which were not possible.

## Completion criteria

- Main user task works through the real backend (or clearly labeled fixtures when live access is impossible).
- UI choices fit the product and user context; no generic fillers or unsupported features.
- Private data is not inadvertently exposed; server authorization remains intact.
- Lists and requests scale reasonably; the agent has evidence for performance claims.
- Responsive design, accessibility and failure recovery have been reviewed.
- Changes, test results and limitations are stated clearly.

**One-shot** means one user request can trigger the full workflow, not that the outcome is guaranteed on every unfamiliar repository.
