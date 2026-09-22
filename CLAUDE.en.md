# Project Rules

## todo-guard operating rules

This project has the todo-guard hook installed. Follow the rules below.

### Preventing dropped work

- When given an instruction, **first** write it to `TODO.md` as `- [ ]`.
  If there are several items, split them into several lines.
- When an item is done, change that line to `- [x]`.
- For an item decided against, change it to `- [~]` and note the reason beside it. Do not delete it.
- If a turn is ended while unfinished items remain, the hook blocks it.

### Document style

- **Before** writing slides or reports, read and apply
  `~/.claude/skills/todo-guard/rules/doc-rules.md`.
- Once done writing, check the changed lines:
  `python3 ~/.claude/skills/todo-guard/scripts/check_docs.py --root . --changed`
- If violations remain, the hook blocks the end of the turn.
- The check covers `.md`, `.txt`, and `.pptx`. `TODO.md` and `CLAUDE.md` are not checked.

### Commands

| When the user says | What to do |
|---|---|
| Check everything | `check_docs.py --root .` |
| Check only what changed | `check_docs.py --root . --changed` |
| Show the check rules | `check_docs.py --list-rules` |
| Turn the doc rules off / on | Set `doc_rules` in `.claude/todo-guard.json` to `false` / `true` |

If the check results contain violations, show the user the file and line.
Do not fix them until separately instructed to do so.
