# Mandatory frontend stack selection

**English-only question.** User choice controls implementation. A backend language or package manager does not authorize a frontend framework.

1. If the user **explicitly chose a stack**, use it unless incompatible with hard project constraints.
2. If the user **explicitly authorized reusing the existing stack** and the repo clearly identifies it, proceed in-place. Don't ask again.
3. Otherwise, inspect existing frontend files, **ask one direct question**, and wait. Do not create or edit frontend implementation files until answered. Never silently fall back to native HTML, React or any preferred framework. Only read-only audit is exempt.

**Do not combine the stack question with an optional swarm question.** Finish stack choice first. All agent questions, explanatory labels and recommendations must be in English.

Examples:
- Existing Vue + Inertia: "I found Vue + Inertia. Should I keep this frontend stack or use another one?"
- Backend-only Laravel: "Which frontend stack should I use for this project?"
- Multiple frontends: "Which existing frontend should I work in?"
- Existing plain HTML: "Should I preserve the existing HTML/CSS/JS frontend?"

## Minimum viable stack, not a bundle

Distinguish the frontend framework from optional CSS, rendering, 3D, state and animation libraries. Recommend **one minimal stack** grounded in project evidence; do not present Next.js, Tailwind, Three.js and Framer Motion as one mandatory recommendation.

For a 3D trading card: CSS perspective/transforms can deliver tilt, flip and glare; use WebGL/Three.js only when actual geometry, shader or scene requirements justify it. Animation libraries are optional when existing CSS or installed project tools can handle the behavior. Next.js is a possible SSR/routing decision, not the default for every card website.

If the user says "choose for me" without naming a stack, this skill still asks for deliberate stack confirmation; include a minimal contextual recommendation in **that one question**. Never silently scaffold a parallel frontend.

## Scope and safety

- Read-only audits can inspect current code without stack consent, but must ask before subsequent implementation.
- A user-approved existing stack means reuse, **not authorization to replace brand, auth, routes or state**.
- If a chosen stack conflicts with platform requirements, explain the exact conflict and ask one focused follow-up.
- After choice, proceed through real implementation and QA without repeated permission prompts.

Behavioral cases: [scenarios.json](../../../evals/scenarios.json). A missing-choice case must ask and leave frontend files unchanged; an approved-choice case should implement and test.
