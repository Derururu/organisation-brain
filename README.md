# Organisation brain

A shared knowledge base for running our OpenAI Student Collective community. Open this repository in Codex to ask questions, plan events, and pick up work without needing the previous chat.

## Start here

1. Read [Organisation context](knowledge/organisation.md) and [Event formats](knowledge/events.md).
2. Check [Active work](operations/active-work.md) before starting a task.
3. Ask Codex what you need. It will follow [the brain instructions](AGENTS.md), read relevant documents, and cite its sources.
4. Before finishing, ask it to save progress and next steps in Active work. Chats alone are not the shared memory.

Try:

- “Onboard me to this organisation. What do we run, and what should I know?”
- “Help me plan a 60-minute workshop. Ask for missing event details and use our checklist.”
- “What is different about approvals and check-in for a Studio Session?”
- “Find our marketing templates and explain the logo rules.”
- “Read the active work and help me continue the next unfinished task.”
- “Process the new materials in INBOX, update the knowledge base, and flag conflicts.”
- “Save a handoff so another teammate can continue this work.”

## Where things live

| Location | Purpose |
| --- | --- |
| [INBOX](INBOX/README.md) | Drop new documents, exports, notes, and links here |
| [knowledge](knowledge/organisation.md) | Organisation context, event comparison, resources, and unanswered questions |
| [playbooks](playbooks/workshops.md) | Practical workshop, Studio Session, and marketing instructions |
| [operations](operations/README.md) | Current work, handoffs, and recorded decisions |
| [templates](templates/event-brief.md) | A reusable event planning brief |
| [sources](sources/README.md) | Source register, preserved text, and the original marketing kit contents |
| [assets](assets/README.md) | Supplied logos and screenshot reference |

## Working together

This is a local Git repository. To make it available to teammates, put it on your organisation's private Git host and grant access. Each teammate can clone it and open their copy in Codex. Pull changes before work and commit/push changes afterwards; a local folder alone is not shared.

Use branches or pull requests when teammates edit the same material. A reviewer should check changes to program rules against their sources. Keep restricted participant records and credentials out of this general knowledge repo; Git retains past versions.

## Adding knowledge

Drop material in INBOX and ask Codex to process it. It should preserve the original, register its origin and dates, update the relevant guide, and report gaps or contradictions. See [the intake instructions](INBOX/README.md).

New files are not processed automatically. The assistant reads repository documents when asked; this repository does not include a background service or a trained model.

## Initial coverage

Imported on 2026-10-20: workshop guidance, Studio Session guidance, marketing guidance, a supplied marketing kit, eight logo/identity files, and one screenshot. Program information is based on supplied materials, not independently confirmed current policy. [Open questions](knowledge/open-questions.md) identify what the team still needs to supply.
