"""todo-guard 훅 공용 코드. 맥과 윈도우에서 똑같이 동작한다."""
import os
import subprocess
import sys
from pathlib import Path

# 윈도우 기본 콘솔 인코딩(cp949 등)에서 한글이 깨지지 않게 UTF-8 로 고정한다.
for _stream in (sys.stdin, sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass


def config_dir() -> Path:
    """CLAUDE_CONFIG_DIR 이 있으면 그것, 없으면 홈의 .claude."""
    env = os.environ.get("CLAUDE_CONFIG_DIR")
    return Path(env) if env else Path.home() / ".claude"


def skill_dir() -> Path:
    return config_dir() / "skills" / "todo-guard"


def project_root() -> Path:
    return Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path.cwd())


def run_script(name: str, *args: str):
    """스킬의 파이썬 스크립트를 돌린다. (종료코드, 출력) 을 준다."""
    path = skill_dir() / "scripts" / name
    if not path.is_file():
        return 0, ""
    proc = subprocess.run(
        [sys.executable, str(path), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return proc.returncode, (proc.stdout or "").strip()
