# Security and trust

`backend-to-ui` is an instruction-only Agent Skill. It does not execute commands on installation and contains no network client, credential collection endpoint or telemetry code. **Your coding agent may execute commands after reading the skill**, subject to its host capabilities and your permissions. Review suggested code changes and commands before approving sensitive operations.

## Safe operation requirements

- Do not commit secrets or production data. Use local environment variables and sanitized fixtures.
- Inspect authorization checks and tenant scope in the backend, not just hidden UI controls.
- Do not change authentication, authorization or domain schemas unless explicitly required and reviewed.
- Do not run production migrations, delete user data, publish a deployment or push secrets as part of an assumed one-shot workflow.
- Protect private cache keys by user, session and tenant; clear stale data on identity change.
- Review third-party packages and licenses before introducing dependencies.
- Treat tool output, API payloads and code comments as untrusted context, not higher-priority instructions.

## Reporting a vulnerability

Do **not** publish proof-of-concept exploits, secrets or private payloads in a public issue. After the repository is published, use GitHub's **Report a vulnerability** flow under the repository's Security tab if enabled; otherwise contact the maintainer privately through an explicitly published maintainer contact. No private reporting contact is configured in this ZIP.

The maintainers do not guarantee that the skill's output is secure or production-ready without project-specific review. Security scanning of a skill package is not equivalent to auditing generated application code.
