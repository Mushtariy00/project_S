# 프로젝트 규칙

## todo-guard 운영 규칙

이 프로젝트는 todo-guard 훅이 걸려 있다. 아래를 지킨다.

### 작업 누락 방지

- 지시를 받으면 **먼저** `TODO.md` 에 `- [ ]` 로 적는다.
  여러 건이면 여러 줄로 나눈다.
- 한 건을 끝내면 그 줄을 `- [x]` 로 바꾼다.
- 하지 않기로 한 건은 `- [~]` 로 바꾸고 이유를 옆에 적는다. 지우지 않는다.
- 미완료가 남은 채로 턴을 끝내려 하면 훅이 막는다.

### 문서 문체

- 슬라이드·보고서를 쓰기 **전에** `~/.claude/skills/todo-guard/rules/doc-rules.md`
  를 읽고 적용한다.
- 다 쓰면 바뀐 줄을 검사한다.
  `python3 ~/.claude/skills/todo-guard/scripts/check_docs.py --root . --changed`
- 위반이 남으면 훅이 턴 종료를 막는다.
- 검사 대상은 `.md`, `.txt`, `.pptx`. `TODO.md` 와 `CLAUDE.md` 는 검사하지 않는다.

### 명령

| 사용자가 말하면 | 할 일 |
|---|---|
| 전체 검수해줘 | `check_docs.py --root .` |
| 바뀐 것만 검수해줘 | `check_docs.py --root . --changed` |
| 검사 규칙 보여줘 | `check_docs.py --list-rules` |
| 문서 규칙 꺼줘 / 켜줘 | `.claude/todo-guard.json` 의 `doc_rules` 를 `false` / `true` 로 |

검수 결과에 위반이 있으면 파일과 줄을 사용자에게 보여준다.
고치라는 지시를 따로 받기 전에는 고치지 않는다.
