# Design references and independent synthesis

This release was informed by a **representative selection**, not an exhaustive review of every design skill online. These projects are independent: backend-to-ui does not bundle or automatically invoke them. The guidance here is independently written and adapted to the goal of transforming existing backend contracts into usable frontends.

| Public reference | Lesson adapted | Important boundary |
| --- | --- | --- |
| [Anthropic: frontend-design](https://skills.sh/anthropics/skills/frontend-design) | Start from subject matter and make a deliberate visual direction | Do not copy layouts or assume bold decoration equals good design |
| [Impeccable](https://skills.sh/pbakaus/impeccable/impeccable) | Choose the right design ambition for operating vs experiential surfaces; inspect rendered results | No external binary or toolkit required by this skill |
| [Vercel: web-design-guidelines](https://skills.sh/vercel-labs/agent-skills/web-design-guidelines) | Review concrete usability/accessibility defects and fix evidence-backed issues | Browser/device QA still requires accessible tools |
| [UI/UX Pro Max](https://skills.sh/nextlevelbuilder/ui-ux-pro-max-skill/ui-ux-pro-max) | Product category and UX patterns matter | Avoid using a large style lookup as an automatic visual generator |
| [antislop-ui](https://skills.sh/site/craftwork.design/antislop-ui) | For each generic tell, identify why it fails and a functional correction | Do not create a simplistic blacklist of colors |
| [Impeccable: distill](https://skills.sh/pbakaus/impeccable/distill) | Remove competing visual layers and clarify hierarchy | Simplifying is not stripping a playful product of its character |

## What backend-to-ui adds

A skill can be technically correct about backend integration and still render a lifeless template. The distinctive addition here is a **stop-ship visual gate** tightly coupled to backend truth:

1. Establish the user's product mode and actual task before choosing layout.
2. Compare competing compositions rather than restyling one default card shell.
3. Map every meaningful action to real supported operations.
4. Capture real desktop/mobile UI and test the task.
5. Reject layouts that bury or undersize their core experience, even when lint, build and functionality pass.
6. Iterate on composition and content hierarchy before cosmetic changes.

See [visual review](../skills/backend-to-ui/references/visual-review.md) and [contextual cases](../skills/backend-to-ui/references/cases.md).

## License and authorship

Links above are educational references, not dependencies or endorsements. This project does not redistribute their instruction text, images, or proprietary assets. Review original licenses before reusing content from another repository.
