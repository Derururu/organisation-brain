# Decisions

## 2026-10-20 — Use a repository for the organisation brain

- Decision: teammates should use a repo as the home for shared organisational knowledge.
- Evidence: the user answered “a repo” when asked where the team should use the AI brain.
- Initial implementation: plain documents, preserved sources, assistant instructions, an intake workflow, and durable work records. This is an implementation choice, not a separate recorded team policy.
- Not yet decided: access membership, content owners, and review frequency.

## 2026-10-20 — Host privately in the user's GitHub account

- Decision: use the user's own GitHub account and keep the repository private.
- Evidence: the user instructed “just do my account, keep it private”.
- Repository: [Derururu/organisation-brain](https://github.com/Derururu/organisation-brain).
- Teammate invitations have not been requested or sent.

## 2026-10-20 — Make the repo's workflows discoverable as skills

- Decision: the organisation brain should be a GitHub repo with skills set up.
- Evidence: the user clarified “there is no need for a custom app, i want a github repo with skills so to say set up”.
- Implementation: `.agents/skills/organisation-brain` routes knowledge work through the existing guides; `.agents/skills/student-collective-marketing` exposes the supplied kit through a relative symlink. No global skill installation is required.
