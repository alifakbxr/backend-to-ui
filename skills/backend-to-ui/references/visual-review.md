# Visual review — stop-ship gates

**Do not confuse a passing build with good design.** Review the rendered interface the way a product designer reviews a working prototype, not a CSS linter reviews code. Screenshot inspection is required when render tools are available.

## Contract-aware review

Before judging a screenshot, read the project's `UI_CONTRACT.json`. Evaluate **the product-specific direction that was recorded**, not the taste of the current model. If an existing brand is user-approved, preserve it; if the design is provisional, distinguish observations from creative choices. No lint script can certify that a UI is visually excellent.

## Review sequence

1. Capture the **first meaningful screen** at a representative desktop viewport, a narrow phone, and one intermediate width when possible. Use real or clearly identified representative data; record viewport sizes.
2. Inspect the complete page and the **interaction close-up**: primary control, empty/loading state, confirmation/result, navigation and any overlay. Test the actual user journey, not just the static landing.
3. Name the **three highest-impact defects**, in priority order, and distinguish visual issues from functionality or backend issues. Use evidence: location on screen, current behavior, why it conflicts with the product's task.
4. Fix the root cause in composition, hierarchy, copy, real assets or interaction. Do not mask an undersized core feature with shadows, gradients or animations.
5. Re-capture the relevant viewport(s) and compare before/after. Repeat until no serious stop-ship defect remains or disclose the limitation.

## Five stop-ship gates

All gates must be checked, not scored by taste alone:

| Gate | Fails when | Correction |
| --- | --- | --- |
| **Product fit** | UI looks interchangeable with an unrelated product; tone contradicts audience | Revisit user job and mode; select specific subject matter, language and affordance |
| **Viewport composition** | Main content is undersized/stranded, excessive unused area, important activity below fold without reason | Reallocate width/height to the primary task; adapt layout rather than just center a fixed-width card |
| **Hierarchy and density** | Badge rows, nav chrome or decoration compete with the main action; everything looks equally important | Remove/relegate noise; use type, scale, grouping and whitespace to make priorities unambiguous |
| **Material and motion** | Fake data/art, inconsistent iconography, generic marketing copy, motion unrelated to feedback | Use appropriate authentic assets; make feedback causal and restrained; respect reduced motion |
| **Usability and states** | Unreadable copy, invisible focus, broken interactions, overlap/overflow, vague loading or error response | Fix accessible structure and real states, then test desktop/mobile behavior |

A serious failure in product fit, composition or usability **blocks a claim of visual readiness**. Minor polish debt can be disclosed. Never claim a pass without a captured render.

## Anti-slop is not a color blacklist

Gradients, vivid palettes, dark themes, cards and playful micro-interactions can be right for the product. The failure is when they are **unmotivated defaults**. Seek coherent visual logic rather than mechanically banning styles or replacing every interface with white editorial minimalism.

Common tells: huge empty hero, centered phone-sized app on desktop, fake KPI strip, repeated rounded cards, decorative orbs, arbitrary neon, random icon badges, tiny low-contrast labels, overloaded sidebars, data-dump tables for browsing, microcopy that sounds like an API specification, and generic congratulations screens with no product-specific outcome.

## Feedback-driven correction

When the user says "generic", "AI slop", "ugly", or provides a screenshot:
- Treat it as a **failed quality gate**, not an invitation for superficial recoloring.
- Read the screenshot and describe concrete mismatches: task, scale, spacing, hierarchy, material, motion and copy.
- Preserve backend operations and functional behavior. Make a substantive composition change. Show the revised rendered UI when tools allow.
- Never claim an unseen screenshot was inspected; if no browser/device is accessible, say visual verification is pending and provide reproducible steps.

## Delivery evidence

Report: target users/mode, chosen direction, viewport screenshots actually inspected, significant before/after change, real interaction tested, accessibility/performance checks performed and what remains unverified. Keep the summary concise and factual.
