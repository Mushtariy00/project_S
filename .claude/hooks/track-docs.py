#!/usr/bin/env python3
"""todo-guard 껍데기 — 문서를 고치면 검사 대상으로 표시한다."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import project_root, run_script

run_script("track_doc.py", "--root", str(project_root()))
sys.exit(0)
