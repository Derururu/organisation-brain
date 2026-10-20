# Organisation brain

A GitHub repository with shared knowledge and reusable Codex skills for running our OpenAI Student Collective community. Open this repository in Codex to ask questions, plan events, and pick up work without needing the previous chat.

## Start here

1. Clone the repo and open the `organisation-brain` folder itself as your working project in Codex.
2. Start with `$organisation-brain Onboard me`. The skill reads organisation context, relevant sources, and current work.
3. Ask for the work you need using the skills below or ordinary language. [AGENTS.md](AGENTS.md) supplies the shared repo rules.
4. Before finishing, ask it to save progress and next steps. Chats alone are not the shared memory.

## Included skills

| Skill | Use it for | Example prompt |
| --- | --- | --- |
| [organisation-brain](.agents/skills/organisation-brain/SKILL.md) | Onboarding, questions, knowledge intake, event planning, and handoffs | `$organisation-brain Process the new materials in INBOX` |
| [student-collective-marketing](.agents/skills/student-collective-marketing/SKILL.md) | Event posters and other marketing materials using the supplied kit | `$student-collective-marketing Show me our Studio Session design examples` |

Other examples: `$organisation-brain Plan a 60-minute workshop`, `$organisation-brain What is different about Studio Session approval?`, or `$organisation-brain Save a handoff for the next teammate`.

The skills are checked in under `.agents/skills`, Codex's repo-scoped discovery location. No global installation or setup script is needed. Codex can also select them from matching ordinary-language requests. In the CLI/IDE, use `/skills` or `$` to find them; if they do not appear, reopen Codex with this repo as the working project. See [official skill discovery documentation](https://learn.chatgpt.com/docs/build-skills).

The marketing skill uses a relative symlink to the existing kit so its artwork, guides, and scripts have one copy. Use a Git clone that preserves symlinks. If the same skill is installed globally, select the entry from this repo. Creating new artwork requires image-generation tools in the teammate's session; the kit itself contains reference images, not an image-generation service.

## Where things live

| Location | Purpose |
| --- | --- |
| [.agents/skills](.agents/skills) | Discoverable organisation and marketing skills |
| [INBOX](INBOX/README.md) | Drop new documents, exports, notes, and links here |
| [knowledge](knowledge/organisation.md) | Organisation context, event comparison, resources, and unanswered questions |
| [playbooks](playbooks/workshops.md) | Practical workshop, Studio Session, and marketing instructions |
| [operations](operations/README.md) | Current work, handoffs, and recorded decisions |
| [templates](templates/event-brief.md) | A reusable event planning brief |
| [sources](sources/README.md) | Source register, preserved text, and the original marketing kit contents |
| [assets](assets/README.md) | Supplied logos and screenshot reference |

## Working together

The shared repository is [Derururu/organisation-brain](https://github.com/Derururu/organisation-brain), hosted privately in the user's GitHub account. The owner needs to grant teammates access before they can use it. Each teammate can clone it and open their copy in Codex:

```sh
git clone https://github.com/Derururu/organisation-brain.git
```

Pull changes before work and commit/push changes afterwards; changes kept only in a local folder are not shared.

Use branches or pull requests when teammates edit the same material. A reviewer should check changes to program rules against their sources. Keep restricted participant records and credentials out of this general knowledge repo; Git retains past versions.

## Adding knowledge

Drop material in INBOX and ask `$organisation-brain Process the new materials in INBOX`. It should preserve the original, register its origin and dates, update the relevant guide, and report gaps or contradictions. See [the intake instructions](INBOX/README.md).

New files are not processed automatically. The assistant reads repository documents when asked; this repository does not include a background service or a trained model.

## Initial coverage

Imported on 2026-10-20: workshop guidance, Studio Session guidance, marketing guidance, a supplied marketing kit, eight logo/identity files, and one screenshot. Program information is based on supplied materials, not independently confirmed current policy. [Open questions](knowledge/open-questions.md) identify what the team still needs to supply.
