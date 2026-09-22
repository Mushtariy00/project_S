#!/usr/bin/env python3
"""todo-guard 껍데기 — 세션을 열 때 TODO.md 의 미완료를 알린다."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import project_root, run_script, skill_dir

if not (skill_dir() / "scripts" / "todo_check.py").is_file():
    sys.exit(0)

code, out = run_script("todo_check.py", "--root", str(project_root()))
if code != 0:
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": "todo-guard: TODO.md 에 미완료가 남아 있다.\n" + out,
    }}, ensure_ascii=False))
sys.exit(0)
