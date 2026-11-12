# Workflow and release gates

This guide explains how the short Agent Skill becomes a complete product interface. It is stack-neutral and does not replace the host repository's architecture.

## 1. Read the product and backend

Inspect existing source, screenshots, brand tokens, user stories, handlers, policies and data shapes. Identify the primary user's task, device and product mode: operate, explore, play, create, read or persuade. Distinguish evidence from inference. A screenshot with negative visual feedback is evidence that the existing UI quality gate failed.

Trace database/query → serialization/page props → network → client state → view. Attach each important control and value to a real authorized operation or field. No fake metrics or unsupported actions.

## 2. Select a composition, not a theme

Outline two truly different options. Choose based on task clarity, proportion, platform, brand fidelity and maintenance. Determine where the user's attention belongs. The defining object or activity should own an appropriate share of the page; header chrome, badges and supporting stats come second.

Decide a coherent typography, spacing, imagery, motion and color system. Avoid the automatic SaaS dashboard silhouette. A playful interactive app may need a large tactile object; a high-volume enterprise screen needs readable density; an editor needs a large canvas.

See [design.md](../skills/backend-to-ui/references/design.md) and [cases.md](../skills/backend-to-ui/references/cases.md).

## 3. Keep data work near its owner

Prefer query-side filtering/aggregation/pagination for large data. Prevent N+1, repeated requests and late-response races; scope private caches. Use existing SSR/SPA/native idioms instead of installing a competing stack. Profile where practical; performance targets are not measured results.

## 4. Implement and verify real flows

Complete the primary user task before decorative polish. Include loading, empty, error, permission and mutation behavior where applicable. Keep controls accessible and test keyboard/touch, reduced motion, focus, narrow layout and latency.

## 5. Run a visual review loop

Capture desktop and phone (plus an intermediate size if feasible), inspect **the actual page**, rank high-impact defects, fix composition/hierarchy first, then capture again. A technically working UI is not ready if its principal feature is lost in a tiny central panel or its visual language could be transplanted to an unrelated product.

Read the full [visual-review.md](../skills/backend-to-ui/references/visual-review.md) gates. A serious product-fit, composition or usability defect is a stop-ship condition, not polish backlog. If no rendering tools are available, disclose that visual review could not be completed.

## Completion criteria

- Primary user flow works through authorized backend operations, or fixtures are explicitly labeled.
- Chosen composition fits the task; real product material and language replace generic filler.
- No fake features, secret exposure or client-only authorization assumptions.
- Requests and rendering are bounded; performance claims are tied to available evidence.
- Screenshot inspection and redesign loop happened when tools permitted.
- Tests, remaining issues and limitations are stated precisely.

**One-shot** means one user prompt can initiate all these stages, not that quality is guaranteed without user context or tools.
