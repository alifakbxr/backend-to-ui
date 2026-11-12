# Verification: engineering and visual quality

A skill instruction can ask for quality but cannot guarantee it. **Claims must match observed evidence.** Run available checks, capture screenshots where possible and report limitations explicitly.

## Functional acceptance

- Main user task works from real entry point to a meaningful result; no dead controls or invented backend actions.
- Values and actions map to authorized contracts; no fake metrics, unsupported odds, unverified reward or price data.
- Forms cover validation, pending, double-submit prevention, success, server conflicts and recovery.
- Loading, empty, permission denial, offline/timeout and retry states are deliberate.
- Back/forward, deep links, search/filter/pagination, long content, keyboard and touch interaction work.

## Data and performance

- Profile real network/render behavior when available; avoid subjective claims of speed.
- Test slow API, burst interactions, duplicate in-flight requests, A/B search races, 10x representative data, list DOM growth and session/tenant cache isolation.
- For games and interactive tools, test animation cost, input responsiveness, reduced motion and meaningful feedback during asynchronous operations.
- Run available build, tests, typecheck and browser/device checks; write down what actually ran.

## Visual acceptance: stop-ship

Read [visual-review.md](visual-review.md) and apply every gate. Capture the **dominant screen**, not just a cropped component. Inspect desktop, mobile and a middle viewport if possible.

1. Product fit: can a new user recognize this exact product and its primary activity?
2. Composition: does the main task or subject own the right amount of viewport, especially at desktop size? No stranded narrow widget unless explicitly intended.
3. Hierarchy: do primary activity, next action and vital context win over navigation, badges and decoration?
4. Material: do copy, imagery, colors, type, density and motion make sense for this product?
5. Accessibility/states: is the interface readable, keyboard reachable, responsive and functional?

**Stop-ship:** a severe product-fit, composition or usability defect means visual readiness is not established even when code compiles. Make a substantive correction, re-capture and test again.

## Review feedback handling

When a user provides a screenshot or says “AI slop,” “generic,” or “ugly,” do not dismiss it or recolor the background. Identify the actual failure in hierarchy, viewport usage, product semantics and interaction. Preserve valid backend behavior while changing the appropriate visual structure. If only screenshots were provided and code isn't accessible, offer an actionable audit without falsely claiming it was implemented.

## Closing report

Report: main workflow built, real endpoints used, design rationale, **visual changes made**, actual viewport screenshots reviewed, data-performance decisions, test results and unverified gaps. Do not claim a Lighthouse score, WCAG audit, browser inspection or live integration without doing it.
