# Product-led design direction

Visual taste is not a list of banned colors. It is making choices that belong to a particular product, audience and task.

## 1. Establish evidence, not a template

Inspect the brief, brand, existing UI, screenshots, copy, routes, product docs, imagery, domain terminology, primary device and user constraints. Keep three buckets: **observed** (source-backed), **inferred** (plausible, reversible) and **unknown** (do not fake). If a user's aesthetic feedback conflicts with an existing visual direction, explicitly resolve it rather than recycling the old theme.

Answer these before implementation:
- Who is using this, where and why? What is the first meaningful action?
- What deserves the most space, contrast, detail or animation? What is secondary?
- What feeling fits this moment: focus, trust, anticipation, play, calm, discovery or urgency?
- What source material is the product made of: characters, data, objects, words, photos, maps, tools, transactions?
- What already exists and should stay (brand, components, permissions, platform behavior)?

## 2. Choose a product mode

Modes guide priorities, not rigid templates. A product may mix modes by screen.

| Mode | Core priority | Typical composition failure |
| --- | --- | --- |
| **Operate** (admin, POS, ops) | Decisions, scanning density, low-friction action | Giant decorative hero above the actual queue |
| **Explore** (catalogue, discovery) | Subject recognition, browsing, comparison | Empty hero, identical cards with generic metadata |
| **Play** (games, interactive toys) | Main interactive object, feedback, delight, clear stakes | Tiny game widget in a large dashboard shell |
| **Create** (editors, builders) | Canvas/workspace, tool affordances, safe undo | Marketing cards occupying workspace area |
| **Read** (docs, records) | Text hierarchy, navigation, legibility, focus | Excessive ornament, line length and competing controls |
| **Persuade** (marketing) | Clear promise, credible proof, conversion action | Unrelated metric cards and filler gradients |

Do not choose a mode from framework or endpoint names. Choose from the user's goal.

## 3. Draft two competing compositions

Before coding, sketch two **meaningfully different** arrangements in a few sentences, not merely two color palettes. Compare them on task clarity, subject prominence, responsive behavior, accessibility, originality and implementation cost. Select one. Avoid creating a large planning artifact unless useful to the repository.

For example, an arcade gacha game could be:
- **Immersive cabinet:** a prominent interactive machine, tight contextual controls, integrated balance, a collection drawer, celebratory results.
- **Collection-led:** a gallery-first view with a compact pull interaction, suitable only if cataloguing is the principal job.

Picking immersive play while rendering a tiny cabinet in a mostly blank desktop viewport is a contradiction. Fix composition, not just colors.

## 4. Build a recognizable visual language

- **Composition first:** establish task flow and visual mass in grayscale; use available viewport intentionally. Negative space should direct attention, not strand the experience.
- **Typography:** choose voice, type scale and widths for this product. Limit redundant uppercase labels and microcopy; hierarchy must remain legible on mobile.
- **Color:** derive roles (surface, text, action, feedback, highlights) from existing identity or subject matter. Test contrast. No blanket ban on bright color: an arcade may legitimately be vivid; use it intentionally.
- **Assets:** prioritize authentic product images, symbols, illustrations or actual records when permitted. Empty icons, random emoji, fake photos and irrelevant stock artwork are not a substitute.
- **Components:** choose forms, tables, shelves, trays, maps, canvases or grids according to task. Do not impose a uniform four-card dashboard.
- **Motion:** animate cause and effect, continuity and reward; avoid gratuitous perpetual movement. Support reduced motion and never delay an important result solely for spectacle.
- **Copy:** speak the user's language. Hide developer plumbing (API transport, schema keys, debug terms) from product UI unless the user is a developer.

Existing brand systems take priority when they are coherent. Do not overwrite working design tokens simply to show novelty.

## 5. Reject generic solutions by evidence

Perform three questions after the first render:
1. **Identity swap:** could another product replace the logo and data without changing layout? If yes, the direction is insufficiently contextual.
2. **Task prominence:** is the defining subject/activity immediately visible and appropriately sized? Is a decorative shell using more room than the product?
3. **Material honesty:** are the imagery, language, affordances and motion truthful to the domain rather than unrelated design trends?

If any answer reveals a serious defect, change the layout or hierarchy first. Border-radius and gradient tweaks are not a redesign. Use [visual-review.md](visual-review.md) for stop-ship review and [cases.md](cases.md) for examples.

## Accessibility is part of craft

Semantic controls, keyboard/screenreader paths, contrast, touch targets, readable size, focus indication, reduced motion and sensible responsive structure are requirements. A visually distinctive UI that blocks use is not successful.
