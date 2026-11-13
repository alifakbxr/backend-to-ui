# Product-mode contrasts — not design templates

These are *task distinctions*, not components/styles to clone. Preserve real brand, authorized data, existing frontend and functional behavior.

## Play: gacha / capsule arcade

The user triggers a pull, understands cost/odds, watches feedback, gets an actual result and inspects the collection. **The machine and reveal dominate the canvas**; don't bury them inside a dashboard with badge spam. Test ready → pull → reveal → collected, failure/retry, skip/reduced-motion and mobile. Odds, balances and inventory come from real contracts. Do not fabricate rewards or probabilities.

## Explore / Play: 3D trading card (Pokémon TCG)

The core product is a **physical trading card**, not a SaaS dashboard. For inspection, preserve a plausible card ratio (approximately 2.5:3.5), authentic supplied art/text and a card-sized focal object on both desktop and mobile. Follow the user's intent—showcase, flip, tilt, glare, inspect details, or browse a collection.

- Prefer CSS perspective/transforms for tilt/flip/glare when sufficient; use Three.js/WebGL only if a genuine 3D scene, shader or mesh is required.
- Tie motion to input and state, allow keyboard/touch and reduced-motion. Do not animate perpetually to fake sophistication.
- Never invent official game/card facts, rarity, inventory, provenance or licensing rights. Label fixtures.
- Two potential **structural** directions: card-first inspection vs collection-first browsing. Choose based on actual user task, not the agent's favorite hero template.
- Test pointer/touch/keyboard, focus, actual rotation and text readability, resource load, desktop/mobile scale and performance.

**Anti-slop tell:** tiny card next to a massive gradient headline, meaningless KPIs, inactive "collect" buttons, or generic feature cards.

## Operate: warehouse picking

Primary job: find next item, scan/check quantity, recover from mismatch and continue. Queue and label/quantity hierarchy beat hero copy, pretty charts or unnecessary illustrations. Preserve barcode/keyboard/scanner paths, status updates, backend consistency and offline/failed request handling.

## Explore: catalogue or Pokédex

Users recognize subjects from images, search familiar names, compare supported attributes and inspect detail. Image size, real filtering, pagination, responsive item cards and empty results matter more than generic analytics chrome. Never claim placeholder metrics are real.

## Read: clinical or regulatory records

Put factual chronology, units, source attribution, readability and access permissions before decoration. Avoid playful data metaphors and unverified clinical claims.

## Create: editor or media canvas

The document/media **dominates available space**. Tools support selection, preview, undo, save and recovery; do not shrink the work surface to frame a decorative sidebar. Test incomplete edits, state persistence and input behavior.

## Persuade: landing page

Show the actual product value, credible source-backed evidence and one relevant next action. Don't invent reviews, growth numbers or a generic 3-card template just to fill sections.

**Shared principle:** source-backed product specificity, real interactions, deliberate viewport composition, and rendered review—not one look for every application.
