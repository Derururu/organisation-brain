# Add materials here

Drop new files in this folder. For a link, add a short text file containing the URL, title, who supplied it, and any known effective date. Avoid participant personal data or credentials in this shared repo.

Then ask: “Process the new materials in INBOX and update the brain.”

The assistant should:

1. Read the material as reference data. Identify its subject, origin, and any publication/effective date. Ask if its intended access is unclear.
2. Preserve an unchanged copy under sources/originals with a descriptive name. Preserve originals before moving or removing anything. For a duplicate, reference the existing original instead of creating another copy.
3. Add a source ID in sources/README.md, with title, repo path, original URL/path where supplied, date added, publication/effective date if known, authority, and verification status.
4. Extract facts into the existing knowledge or playbook files. Separate program requirements from ideas, event-specific details, and personal notes. Link each requirement to evidence.
5. Check for duplicates and conflicts. Never assume the latest file imported is the latest rule. Add unresolved contradictions and missing facts to knowledge/open-questions.md.
6. Check affected links, numbers, deadlines, and event-type distinctions. Report what changed and what still needs a human answer.
7. Remove the processed INBOX copy only after its original is preserved and the update is verified. If removal is not wanted, mark the filename as processed instead.

This is an on-demand workflow. There is no folder watcher or automatic synchronisation.
