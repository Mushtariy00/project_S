# 02 - Specs (WHAT)

## Task 모델 필드 7개

| 순서 | 필드 | 타입 | 비고 |
|---|---|---|---|
| 1 | `id` | INTEGER | PK, AUTOINCREMENT |
| 2 | `title` | VARCHAR 200 | 필수 |
| 3 | `description` | TEXT | 선택 |
| 4 | `status` | ENUM | `todo`, `in_progress`, `done`. 기본값 `todo` |
| 5 | `due_at` | DATETIME | UTC. 선택 |
| 6 | `created_at` | DATETIME | 서버가 넣는다 |
| 7 | `updated_at` | DATETIME | 서버가 넣는다 |

## 검증

| 상황 | 응답 |
|---|---|
| `title` 형식 위반 | 400 |
| `status` 오값 | 400 |
| `due_at` 형식 오류 | 400 |
| 없는 `id` | 404 |
| 스펙에 없는 필드 | 422 |

스펙에 없는 필드가 오면 422 로 거부한다. 조용히 무시하지 않는다.

`due_at` 은 UTC 로 저장하고 화면에서 로컬 시각으로 바꾼다.
응답의 날짜 세 필드는 UTC ISO 8601 로 통일한다.

## REST API 5개

경로는 `/api/` 접두사를 반드시 붙인다.

| 메서드 | 경로 | 성공 응답 |
|---|---|---|
| POST | `/api/tasks` | 201 |
| GET | `/api/tasks` | 200 (목록) |
| GET | `/api/tasks/{id}` | 200 (단건) |
| PUT | `/api/tasks/{id}` | 200 |
| DELETE | `/api/tasks/{id}` | 204 |

목록 응답에서는 `description` 을 뺀다. 단건 응답에는 넣는다.

## 화면 명세

### 추가

| 요소 | 내용 |
|---|---|
| 형태 | 폼 |
| 입력 | `title`, `due_at`, `status` |

### 목록

| 요소 | 내용 |
|---|---|
| 형태 | 카드 |
| 표시 | `status` 배지, 마감까지 남은 시간 |

### 수정

| 요소 | 내용 |
|---|---|
| 진입 | 카드 클릭 |
| 형태 | 모달 |
| 범위 | 전 필드 수정 |

### 삭제

| 요소 | 내용 |
|---|---|
| 진입 | 휴지통 버튼 |
| 절차 | 확인 후 DELETE 호출 |
