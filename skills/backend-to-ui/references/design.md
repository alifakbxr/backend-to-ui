# Context-first visual design

## Study the actual product

Prioritize evidence in project docs, routes, models, existing copy/brand, user stories, screenshots, support tickets. Infer likely people and their context cautiously. Separate **observed**, **inferred**, and **unknown**. A healthcare workflow, local restaurant POS, creative portfolio, and issue tracker should not share one UI treatment.

Before drawing, answer:
- Who uses this, on what device, in what setting, to achieve which outcome?
- What does the user need to notice first? What would be distracting or risky?
- Which visual cues are native to this domain? Is the product utilitarian, playful, quiet, editorial, technical, or operational?
- What must persist across desktop/mobile? What can collapse? What cannot be hidden?

Choose one cohesive direction based on those answers. Derive a small token set for color roles, typography, spacing, surfaces, interaction states, motion. Protect genuine whitespace without sacrificing information density. Use imagery/illustration only when it helps the subject; no generic stock graphics as filler.

## Anti-slop pass

Reject or refine if:
- Removing its logo/text makes the screen indistinguishable from unrelated SaaS demos.
- You can swap its data for another industry without changing layout or content hierarchy.
- It uses giant slogans, gradients, glass cards, icon confetti, meaningless chart panels, or emoji as substitutes for a product concept.
- Every view is a grid of cards even though the task is scanning a queue, editing a record, or comparing details.
- Technical terms (schema names, raw statuses, API transport terms) leak into user-facing copy.
- Components use generic empty/error text, hidden actions, poor contrast, jittery loading, or inconsistent density.

## Interaction quality

Make the primary action legible. Use semantic HTML/native controls, visible focus, keyboard paths, sensible touch targets, readable contrast, screenreader labels, and meaningful empty/error recovery. Motion should explain spatial continuity or state change; support reduced-motion and never slow perceived response. Preserve existing design systems if they are established and usable.

Inspect screenshots in at least one desktop and one phone size when tools exist. Critique it as a user in that domain, make a correction, and re-test—not just lint or CSS inspection.
