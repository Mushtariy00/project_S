#!/usr/bin/env python3
"""todo-guard 껍데기 — 미완료나 문체 위반이 남으면 턴 종료를 막는다."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import project_root, run_script, skill_dir

if not skill_dir().is_dir():
    sys.exit(0)

# 이미 이 훅 때문에 멈춘 상태면 다시 막지 않는다. 무한루프 방지.
try:
    payload = json.load(sys.stdin)
except Exception:
    payload = {}
if payload.get("stop_hook_active"):
    sys.exit(0)

root = project_root()
reasons = []

code, out = run_script("todo_check.py", "--root", str(root))
if code != 0 and out:
    reasons.append(out)

dirty = root / ".claude" / "todo-guard-dirty"
if dirty.is_file():
    code, out = run_script("check_docs.py", "--root", str(root), "--changed")
    if code != 0 and out:
        reasons.append(out)
    dirty.unlink(missing_ok=True)

if reasons:
    print(json.dumps({
        "decision": "block",
        "reason": "todo-guard 가 턴 종료를 막았다.\n\n" + "\n".join(reasons) +
                  "\n\n남은 일을 끝내거나, 하지 않기로 했으면 TODO.md 에서 "
                  "`- [~]` 로 바꾸고 이유를 적는다. 문체 위반은 해당 줄을 고친다.",
    }, ensure_ascii=False))
sys.exit(0)
