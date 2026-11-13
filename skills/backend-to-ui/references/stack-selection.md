# Mandatory frontend stack selection

**Scope:** frontend implementation or redesign. Ask stack questions **in English**, regardless of the user's chat language. This is a user-choice gate, not permission for the model to recommend its favorite framework.

## The decision, in order

1. **Read the user's explicit frontend choice.** Examples: React, Vue, Vue + Inertia, Next.js, Angular, Svelte, Flutter, SwiftUI, native HTML/CSS/JavaScript. This resolves the gate. A backend language (Laravel, Django, Go) or API format (REST, JSON, GraphQL) alone does **not** specify a frontend stack.
2. **Check for explicit authorization to keep the project's existing frontend stack.** Examples: "reuse the current frontend framework", "stay with the existing UI stack", "do not replace the frontend framework". Only treat this as sufficient if the actual frontend technology is unambiguous from files and dependencies. If the repository is backend-only, this cannot authorize a nonexistent frontend stack.
3. **Otherwise inspect project files and ask one question in English.** Only one blocking question may be pending: **do not also ask about optional swarm/subagents in the same turn**. If one existing stack is discovered, offer to retain it before suggesting migration. Detection is **context for the question, not permission to implement**:
   - Detected Vue + Inertia: "I found Vue + Inertia. Should I use that for the frontend, or do you want a different stack?"
   - Backend-only Laravel: "Which frontend stack should I use for this Laravel backend (for example, Vue + Inertia, React + Inertia, or another stack)?"
   - Existing static site: "This project uses plain HTML/CSS/JavaScript. Should I continue with that, or use a framework?"
   - Mixed/ambiguous frontend: "I found multiple frontend frameworks. Which one should this work use?"
4. **Do not create or edit frontend implementation files until answered.** Reading the repository, inspecting API contracts, and giving a concise preliminary design assessment are allowed. Do not quietly scaffold plain HTML, install dependencies, pick React, or start generating components.
5. Once the user confirms, continue autonomously through actual mapping, implementation and testing. Never repeat resolved choices. Preserve auth, backend contracts and user decisions.

## Minimum viable stack — minimal-dependency recommendation

A **frontend framework** choice is distinct from optional UI libraries, animation packages, WebGL engines and CSS systems. Never describe several technologies as a mandatory combined "recommended stack" without separate evidence.

For a 3D Pokémon TCG card, evaluate the actual interaction: CSS `perspective`, `transform-style` and pointer motion may suffice for tilt, flip and glare; true meshes, shaders or 3D scenes might justify Three.js. Framer Motion and Tailwind are **optional**, not automatic requirements. Next.js should be considered for actual SSR, routing, content or SEO needs—not simply because "website" appears in the prompt. Preserve existing packages whenever possible. Avoid choosing a different tool for every visual effect.

A good question presents **one minimal recommended framework or existing stack** and asks confirmation, instead of forcing a choice between entire preassembled stacks. Do not choose visual style based on which framework wins.

## Exceptions

- **Read-only audits / design reviews:** can proceed without a selected stack because they do not implement UI. If the user later requests implementation, run this gate.
- **Explicit native HTML request:** use native HTML/CSS/JS. Native HTML is valid when chosen by the user; it is not a fallback.
- **Existing stack explicitly authorized:** "use the existing stack" is sufficient when that stack is unambiguous. Never demand a second confirmation just to create extra back-and-forth.
- **Explicit "choose for me" without naming a stack:** still ask, because this skill intentionally requires a deliberate frontend technology decision. Offer a contextual recommendation in the question if helpful.
- **A user asks to keep everything while changing only copy or styles:** this is still implementation. If no stack is specified or existing-stack reuse authorized, ask first. The goal is predictable behavior, not maximizing zero-question turns.

## Conflict handling

If the chosen stack conflicts with platform requirements or the repository architecture, explain the conflict and ask one focused question about changing the choice. Do not silently override. Do not rewrite backend auth/data contracts just to accommodate a preferred frontend tool.

## Evaluation expectations

For a missing-stack scenario:
- Agent asks an explicit frontend-stack question.
- No frontend files changed; no dependency installation or scaffolding.
- Question can name detected framework, but cannot imply it was already authorized.

For an approved-stack scenario:
- Agent does **not** ask the same question again.
- Agent proceeds through real backend mapping and functional/visual QA.
- Native HTML appears **only** when explicitly chosen.

See [evaluation scenarios](../../../evals/scenarios.json) and [run instructions](../../../evals/README.md).
