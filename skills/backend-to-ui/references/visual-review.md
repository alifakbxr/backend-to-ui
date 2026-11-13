# Visual review — stop-ship gates

A passing build or attractive code is **not** evidence of a good interface. Review real desktop/mobile renders and changed interactions. If `UI_CONTRACT.json` exists, use its approved/observed direction; otherwise inspect the actual project brand. Never replace it with the current agent's taste.

## Product specificity check

For the redesigned primary screen, provide at least three **source-backed, product-specific choices**:
1. Its defining authentic object/content (e.g. the collectible card, document canvas or packing slip).
2. Proportions, hierarchy or layout clearly motivated by real users/tasks.
3. A meaningful product-specific interaction or state, not a decorative animation.

Use real files, user instructions or observed interactions as evidence. Do not invent facts to satisfy a checklist. **Identity swap test:** if replacing the logo and text makes it work for an unrelated SaaS, the composition remains generic. Fix structure first, not border radii or colors.

For 3D cards, inspect actual artwork/text clarity, physical card proportion, dominant on-screen size, tilt/flip behavior, focus/keyboard/touch and reduced-motion. A screenshot alone **cannot** establish animation fidelity.

## Screenshot loop

1. Capture the **first meaningful screen** at representative desktop, phone and intermediate width where practical; use real or labeled fixture data.
2. Test the actual main route and interaction in a browser (see [live-browser.md](live-browser.md)). Inspect a result, an empty/error state if applicable, and overlays—not only the first frame.
3. Name the three most consequential issues, with location, expected behavior and proof. Separate UI defects from API/backend failures.
4. Correct the underlying hierarchy, proportions, content, state or interaction. Re-render only affected views and retest.
5. Report what was genuinely verified and what remains unverified.

## Five stop-ship gates

| Gate | Fails when |
| --- | --- |
| **Product fit** | Interface is interchangeable with unrelated products; content or tone is fabricated |
| **Viewport composition** | Primary task/object is undersized or stranded behind navigation, whitespace and decoration |
| **Hierarchy / density** | Everything looks equal; cards, pills and metrics drown the main user action |
| **Material / motion** | Fake imagery/data, generic copy, random neon, unjustified effects or janky animation |
| **Usability / states** | Inaccessible contrast/focus, broken buttons, overflow, missing error/recovery or mobile input |

**Stop-ship:** serious product-fit, composition or usability defects block visual-readiness claims. A missing browser tool means **unverified**, not passed.

## No blanket aesthetic blacklist

Cards, gradients, colors and expressive motion can be right when brand and task justify them. Reject **unmotivated defaults**: fake KPI strips, huge slogans above tiny tools, repeated identical rounded cards, decorative orbs, placeholder art, inconsistent fonts and developer-centric copy.

When a user reports "generic", "slop" or "ugly", investigate **task, scale, hierarchy, identity, assets and behavior**. Don't treat it as a request for another color theme. Preserve working integrations, fix the product-specific direction, and inspect updated renders.

## Delivery

Briefly state the chosen product direction and why, viewport sizes/screenshots actually inspected, interactions tested, substantive correction, accessibility/performance evidence and unverified gaps. Never claim to have seen a screenshot, used DevTools or measured speed without actually doing so.
