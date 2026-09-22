# 05 - Conventions (규약)

## 명명

| 영역 | 규칙 |
|---|---|
| 백엔드 | `snake_case` |
| 프론트 | `camelCase` |
| 컴포넌트 | `PascalCase` |

식별자는 영어로 쓴다. 주석만 한국어로 쓴다.

## 금지 5개

| 금지 | 이유 | 대안 |
|---|---|---|
| `print` 디버깅 | 로그가 노이즈로 남는다 | `logging` 모듈 |
| bare `except` | 예외를 삼킨다 | `except SpecificError` |
| 비밀번호 하드코딩 | 보안 사고로 이어진다 | `.env` + `os.getenv` |
| `any` 타입 | 의미를 잃는다 | 명시적 타입 |
| `!important` | 우선순위가 꼬인다 | 셀렉터 개선 |

## .gitignore

`__pycache__/`, `.venv/`, `*.db`, `*.log` 를 넣는다.

## 테스트 매트릭스

| 케이스 | 요청 | 기대 응답 |
|---|---|---|
| 정상 생성 | POST, `title` 만 | 201 |
| 목록 | GET `/api/tasks` | 200, `description` 없음 |
| 단건 | GET `/api/tasks/{id}` | 200, `description` 있음 |
| 수정 | PUT, 전 필드 | 200 |
| 삭제 | DELETE | 204 |
| `title` 누락 | POST | 400 |
| `status` 오값 | POST | 400 |
| `due_at` 형식 오류 | POST | 400 |
| 없는 `id` | GET | 404 |
| 스펙 외 필드 | POST | 422 |

## git 커밋 규칙

접두사는 `feat`, `fix`, `docs`, `refactor`, `test`, `chore` 를 쓴다.
접두사 뒤에는 한국어 요약을 붙인다.

예: `docs: Phase 1 설계 문서 7종 작성`
