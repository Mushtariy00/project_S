# TODO

받은 지시를 여기에 적는다.
`- [ ]` 미완료 / `- [x]` 완료 / `- [~]` 하지 않기로 함 (이유를 옆에 적는다)

미완료가 남으면 todo-guard 가 턴 종료를 막는다.

## 할 일

- [x] todo-guard 스킬 설치
- [x] 프로젝트 세팅 (훅 4개, settings.json, todo-guard.json)
- [x] anthropics/skills 마켓플레이스를 프로젝트 범위로 추가
- [x] document-skills 플러그인 설치
- [x] claude-hud 스테이터스라인 설정 (/claude-hud:setup)
- [x] Node.js 설치 및 conda base 환경 sqlite 충돌 복구
- [x] HUD 화면 표시 확인 — 사용자가 화면에서 확인함
- [x] /claude-api — 사용할 언어와 만들 기능 확인 (Python, 단일 호출 예제)
- [x] Python 단일 호출 예제 작성 (claude_single_call.py)
- [x] /claude-hud:setup 재실행 — 기존 설정과 동일함을 확인, 변경 없음
- [x] 이전 작업 결과를 영어로 다시 정리해서 보여주기
- [~] /claude-hud:configure — HUD 표시 설정 조정 (사용자가 설정 질문 단계에서 취소함)
- [x] ~/.claude/skills 폴더 내용 보여주기
- [x] %USERPROFILE%\.claude\skills 경로가 이 맥에서 어디인지 설명
- [x] todo-guard 를 윈도우에서 쓰도록 이식 — 훅 4개를 파이썬으로 다시 쓰고 윈도우용 settings.json 안내
- [x] ~/.claude/skills/todo-guard/ 내용 보여주기
- [x] todo-guard SKILL.md 파일을 줄번호와 함께 보여주기
- [x] scripts/check-todo.sh 를 찾아보고 결과 알리기
- [x] scripts/session-start.sh 를 찾아보고 실제 위치의 파일 보여주기
- [x] TODO.md 현재 내용과 집계 보여주기
- [x] .claude/hooks/todo-check.sh 를 찾아보고 결과 알리기
- [x] .claude/settings.json 내용 보여주기
- [x] git init -b main 실행
- [x] git config --local user.name "BulNim" 설정
- [x] git config --local user.email 설정
- [x] 현재 상태 보고 (git + TODO)
- [x] 이 PC 에 연결된 git 계정 확인
- [x] SSH 키 만드는 법과 깃허브에 붙여넣는 위치 안내
- [x] 프로젝트의 바이브코딩 문서 찾아서 내용 분석 (pdf·ppt 원본은 없고 md 전사본만 있음)
- [x] 바이브코딩_CICD_기초편_v26.pdf 를 KO-EN 마크다운과 대조 검증 (217쪽 일치, 누락은 스크린샷 안 글자뿐)
- [x] 한국어 PDF 의 영어판 만들기 — 217쪽 영어 PDF 생성 (Claude outputs/VibeCoding_CICD_Foundations_EN.pdf)
- [x] 현재 강의 진도 파악 — 7장 7-5 (git init 까지 완료, 첫 커밋 전)
- [x] 7장 마무리 — 7-7/7-8 .gitignore 만들기 (.env 실습까지 포함)
- [x] 7장 마무리 — 7-5 첫 커밋 (da83b39)
- [x] 7장 마무리 — 7-9 브랜치 전략 확인 (main 단독)
- [x] 7장 마무리 — 7-10 전체 환경 최종 확인 (node·git·python·claude 모두 기준 통과)
- [~] 7장 마무리 — 7-6 GitHub 저장소 생성 & push (사용자가 깃허브 웹에서 빈 저장소를 만들어야 진행 가능)
- [x] 기존 커밋 3건에서 Co-Authored-By 줄 제거 — 기여자는 BulNim 한 명
- [x] todo-guard skip_files 에 KO-EN 전사본 추가 (PDF 는 검사 대상 확장자가 아니라 제외 불필요)
- [x] 세션이나 기기를 다시 시작해야 하는지 확인해서 알려주기
- [x] todo-guard 설정과 TODO.md 변경분 커밋
- [x] 8장 — 8-2 taskflow-simple 에서 한 줄 지시로 앱 생성 (Node + JSON 파일)
- [x] 8장 — 8-3/8-4 결과 관찰 + 실제 실행 확인 (추가·상태변경·삭제 모두 동작, 서버 종료 확인)
- [x] 8장 — 8-6~8-8 한계 4가지와 원인 분석
- [x] 8장 — 8-9 커밋 완료 (push 는 원격 저장소가 없어 보류)
- [~] 깃허브에 빈 저장소 만들고 push — 저장소 생성은 gh CLI 나 토큰이 없어 불가. origin 은 미리 걸어 두었고, 사용자가 웹에서 만들면 바로 push 한다
- [x] origin 을 git@github.com:Mushtariy00/project_S.git 으로 미리 설정
- [x] 원격 저장소 확인 후 main push
- [x] 만든 앱을 볼 수 있는 주소 안내 + 로컬 서버 띄우기
- [x] 9장 — taskflow-pro 폴더와 CLAUDE.md 작성 (9-1)
- [x] 9장 — docs 6종 작성 (9-2 ~ 9-7), 문체 검사 통과
- [x] 9장 — 8장과 9장 비교 정리 (9-8) 및 변경사항 점검, 커밋·push 완료
- [x] 05-conventions.md 매트릭스와 02-specs.md 문서 대조 (10건 모두 근거 있음, 누락 없음)
- [~] 매트릭스 실제 실행 검증 — backend/ 가 없어 지금은 불가. Phase 2 (10장) 를 먼저 해야 한다
- [x] 답변을 영어로 다시 정리 (앞 답변이 한국어로 나간 것을 바로잡음)
- [x] 로컬에서 열 수 있는 주소 알려주기
- [x] 10-2-1 슬라이드 화면과 내 로컬 화면이 다른 이유 설명 (8장 Node 앱 vs 10장 FastAPI Swagger)
- [x] Phase 2 — 8장 서버 종료 (포트 8000 충돌 해소)
- [x] Phase 2 — 2.1~2.2 backend/ 가상환경과 의존성 5개 (승인 목록만)
- [x] Phase 2 — 2.3~2.4 DB 모델과 스키마 (필드 7개)
- [x] Phase 2 — 2.5~2.8 CRUD API 5개
- [x] Phase 2 — 2.9 검증 규칙 400/404/422
- [x] Phase 2 — 2.10 pytest 매트릭스 10건 통과 (10 passed)
- [x] Phase 2 까지 전부 push 됐는지 확인
- [x] Phase 3 — 3.1~3.2 frontend/ 두 파일과 테마 토글
- [x] Phase 3 — 3.3~3.6 목록·추가·수정·삭제 화면
- [x] Phase 3 — 3.7 StaticFiles 같은 오리진 제공 확인 (360px 눈 확인은 사용자 몫)
- [x] Phase 3 — 3.8 커밋과 push
- [x] Vercel CLI 설치 (vercel@59.25.0, miniconda3/bin 에 설치됨)
- [x] Vercel 배포 준비 — vercel.json 과 API 주소 설정 분리 (frontend 는 2파일 유지)
- [x] Vercel 배포 준비 — 백엔드 CORS 허용 (CORS_ORIGINS 비면 미적용)
- [x] Vercel 배포 준비 — 03-design.md 에 배포 결정 기록
- [~] Vercel 실제 배포 — 로그인이 대화형이라 사용자가 `vercel login` 을 해야 한다
