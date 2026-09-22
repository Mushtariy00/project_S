#!/usr/bin/env python3
"""todo-guard 껍데기 — 받은 지시를 TODO.md 에 적으라고 일깨운다."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import project_root, skill_dir

if not skill_dir().is_dir():
    sys.exit(0)

msg = ("todo-guard: 이번 지시에서 할 일을 TODO.md 에 `- [ ]` 로 먼저 적는다. "
       "여러 건이면 여러 줄로 나눈다. 끝낸 줄은 `- [x]`, "
       "하지 않기로 한 줄은 `- [~]` 로 바꾸고 이유를 적는다.")
if not (project_root() / "TODO.md").exists():
    msg += " TODO.md 가 없으면 만든다."

print(json.dumps({"hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": msg,
}}, ensure_ascii=False))
sys.exit(0)
