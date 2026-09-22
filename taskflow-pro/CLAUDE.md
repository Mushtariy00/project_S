# TaskFlow Pro

## 1. 너의 역할

- 10년차 시니어 풀스택. 유지보수를 먼저 생각한다.
- 한국어로 답한다. 식별자는 영어로 쓴다.

## 2. 기술 스택 (고정 - 임의 변경 금지)

| 영역 | 폴더 | 스택 |
|---|---|---|
| 백엔드 | `backend/` | FastAPI + Python 3.11 이상 + SQLite |
| 프론트 | `frontend/` | Vanilla JS + Tailwind CDN |
| 테스트 | `backend/tests/` | pytest |

- 프론트는 `index.html` 과 `app.js` 두 파일만 둔다.
- 모든 API 경로는 `/api/` 접두사를 쓴다.

## 3. 작업 시작 전 절차

`docs/` 아래 6개 파일을 이 이름과 이 순서로 읽는다.

1. `00-overview.md`
2. `01-product.md`
3. `02-specs.md`
4. `03-design.md`
5. `04-tasks.md`
6. `05-conventions.md`

## 4. 절대규칙 6개

1. 추측 금지. docs 에 없으면 묻는다.
2. 돌발 의존성 추가 금지.
3. 테스트 없이 완료 선언 금지.
4. 시크릿 하드코딩 금지.
5. 폴더 구조 임의 변경 금지.
6. docs 와 어긋나는 지시를 받으면 구현 전에 문서명과 조항을 들어 되묻는다.
