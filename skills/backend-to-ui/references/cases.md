# Contextual examples — not templates

These are decision examples, **not code or aesthetics to clone**. Adapt the principles to the target repository and respect existing branding. Do not treat an illustrative operation as a real backend contract.

## Play: capsule / gacha-style arcade

**Observed failure pattern:** a narrow, phone-sized machine sits in the middle of an enormous dark desktop viewport. Red/gold neon panels, badge chips, balances, pity bars and navigation all compete with the game. The machine is technically present yet visually subordinate. Generic dashboard framing takes attention away from play.

**User goal:** understand cost and odds, trigger a pull, feel anticipation, see the result, inspect the collection and try again. This is primarily **play**, not operate or analytics.

**Better decisions:**
- On desktop, allocate substantial space to the machine and reveal/result area; contextualize credits, rates and collection without building an entire admin header.
- At phone width, stack controls naturally while keeping the pull action and visual feedback obvious; do not merely shrink desktop.
- Make machine state visible: ready → committed pull → anticipation → reveal → collected. Feedback and motion should correspond to real state, with skip/reduced-motion support.
- Use subject-specific art and audio only if available and permitted, with fallbacks; no placeholder icon soup or unrelated neon decoration.
- Put probability and pity information where it is discoverable, readable and truthful. Do not hide material odds behind misleading gamification.
- Source inventory, prices, rewards and probabilities from supported backend logic; never simulate paid outcomes in production or fabricate a rarity guarantee.
- Check the viewport: if the machine remains tiny while the page is mostly blank, the layout is not done.

**Do not** convert every game into this exact cabinet composition. A collection-first inventory app may require a completely different dominant surface.

## Explore / Play: 3D trading card viewer (Pokémon TCG)

**Actual goal determines design:** showcase one collectible card's artwork and physicality, inspect details, flip/tilt it and understand context. This is not a SaaS dashboard and does not call for a KPI strip, card-grid marketing hero or made-up rarity statistics.

**Specific decisions to evaluate:**
- Give the card object the main viewport, using realistic card aspect ratio (about 2.5:3.5 for a physical trading card) and preserved readable artwork/text where legitimate assets are provided.
- Tie tilt/flip/glare to pointer, touch or keyboard interaction; avoid decorative infinite spin. Offer reduced-motion controls and a clear neutral pose.
- If the user provides card imagery or a dataset, use it accurately with provenance. Never generate fake card facts and present them as official.
- Prefer `perspective`/`transform`/CSS variables for card surface effects; use a WebGL library only for truly 3D meshes, shaders or scene requirements. Don't install Next.js + Three.js + Framer Motion by reflex.
- Compare a card-focused inspection composition with a collection-led composition **only when a new visual direction is requested**. The user task determines which wins.
- Check real desktop/mobile rendered screenshot, actual interaction (pointer/touch), texture quality, loading, keyboard focus and GPU overhead.

**Anti-slop failure:** a tiny tilted card floating beside fake metrics, an enormous headline, random gradient blobs, and buttons that do nothing.

## Operate: warehouse picking

**User goal:** find the next item quickly, scan or confirm it, recover from a mismatch, move on. Composition favors a clear task queue, high-contrast quantities and large touch actions, not a hero headline, charts or decorative illustrations. Slow network and offline states matter. Inventory changes must be reconciled server-side.

## Explore: catalogue / Pokédex

**User goal:** recognize an item visually, search by familiar name, compare attributes and open details. Images and familiar labels carry identity; developer schema keys are secondary. Desktop may use a multi-column gallery, but actual item size and detail must remain usable. Empty results teach how to recover.

## Read: clinical record

**User goal:** understand accurate information safely. Favor reliable text hierarchy, units, provenance, chronology and cautious permissions. Creativity belongs in clarity and precise information design, not animations, playful metaphors or glossy cards.

## Create: photo or document editor

**User goal:** manipulate a canvas safely and see the result. Keep the document or media large; tool chrome must support rather than crowd it. Model saving, undo, background processing and error recovery from real capabilities.

## Persuade: product landing

**User goal:** decide if a product is relevant and trustworthy. Open with a meaningful demonstration or specific claim, not three fake KPIs and a generic gradient. Show real evidence and a clear next step, not app chrome borrowed from an admin dashboard.

Across all examples, the shared rule is **task-first composition + honest backend integration + screenshot review**. The visual result should not be identical across modes.
