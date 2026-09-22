# 바이브코딩 CI/CD (기초편) — Bilingual Slide Text
# Vibe Coding CI/CD (Foundations) — Korean / English side-by-side

> Source: `바이브코딩_CICD_기초편_v26.pdf` (217 slides)
> Each slide below shows the original Korean text on the left and the English rendering on the right, in slide order.
> Text baked into screenshots is not translated — image captions are marked *(image)*.

**Recurring UI labels**

| 한국어 | English |
|---|---|
| 학습 내용 | What you will learn |
| 체크포인트 | Checkpoint |
| 실습 | Hands-on |
| 정리 | Summary |
| 장 | Chapter |
| 기초편 / 심화편 | Foundations / Advanced |

---

## OPENING

### Slide 1 — Title

| 한국어 | English |
|---|---|
| Claude Code와 OpenSpec을 활용한 | Using Claude Code and OpenSpec |
| **바이브코딩 CI/CD (기초편)** | **Vibe Coding CI/CD (Foundations)** |
| AI 개요, 개발에서 AI 활용, 바이브코딩+AI-DLC, Claude Code, 심플 바이브, 스팩기반 백엔드/프론트 개발 | AI overview, using AI in development, vibe coding + AI-DLC, Claude Code, simple vibe, spec-driven backend/frontend development |
| Claude Code · FastAPI · Vanilla JS · Tailwind CSS · GitHub · Vercel, Railway | Claude Code · FastAPI · Vanilla JS · Tailwind CSS · GitHub · Vercel, Railway |
| 기초편 | Foundations |
| 12장 구성, 터미널 기초 + 환경설정 + 스킬·플러그인 + 심플 바이브 + 기초 개발 | 12 chapters: terminal basics + environment setup + skills & plugins + simple vibe + foundational development |

### Slide 2 — 교육 목표 / Course Objectives

| 한국어 | English |
|---|---|
| OPENING, 교육 목표 | OPENING — Course objectives |
| **교육 목표** | **Course Objectives** |
| 수료 후 수행 가능한 작업 – 1~6 기초편 12장 · 7~8 심화편 | What you will be able to do after the course — items 1–6 cover the 12 Foundations chapters, 7–8 the Advanced course |
| 1. 1~3장 AI, 바이브코딩, AI-DLC 개념 이해 | 1. Ch. 1–3 — Understand AI, vibe coding and AI-DLC concepts |
| 2. 4~5장 터미널 기초 + Claude Code 설치 · 인증 · 비용 설정 | 2. Ch. 4–5 — Terminal basics + installing, authenticating and setting up billing for Claude Code |
| 3. 6장 스킬과 플러그인으로 반복 작업 자동화 | 3. Ch. 6 — Automate repetitive work with skills and plugins |
| 4. 7장 Git + GitHub 버전 관리 및 협업 환경 구성 | 4. Ch. 7 — Set up version control and collaboration with Git + GitHub |
| 5. 8장 설계 문서 없이 만들어 보고 한계를 직접 체감 | 5. Ch. 8 — Build without design documents and feel the limits first-hand |
| 6. 9장 CLAUDE.md + docs 6종으로 AI 에게 체계적 지시 | 6. Ch. 9 — Instruct AI systematically with CLAUDE.md and six kinds of docs |
| 7. 10~11장 FastAPI 백엔드 + Vanilla JS · Tailwind 프론트 완성 | 7. Ch. 10–11 — Complete a FastAPI backend and a Vanilla JS · Tailwind frontend |
| 8. [심화] OpenSpec · CI/CD 자동 배포로 팀 개발까지 확장 | 8. [Advanced] Extend to team development with OpenSpec and CI/CD automated deployment |

### Slide 3 — 전체 커리큘럼 로드맵 / Full Curriculum Roadmap

| 한국어 | English |
|---|---|
| **전체 커리큘럼 로드맵** | **Full Curriculum Roadmap** |
| 기초편 12장 + 심화편 9장. 한 편에 한 색만 써서 어디까지 왔는지만 보이게 함 | 12 Foundations chapters + 9 Advanced chapters. One color per course, so you can see at a glance how far you have come |
| **기초편 12장 – 이론 · 환경 설정 · 심플 바이브 · 기초 개발** | **Foundations, 12 chapters — theory · environment setup · simple vibe · foundational development** |
| 1장 AI 개요 | Ch. 1 AI overview |
| 2장 AI 활용 | Ch. 2 Using AI |
| 3장 바이브코딩 + AI-DLC | Ch. 3 Vibe coding + AI-DLC |
| 4장 터미널 기초 | Ch. 4 Terminal basics |
| 5장 Claude Code 설치 | Ch. 5 Installing Claude Code |
| 6장 스킬 & 플러그인 | Ch. 6 Skills & plugins |
| 7장 Git & GitHub | Ch. 7 Git & GitHub |
| 8장 심플 바이브 실습 | Ch. 8 Simple vibe practice |
| 9장 CLAUDE.md + docs | Ch. 9 CLAUDE.md + docs |
| 10장 FastAPI 백엔드 | Ch. 10 FastAPI backend |
| 11장 Vanilla JS 프론트 | Ch. 11 Vanilla JS frontend |
| 12장 회고 & 심화편 예고 | Ch. 12 Retrospective & preview of the Advanced course |
| **심화편 9장 – AI-DLC 심화 · OpenSpec · CI/CD · 배포 · 발표** | **Advanced, 9 chapters — AI-DLC in depth · OpenSpec · CI/CD · deployment · presentation** |
| 1장 AI-DLC 심화 | Ch. 1 AI-DLC in depth |
| 2장 OpenSpec 방법론 | Ch. 2 The OpenSpec methodology |
| 3장 OpenSpec 앱 재설계 | Ch. 3 Redesigning the app with OpenSpec |
| 4장 Tailwind CSS | Ch. 4 Tailwind CSS |
| 5장 로그인 · 팀 기능 | Ch. 5 Login & team features |
| 6장 CI/CD 자동 배포 | Ch. 6 CI/CD automated deployment |
| 7장 Kanban + 채팅 | Ch. 7 Kanban + chat |
| 8장 기능 확장 · 디버깅 | Ch. 8 Feature expansion & debugging |
| 9장 발표 & 마무리 | Ch. 9 Presentation & wrap-up |
| 두 편을 마치면 남는 것 | What you are left with after both courses |
| 로그인 · 팀 · Kanban · 채팅을 갖춘 풀스택 앱 하나와 자동 배포 주소 (Vercel + Railway) | One full-stack app with login, teams, Kanban and chat, plus a live auto-deployed URL (Vercel + Railway) |

---

## 1장. AI 개요 / Chapter 1. AI Overview

### Slide 4 — Chapter cover

| 한국어 | English |
|---|---|
| **AI (Artificial Intelligence) 개요** | **AI (Artificial Intelligence) Overview** |
| 인공지능 개념 + AI 서비스 예시 7가지 + 생성형 AI 분류 | The concept of AI + 7 example AI services + a taxonomy of generative AI |
| 학습 내용 | What you will learn |
| 1. 인공지능 정의 | 1. Defining artificial intelligence |
| 2. AI 서비스 예시 7가지 | 2. Seven example AI services |
| 3. 생성형 AI 서비스 분류 | 3. A taxonomy of generative AI services |

### Slide 5 — 1-1. 인공지능의 정의 / Defining AI

| 한국어 | English |
|---|---|
| **1-1. 인공지능의 정의** | **1-1. Defining Artificial Intelligence** |
| Artificial Intelligence | Artificial Intelligence |
| 1. 인공지능 – 인간의 지능을 모방 또는 대체하는 기술 | 1. Artificial intelligence — technology that imitates or substitutes for human intelligence |
| 2. 단순 수치 계산이 아닌 – 학습, 추론, 문제해결, 인식 등 고차원적 능력 | 2. Not mere numeric computation — higher-order abilities such as learning, reasoning, problem solving and perception |
| 3. 생성형 AI – 텍스트, 이미지, 음성, 영상, 코드를 스스로 생성하는 AI | 3. Generative AI — AI that produces text, images, audio, video and code on its own |
| 4. 대표 모델 – ChatGPT (OpenAI), Claude (Anthropic), Gemini (Google) | 4. Leading models — ChatGPT (OpenAI), Claude (Anthropic), Gemini (Google) |

### Slide 6 — 1-2. 생성형 AI 서비스 분류 / Taxonomy of Generative AI Services

| 한국어 | English |
|---|---|
| **1-2. 생성형 AI 서비스 분류 – 다음 장부터 분야별로 하나씩** | **1-2. A Taxonomy of Generative AI Services — one field per slide from here on** |
| 분야 · 대표 서비스 · 특징 | Field · Representative services · Characteristics |
| 텍스트 · ChatGPT, Claude, Gemini · 범용 지식, 대화, 코드, 문서 | Text · ChatGPT, Claude, Gemini · General knowledge, conversation, code, documents |
| 이미지 · Gemini, DALL-E, Midjourney · 텍스트 > 이미지 생성 | Image · Gemini, DALL-E, Midjourney · Text to image generation |
| 음성 · Whisper, Clova Note, ElevenLabs · 음성 인식, 전사, 합성 | Speech · Whisper, Clova Note, ElevenLabs · Speech recognition, transcription, synthesis |
| 영상 · Google Veo, Grok, Sora · 영화급 영상+오디오 생성 | Video · Google Veo, Grok, Sora · Cinema-grade video and audio generation |
| 코드 (바이브) · Claude Code, Antigravity, Cursor, Codex CLI · 자연어로 전체 기능 자율 구현 | Code (vibe) · Claude Code, Antigravity, Cursor, Codex CLI · Implements whole features autonomously from natural language |
| 코드 (보조) · GitHub Copilot, ChatGPT · 자동완성, 버그수정, 코드리뷰 | Code (assisted) · GitHub Copilot, ChatGPT · Autocomplete, bug fixing, code review |
| 로컬 LLM · Ollama, LM Studio · 오프라인 AI 실행 | Local LLM · Ollama, LM Studio · Running AI offline |

### Slide 7 — 1-2-1. 코딩 (ChatGPT) / Coding (ChatGPT)

| 한국어 | English |
|---|---|
| **1-2-1. AI 서비스 예시 – 코딩 (ChatGPT)** | **1-2-1. Example AI Service — Coding (ChatGPT)** |
| 원하는 기능 코드로 구현 | Turning the feature you describe into code |
| *(image)* ChatGPT로 만든 웹페이지 | *(image)* A web page built with ChatGPT |
| 1. 원하는 기능을 말하면 코드로 구현 | 1. Describe the feature you want and it is implemented in code |
| 2. 웹페이지, API, 스크립트 자동 생성 | 2. Automatically generates web pages, APIs and scripts |
| 3. 버그 수정 및 코드 설명 요청 | 3. Ask it to fix bugs and explain code |
| 4. 사용 예: 회사 소개 웹페이지 만들어줘 | 4. Example prompt: "Build me a company introduction web page" |
| 5. https://chatgpt.com | 5. https://chatgpt.com |
| 6. 실습 공유 링크 (클릭) | 6. Shared hands-on link (click) |

### Slide 8 — 1-2-2. 바이브 코딩 / Vibe Coding (Claude Code / Cursor)

| 한국어 | English |
|---|---|
| **1-2-2. AI 서비스 예시 – 바이브 코딩 (Claude Code / Cursor)** | **1-2-2. Example AI Service — Vibe Coding (Claude Code / Cursor)** |
| 자연어 지시만으로 AI가 직접 코딩 | The AI writes the code itself, from natural-language instructions alone |
| *(image)* Claude Code 터미널 화면 | *(image)* The Claude Code terminal screen |
| 1. Claude Code – 터미널 기반 AI 에이전트 (본 과정에서 사용) | 1. Claude Code — a terminal-based AI agent (the tool used in this course) |
| 2. Cursor – IDE 기반 AI 협업 에디터 | 2. Cursor — an IDE-based AI collaborative editor |
| 3. 자연어로 지시 > AI가 파일 생성, 수정, 실행 | 3. Instruct in natural language, and the AI creates, edits and runs files |
| 4. 코드를 한 줄도 직접 쓰지 않아도 됨 | 4. You never have to write a single line of code yourself |
| 5. https://claude.ai/code / https://www.cursor.com | 5. https://claude.ai/code / https://www.cursor.com |

### Slide 9 — 1-2-3. 문서 작성 (Claude) / Writing Documents (Claude)

| 한국어 | English |
|---|---|
| **1-2-3. AI 서비스 예시 – 문서 작성 (Claude)** | **1-2-3. Example AI Service — Document Writing (Claude)** |
| 소설, 제안서, 보고서, PPT 그림 | Fiction, proposals, reports, slide graphics |
| *(image)* Claude 문서 작성 화면 | *(image)* Writing a document in Claude |
| 1. 소설 / 제안서 작성 | 1. Writing fiction and proposals |
| 2. PPT 그림 및 보고서 작성 | 2. Creating slide graphics and reports |
| 3. 이메일 초안 자동 생성 | 3. Automatically drafting emails |
| 4. 회의록 정리 및 요약 | 4. Organizing and summarizing meeting notes |
| 5. https://claude.ai | 5. https://claude.ai |

### Slide 10 — 1-2-4. 이미지 생성 (Gemini) / Image Generation (Gemini)

| 한국어 | English |
|---|---|
| **1-2-4. AI 서비스 예시 – 이미지 생성 (Gemini)** | **1-2-4. Example AI Service — Image Generation (Gemini)** |
| 텍스트 한 줄로 고품질 이미지 생성 | High-quality images from a single line of text |
| *(image)* Gemini 이미지 생성 예시 | *(image)* An example of image generation in Gemini |
| 1. 텍스트 한 줄 > 고품질 이미지 생성 | 1. One line of text produces a high-quality image |
| 2. 사진 스타일 변환, 편집 | 2. Style transfer and editing of photos |
| 3. Gemini 3.1 Flash Image 활용 | 3. Uses Gemini 3.1 Flash Image |
| 4. 디자인 초안, 마케팅 이미지 제작 | 4. Producing design drafts and marketing imagery |
| 5. https://gemini.google.com | 5. https://gemini.google.com |

### Slide 11 — 1-2-5. 음성 인식 / Speech Recognition (Whisper / Clova Note)

| 한국어 | English |
|---|---|
| **1-2-5. AI 서비스 예시 – 음성 인식 (Whisper / Clova Note)** | **1-2-5. Example AI Service — Speech Recognition (Whisper / Clova Note)** |
| 음성을 텍스트로, 텍스트를 음성으로 | Speech to text, and text to speech |
| *(image)* Naver Clova Note 화면 | *(image)* The Naver Clova Note screen |
| 1. OpenAI Whisper – 유튜브 영상 자막 자동 생성 | 1. OpenAI Whisper — automatic subtitles for YouTube videos |
| 2. 네이버 Clova Note – 회의, 강의 녹음 자동 전사 | 2. Naver Clova Note — automatic transcription of meeting and lecture recordings |
| 3. 실시간 자막 생성 가능 | 3. Can generate subtitles in real time |
| 4. 다국어 지원 | 4. Multilingual support |
| 5. https://openai.com/research/whisper / https://clovanote.naver.com | 5. https://openai.com/research/whisper / https://clovanote.naver.com |

### Slide 12 — 1-2-6. 동영상 생성 / Video Generation (Grok / Veo 3)

| 한국어 | English |
|---|---|
| **1-2-6. AI 서비스 예시 – 동영상 생성 (Grok / Veo 3)** | **1-2-6. Example AI Service — Video Generation (Grok / Veo 3)** |
| 영화급 영상 + 오디오 동시 생성 | Cinema-grade video and audio generated together |
| *(image)* Google Veo 3 영상 생성 예시 | *(image)* An example of video generation with Google Veo 3 |
| 1. xAI Grok Imagine – 창의적, 감성적 영상 생성 | 1. xAI Grok Imagine — creative, emotive video generation |
| 2. Google Veo 3 – 영화급 고품질 영상+오디오 | 2. Google Veo 3 — cinema-grade video with audio |
| 3. 텍스트 한 줄로 영상 생성 | 3. Generates video from a single line of text |
| 4. 광고, 콘텐츠 제작에 활용 | 4. Used for advertising and content production |
| 5. https://x.ai / https://deepmind.google/technologies/veo | 5. https://x.ai / https://deepmind.google/technologies/veo |

### Slide 13 — 1-2-7. 로컬 LLM / Local LLMs (Ollama / LM Studio)

| 한국어 | English |
|---|---|
| **1-2-7. AI 서비스 예시 – 로컬 LLM (Ollama / LM Studio)** | **1-2-7. Example AI Service — Local LLMs (Ollama / LM Studio)** |
| 인터넷 없이 내 컴퓨터에서 LLM 실행 | Running an LLM on your own machine, with no internet |
| *(image)* Ollama 모델 + LM Studio 화면 | *(image)* Ollama models and the LM Studio screen |
| 1. Ollama – CLI 기반 로컬 LLM 실행, 서빙 (ollama.com) | 1. Ollama — runs and serves local LLMs from the CLI (ollama.com) |
| 2. LM Studio – GUI 기반 로컬 LLM 실행 도구 | 2. LM Studio — a GUI tool for running local LLMs |
| 3. 장점: 인터넷 불필요, 데이터 외부 유출 없음 | 3. Upside: no internet needed, and no data leaves your machine |
| 4. 단점: 고성능 GPU 필요, 상용 모델 대비 성능 낮음 | 4. Downside: needs a powerful GPU, and performs worse than commercial models |
| 5. https://ollama.com / https://lmstudio.ai | 5. https://ollama.com / https://lmstudio.ai |

### Slide 14 — 체크포인트 / Checkpoint

| 한국어 | English |
|---|---|
| **체크포인트** | **Checkpoint** |
| 1. 인공지능 정의 | 1. Defining artificial intelligence |
| 2. AI 서비스 예시 7가지 | 2. Seven example AI services |
| 3. 생성형 AI 분류 | 3. A taxonomy of generative AI |

---

## 2장. 개발에서 AI 활용 / Chapter 2. Using AI in Development

### Slide 15 — Chapter cover

| 한국어 | English |
|---|---|
| **개발에서 AI 활용** | **Using AI in Development** |
| 소프트웨어 개발 전 과정에서 AI 활용 방법 | How to use AI across the whole software development process |
| 학습 내용 | What you will learn |
| 1. 개발 단계별 AI 활용 | 1. Using AI at each stage of development |
| 2. AI 보조 코딩 vs 바이브 코딩 | 2. AI-assisted coding vs. vibe coding |
| 3. Claude Code = 본 과정의 핵심 도구 | 3. Claude Code — the core tool of this course |

### Slide 16 — 2-1. 기획 단계 / The Planning Stage

| 한국어 | English |
|---|---|
| **2-1. 기획 단계 – AI로 기획하기** | **2-1. The Planning Stage — Planning with AI** |
| 초기 아이디어 발상부터 PRD 작성, 화면 설계까지 – AI 도구로 기획 시간 단축 | From the first idea through the PRD to screen design — AI tools cut planning time |
| 단계 · 도구 · 주요 기능 | Stage · Tool · Key capability |
| 리서치 & 아이디어 · Perplexity · 출처 기반 시장 조사, 경쟁사 분석, 트렌드 파악 | Research & ideation · Perplexity · Source-backed market research, competitor analysis, trend spotting |
| 리서치 & 아이디어 · Claude / ChatGPT · 콘셉트 구체화, 사용자 페르소나, 기능 명세서 초안 | Research & ideation · Claude / ChatGPT · Fleshing out concepts, user personas, draft functional specs |
| 기획서 & 문서화 · Gamma · 텍스트 입력 > PPT, 랜딩 페이지 형태 기획서 자동 생성 | Proposals & documentation · Gamma · Enter text and get a proposal as slides or a landing page |
| 기획서 & 문서화 · Manyfast · 아이디어 > PRD + 와이어프레임 한 번에 자동 생성 | Proposals & documentation · Manyfast · Turns an idea into a PRD plus wireframes in one pass |
| UI/UX 디자인 · Figma AI · 프롬프트 > 와이어프레임, UI 프로토타입 빠르게 제작 | UI/UX design · Figma AI · Prompts into wireframes and UI prototypes, fast |
| UI/UX 디자인 · Uizard · 스케치, 텍스트 > 고충실도 UI 화면으로 변환 | UI/UX design · Uizard · Turns sketches and text into high-fidelity UI screens |
| 마인드맵 & 구조화 · EdrawMind · 서비스 기획 구조와 핵심 로직 마인드맵 시각화 | Mind mapping & structuring · EdrawMind · Visualizes service structure and core logic as a mind map |

### Slide 17 — 2-1-1. Perplexity

| 한국어 | English |
|---|---|
| **2-1-1. Perplexity – 출처 기반 AI 리서치 도구** | **2-1-1. Perplexity — Source-Backed AI Research** |
| 출처 확인이 가능한 리서치에 강점 | Strong where you need to verify sources |
| *(image)* Perplexity 화면 | *(image)* The Perplexity screen |
| 1. 출처가 표시된 검색 결과 제공 – 정보 신뢰도 확인 가능 | 1. Search results carry their sources, so you can judge how reliable the information is |
| 2. 시장 조사, 경쟁사 분석, 트렌드 파악에 최적화 | 2. Tuned for market research, competitor analysis and trend spotting |
| 3. 관련 질문 자동 제안 – 심층 리서치 효율 향상 | 3. Suggests related questions automatically, making deep research more efficient |
| 4. 활용 예: '2025년 업무 관리 SaaS 시장 트렌드 분석해줘' | 4. Example prompt: "Analyze 2025 trends in the task-management SaaS market" |
| 5. https://www.perplexity.ai | 5. https://www.perplexity.ai |

### Slide 18 — 2-1-2. Claude / ChatGPT

| 한국어 | English |
|---|---|
| **2-1-2. Claude / ChatGPT – 서비스 기획 및 명세서 작성** | **2-1-2. Claude / ChatGPT — Service Planning and Spec Writing** |
| 콘셉트 구체화부터 페르소나, 기능 명세서까지 | From fleshing out the concept to personas and functional specs |
| *(image)* Claude 기획 – CLAUDE.md 예시 | *(image)* Planning in Claude — a CLAUDE.md example |
| 1. 서비스 콘셉트 구체화 – 아이디어를 기획서 형태로 정리 | 1. Flesh out the service concept — turn an idea into a written proposal |
| 2. 사용자 페르소나 자동 생성 – 타겟 유저 시나리오 도출 | 2. Generate user personas automatically and derive target-user scenarios |
| 3. 기능 명세서 초안 – 기능 목록, 우선순위, 조건 정리 | 3. Draft a functional spec — feature list, priorities and conditions |
| 4. 활용 예: 'B2B 협업 도구 핵심 사용자 페르소나 3개 만들어줘' | 4. Example prompt: "Create three core user personas for a B2B collaboration tool" |
| 5. https://claude.ai / https://chatgpt.com | 5. https://claude.ai / https://chatgpt.com |

### Slide 19 — 2-1-3. Gamma

| 한국어 | English |
|---|---|
| **2-1-3. Gamma – AI 기획서 및 PPT 자동 생성** | **2-1-3. Gamma — Automatic AI Proposals and Slide Decks** |
| 텍스트 한 줄 > PPT, 랜딩 페이지 형태 기획서 | One line of text becomes a deck or a landing-page-style proposal |
| *(image)* Gamma 자동 생성 슬라이드 | *(image)* Slides generated automatically by Gamma |
| 1. 텍스트 입력만으로 PPT 또는 랜딩 페이지 형태 기획서 자동 생성 | 1. Text alone produces a proposal as a slide deck or a landing page |
| 2. 헤더, 카드, 차트가 한 번에 – 디자인 작업 불필요 | 2. Headers, cards and charts come together — no design work needed |
| 3. AI 어시스턴트로 슬라이드 추가, 수정, 개선 가능 | 3. An AI assistant can add, edit and improve slides |
| 4. 활용 예: 'B2B 협업 도구 서비스 제안서 만들어줘' | 4. Example prompt: "Create a service proposal for a B2B collaboration tool" |
| 5. https://gamma.app | 5. https://gamma.app |

### Slide 20 — 2-1-4. Manyfast

| 한국어 | English |
|---|---|
| **2-1-4. Manyfast – 아이디어 > PRD(제품 요구사항 문서) + 와이어프레임** | **2-1-4. Manyfast — Idea to PRD (Product Requirements Document) plus Wireframes** |
| 기획서부터 와이어프레임까지 한 번에 | From proposal to wireframe in a single pass |
| *(image)* Manyfast – PRD + 기능명세 생성 | *(image)* Manyfast generating a PRD and functional spec |
| 1. 아이디어를 입력하면 PRD(제품 요구사항 문서) 자동 생성 | 1. Enter an idea and a PRD (product requirements document) is generated automatically |
| 2. 와이어프레임까지 한 번에 – 기획과 설계 동시 진행 | 2. Wireframes come with it — planning and design advance together |
| 3. PRD: 기능 정의, 우선순위, 제약사항, 성공 지표 포함 | 3. The PRD covers feature definitions, priorities, constraints and success metrics |
| 4. 활용 예: '업무 관리 앱 PRD(제품 요구사항 문서)와 와이어프레임 만들어줘' | 4. Example prompt: "Create a PRD and wireframes for a task-management app" |
| 5. https://www.manyfast.ai | 5. https://www.manyfast.ai |

### Slide 21 — 2-1-5. Figma AI

| 한국어 | English |
|---|---|
| **2-1-5. Figma AI – 프롬프트 > UI 프로토타입** | **2-1-5. Figma AI — Prompt to UI Prototype** |
| 요구사항을 기반으로 와이어프레임, UI 자동 제작 | Wireframes and UI built automatically from your requirements |
| *(image)* Figma AI – 와이어프레임 자동 생성 | *(image)* Figma AI generating a wireframe |
| 1. 텍스트 프롬프트로 와이어프레임과 UI 프로토타입을 빠르게 생성 | 1. A text prompt quickly produces wireframes and UI prototypes |
| 2. 기존 Figma 환경 그대로 – 생성 후 바로 편집 가능 | 2. It stays inside Figma, so you can edit the result straight away |
| 3. 모바일, 웹 레이아웃 모두 지원 | 3. Supports both mobile and web layouts |
| 4. 활용 예: 'B2B 협업 도구의 모바일 홈 화면을 만들어줘' | 4. Example prompt: "Design the mobile home screen for a B2B collaboration tool" |
| 5. https://www.figma.com | 5. https://www.figma.com |

### Slide 22 — 2-1-6. Uizard

| 한국어 | English |
|---|---|
| **2-1-6. Uizard – 스케치 및 텍스트 > 고충실도 UI** | **2-1-6. Uizard — Sketches and Text to High-Fidelity UI** |
| 손 그림 스케치도 UI로 변환 | Even a hand-drawn sketch becomes a UI |
| *(image)* Uizard – 템플릿 선택 화면 | *(image)* Uizard's template picker |
| 1. 텍스트 설명 > 고충실도(High-fidelity) UI 화면으로 변환 | 1. Turns a written description into a high-fidelity UI screen |
| 2. 손 그림 스케치 사진 > UI 화면으로 자동 변환 | 2. Converts a photo of a hand-drawn sketch into a UI screen automatically |
| 3. 3가지 시안 자동 생성 – 원하는 스타일 선택 | 3. Generates three variants so you can pick the style you want |
| 4. 활용 예: 텍스트로 화면 묘사 > 3가지 UI 시안 비교 선택 | 4. Example use: describe a screen in text, then compare three UI variants and choose |
| 5. https://uizard.io | 5. https://uizard.io |

### Slide 23 — 2-1-7. EdrawMind

| 한국어 | English |
|---|---|
| **2-1-7. EdrawMind – 마인드맵 및 로직 구조화** | **2-1-7. EdrawMind — Mind Mapping and Structuring Logic** |
| 서비스 기획 구조와 핵심 로직 시각화 | Visualizing service structure and core logic |
| *(image)* EdrawMind – 마인드맵 시각화 | *(image)* A mind map visualized in EdrawMind |
| 1. 서비스 기획 구조와 핵심 로직을 마인드맵 형태로 시각화 | 1. Visualize the structure of a service plan and its core logic as a mind map |
| 2. AI 자동 생성 – 초기 마인드맵 골격을 빠르게 구성 | 2. AI generation builds the initial skeleton of the map quickly |
| 3. 사용자, 기능, 비즈니스, 기술 축으로 서비스 전체 구조 파악 | 3. Grasp the whole service across four axes: users, features, business and technology |
| 4. 활용 예: 서비스 기획 마인드맵 > 팀원과 구조 공유 | 4. Example use: build a planning mind map and share the structure with teammates |
| 5. https://www.edrawmind.com | 5. https://www.edrawmind.com |

### Slide 24 — 2-2. AI 보조 코딩 / AI-Assisted Coding

| 한국어 | English |
|---|---|
| **2-2. AI 보조 코딩 (Assisted Coding)** | **2-2. AI-Assisted Coding** |
| 개발자가 코드 작성 중 AI가 보조 | The AI assists while the developer writes the code |
| 1. 개발자가 코드를 직접 작성, AI 는 제안까지 담당 | 1. The developer writes the code; the AI's job stops at suggestions |
| 2. 자동완성 제안, 버그 수정, 코드 리뷰 | 2. Autocomplete suggestions, bug fixes, code review |
| 3. 기존 개발 방식의 연장선 – 코드를 이해해야 함 | 3. An extension of conventional development — you still have to understand the code |
| 4. 대표 도구: GitHub Copilot, ChatGPT | 4. Leading tools: GitHub Copilot, ChatGPT |
### Slide 25 — 2-2-1. GitHub Copilot

| 한국어 | English |
|---|---|
| **2-2-1. GitHub Copilot – IDE 플러그인 자동완성** | **2-2-1. GitHub Copilot — Autocomplete as an IDE Plugin** |
| Microsoft, OpenAI 협업, 2022년 출시 | A Microsoft–OpenAI collaboration, released in 2022 |
| *(image)* GitHub Copilot 동작 화면 | *(image)* GitHub Copilot in action |
| 1. IDE에 플러그인으로 설치 (VS Code, JetBrains 등) | 1. Installed as an IDE plugin (VS Code, JetBrains and others) |
| 2. 코드 입력 중 실시간 자동완성 제안 | 2. Suggests completions in real time as you type |
| 3. Tab 키로 수락, 계속 타이핑으로 무시 | 3. Press Tab to accept, or keep typing to ignore |
| 4. 월 $10 (개인), $19 (비즈니스) | 4. $10/month for individuals, $19 for business |
| 5. https://github.com/features/copilot | 5. https://github.com/features/copilot |

### Slide 26 — 2-2-2. ChatGPT — 버그 수정 및 리팩토링 / Bug Fixing and Refactoring

| 한국어 | English |
|---|---|
| **2-2-2. ChatGPT – 버그 수정 및 리팩토링** | **2-2-2. ChatGPT — Bug Fixing and Refactoring** |
| 가장 범용적인 AI 코딩 도구 | The most general-purpose AI coding tool |
| *(image)* ChatGPT – todo HTML 코드 생성 | *(image)* ChatGPT generating HTML for a to-do app |
| 1. 코드 붙여넣기 > 버그 수정 요청 | 1. Paste in code and ask for the bug to be fixed |
| 2. 코드 설명 / 리팩토링 / 테스트 코드 생성 | 2. Explain code, refactor it, or generate tests |
| 3. 특정 언어로 변환 요청 가능 | 3. You can ask it to translate code into another language |
| 4. 무료 버전도 충분히 활용 가능 | 4. The free tier is already useful enough |

### Slide 27 — 2-3. AI 바이브 코딩 / AI Vibe Coding

| 한국어 | English |
|---|---|
| **2-3. AI 바이브 코딩 (Vibe Coding)** | **2-3. AI Vibe Coding** |
| 자연어 한 문장으로 AI 가 전체 코드 생성 | One sentence of natural language, and the AI writes all the code |
| 1. 개발자가 코드를 직접 작성하지 않음 | 1. The developer does not write the code |
| 2. AI에게 의도를 전달 > AI가 전체 기능 구현 | 2. You convey intent to the AI, and it implements the whole feature |
| 3. 개발자 역할 = 의도 전달 + 결과 검증 | 3. The developer's role is conveying intent and verifying the result |
| 4. 대표 도구: Claude Code, Antigravity, Cursor, OpenAI Codex CLI | 4. Leading tools: Claude Code, Antigravity, Cursor, OpenAI Codex CLI |

### Slide 28 — 2-3-1. Claude Code

| 한국어 | English |
|---|---|
| **2-3-1. Claude Code – 본 과정의 핵심 도구** | **2-3-1. Claude Code — The Core Tool of This Course** |
| Anthropic 제작, 터미널 기반 AI 에이전트 | Built by Anthropic; a terminal-based AI agent |
| *(image)* Claude Code – 자연어 지시로 index.html 생성 | *(image)* Claude Code creating index.html from a natural-language instruction |
| 1. 터미널에서 자연어로 지시 | 1. You instruct it in natural language from the terminal |
| 2. 파일 생성, 수정, 실행까지 자율 수행 | 2. It creates, edits and runs files autonomously |
| 3. CLAUDE.md로 프로젝트 맥락 유지 | 3. CLAUDE.md keeps the project context |
| 4. API Key 방식 (강사 제공) – 본 과정 적용 | 4. Uses an API key (provided by the instructor) for this course |
| 5. https://claude.ai/code | 5. https://claude.ai/code |

### Slide 29 — 2-3-2. Antigravity

| 한국어 | English |
|---|---|
| **2-3-2. Antigravity – Google DeepMind AI 에이전트** | **2-3-2. Antigravity — Google DeepMind's AI Agent** |
| VS Code 기반 차세대 AI 개발 환경 | A next-generation AI development environment built on VS Code |
| *(image)* Antigravity – Implementation Plan 실행 | *(image)* Antigravity executing an implementation plan |
| 1. Google DeepMind 제작, VS Code 기반 | 1. Built by Google DeepMind, on top of VS Code |
| 2. Gemini 모델 기반, 병렬 에이전트 실행 | 2. Runs on Gemini models, with agents executing in parallel |
| 3. 브라우저 에이전트 – 웹 서비스 직접 조작 | 3. A browser agent operates web services directly |
| 4. Google 생태계 사용 시 Claude Code 대안 | 4. An alternative to Claude Code if you live in the Google ecosystem |
| 5. https://antigravity.dev | 5. https://antigravity.dev |

### Slide 30 — 2-3-3. Cursor

| 한국어 | English |
|---|---|
| **2-3-3. Cursor – IDE 기반 AI 협업 에디터** | **2-3-3. Cursor — An IDE-Based AI Collaborative Editor** |
| VS Code 포크, AI 기능 내장 | A fork of VS Code with AI built in |
| *(image)* Cursor – @Codebase 채팅으로 코드 분석 | *(image)* Cursor analyzing code through @Codebase chat |
| 1. VS Code 기반 – 기존 환경 그대로 사용 | 1. Built on VS Code, so your existing setup carries over |
| 2. 파일 단위 AI 수정, 채팅 방식 | 2. AI edits at file level, driven through chat |
| 3. AI와 대화하며 코드 개발 | 3. You develop code in conversation with the AI |
| 4. 월 $20, 학생 할인 가능 | 4. $20/month, with a student discount available |
| 5. https://www.cursor.com | 5. https://www.cursor.com |

### Slide 31 — 2-3-4. OpenAI Codex CLI

| 한국어 | English |
|---|---|
| **2-3-4. OpenAI Codex CLI – 터미널 기반 AI 코딩** | **2-3-4. OpenAI Codex CLI — Terminal-Based AI Coding** |
| Claude Code와 동일 계열 – 바이브 코딩 도구 | Same family as Claude Code — a vibe coding tool |
| *(image)* Codex CLI – Explain this code base | *(image)* Codex CLI — "Explain this code base" |
| 1. 터미널 기반 AI 에이전트, Claude Code와 유사 | 1. A terminal-based AI agent, much like Claude Code |
| 2. 자연어 > 코드 자동 생성 | 2. Natural language in, generated code out |
| 3. OpenAI가 만든 코딩 전용 CLI 도구 | 3. A coding-specific CLI tool made by OpenAI |
| 4. Codex CLI = 바이브 코딩 도구 (보조 코딩 아님) | 4. Codex CLI is a vibe coding tool, not an assisted-coding one |
| 5. https://openai.com/blog/openai-codex | 5. https://openai.com/blog/openai-codex |

### Slide 32 — 2-4. 보조 코딩 vs 바이브 코딩 / Assisted vs. Vibe Coding

| 한국어 | English |
|---|---|
| **2-4. AI 보조 코딩 vs AI 바이브 코딩** | **2-4. AI-Assisted Coding vs. AI Vibe Coding** |
| 항목 · AI 보조 코딩 · AI 바이브 코딩 | Aspect · AI-assisted coding · AI vibe coding |
| 코드 작성 주체 · 개발자가 직접 작성 · AI가 전체 생성 | Who writes the code · The developer · The AI generates all of it |
| 개발자 역할 · 코드 작성자 · 의도 전달 + 결과 검증 | Developer's role · Code author · Conveying intent and verifying results |
| 필요 역량 · 코딩 실력 필수 · 판단력 + 프롬프팅 | Skills needed · Coding ability is essential · Judgment and prompting |
| 에러 처리 · 개발자가 직접 수정 · AI가 스스로 수정 | Error handling · The developer fixes it · The AI fixes it itself |
| 속도 향상 · 기존 대비 20~30% · 기존 대비 50~80% | Speed gain · 20–30% over conventional work · 50–80% over conventional work |
| 대표 도구 · Copilot, ChatGPT · Claude Code, Antigravity, Cursor, Codex CLI | Leading tools · Copilot, ChatGPT · Claude Code, Antigravity, Cursor, Codex CLI |
| 본 과정 · – · 바이브 코딩으로 풀스택 앱 완성 | This course · – · Builds a complete full-stack app through vibe coding |

### Slide 33 — 2-5. 서비스 단계 / The Service Stage — AI API Integration

| 한국어 | English |
|---|---|
| **2-5. 서비스 단계 – AI API 연동** | **2-5. The Service Stage — Integrating AI APIs** |
| AI 기능을 내 앱에 직접 탑재 | Putting AI features inside your own app |
| 1. AI API 연동 – OpenAI, Claude, Gemini API로 챗봇, 요약, 검색, 분류 기능 구현 | 1. AI API integration — build chatbots, summarization, search and classification with the OpenAI, Claude and Gemini APIs |
| 2. RAG – Retrieval-Augmented Generation, 내 문서 기반 AI 답변 시스템 | 2. RAG — Retrieval-Augmented Generation, an AI answering system grounded in your own documents |
| 3. LangChain / LangGraph / Flowise – AI 기능 파이프라인 구축 프레임워크 | 3. LangChain / LangGraph / Flowise — frameworks for building AI feature pipelines |
| 4. 본 과정에서는 개념만 소개 > 심화는 LangChain/Flowise 별도 과정 | 4. This course covers the concepts only; the depth is in a separate LangChain/Flowise course |
| 5. https://aistudio.google.com / https://console.anthropic.com / https://platform.openai.com | 5. https://aistudio.google.com / https://console.anthropic.com / https://platform.openai.com |

### Slide 34 — 2-5-1. Google AI Studio

| 한국어 | English |
|---|---|
| **2-5-1. AI API 연동 – Google AI Studio** | **2-5-1. AI API Integration — Google AI Studio** |
| 가장 쉽게 시작하는 AI API 연동 | The easiest place to start with AI APIs |
| *(image)* Google AI Studio – Gemini API 사용량 | *(image)* Gemini API usage in Google AI Studio |
| 1. Google AI Studio – Gemini API Key 무료 발급, 브라우저에서 바로 테스트 | 1. Google AI Studio — free Gemini API keys, testable right in the browser |
| 2. Anthropic Console – Claude API Key 발급, claude-3-5-sonnet 등 모델 선택 | 2. Anthropic Console — issue Claude API keys and choose models such as claude-3-5-sonnet |
| 3. OpenAI Platform – GPT-4o API Key 발급, 코드 예시 제공 | 3. OpenAI Platform — issue GPT-4o API keys, with code examples provided |
| 4. 공통 흐름: API Key 발급 > 코드에 Key 설정 > API 호출 > 응답 처리 | 4. The common flow: issue an API key, set it in your code, call the API, handle the response |
| 5. 공식: aistudio.google.com / console.anthropic.com / platform.openai.com | 5. Official sites: aistudio.google.com / console.anthropic.com / platform.openai.com |

### Slide 35 — 2-5-2. RAG

| 한국어 | English |
|---|---|
| **2-5-2. RAG – Retrieval-Augmented Generation (검색 증강 생성)** | **2-5-2. RAG — Retrieval-Augmented Generation** |
| 검색 증강 생성 · 내 문서를 AI가 읽고 답변 | Retrieval-augmented generation — the AI reads your documents and answers from them |
| *(image)* RAG 벡터 공간 – 의미 유사 질문 클러스터링 | *(image)* RAG vector space — semantically similar questions clustering together |
| 1. AI가 답할 때 외부 문서를 직접 검색, 참조하는 기술 | 1. A technique where the AI searches and consults external documents as it answers |
| 2. 기존 AI 문제 – 학습된 데이터 외 질문에 엉뚱한 답변 (환각) | 2. The problem with plain AI — it answers nonsensically outside its training data (hallucination) |
| 3. RAG 해결 – 내 문서를 벡터DB에 저장 > 질문 시 관련 문서 검색 > AI가 참조하여 정확 답변 | 3. RAG's fix — store your documents in a vector database, retrieve the relevant ones per question, and let the AI answer accurately from them |
| 4. 활용 예 – 사내 규정 챗봇, 제품 매뉴얼 Q&A, 법률 문서 검색 | 4. Example uses — an internal-policy chatbot, product-manual Q&A, legal document search |

### Slide 36 — 2-5-3. LangChain

| 한국어 | English |
|---|---|
| **2-5-3. LangChain – AI 앱 개발 프레임워크** | **2-5-3. LangChain — A Framework for Building AI Apps** |
| 여러 AI 기능을 체인처럼 연결 | Linking several AI capabilities together like a chain |
| *(image)* LangChain 챗봇 – 응답 + 단계별 소요 시간 | *(image)* A LangChain chatbot — the response and the time each step took |
| 1. LLM을 활용한 앱을 쉽게 만드는 Python/JS 프레임워크 | 1. A Python/JS framework that makes LLM-powered apps easy to build |
| 2. 체인(Chain) – 여러 AI 기능을 순서대로 연결 (입력 > 처리 > 출력) | 2. A chain links AI steps in sequence: input, processing, output |
| 3. RAG, 챗봇, 요약, 분류 등 다양한 AI 기능 구현 가능 | 3. Supports RAG, chatbots, summarization, classification and more |
| 4. 활용 예 – 문서 요약 봇, 고객 상담 AI, 코드 리뷰 자동화 | 4. Example uses — a document summarizer, a customer-support AI, automated code review |
| 5. https://www.langchain.com | 5. https://www.langchain.com |

### Slide 37 — 2-5-4. LangGraph

| 한국어 | English |
|---|---|
| **2-5-4. LangGraph – 그래프 기반 AI 에이전트** | **2-5-4. LangGraph — Graph-Based AI Agents** |
| 조건 분기, 반복이 있는 복잡한 AI 워크플로우 | Complex AI workflows with branching and loops |
| *(image)* LangGraph Studio – memory-agent 그래프 | *(image)* LangGraph Studio — the memory-agent graph |
| 1. LangChain의 확장 – 그래프(흐름도) 방식으로 AI 에이전트 구성 | 1. An extension of LangChain that composes agents as a graph (a flow diagram) |
| 2. 조건 분기, 반복, 병렬 처리 – 복잡한 AI 에이전트 구현에 최적 | 2. Branching, looping and parallelism — ideal for complex agents |
| 3. 예: 질문 유형에 따라 다른 AI 도구를 선택하는 라우팅 에이전트 | 3. For example, a routing agent that picks a different AI tool depending on the type of question |
| 4. 활용 예 – 다단계 리서치 봇, 자율 작업 에이전트, 복잡한 비즈니스 프로세스 자동화 | 4. Example uses — multi-step research bots, autonomous task agents, complex business-process automation |
| 5. https://langchain-ai.github.io/langgraph | 5. https://langchain-ai.github.io/langgraph |

### Slide 38 — 2-5-5. Flowise

| 한국어 | English |
|---|---|
| **2-5-5. Flowise – 노코드 AI 파이프라인 도구** | **2-5-5. Flowise — A No-Code AI Pipeline Tool** |
| LangChain을 드래그앤드롭으로 | LangChain by drag and drop |
| *(image)* Flowise – Agentflow 구성 + 챗봇 테스트 | *(image)* Flowise — building an Agentflow and testing the chatbot |
| 1. LangChain을 코드 없이 GUI로 사용하는 노코드 도구 | 1. A no-code tool that drives LangChain through a GUI |
| 2. 드래그앤드롭 – 블록을 연결해서 AI 파이프라인 시각적으로 구성 | 2. Drag and drop — connect blocks to compose an AI pipeline visually |
| 3. 빠른 프로토타이핑 – 코드 없이 RAG, 챗봇 등 AI 서비스 즉시 구현 | 3. Rapid prototyping — stand up RAG, chatbots and other AI services without code |
| 4. 활용 예 – 비개발자도 챗봇 구축, AI 기능 빠른 테스트, MVP 구현 | 4. Example uses — non-developers building chatbots, quick tests of AI features, MVPs |
| 5. https://flowiseai.com | 5. https://flowiseai.com |

### Slide 39 — 2-6. 개발 단계별 AI 활용 정리 / AI by Development Stage

| 한국어 | English |
|---|---|
| **2-6. 개발 단계별 AI 활용 정리** | **2-6. Summary — Using AI at Each Development Stage** |
| 단계 · 방법 · 대표 도구 | Stage · Approach · Leading tools |
| 1) 기획 · 요구사항, 기획서, API 설계 자동화 · Claude, ChatGPT | 1) Planning · Automating requirements, proposals and API design · Claude, ChatGPT |
| 2) 보조 코딩 · 자동완성, 버그 수정, 리팩토링 · Copilot, ChatGPT | 2) Assisted coding · Autocomplete, bug fixes, refactoring · Copilot, ChatGPT |
| 3) 바이브 코딩 · 자연어로 전체 기능 구현 · Claude Code, Antigravity, Cursor, Codex CLI | 3) Vibe coding · Implementing whole features from natural language · Claude Code, Antigravity, Cursor, Codex CLI |
| 4) 서비스 · AI 기능 앱에 탑재 · OpenAI API, LangChain | 4) Service · Embedding AI features in the app · OpenAI API, LangChain |

### Slide 40 — 체크포인트 / Checkpoint

| 한국어 | English |
|---|---|
| **체크포인트** | **Checkpoint** |
| 1. 개발 단계별 AI 활용 방법 | 1. How to use AI at each development stage |
| 2. 바이브 코딩 도구 4종의 차이 | 2. How the four vibe coding tools differ |
| 3. AI API 연동과 RAG 의 쓰임 | 3. What AI API integration and RAG are for |

---

## 3장. 바이브코딩 + AI-DLC / Chapter 3. Vibe Coding + AI-DLC

### Slide 41 — Chapter cover

| 한국어 | English |
|---|---|
| **바이브코딩 개발론 + AI-DLC 개념** | **The Vibe Coding Development Philosophy + the AI-DLC Concept** |
| 바이브코딩 정의 + AI-DLC 프레임워크 + OpenSpec 예고 | Defining vibe coding, the AI-DLC framework, and a preview of OpenSpec |
| 학습 내용 | What you will learn |
| 1. 바이브코딩 정의 | 1. What vibe coding is |
| 2. AI-DLC 인간 vs AI 역할 | 2. Human vs. AI roles in AI-DLC |
| 3. 바이브코딩 함정 3가지 | 3. Three pitfalls of vibe coding |

### Slide 42 — 3-1. AI 코딩 도구 진화 / How AI Coding Tools Evolved

| 한국어 | English |
|---|---|
| **3-1. AI 코딩 도구 진화 – 자동완성에서 자율 개발까지** | **3-1. The Evolution of AI Coding Tools — from Autocomplete to Autonomous Development** |
| 2022 · GitHub Copilot · IDE 플러그인 · 한 줄 자동완성 | 2022 · GitHub Copilot · IDE plugin · Line-by-line autocomplete |
| 2023 · ChatGPT 코딩 · 대화형 · 코드 생성, 수정 | 2023 · Coding with ChatGPT · Conversational · Generating and editing code |
| 2023~24 · Cursor · IDE 기반 · AI 협업 에디터 | 2023–24 · Cursor · IDE-based · AI collaborative editor |
| 2025 · Claude Code · 터미널 에이전트 · 전체 자율 개발 | 2025 · Claude Code · Terminal agent · Fully autonomous development |
| 2025 · Antigravity · VS Code 에이전트 · Google DeepMind | 2025 · Antigravity · VS Code agent · Google DeepMind |

### Slide 43 — 3-2. 바이브코딩의 정의 / Defining Vibe Coding

| 한국어 | English |
|---|---|
| **3-2. 바이브코딩의 정의** | **3-2. Defining Vibe Coding** |
| Andrej Karpathy, 2025.02 | Andrej Karpathy, February 2025 |
| 1. "코드를 직접 짜는 게 아니라 의도를 전달하고 AI 출력을 검증하는 방식" | 1. "Rather than writing the code yourself, you convey intent and verify the AI's output" |
| 2. 개발자 역할 변화 – 코드 작성자 > AI 감독자, 검증자 | 2. The developer's role shifts — from code author to supervisor and verifier of the AI |
| 3. 학습 필요성 – 개발자 84% AI 사용, 속도 55% 향상 | 3. Why you need to learn it — 84% of developers use AI, with a 55% speed gain |
| 4. 미학습 시 – 경쟁력 하락, 생산성 격차 확대 | 4. If you don't — you lose competitiveness and the productivity gap widens |

### Slide 44 — 3-3. 개발자 역할 변화 / How the Developer's Role Changes

| 한국어 | English |
|---|---|
| **3-3. 개발자 역할 변화** | **3-3. How the Developer's Role Changes** |
| 바이브코딩 이후 달라지는 것 | What is different after vibe coding |
| 1. Before – 코드 직접 작성, 문법 암기, 에러 디버깅 | 1. Before — writing code by hand, memorizing syntax, debugging errors |
| 2. After – 의도 전달, 결과 검증, 방향 결정 | 2. After — conveying intent, verifying results, deciding direction |
| 3. 새로운 핵심 역량 – 좋은 프롬프트 작성, 결과물 판단력 | 3. The new core skills — writing good prompts, and judging the output |
| 4. 사라지지 않는 것 – 시스템 설계, 비즈니스 이해, 품질 판단 | 4. What does not go away — system design, business understanding, quality judgment |

### Slide 45 — 3-4. AI-DLC

| 한국어 | English |
|---|---|
| **3-4. AI-DLC – AI 주도 개발 라이프사이클** | **3-4. AI-DLC — the AI-Driven Development Life Cycle** |
| AI-Driven Development Life Cycle · AWS가 제안한 방법론 | AI-Driven Development Life Cycle — a methodology proposed by AWS |
| 1. AI-DLC 정의 – AI 를 단순 보조가 아닌 개발 전 과정의 핵심 협력자로 활용하는 방법론 | 1. What AI-DLC is — a methodology that treats AI not as a mere assistant but as a core collaborator across the whole development process |
| 2. 제안 – AWS(Amazon Web Services)가 실제 프로덕션 경험 기반으로 공개한 방법론 | 2. Origin — published by AWS (Amazon Web Services) out of real production experience |
| 3. 핵심 원칙 1) – AI 주도 실행 + 인간 감독: AI가 계획, 코드 생성, 인간이 검토, 승인 | 3. Core principle 1 — AI-led execution with human oversight: the AI plans and generates code, the human reviews and approves |
| 4. 핵심 원칙 2) – 단순 바이브코딩 vs AI-DLC: 바이브코딩은 한 번에 생성, AI-DLC는 단계별 검증 | 4. Core principle 2 — plain vibe coding generates it all at once; AI-DLC verifies stage by stage |
| 5. https://github.com/awslabs/aidlc-workflows / https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle | 5. https://github.com/awslabs/aidlc-workflows / https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle |

### Slide 46 — 3-5. AI-DLC 5단계 프로세스 / The Five-Stage AI-DLC Process

*Grid layout: five stages across, three rows (Human / AI / Tools).*

| 한국어 | English |
|---|---|
| **3-5. AI-DLC 5단계 프로세스** | **3-5. The Five-Stage AI-DLC Process** |
| AWS AI-Driven Development Life Cycle · 인간과 AI의 역할을 단계별로 명확히 분리 | AWS AI-Driven Development Life Cycle — human and AI roles cleanly separated at every stage |
| 단계 1) 요구사항 분석 | Stage 1) Requirements analysis |
| — 인간: 목표 정의, 제약 결정 | — Human: define the goal, decide the constraints |
| — AI: 유사 사례 분석 | — AI: analyze comparable cases |
| — 도구: 외부 도구 + OpenSpec | — Tools: external tools + OpenSpec |
| 단계 2) 스펙 작성 | Stage 2) Writing the spec |
| — 인간: WHY 결정, 검토, 승인 | — Human: decide the WHY, review and approve |
| — AI: WHAT/HOW 제안 | — AI: propose the WHAT and HOW |
| — 도구: OpenSpec | — Tools: OpenSpec |
| 단계 3) 코드 생성 | Stage 3) Code generation |
| — 인간: 방향 결정, 결과 검토 | — Human: set the direction, review the result |
| — AI: 코드 자동 생성 | — AI: generate the code |
| — 도구: Claude Code + OpenSpec | — Tools: Claude Code + OpenSpec |
| 단계 4) 검증 & 테스트 | Stage 4) Verification & testing |
| — 인간: 품질 최종 판단, 승인 | — Human: final quality judgment and approval |
| — AI: 자동 테스트, 오류 탐지 | — AI: automated tests and error detection |
| — 도구: pytest + Claude Code + OpenSpec | — Tools: pytest + Claude Code + OpenSpec |
| 단계 5) 배포 & 운영 | Stage 5) Deployment & operations |
| — 인간: 승인, 모니터링 | — Human: approve and monitor |
| — AI: CI/CD 자동 실행 | — AI: run CI/CD automatically |
| — 도구: Actions + Vercel + OpenSpec | — Tools: Actions + Vercel + OpenSpec |
| 모든 단계가 OpenSpec 산출물 (proposal / specs / design / tasks) 위에서 동작 · 단계별 역할 변화는 다음 장 | Every stage runs on OpenSpec artifacts (proposal / specs / design / tasks). The next slide shows how roles shift stage by stage |

### Slide 47 — 3-6. S-DLC vs AI-DLC

| 한국어 | English |
|---|---|
| **3-6. S-DLC vs AI-DLC – 개발자 역할의 이동** | **3-6. S-DLC vs. AI-DLC — the Shift in the Developer's Role** |
| 3-5 의 5단계를 그대로 세로축으로 – 단계마다 달라지는 개발자 역할 · 실현 도구는 심화편 OpenSpec 에서 | The same five stages as slide 3-5, now down the vertical axis — how the developer's role changes at each. The enabling tools come in the Advanced course's OpenSpec chapter |
| 단계 · S-DLC (전통) · AI-DLC · 개발자 역할 · 실현 도구 | Stage · S-DLC (traditional) · AI-DLC · Developer's role · Enabling tool |
| 요구분석 · 인터뷰, 문서화 · AI 자동 분석 + 사람 확정 · 수집자 > 정의자 · OpenSpec > proposal.md | Requirements · Interviews, documentation · AI analyzes, the human confirms · Collector becomes definer · OpenSpec > proposal.md |
| 스펙, 설계 · UML, API 수작업 · OpenSpec 자동 생성 + 승인 · 작성자 > 검토자 · OpenSpec > specs/{기능}/spec.md | Spec & design · Hand-written UML and APIs · OpenSpec generates, the human approves · Author becomes reviewer · OpenSpec > specs/{feature}/spec.md |
| 구현 · 라인 by 라인 · 바이브코딩 자동 + 방향 · 타이퍼 > 디렉터 · Claude Code <- design.md | Implementation · Line by line · Vibe coding automates it, the human steers · Typist becomes director · Claude Code <- design.md |
| 테스트 · 케이스 수작업 · AI 자동 생성, 실행 · 작성자 > 판단자 · pytest + Claude Code <- tasks.md | Testing · Hand-written cases · The AI generates and runs them · Author becomes judge · pytest + Claude Code <- tasks.md |
| 배포 · 수동 배포 · 개발자 push > 이후 자동 · 운영자 > 감독자 · git push + Actions + Vercel <- tasks.md | Deployment · Manual · The developer pushes, the rest is automatic · Operator becomes overseer · git push + Actions + Vercel <- tasks.md |
| S-DLC: 실행자 (Worker) · AI-DLC: 결정자 (Decision Maker) | S-DLC: the worker · AI-DLC: the decision maker |
| 개발자가 '왜, 무엇, 언제' 결정 / AI 가 '어떻게' 실행 | The developer decides why, what and when; the AI executes the how |
| 코딩 실력보다 판단 실력 – 실현 도구인 OpenSpec 산출물 4종은 심화편 2장에서 | Judgment matters more than coding skill. The four OpenSpec artifacts that make this work come in Chapter 2 of the Advanced course |

### Slide 48 — 3-7. 바이브코딩의 함정 / The Pitfalls of Vibe Coding

| 한국어 | English |
|---|---|
| **3-7. 바이브코딩의 함정** | **3-7. The Pitfalls of Vibe Coding** |
| 왜 체계적 방법론이 필요한가 | Why you need a systematic methodology |
| 1. 보안 취약점 45% – AI가 만든 코드에 보안 문제 포함 가능 | 1. 45% security vulnerabilities — AI-generated code can carry security problems |
| 2. 코드 판독 불가 시 디버깅 불가 – AI 오류를 판별 불가 | 2. If you cannot read the code you cannot debug it — you cannot tell when the AI is wrong |
| 3. 컨텍스트 없이 지시 > 매번 다른 구조의 코드 생성 | 3. Instructions without context produce differently structured code every time |
| 4. 해결책 – CLAUDE.md + OpenSpec으로 일관성 확보 | 4. The fix — secure consistency with CLAUDE.md and OpenSpec |
### Slide 49 — 3-8. SDD 도입은 AI 도입과 별개 / Adopting SDD Is Separate from Adopting AI

| 한국어 | English |
|---|---|
| **3-8. SDD 도입은 AI 도입과 별개** | **3-8. Adopting SDD Is a Separate Matter from Adopting AI** |
| SDD (Spec Driven Development) 는 도구가 아니라 개발 프로세스의 표준화 | SDD (Spec-Driven Development) is not a tool — it is the standardization of the development process |
| AI 는 교체되어도 스펙은 자산으로 남음 | Swap the AI out and the spec remains as an asset |
| Claude Code · Codex · Gemini — 교체 대상 | Claude Code · Codex · Gemini — all replaceable |
| > 요구사항 / 설계 의도 / 승인 이력 | > Requirements / design intent / approval history |
| **SDD 없이 AI 만 도입** | **Adopting AI without SDD** |
| – 개발자마다 프롬프트 방식이 제각각 | – Every developer prompts differently |
| – 같은 요구에도 결과물 편차가 큼 | – The same request produces wildly different output |
| – 설계 근거가 기록되지 않음 | – The reasoning behind the design is never recorded |
| – 리뷰 기준이 사람마다 다름 | – Review criteria vary from person to person |
| – 신입에게 넘길 기준 문서가 없음 | – There is no reference document to hand a new joiner |
| **SDD 도입** | **Adopting SDD** |
| – 스펙 기준으로 구현 지시 – 표준화 | – Implementation is directed against the spec — standardized |
| – 코드 리뷰 기준이 문서로 고정 | – Code review criteria are fixed in a document |
| – 결정 이력이 남아 맥락 추적 가능 | – Decisions leave a record, so context can be traced |
| – AI 를 바꿔도 스펙은 그대로 재사용 | – Change the AI and the spec is still reusable |
| – 신입에게 스펙 하나로 인계 가능 | – A new joiner can be onboarded with the spec alone |

### Slide 50 — 3-9. 바이브 코딩 실전 원칙 / Practical Principles of Vibe Coding

| 한국어 | English |
|---|---|
| **3-9. 바이브 코딩 실전 원칙** | **3-9. Practical Principles of Vibe Coding** |
| 의도 전달 > 결과 검증 > 반복 | Convey intent, verify the result, repeat |
| 1. 구체적으로 지시 – 스택, 구조, 기능을 명확히 설명 | 1. Be specific — spell out the stack, the structure and the features |
| 2. 결과를 검증 – AI가 만든 코드도 실행하고 확인 | 2. Verify the result — run and check the AI's code too |
| 3. 모르면 질문 – '이 코드 어떻게 동작해?' 로 AI 에 확인 | 3. Ask when unsure — "How does this code work?" |
| 4. 작은 단위로 지시 – 한 번에 하나씩 | 4. Instruct in small units — one thing at a time |

### Slide 51 — 체크포인트 / Checkpoint

| 한국어 | English |
|---|---|
| **체크포인트** | **Checkpoint** |
| 1. 바이브코딩 정의 | 1. What vibe coding is |
| 2. AI-DLC 인간 vs AI 역할 분리 | 2. How AI-DLC separates human and AI roles |
| 3. 바이브코딩 함정 3가지 | 3. Three pitfalls of vibe coding |

---

## 4장. 터미널 기초 / Chapter 4. Terminal Basics

### Slide 52 — Chapter cover

| 한국어 | English |
|---|---|
| **명령어 10개로 터미널에 손 익히기** | **Getting Your Hands Used to the Terminal with Ten Commands** |
| 드라이브 이동 > 폴더 생성 > 파일 다루기 > 삭제 > Tab 자동완성 | Switching drives, creating folders, handling files, deleting, Tab completion |
| 학습 내용 | What you will learn |
| 1. 명령어 10개 직접 쳐 보기 | 1. Type the ten commands yourself |
| 2. Tab 자동완성 + 방향키 히스토리 | 2. Tab completion and arrow-key history |
| 3. 자주 나는 에러 5종 대처 | 3. Handling the five most common errors |

### Slide 53 — 4-1. CLI 를 익혀야 하는 이유 / Why You Need the CLI

| 한국어 | English |
|---|---|
| **4-1. CLI (Command Line Interface) 를 익혀야 하는 이유** | **4-1. Why You Need to Learn the CLI (Command Line Interface)** |
| 특정 도구를 쓰기 위한 준비 과정이 아니라, 백엔드·DevOps·시스템 운영 전 직무의 공통 인터페이스 | Not a warm-up for one particular tool — it is the shared interface across backend, DevOps and systems roles |
| **서버 환경에는 GUI 가 없음** — 리눅스 서버는 GUI (Graphical User Interface) 미설치가 표준 구성. SSH 원격 접속 시 셸만 제공 | **Servers have no GUI** — a Linux server with no graphical interface installed is the standard configuration. Connect over SSH and all you get is a shell |
| **운영 도구 체계가 CLI 기반** — docker, kubectl, systemctl, nginx 등 주요 도구가 명령 단위 제어를 전제로 설계 | **The operations toolchain is CLI-based** — docker, kubectl, systemctl, nginx and the rest are designed around command-level control |
| **반복 작업의 자동화** — GUI 조작은 재사용이 불가하나, 명령은 스크립트로 묶어 재실행·스케줄링 가능 | **Automating repetitive work** — GUI actions cannot be reused, but commands can be bundled into scripts, re-run and scheduled |
| **장애 대응 시간 단축** — tail, grep 조합으로 대용량 로그에서 원인 구간을 즉시 필터링 | **Faster incident response** — combine tail and grep to filter straight to the cause in a huge log |
| **CI/CD 파이프라인의 실체** — CI/CD (Continuous Integration / Delivery) 워크플로는 실행할 명령의 순차 정의 | **What a CI/CD pipeline actually is** — a CI/CD (continuous integration / delivery) workflow is a sequence of commands to run |
| **학습 자산의 지속성** — GUI 는 제품별로 상이하고 개편이 잦으나, POSIX 표준 명령은 인터페이스가 장기간 유지 | **What you learn keeps its value** — GUIs differ per product and get redesigned often, while POSIX standard commands keep their interface for decades |
| 직무별로 보면 | By role |
| 백엔드 개발자 – 서버 기동·DB 마이그레이션·테스트 실행 | Backend developer — starting servers, running DB migrations and tests |
| DevOps 엔지니어 – 빌드·배포·IaC (Infrastructure as Code) | DevOps engineer — builds, deployments, IaC (infrastructure as code) |
| 시스템 엔지니어 – 계정·권한·프로세스·네트워크 점검 | Systems engineer — checking accounts, permissions, processes and networking |
| 데이터 엔지니어 – 배치 실행·로그 확인·스케줄 등록 | Data engineer — running batches, checking logs, registering schedules |
| CLI 는 특정 도구의 부속이 아니라, 개발 직무 전반에서 공통으로 사용하는 표준 인터페이스 | The CLI is not an accessory to one tool — it is the standard interface used right across development roles |

### Slide 54 — 4-2. Claude Code 가 CLI 기반인 이유 / Why Claude Code Is CLI-Based

| 한국어 | English |
|---|---|
| **4-2. Claude Code 가 CLI 기반인 이유 – 터미널에서만 가능한 범위** | **4-2. Why Claude Code Is CLI-Based — What Only the Terminal Makes Possible** |
| 편집기 프로세스에 종속된 도구와 달리, 개발자가 수행하는 작업 범위를 그대로 수행 가능 | Unlike tools bound to an editor process, it can do the full range of what a developer does |
| 1. 프로젝트 전체가 작업 범위 – 편집기에 열린 파일이 아니라 저장소 전체를 탐색·참조 | 1. The whole project is in scope — it explores and references the entire repository, not just the files open in an editor |
| 2. 파일 조작까지 직접 수행 – 코드 제안에 그치지 않고 생성·수정·삭제를 직접 실행 | 2. It manipulates files directly — not just suggesting code but creating, editing and deleting |
| 3. 명령 실행과 결과 해석 – pip install, pytest, git commit, 서버 기동을 실행하고 출력을 판독 | 3. It runs commands and reads the output — pip install, pytest, git commit, starting a server |
| 4. 원격 환경에서도 동일 동작 – SSH (Secure Shell) 로 접속한 서버에서 그대로 구동 – GUI 불필요 | 4. It behaves identically on remote machines — runs as-is on a server reached over SSH, no GUI needed |
| 5. 자동화 파이프라인에 편입 가능 – claude -p 로 스크립트·CI 파이프라인에 포함해 무인 실행 | 5. It slots into automation — `claude -p` lets you embed it in scripts and CI pipelines for unattended runs |
| 6. 운영체제·편집기 비종속 – macOS·Windows·Linux 동일 동작. 편집기 선택과 무관 | 6. It is independent of OS and editor — identical on macOS, Windows and Linux, whatever editor you use |
| IDE (통합 개발 환경) 플러그인: 개발자가 주도, AI 는 제안까지 담당 · 터미널 (Claude Code): AI 가 실행, 개발자는 검토·승인 담당 | An IDE plugin: the developer leads and the AI stops at suggestions. The terminal (Claude Code): the AI executes and the developer reviews and approves |

### Slide 55 — 4-3. PowerShell 실행 / Launching PowerShell

| 한국어 | English |
|---|---|
| **4-3. PowerShell 실행 – 모든 실습의 출발점** | **4-3. Launching PowerShell — the Starting Point for Every Exercise** |
| 방법 두 가지. 검색창이 더 간단하므로 이쪽을 먼저 사용 | Two ways. The search box is simpler, so use that one first |
| 1. 방법 1. 작업표시줄 검색창에 pow 입력 *(최적)* | 1. Method 1 — type `pow` into the taskbar search box *(best)* |
| 2. 목록 맨 위 Windows PowerShell 선택 후 Enter | 2. Pick "Windows PowerShell" at the top of the list and press Enter |
| 3. 방법 2. Windows 키 + R > powershell > Enter | 3. Method 2 — Windows key + R, then `powershell`, then Enter |
| 4. `PS C:\Users\내이름>` 이 보이면 실행 완료 | 4. When you see `PS C:\Users\yourname>` it is running |
| 5. 이 `PS ...>` 부분이 프롬프트 | 5. That `PS ...>` part is the prompt |
| 6. 프롬프트 = 현재 작업 중인 폴더 위치 | 6. The prompt tells you which folder you are currently working in |
| 7. 본 과정은 전부 PowerShell 기준 | 7. This whole course assumes PowerShell |
| 제목 표시줄이 명령 프롬프트면 CMD – 닫고 다시 실행 | If the title bar says "Command Prompt" you are in CMD — close it and start again |
| 맨 아랫줄이 프롬프트 – 여기에 명령 입력 | The bottom line is the prompt — type your commands there |

### Slide 56 — 4-4. 필수 PowerShell 명령어 10개 / Ten Essential PowerShell Commands

| PowerShell 명령어 / Command | 하는 일 / What it does | CMD 에서는 / In CMD |
|---|---|---|
| `pwd` | 지금 내가 어느 폴더에 있는지 — Which folder am I in right now | `cd` (typed alone) |
| `cd 폴더명` | 그 폴더 안으로 들어가기 — Go into that folder | `cd foldername` |
| `cd ..` | 한 단계 위 폴더로 나가기 — Go up one level | `cd ..` |
| `D:` | D 드라이브로 이동 — Switch to the D drive | `D:` |
| `dir` | 지금 폴더 안의 파일 목록 — List files in the current folder | `dir` |
| `mkdir 폴더명` | 새 폴더 만들기 — Create a new folder | `md foldername` |
| `cat 파일명` | 파일 내용 보기 — Show a file's contents | `type filename` |
| `Remove-Item 파일명` | 파일 하나 지우기 — Delete a single file | `del filename` |
| `Remove-Item -Recurse -Force 폴더명` | 폴더를 통째로 지우기 (되돌리기 불가) — Delete a whole folder (cannot be undone) | `rd /s /q foldername` |
| `cls` | 화면 지우기 (파일은 유지) — Clear the screen (files are untouched) | `cls` |

### Slide 57 — 4-5. 실습 1 / Exercise 1 — Switch Drive and Create a Folder

| 한국어 | English |
|---|---|
| **4-5. 실습 1 – D 드라이브로 이동 + 폴더 만들기** | **4-5. Exercise 1 — Move to the D Drive and Create a Folder** |
| 흰 글씨 = 내가 치는 줄 / 연한 글씨 = 화면에 나오는 결과 | White text is what you type; grey text is what the screen prints back |
| 터미널로 하면 | Doing it in the terminal |
| `# 1. D 드라이브로 이동 (콜론 : 까지)` | `# 1. Move to the D drive (include the colon)` |
| `PS C:\Users\student> D:` → `PS D:\>` | `PS C:\Users\student> D:` → `PS D:\>` |
| `# 2. 지금 내 위치 확인` → `pwd` → `Path ---- D:\` | `# 2. Check where you are` → `pwd` → `Path ---- D:\` |
| `# 3. 연습용 폴더 만들고 들어가기` | `# 3. Create a practice folder and go into it` |
| `PS D:\> mkdir cli-test` / `PS D:\> cd cli-test` / `PS D:\cli-test>` | `PS D:\> mkdir cli-test` / `PS D:\> cd cli-test` / `PS D:\cli-test>` |
| 탐색기로 하면 (같은 일): 빈 곳 우클릭 > 새로 만들기 > 폴더 | Doing the same thing in File Explorer: right-click an empty spot > New > Folder |
| 같은 일. 탐색기에서 D 드라이브를 눌러 들어가고 우클릭으로 폴더를 만드는 절차 = mkdir cli-test 한 줄 | Same outcome. Clicking into the D drive in Explorer and right-clicking to make a folder is one line: `mkdir cli-test` |

### Slide 58 — 4-6. 실습 2 / Exercise 2 — Create a File, Add Content, Check It

| 한국어 | English |
|---|---|
| **4-6. 실습 2 – 파일 만들고 / 내용 넣고 / 확인하기** | **4-6. Exercise 2 — Create a File, Put Content In, Check It** |
| 메모장으로 하던 일을 명령 세 줄로 | What you used to do in Notepad, in three commands |
| `# 1. 빈 파일 만들기` → `New-Item -ItemType File memo.txt` | `# 1. Create an empty file` → `New-Item -ItemType File memo.txt` |
| 출력: `디렉터리: D:\cli-test` / `Mode LastWriteTime Length Name` / `-a---- 2026-08-05 17:27 0 memo.txt` | Output: `Directory: D:\cli-test` / `Mode LastWriteTime Length Name` / `-a---- 2026-08-05 17:27 0 memo.txt` |
| `# 2. 파일에 내용 쓰기` → `Set-Content memo.txt "첫 번째 줄"` | `# 2. Write content to the file` → `Set-Content memo.txt "first line"` |
| `# 3. 파일 내용 보기` → `cat memo.txt` → `첫 번째 줄` | `# 3. Show the file's contents` → `cat memo.txt` → `first line` |
| 탐색기로 하면 (같은 일): 우클릭 > 새로 만들기 > 텍스트 문서, 메모장으로 열어 쓰고 저장 | The same thing in Explorer: right-click > New > Text Document, open it in Notepad, type and save |
| cat 은 파일을 열지 않고 내용만 화면에 뿌리는 명령. 파일이 많을 때 메모장을 하나씩 여는 방식보다 빠름 | `cat` dumps the contents to the screen without opening the file — far quicker than opening files one by one in Notepad |

### Slide 59 — 4-7. Tab 자동 완성과 명령 히스토리 / Tab Completion and Command History

| 한국어 | English |
|---|---|
| **4-7. Tab 자동 완성과 명령 히스토리** | **4-7. Tab Completion and Command History** |
| 입력량을 줄이면 오타가 줄고, 오타가 줄면 실습 중단이 줄어듦 | Type less and you make fewer typos; fewer typos means fewer interruptions |
| 1. cli 까지만 입력 → 2. Tab 한 번 > 자동완성 → 3. ↑ 키 > 직전 명령 재호출 | 1. Type just `cli` → 2. Press Tab once and it completes → 3. Press ↑ to recall the previous command |
| `PS D:\> cd cli` + Tab → `PS D:\> cd cli-test` (나머지가 저절로 채워짐) | `PS D:\> cd cli` + Tab → `PS D:\> cd cli-test` (the rest fills itself in) |
| Tab – 폴더·파일 이름 자동완성 – 앞 몇 글자만 치고 Tab | Tab — completes folder and file names; type the first few characters and press Tab |
| Tab 여러 번 – 후보가 여러 개면 계속 눌러 다음 후보로 이동 | Tab repeatedly — if there are several candidates, keep pressing to cycle through them |
| ↑ 위 방향키 – 방금 친 명령 다시 불러오기 – 오타 났을 때 재입력 불필요 | ↑ — recalls the command you just typed, so a typo does not mean retyping |
| ↓ 아래 방향키 – 히스토리에서 앞으로 이동 | ↓ — moves forward through history |
| Ctrl + C – 명령이 안 끝나고 멈춰 있을 때 강제 중단 | Ctrl + C — force-stops a command that has hung |
| cls – 화면만 정리 – 파일은 유지 | `cls` — tidies the screen only; files are untouched |
| 실습 중단 원인의 대부분은 입력 오류 – Tab 과 위 방향키만으로 대부분 예방 가능 | Most stalled exercises come down to typing errors — Tab and the up arrow prevent nearly all of them |

### Slide 60 — 4-8. 복사·붙여넣기 / Copy and Paste in PowerShell

| 한국어 | English |
|---|---|
| **4-8. 복사·붙여넣기 – PowerShell 의 동작 규칙** | **4-8. Copy and Paste — How PowerShell Behaves** |
| 장문 프롬프트는 직접 입력이 불가하므로, 실습 진행의 전제 조건에 해당 | Long prompts cannot realistically be typed out, so this is a prerequisite for the exercises |
| **PowerShell 에 붙여넣기 (세 방식 중 택일)** | **Pasting into PowerShell (pick one of three)** |
| 마우스 우클릭 – 창 안에서 오른쪽 버튼 – 가장 확실 | Right-click — right button inside the window; the most reliable |
| Ctrl + V – Windows 10 이후 기본 동작 | Ctrl + V — the default since Windows 10 |
| Shift + Insert – 위 두 방식이 안 되는 구형 콘솔용 | Shift + Insert — for older consoles where the two above fail |
| **PowerShell 에서 복사하기** | **Copying out of PowerShell** |
| 드래그 후 Enter – 복사할 텍스트를 선택 후 Enter | Drag then Enter — select the text, then press Enter |
| 드래그 후 우클릭 – 선택 후 오른쪽 버튼 – 동일 결과 | Drag then right-click — same result |
| Ctrl + C – 텍스트를 선택한 상태에서만 복사 | Ctrl + C — copies only while text is selected |
| Ctrl + C 는 선택 상태에 따라 동작이 달라짐 – 가장 혼동이 잦은 지점 | Ctrl + C behaves differently depending on whether anything is selected — the most common source of confusion |
| 텍스트를 선택한 상태 > 복사 수행 · 선택 없는 상태 > 실행 중인 명령 중단 | With text selected it copies; with nothing selected it interrupts the running command |
| 여러 줄을 붙여넣어도 Enter 입력 전에는 실행되지 않음 – 전체가 들어갔는지 확인 후 Enter | Even a multi-line paste does not run until you press Enter — check the whole thing pasted, then press Enter |

### Slide 61 — 4-9. 세션 창 종료 후 복귀 절차 / Getting Back After Closing the Window

| 한국어 | English |
|---|---|
| **4-9. 세션 창 종료 후 복귀 절차** | **4-9. How to Get Back After Closing the Window** |
| 창을 종료해도 생성한 파일은 디스크에 유지됨 – 재실행 후 해당 폴더로 이동하면 복귀 완료 | Closing the window leaves your files on disk — reopen it, move to the folder, and you are back |
| 안심 사항: 창을 닫아도 폴더와 파일은 그대로 유지. 사라지는 대상은 화면에 찍힌 글자뿐 | Reassurance: closing the window keeps every folder and file. The only thing lost is the text printed on screen |
| 1. 창 다시 열기 – 검색창에 pow 입력 > Enter | 1. Reopen the window — type `pow` in the search box and press Enter |
| 2. 작업 폴더로 이동 – `D:` > `cd 폴더이름` (Tab 활용) | 2. Move to your working folder — `D:` then `cd foldername` (use Tab) |
| 3. 위치 확인 – `PS D:\내폴더>` 로 바뀌면 정상 | 3. Check where you are — when it reads `PS D:\yourfolder>` you are set |
| **자주 하는 착각** | **Common misconceptions** |
| ✗ 창을 닫으면 내가 만든 것도 사라짐 → 아님 – 파일은 디스크에 그대로. 탐색기로 열어 보면 있음 | ✗ Closing the window destroys what I made → No — the files are still on disk; open Explorer and there they are |
| ✗ 창을 새로 열면 아까 그 폴더에 있다 → 아님 – 항상 `C:\Users\내이름` 에서 시작. 다시 cd 로 이동 | ✗ A new window opens in the folder I was in → No — it always starts at `C:\Users\yourname`; `cd` back |
| ✗ 명령이 안 먹으면 컴퓨터가 고장난 것 → 아님 – 대부분 폴더 위치가 다르거나 오타. 프롬프트를 먼저 확인 | ✗ If a command does not work the computer is broken → No — it is nearly always the wrong folder or a typo. Check the prompt first |
| 위치가 불확실하면 pwd – 현재 경로부터 확인 | Unsure where you are? `pwd` — start by checking the current path |

### Slide 62 — 4-10. 실습 3 / Exercise 3 — Deleting Files and Folders

| 한국어 | English |
|---|---|
| **4-10. 실습 3 – 파일 삭제 / 폴더 통째로 삭제 + 뒷정리** | **4-10. Exercise 3 — Delete a File, Delete a Whole Folder, Clean Up** |
| 삭제는 되돌릴 수 없음 – 경로 확인 후 Enter | Deletion cannot be undone — check the path before you press Enter |
| `# 1. 파일 하나 삭제` → `Remove-Item memo.txt` | `# 1. Delete a single file` → `Remove-Item memo.txt` |
| `# 2. 확인 – 출력이 없으면 빈 폴더` → `dir` | `# 2. Check — no output means the folder is empty` → `dir` |
| `# 3. 연습 폴더를 통째로 삭제 (-Recurse = 안까지)` → `cd ..` → `Remove-Item -Recurse -Force D:\cli-test` | `# 3. Delete the practice folder entirely (-Recurse means contents too)` → `cd ..` → `Remove-Item -Recurse -Force D:\cli-test` |
| `# 4. 지워졌는지 확인 – False 면 성공` → `Test-Path D:\cli-test` → `False` | `# 4. Confirm it is gone — False means success` → `Test-Path D:\cli-test` → `False` |
| 탐색기로 하면: 파일 선택 > Delete 키 / "이 폴더를 휴지통으로 이동하시겠습니까?" 예(Y) 아니요(N) | In Explorer: select the file and press Delete / "Move this folder to the Recycle Bin?" Yes (Y) No (N) |
| 차이: 탐색기 삭제는 휴지통 경유, Remove-Item 은 휴지통 미경유 즉시 삭제. 실행 전 경로 확인 필수 | The difference: Explorer sends things to the Recycle Bin; `Remove-Item` deletes immediately, bypassing it. Always check the path first |

### Slide 63 — 4-11. PowerShell 과 CMD 비교 / PowerShell vs. CMD

| 하려는 작업 / Task | PowerShell (파란 창 / blue window) | CMD (검은 창 / black window) | 맥 · 리눅스 / macOS · Linux |
|---|---|---|---|
| 파일 목록 보기 / List files | `dir` or `ls` | `dir` (`ls` unsupported) | `ls` |
| 파일 내용 보기 / Show file contents | `cat` | `type` | `cat` |
| 폴더 만들기 / Create a folder | `mkdir` | `md` | `mkdir` |
| 파일 지우기 / Delete a file | `Remove-Item` | `del` | `rm` |
| 폴더 지우기 / Delete a folder | `Remove-Item -Recurse` | `rd /s /q` | `rm -r` |
| 현재 위치 보기 / Show current location | `pwd` | `cd` (typed alone) | `pwd` |
| 화면 지우기 / Clear the screen | `cls` | `cls` | `clear` |

| 한국어 | English |
|---|---|
| CMD – 명령 체계가 PowerShell·리눅스와 각각 다름 | CMD — its command set differs from both PowerShell and Linux |
| PowerShell (이 강의 기준) – 맥·리눅스와 명령이 거의 같아 한 번 익히면 그대로 사용 | PowerShell (what this course uses) — its commands are nearly the same as macOS and Linux, so learning them once carries over |

### Slide 64 — 4-12. 자주 발생하는 오류와 조치 / Common Errors and Fixes

| 화면에 이렇게 나옴 / What you see | 원인 / Cause | 해결 / Fix |
|---|---|---|
| 경로를 찾을 수 없습니다 — "Cannot find path" | 폴더 이름 오타 또는 없음 — Folder name misspelled or missing | `dir` 로 확인 후 Tab 자동완성 — Check with `dir`, then use Tab completion |
| 'ls' 은(는) 내부 명령이 아님 — "'ls' is not recognized" | CMD 창에서 PowerShell 명령 입력 — You typed a PowerShell command in CMD | 검색창에 pow 입력해 다시 열기 — Reopen via `pow` in the search box |
| 스크립트를 실행할 수 없으므로 — "Cannot run scripts" | 실행 정책 차단 (npx 사용 시) — Execution policy is blocking it (when using npx) | `Set-ExecutionPolicy RemoteSigned` |
| 'claude' 용어가 인식되지 않음 — "'claude' is not recognized" | 설치 후 터미널 재실행 안 함 — You did not restart the terminal after installing | 터미널을 닫고 새로 열기 — Close the terminal and open a new one |
| 액세스가 거부되었습니다 — "Access is denied" | 다른 프로그램이 폴더 사용 중 — Another program is using the folder | VS Code / 탐색기 닫고 재시도 — Close VS Code and Explorer, then retry |

### Slide 65 — 체크포인트 / Checkpoint

| 한국어 | English |
|---|---|
| **체크포인트** | **Checkpoint** |
| 1. `D:` 로 드라이브 이동 가능 | 1. I can switch drives with `D:` |
| 2. `mkdir` 로 폴더 생성, `cd` 로 진입 가능 | 2. I can create a folder with `mkdir` and enter it with `cd` |
| 3. `dir` 로 목록, `cat` 으로 파일 내용 확인 가능 | 3. I can list with `dir` and read a file with `cat` |
| 4. `Remove-Item` 으로 파일·폴더 삭제 가능 | 4. I can delete files and folders with `Remove-Item` |
| 5. Tab 자동완성과 위 방향키 사용 가능 | 5. I can use Tab completion and the up arrow |

---

## 5장. Claude Code 설치 / Chapter 5. Installing Claude Code

### Slide 66 — Chapter cover

| 한국어 | English |
|---|---|
| **Claude Code 설치 + 인증 + 비용 설정** | **Installing, Authenticating and Budgeting Claude Code** |
| 설치 > API Key 인증 > 비용 설정 > 슬래시 커맨드 > CLAUDE.md > 권한과 훅 | Install, authenticate with an API key, set up costs, slash commands, CLAUDE.md, permissions and hooks |
| 학습 내용 | What you will learn |
| 1. `claude --version` 실행 | 1. Running `claude --version` |
| 2. API Key 인증 & 첫 대화 | 2. API key authentication and your first conversation |
| 3. 모델·effort 로 비용 설정 | 3. Controlling cost through model and effort |

### Slide 67 — 5-1. Claude Code 개요 / Claude Code Overview

| 한국어 | English |
|---|---|
| **5-1. Claude Code 개요** | **5-1. Claude Code Overview** |
| 터미널 기반 AI 코딩 에이전트, 왜 대세인가 | A terminal-based AI coding agent — why it has taken over |
| 1. Anthropic이 만든 터미널 기반 AI 코딩 에이전트 | 1. A terminal-based AI coding agent built by Anthropic |
| 2. 자연어로 지시 > 파일 생성, 수정, 실행까지 자율 수행 | 2. Instruct in natural language; it creates, edits and runs files on its own |
| 3. 기본 도구 5종 – Read / Write / Edit / Bash / Glob, Grep | 3. Five built-in tools — Read / Write / Edit / Bash / Glob, Grep |
| 4. CLAUDE.md – 프로젝트 메모리, 매 세션 자동으로 읽힘 | 4. CLAUDE.md — project memory, read automatically at the start of every session |
| **Claude Code 핵심 강점 6종** | **Six core strengths of Claude Code** |
| Skills – 디자인, 문서, 워크플로우를 재사용 가능한 스킬로 묶기 | Skills — bundle design, documentation and workflows into reusable skills |
| Plugins – MCP 서버 연결로 외부 도구 (DB, API) 직접 연동 | Plugins — connect MCP servers to integrate external tools (databases, APIs) directly |
| Subagent – 작업 분기, 병렬 실행, 컨텍스트 격리 | Subagents — branch work, run in parallel, isolate context |
| Hooks – 작업 전/후 자동 실행, 절대규칙 강제 | Hooks — run automatically before and after work, and enforce hard rules |
| CLAUDE.md – 프로젝트 컨텍스트 영속화, 시니어 협업 가능 | CLAUDE.md — persists project context, enabling senior-level collaboration |
| 터미널 – IDE 종속 없음, Mac/Windows/Linux 어디서든 | Terminal — no IDE dependency; works on Mac, Windows and Linux alike |

### Slide 68 — 5-1-1. 하네스와 모델의 구분 / Harness vs. Model

| 한국어 | English |
|---|---|
| **5-1-1. Claude Code(하네스) 와 Claude(모델) 의 구분** | **5-1-1. Telling Claude Code (the Harness) Apart from Claude (the Model)** |
| 둘을 구분해야 /model 이 무엇을 바꾸는지, 비용이 어디서 나오는지 파악 가능 | Keep the two apart and you can see what `/model` actually changes and where the cost comes from |
| **모델 (Model) – 판단 담당** | **The model — does the thinking** |
| Opus 5 / Sonnet 5 / Haiku 4.5 / Fable 5 | Opus 5 / Sonnet 5 / Haiku 4.5 / Fable 5 |
| 문장과 코드를 생성 | Generates prose and code |
| 파일 직접 읽기 불가 | Cannot read files itself |
| 명령 직접 실행 불가 | Cannot run commands itself |
| 토큰 사용량만큼 요금 발생 | You are billed for the tokens it uses |
| /model sonnet 입력 시 모델 교체 | Typing `/model sonnet` swaps the model |
| **하네스 (Harness) – 실행 담당** | **The harness — does the doing** |
| Claude Code (터미널 프로그램) | Claude Code (the terminal program) |
| 모델에 도구를 연결 (Read/Write/Bash) | Connects tools to the model (Read/Write/Bash) |
| 파일을 읽어 모델에 전달 | Reads files and passes them to the model |
| 모델의 지시대로 파일을 실제로 기록 | Actually writes the files the model asks for |
| 프로그램 자체는 무료 – 요금 없음 | The program itself is free — no charge |
| 모델을 바꿔도 Claude Code 는 그대로 | Change the model and Claude Code stays the same |
| **같은 모델을 다른 도구에 연결한 조합** | **Combinations of the same model with different tools** |
| Claude Code + Sonnet – 본 과정 | Claude Code + Sonnet — what this course uses |
| Cursor + Sonnet – 같은 모델, 다른 하네스 | Cursor + Sonnet — same model, different harness |
| Claude Code + Opus – 같은 하네스, 다른 모델 | Claude Code + Opus — same harness, different model |
| API 직접 호출 + Sonnet – 하네스 없이 모델만 | Calling the API directly + Sonnet — the model with no harness |
| 정리: 요금은 모델이 읽고 쓴 토큰에서만 발생 – 모델을 Sonnet, effort 를 low 로 낮추면 비용 감소 | In short: you are billed only for the tokens the model reads and writes — drop to Sonnet and set effort to low and the cost falls |

### Slide 69 — 5-1-2. 코딩 에이전트 세 가지 비교 / Three Coding Agents Compared

| 항목 / Aspect | Claude Code | Codex CLI | Gemini CLI |
|---|---|---|---|
| 만든 곳 / Maker | Anthropic | OpenAI | Google |
| 쓰는 모델 / Models used | Claude Opus · Sonnet | GPT 계열 / the GPT family | Gemini 계열 / the Gemini family |
| 업무 사용률 / Share of professional use | 39% | 14% | 9% |
| 강점 / Strength | 긴 작업을 끝까지 밀고 감 — Pushes long tasks through to the end | ChatGPT 구독에 포함 — Included with a ChatGPT subscription | 무료 구간이 넓음 — A generous free tier |

| 한국어 | English |
|---|---|
| **5-1-2. 코딩 에이전트 세 가지 비교** | **5-1-2. Three Coding Agents Compared** |
| 터미널에서 도는 같은 형태의 도구 셋 – Anthropic · OpenAI · Google 이 각각 출시 | Three tools of the same shape, all running in the terminal — one each from Anthropic, OpenAI and Google |
| 셋의 공통점: 셋 다 터미널에서 문장으로 지시 – 코드를 보지 않아도 됨. 본 과정은 사용률이 가장 높은 Claude Code 로 진행 | What they share: all three take sentences in the terminal, so you never have to look at code. This course uses Claude Code, the most widely used of them |

### Slide 70 — 5-1-3. 편집기 계열과의 차이 / How It Differs from Editor-Based Tools

| 항목 / Aspect | Claude Code | Cursor | GitHub Copilot |
|---|---|---|---|
| 형태 / Form | 터미널에서 도는 에이전트 — An agent running in the terminal | AI 가 들어간 코드 편집기 — A code editor with AI inside | 기존 편집기에 붙이는 확장 — An extension bolted onto your editor |
| 사람이 하는 일 / What the human does | 문장으로 무엇을 원하는지 — States what they want, in sentences | 코드를 보며 고침 — Reads the code and fixes it | 타이핑 뒤를 이어 써 줌 — It continues what you type |
| 업무 사용률 / Share of professional use | 39% | 12% | 21% |
| 코드를 못 봐도 / If you can't read code | 가능 — Workable | 어려움 — Difficult | 효과 적음 — Little benefit |

| 한국어 | English |
|---|---|
| **5-1-3. 편집기 계열과의 차이 – Cursor · Copilot** | **5-1-3. How It Differs from Editor-Based Tools — Cursor and Copilot** |
| Cursor 와 GitHub Copilot 은 코드를 보면서 쓰는 도구 – 출발점이 다름 | Cursor and GitHub Copilot are tools you use while looking at code — a different starting point |
| 본 과정이 Claude Code 를 쓰는 이유: 나머지 둘은 코드를 볼 줄 아는 사람을 전제 – 코드를 보지 않는 수강생에게 결정적 차이 | Why this course uses Claude Code: the other two assume someone who can read code — a decisive difference for learners who will not be reading it |

### Slide 71 — 5-1-4. 첫 지시 한 줄로 만든 결과 / What One Line of Instruction Produced

| 한국어 | English |
|---|---|
| **5-1-4. 첫 지시 한 줄로 만든 결과** | **5-1-4. What a Single Opening Instruction Produced** |
| 문장 세 줄로 만들고 고치고 확인까지 – 코드를 한 번도 열지 않음 | Built, revised and verified in three sentences — without once opening the code |
| `> 브라우저에서 바로 돌아가는 두더지 잡기 게임 만들어 줘` | `> Make me a whack-a-mole game that runs straight in the browser` |
| `● Write index.html` / `✓ 한 파일 완성 – 더블클릭하면 실행` | `● Write index.html` / `✓ One file, done — double-click to run` |
| `◆ 3×3 칸에 두더지가 무작위로 나오고 점수와 남은 시간이 표시됨` | `◆ Moles pop up at random in a 3×3 grid, with score and time remaining on screen` |
| `> 난이도 올려 줘. 시간 지날수록 빨라지게` | `> Make it harder — speed it up as time passes` |
| `● Edit index.html` / `✓ 적용 완료 – 두더지가 나올수록 빨라짐` | `● Edit index.html` / `✓ Applied — the moles come faster as the game goes on` |
| `> 브라우저로 열어서 확인해 줘` / `✓ 30초 동안 점수 집계 – 정상 동작` | `> Open it in the browser and check it` / `✓ Scores tally over 30 seconds — works correctly` |
| 화면에서 볼 것: 내가 친 줄은 왼쪽 끝에서 시작 · ● 는 도구 실행 · ✓ 는 결과 · 고칠 때도 코드가 아니라 문장으로 지시 | What to notice on screen: your own lines start at the far left; ● marks a tool running; ✓ marks a result; and even the fixes are given as sentences, not code |

### Slide 72 — 5-2. 사전 설치 필수 프로그램 / Prerequisites to Install

| 프로그램 / Program | 버전 / Version | 용도 / Why | 링크 / Link |
|---|---|---|---|
| Node.js | v24 이상 / v24+ | `npx claude-api-setup` 실행에 필요 — Needed to run `npx claude-api-setup` | https://nodejs.org |
| Git | 2.40 이상 / 2.40+ | 버전 관리, GitHub 연동, Claude Code와 협업 — Version control, GitHub integration, working with Claude Code | https://git-scm.com |
| Python | 3.11 이상 / 3.11+ | FastAPI 백엔드 개발 (10장에서 사용) — FastAPI backend development (used in Chapter 10) | https://python.org |
| VS Code | 최신 / latest | 코드 파일 확인, 편집용 에디터 (Claude Code 옆에서 사용) — An editor for viewing and editing files, used alongside Claude Code | https://code.visualstudio.com |
| Claude Code | 2.1 이상 / 2.1+ | 본 과정의 핵심 도구 – 다음 슬라이드에서 설치 — The core tool of this course; installed on the next slide | https://claude.ai/code |

| 한국어 | English |
|---|---|
| **5-2. 사전 설치 필수 프로그램** | **5-2. Prerequisites You Must Install** |
| Claude Code 실습 전 아래 5가지 모두 설치 필요 | All five of these must be installed before the Claude Code exercises |
### Slide 73 — 5-2-1. Node.js 설치 / Installing Node.js

| 한국어 | English |
|---|---|
| **5-2-1. Node.js 설치** | **5-2-1. Installing Node.js** |
| nodejs.org 에서 LTS 판 – Windows Installer (.msi) – 구성 요소는 기본값 그대로 | Get the LTS build from nodejs.org — the Windows Installer (.msi) — and leave every component at its default |
| LTS 와 Current – LTS 는 장기 지원 안정판. Current 최신 기능판은 쓰지 않음 | LTS vs. Current — LTS is the long-term support stable build. Do not use Current, the bleeding-edge build |
| 함께 깔리는 항목 – npm 과 PATH 는 기본 포함 – 따로 고를 필요 없음 | What comes with it — npm and the PATH entry are included by default; nothing extra to select |
| 설치 화면 – 다음 · 다음 · 설치 · 마침. 구성 요소는 바꾸지 않음 | The installer — Next, Next, Install, Finish. Change no components |
| 확인 – 새 터미널에서 `node -v` · `npm -v` | Verify — in a **new** terminal, run `node -v` and `npm -v` |
| LTS 판을 고르고 Windows Installer (.msi) 클릭 | Pick the LTS build and click Windows Installer (.msi) |
| 확인은 새 터미널에서 – 설치 전에 열어 둔 창은 옛 PATH 를 그대로 지녀 값이 나오지 않음 | Verify in a new terminal — a window opened before the install still holds the old PATH and will print nothing |

### Slide 74 — 5-2-2. Git 설치 / Installing Git

| 한국어 | English |
|---|---|
| **5-2-2. Git 설치** | **5-2-2. Installing Git** |
| git-scm.com 에서 Windows 판 – 선택 화면 약 10회 전부 기본값 그대로 다음 | Get the Windows build from git-scm.com — roughly ten option screens, all left at their defaults, Next each time |
| Git 이 하는 일 – 수정 전 상태를 저장하고, 오류가 나면 그 시점으로 되돌림 | What Git does — saves the state before a change so you can roll back to it when something breaks |
| 쓰는 쪽 – 사람이 아니라 Claude Code. 이 과정에서 직접 칠 일은 없음 | Who uses it — Claude Code, not you. You will never type a Git command in this course |
| 설치 화면 – 선택 화면이 약 10회. 전부 기본값 그대로 다음 | The installer — about ten option screens; leave all defaults and press Next |
| 확인 – 새 터미널에서 `git --version` | Verify — run `git --version` in a new terminal |
| Click here to download – 설치 파일 내려받기 | "Click here to download" — get the installer |
| 선택 항목을 바꾸지 말 것 – 기본값이 아닌 조합은 뒤에서 원인을 찾기 어려운 오류로 돌아옴 | Do not change the options — a non-default combination comes back later as an error that is very hard to trace |

### Slide 75 — 5-2-3. Python 설치 / Installing Python

| 한국어 | English |
|---|---|
| **5-2-3. Python 설치** | **5-2-3. Installing Python** |
| python.org – 첫 화면 버튼이 바뀌어 설치 파일 목록으로 한 번 더 들어가야 함 | python.org — the front-page button has changed, so you need one more click through to the list of installers |
| 1. python.org 첫 화면 – 목록으로 이동 | 1. python.org front page — go to the list |
| 2. 설치 파일 목록 – Windows installer (64-bit) | 2. The installer list — Windows installer (64-bit) |
| 3. 설치 관리자 – PATH 체크 후 Install Now | 3. The installer — tick the PATH box, then Install Now |
| 체크 한 칸이 갈림길: Add python.exe to PATH – 이 체크를 빠뜨리는 것이 설치 실패 최다 원인. 빠뜨렸으면 지우고 다시 설치하는 편이 빠름 | One checkbox decides everything: **Add python.exe to PATH**. Missing it is the single most common cause of a failed install — if you missed it, uninstalling and reinstalling is faster than fixing it |

### Slide 76 — 5-2-4. 설치 실습 (Windows PowerShell) / Install Walkthrough — Windows PowerShell

| 한국어 | English |
|---|---|
| **5-2-4. 설치 실습 – Windows PowerShell** | **5-2-4. Install Walkthrough — Windows PowerShell** |
| irm 네이티브 설치 > 버전 확인 > API Key 영구 등록 > claude 실행 | Native install via `irm`, check the version, register the API key permanently, run `claude` |
| `# 사전 준비 – Node.js 확인` → `node --version` → `v24.15.0` | `# Prerequisite — check Node.js` → `node --version` → `v24.15.0` |
| `# 1. 실행 정책 설정 (npx 사용에 필요)` → `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` → `[Y] 예(Y) [A] 모두 예(A) [N] 아니요(N): Y` | `# 1. Set the execution policy (needed for npx)` → `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` → `[Y] Yes [A] Yes to All [N] No: Y` |
| `# 2. Claude Code 네이티브 설치` → `irm https://claude.ai/install.ps1 \| iex` → `Claude Code installed successfully` | `# 2. Native install of Claude Code` → `irm https://claude.ai/install.ps1 \| iex` → `Claude Code installed successfully` |
| `# 3. 버전 확인` → `claude --version` → `Claude Code 2.1.222` | `# 3. Check the version` → `claude --version` → `Claude Code 2.1.222` |
| `# 4. API Key 등록 (강사 제공 Key 입력)` → `npx claude-api-setup 배포키` → `API Key configured successfully` | `# 4. Register the API key (enter the key the instructor gives you)` → `npx claude-api-setup <distributed-key>` → `API Key configured successfully` |
| `claude` → `Claude Code 시작됨` | `claude` → `Claude Code started` |

### Slide 77 — 5-2-5. 설치 실습 (Windows CMD) / Install Walkthrough — Windows CMD

| 한국어 | English |
|---|---|
| **5-2-5. 설치 실습 – Windows CMD (명령 프롬프트)** | **5-2-5. Install Walkthrough — Windows CMD (Command Prompt)** |
| curl 네이티브 설치 > 버전 확인 > API Key 영구 등록 > claude 실행 | Native install via `curl`, check the version, register the API key permanently, run `claude` |
| `# 사전 준비 – Node.js 확인` → `node --version` → `v24.15.0` | `# Prerequisite — check Node.js` → `node --version` → `v24.15.0` |
| `# 1. Claude Code 네이티브 설치` → `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd` | `# 1. Native install of Claude Code` → `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd` |
| `# 2. 버전 확인` → `claude --version` → `Claude Code 2.1.222` | `# 2. Check the version` → `claude --version` → `Claude Code 2.1.222` |
| `# 3. API Key 등록 (강사 제공 Key 입력)` → `npx claude-api-setup 배포키` | `# 3. Register the API key (enter the key the instructor gives you)` → `npx claude-api-setup <distributed-key>` |
| `claude` → `Claude Code 시작됨` | `claude` → `Claude Code started` |

### Slide 78 — 5-2-6. 설치 실습 (Mac Terminal, zsh) / Install Walkthrough — Mac Terminal (zsh)

| 한국어 | English |
|---|---|
| **5-2-6. 설치 실습 – Mac Terminal (zsh)** | **5-2-6. Install Walkthrough — Mac Terminal (zsh)** |
| curl 네이티브 설치 > 버전 확인 > API Key 영구 등록 > claude 실행 | Native install via `curl`, check the version, register the API key permanently, run `claude` |
| `# 사전 준비 – Node.js 확인` → `node --version` → `v24.15.0` | `# Prerequisite — check Node.js` → `node --version` → `v24.15.0` |
| `# 1. Claude Code 네이티브 설치` → `curl -fsSL https://claude.ai/install.sh \| bash` → `Claude Code installed successfully` | `# 1. Native install of Claude Code` → `curl -fsSL https://claude.ai/install.sh \| bash` → `Claude Code installed successfully` |
| `# 2. 버전 확인` → `claude --version` → `Claude Code 2.1.222` | `# 2. Check the version` → `claude --version` → `Claude Code 2.1.222` |
| `# 3. API Key 등록 (강사 제공 Key 입력)` → `npx claude-api-setup 배포키` → `API Key configured successfully` | `# 3. Register the API key (enter the key the instructor gives you)` → `npx claude-api-setup <distributed-key>` → `API Key configured successfully` |
| `claude` → `Claude Code 시작됨` | `claude` → `Claude Code started` |

### Slide 79 — 5-2-7. claude 가 인식되지 않을 때 / When `claude` Is Not Recognized

| 한국어 | English |
|---|---|
| **5-2-7. claude 가 인식되지 않을 때 – 환경 변수 열기** | **5-2-7. When `claude` Is Not Recognized — Opening Environment Variables** |
| 설치가 실패한 것이 아니라 창이 설치 위치를 모르는 것 – 화면 그대로 따라 등록 | The install did not fail; the window simply does not know where it went. Follow the screens and register it |
| 1. 시작 메뉴에 "환경 변수" 입력 – 시스템 환경 변수 편집 | 1. Type "environment variables" into the Start menu — Edit the system environment variables |
| 2. 고급 탭 – 환경 변수(N) 버튼 | 2. The Advanced tab — the "Environment Variables" button |
| 증상: `claude --version` 에서 「'claude' 용어가 인식되지 않습니다」 – 설치는 끝났으나 창이 실행 파일의 위치를 모르는 상태 | Symptom: `claude --version` reports "'claude' is not recognized" — the install finished, but the window does not know where the executable is |

### Slide 80 — 5-2-8. PATH 에 설치 위치 등록 / Adding the Install Location to PATH

| 한국어 | English |
|---|---|
| **5-2-8. PATH 에 설치 위치 등록하고 새 창에서 확인** | **5-2-8. Add the Install Location to PATH and Verify in a New Window** |
| 사용자 변수의 Path 에 한 줄 추가 – 시스템 변수가 아님 | Add one line to Path under **User variables** — not System variables |
| 3. 사용자 변수의 Path 선택 – 편집(E) | 3. Select Path under User variables — Edit |
| 4. 새로 만들기 – 값 붙여넣기 – 확인 | 4. New — paste the value — OK |
| 넣을 값과 그 뒤: `%USERPROFILE%\.local\bin` · 확인을 세 번 눌러 닫고, 창을 닫은 뒤 새 터미널에서 `claude --version` 재확인 | The value, and what follows: `%USERPROFILE%\.local\bin`. Click OK three times to close out, shut the window, then re-run `claude --version` in a new terminal |

### Slide 81 — 5-2-9. CCKit / A Bulk Installer for the Prerequisites

| 한국어 | English |
|---|---|
| **5-2-9. CCKit – 선행 프로그램 일괄 설치 도구** | **5-2-9. CCKit — a Bulk Installer for the Prerequisites** |
| Node.js · Git · Python · Claude Code 를 한 번에 설치하고 세션까지 관리하는 도구 | A tool that installs Node.js, Git, Python and Claude Code in one go, and manages sessions too |
| 무엇을 대신해 주나 – 5-2-1 부터 5-2-6 까지의 개별 설치를 화면 하나로 끝냄 | What it replaces — everything from 5-2-1 to 5-2-6, done from a single screen |
| 받는 곳 – github.com/hull-kr/Claude-Code-Kit 의 Releases – 최신판 – Assets | Where to get it — github.com/hull-kr/Claude-Code-Kit, under Releases, latest version, Assets |
| 받을 파일 두 가지 – CCKitSetup.exe 를 먼저 시도. 막히면 CCKitSetup.zip | Two files to choose from — try CCKitSetup.exe first; if it is blocked, take CCKitSetup.zip |
| GitHub 릴리스 – Assets 의 CCKitSetup.exe 내려받기 | GitHub release — download CCKitSetup.exe from Assets |
| 이미 개별 설치를 끝냈으면 – 건너뛰어도 됨. 새 PC 나 실습실 PC 를 한꺼번에 맞출 때 쓰는 도구 | If you already installed everything individually, skip this. It is for setting up a new machine or a whole lab at once |

### Slide 82 — 5-2-10. CCKit — 브라우저와 Windows 차단 해제 / Getting Past Browser and Windows Blocks

| 한국어 | English |
|---|---|
| **5-2-10. CCKit – 브라우저와 Windows 의 차단 해제** | **5-2-10. CCKit — Clearing the Browser and Windows Blocks** |
| 배포 서명이 없는 파일이라 브라우저와 Windows 가 한 번씩 막음 – 정상 절차 | The file is unsigned, so the browser and Windows each block it once. This is expected |
| 브라우저 차단 · SmartScreen | Browser block · SmartScreen |
| 막히는 이유: 유료 코드 서명을 하지 않아 생기는 경고. 악성 판정이 아님 – exe 가 막히면 zip 을 받아 압축 해제 | Why it is blocked: a warning triggered by the absence of paid code signing, not a malware verdict. If the .exe is blocked, download the .zip and extract it |

### Slide 83 — 5-2-11. CCKit 설치 / Installing CCKit

| 한국어 | English |
|---|---|
| **5-2-11. CCKit 설치 – 관리자 권한 없이, 선행 프로그램까지 한 번에** | **5-2-11. Installing CCKit — No Admin Rights Needed, Prerequisites Included** |
| 설치 위치는 `%LOCALAPPDATA%\CCKit` – 사용자 계정 권한으로 설치 | It installs to `%LOCALAPPDATA%\CCKit`, under your own user account's permissions |
| 설치 시작 · 선행 프로그램 이 화면에서 함께 설치 | Start the install · The prerequisites are installed from this same screen |
| 네 가지를 한 번에 설치 · 이미 설치된 항목은 목록에 나오지 않음 · winget 이 받는 동안 관리자 권한 승인 창이 뜰 수 있음 | All four are installed together; anything already present is left off the list; an admin-approval dialog may appear while winget downloads |

### Slide 84 — 5-2-12. CCKit 컨트롤 패널 / The CCKit Control Panel

| 한국어 | English |
|---|---|
| **5-2-12. CCKit 컨트롤 패널 – 세션 목록과 새 세션** | **5-2-12. The CCKit Control Panel — Session List and New Sessions** |
| 작업 폴더별 Claude Code 세션을 목록으로 관리 – 열림과 닫힘 상태가 한눈에 보임 | Manages Claude Code sessions per working folder as a list — open and closed states visible at a glance |
| 세션 목록 – 작업 폴더마다 한 줄. 열림과 닫힘이 색으로 구분됨 | Session list — one row per working folder, colour-coded open or closed |
| 열기 버튼 – `claude --resume` 과 같은 동작. 그 폴더에서 이어서 시작 | Open button — the same as `claude --resume`; picks up where you left off in that folder |
| 새 세션 버튼 – 폴더만 고르면 터미널이 열리고 claude 가 실행됨 | New Session button — pick a folder and a terminal opens with `claude` already running |
| 그룹 – 프로젝트별로 묶어 두면 실습 폴더를 찾기 쉬움 | Groups — group by project and your practice folders are easy to find |
| 명령 대신 고르는 방식 – 긴 옵션을 외우지 않아도 목록에서 골라 같은 일을 시킬 수 있음 | Choosing instead of typing — you get the same result from a list without memorizing long options |

### Slide 85 — 5-2-13. ccd 단축 명령 / The `ccd` Shortcut

| 한국어 | English |
|---|---|
| **5-2-13. ccd 단축 명령 – 권한 확인 없이 실행** | **5-2-13. The `ccd` Shortcut — Running Without Permission Prompts** |
| 긴 옵션을 매번 치지 않아도 되지만 승인 절차를 건너뛰므로 어디서 쓸지 가려야 함 | It saves you typing a long option every time, but it skips the approval step, so be selective about where you use it |
| ccd 가 하는 일 – `claude --dangerously-skip-permissions` 를 대신 쳐 줌 | What `ccd` does — types `claude --dangerously-skip-permissions` for you |
| 생략되는 절차 – 파일 수정과 명령 실행을 묻지 않고 바로 진행 | What gets skipped — it edits files and runs commands without asking |
| 어디서 쓰나 – 실습 폴더 안에서만. 회사 자료 폴더에서는 claude 로 실행 | Where to use it — inside practice folders only. In a folder holding company material, run plain `claude` |
| 트레이 메뉴 – 이어서 열기로 최근 세션을 그대로 재개 | Tray menu — "Resume" reopens the most recent session as it was |
| 가려서 쓸 것 – 승인 절차를 남겨야 하는 폴더에서는 ccd 대신 claude 로 실행할 것 | Be selective — where the approval step matters, run `claude`, not `ccd` |

### Slide 86 — 5-3. 인증 방식 / Authentication — Registering an API Key

| 한국어 | English |
|---|---|
| **5-3. 인증 방식 – API Key 등록** | **5-3. Authentication — Registering an API Key** |
| Claude Code가 Anthropic 서버에 접속하기 위한 인증 | The credential Claude Code uses to reach Anthropic's servers |
| 1. API Key 정의 – 강사가 제공하는 배포키, Claude AI 서버 접속 허가증 | 1. What an API key is — the distributed key your instructor provides; a permit to reach the Claude servers |
| 2. 본 과정 등록 방법 – `npx claude-api-setup 배포키` 한 줄 | 2. How to register it in this course — one line: `npx claude-api-setup <distributed-key>` |
| 3. OAuth 방식 – 브라우저에서 claude.ai 계정으로 로그인 (개인 유료 계정 사용 시) | 3. The OAuth route — sign in with your claude.ai account in a browser (if you are using your own paid account) |
| 4. 토큰 비용 – API 사용량만큼 과금됨, 본 과정은 강사 제공 배포키 사용 (수강생 무료) | 4. Token cost — billed by API usage. This course uses the instructor's distributed key, so it is free for students |
| 5. 강의 종료 후 – `npx claude-api-setup restore` 로 키 삭제 | 5. After the course — remove the key with `npx claude-api-setup restore` |

### Slide 87 — 5-3-1. 비용 설정 / How Charges Arise, and How to Cut Them

| 한국어 | English |
|---|---|
| **5-3-1. 비용 설정 – 요금 발생 구조** | **5-3-1. Managing Cost — Where the Charges Come From** |
| 요금은 토큰에서만 발생 – 무엇이 토큰을 늘리는지 알면 설정으로 줄일 수 있음 | You are charged for tokens and nothing else — know what inflates them and you can cut the bill through settings |
| **요금이 정해지는 방식** | **How the charge is determined** |
| 입력 토큰 – 내가 친 글 + 읽힌 파일 + CLAUDE.md | Input tokens — what you typed, plus the files read, plus CLAUDE.md |
| 출력 토큰 – Claude 가 써 낸 글과 코드. 입력보다 단가가 높음 | Output tokens — the prose and code Claude writes. Priced higher than input |
| 컨텍스트 재전송 – 대화가 길어지면 매 요청마다 그때까지의 전부를 다시 보냄 | Context resent — once the conversation is long, every request resends everything so far |
| 같은 질문도 대화 앞부분이 길수록 요금이 커짐 | The same question costs more the longer the preceding conversation |
| **줄이는 방법** | **How to reduce it** |
| 모델 – `/model` – Opus 는 Sonnet 보다 비쌈. 실습은 Sonnet 으로 충분 | Model — `/model`. Opus costs more than Sonnet; Sonnet is plenty for the exercises |
| 생각 깊이 – effort – `/model` 화면에서 low 로. 높일수록 출력 토큰이 늘어남 | Thinking depth — effort. Set it to low on the `/model` screen; higher settings produce more output tokens |
| 대화 비우기 – `/clear` – 작업이 끝나면 비우기. 앞 내용이 계속 따라다니지 않게 | Clear the conversation — `/clear` when a task is done, so earlier content stops trailing along |
| 요약하기 – `/compact` – 대화가 길어졌지만 이어가야 할 때. 앞부분을 줄여서 들고 감 | Compact it — `/compact` when the conversation is long but must continue; it carries a shortened version of the earlier part |
| MCP 도구 끄기 – 켜 두기만 해도 설명문이 매 요청에 실림. 안 쓰면 끌 것 | Turn off MCP tools — merely leaving them on loads their descriptions into every request. Switch off what you do not use |
| 확인은 `/cost` 와 `/context` | Check with `/cost` and `/context` |
| 본 과정은 강사 배포키라 수강생 부담 없음 – 자기 계정으로 옮긴 뒤에는 이 다섯 가지가 그대로 요금 차이 | This course runs on the instructor's key, so students pay nothing. Once you move to your own account, these five items are the difference in your bill |

### Slide 88 — 5-3-2. 모델별 단가 / Price per Model, per Million Tokens

| 모델 / Model | 입력 / Input per MTok | 출력 / Output per MTok | 캐시 읽기 / Cache read | 비고 / Note |
|---|---|---|---|---|
| Opus 5 | $5 | $25 | $0.50 | 가장 비쌈 · 어려운 판단 — Most expensive; for hard judgment calls |
| Sonnet 5 | $2 | $10 | $0.20 | 본 과정 기본값 — The default for this course |
| Haiku 4.5 | $1 | $5 | $0.10 | 가장 쌈 · 단순 작업 — Cheapest; simple work |
| Fable 5.1 | $10 | $50 | $0.25 | 글쓰기 특화 — Specialized for writing |

| 한국어 | English |
|---|---|
| **5-3-2. 모델별 단가 – 100만 토큰 기준** | **5-3-2. Price per Model — per Million Tokens** |
| MTok = 100만 토큰. 입력과 출력에 각각 단가가 붙고 출력이 다섯 배 | MTok = one million tokens. Input and output are priced separately, and output is five times the input rate |
| 출력이 다섯 배 – 길게 답하게 두면 요금이 빨리 오름. 필요한 만큼만 시킬 것 | Output is 5× — let it answer at length and the bill climbs fast. Ask for only what you need |
| 캐시 읽기는 10분의 1 – 같은 자료를 다시 보낼 때 값이 크게 내려감. Claude Code 가 자동으로 사용 | Cache reads cost a tenth — resending the same material is far cheaper, and Claude Code uses caching automatically |
| Sonnet 이면 충분 – 실습 난이도에서 Opus 와 결과 차이가 크지 않음 | Sonnet is enough — at this level of exercise, Opus does not produce noticeably better results |
| 같은 일을 시켰을 때 – 입력 5만 · 출력 1만 토큰 기준: Opus 5 $0.50 · Sonnet 5 $0.20 · Haiku 4.5 $0.10 | For the same task, at 50,000 input and 10,000 output tokens: Opus 5 $0.50 · Sonnet 5 $0.20 · Haiku 4.5 $0.10 |
| 구독은 별도 – Pro · Max 구독은 정액. 위 표는 API 종량제 기준 | Subscriptions are separate — Pro and Max are flat-rate. The table above is pay-as-you-go API pricing |
| 출처와 시점 – Anthropic 공식 요금표 · 2026-09-07 확인 – 단가는 바뀌므로 강의 때 platform.claude.com 에서 다시 볼 것 | Source and date — Anthropic's official price list, checked 2026-09-07. Prices change, so check platform.claude.com again on the day |

### Slide 89 — 5-4. 기본 도구 5종 / The Five Built-in Tools

| 한국어 | English |
|---|---|
| **5-4. 기본 도구 5종** | **5-4. The Five Built-in Tools** |
| Claude Code가 사용하는 도구들 | The tools Claude Code works with |
| 1. Read – 파일 내용 읽기 (코드 분석, 내용 확인) | 1. Read — read a file's contents (analyzing code, checking content) |
| 2. Write – 새 파일 생성 (코드, 설정 파일 생성) | 2. Write — create new files (code, configuration) |
| 3. Edit – 기존 파일 수정 (코드 일부 변경) | 3. Edit — modify an existing file (changing part of the code) |
| 4. Bash – 터미널 명령 실행 (npm install, pip install 등) | 4. Bash — run terminal commands (`npm install`, `pip install` and so on) |
| 5. Glob, Grep – 파일 검색 (특정 패턴 파일 찾기) | 5. Glob, Grep — search files (finding files matching a pattern) |

### Slide 90 — 5-5. 슬래시 커맨드 / Slash Commands

| 커맨드 / Command | 기능 / What it does | 사용 시점 / When to use it |
|---|---|---|
| `/model` | 모델 + effort 를 함께 변경 — Change model and effort together | 세션 시작 직후 – Sonnet + low — Right after starting a session: Sonnet + low |
| `/clear` | 대화 기록을 비움 — Clear the conversation history | 작업 단위가 바뀔 때 (토큰 절약) — When you switch tasks, to save tokens |
| `/compact` | 대화를 요약해 컨텍스트 확보 — Summarize the conversation to free up context | 대화가 길어져 느려질 때 — When it has grown long and slow |
| `/context` | 지금 컨텍스트를 얼마나 썼는지 표시 — Show how much context is in use | 응답이 느려졌다고 느낄 때 — When responses start feeling slow |
| `/usage` | 사용량과 남은 한도 확인 (`/cost` `/stats` 는 별칭) — Check usage and remaining quota (`/cost` and `/stats` are aliases) | 한도가 궁금할 때 — When you want to know your quota |
| `/init` | CLAUDE.md 자동 생성 — Generate CLAUDE.md automatically | 프로젝트를 처음 열었을 때 — The first time you open a project |
| `/config` | 설정을 영구 저장 (language 등) — Save settings permanently (language and so on) | 한국어 설정을 고정할 때 — When pinning the Korean language setting |
| `/resume` | 이전 대화 목록에서 골라 이어가기 — Pick an earlier conversation from a list and continue it | 세션이 끊겼을 때 — When a session was cut off |

| 한국어 | English |
|---|---|
| **5-5. 슬래시 커맨드** | **5-5. Slash Commands** |
| 대화 중 `/`를 입력하면 사용 가능한 명령어 표시 | Type `/` mid-conversation to see the available commands |
| `/` 입력 시 전체 목록 표시, 타이핑으로 필터링 · 자주 쓰는 것: `/model` `/clear` `/compact` `/context` | `/` shows the full list and typing filters it. The ones you will use most: `/model`, `/clear`, `/compact`, `/context` |

### Slide 91 — 5-5-1. 연습 폴더 생성 & claude 실행 / Create a Practice Folder and Run Claude

| 한국어 | English |
|---|---|
| **5-5-1. 연습 폴더 생성 & claude 실행** | **5-5-1. Creating a Practice Folder and Running Claude** |
| D 드라이브로 이동 > claude-test 폴더 생성 > claude 실행 | Switch to the D drive, create a `claude-test` folder, run `claude` |
| `# 1. D 드라이브로 이동` → `D:` | `# 1. Move to the D drive` → `D:` |
| `# 2. claude-test 폴더 생성 & 이동` → `mkdir claude-test` → `cd claude-test` | `# 2. Create the claude-test folder and enter it` → `mkdir claude-test` → `cd claude-test` |
| `# 3. Claude Code 실행` → `claude` → `Claude Code v2.1.222 / Sonnet 5, effort low / D:\claude-test` | `# 3. Run Claude Code` → `claude` → `Claude Code v2.1.222 / Sonnet 5, effort low / D:\claude-test` |

### Slide 92 — 5-5-2. 두 화면 구분 / Telling the Two Screens Apart

| 한국어 | English |
|---|---|
| **5-5-2. 두 화면 구분 – 입력 위치에 따른 차이** | **5-5-2. Telling the Two Screens Apart — What Changes with Where You Type** |
| 앞으로 나오는 모든 실습 화면은 이 두 가지 중 하나 – 줄 앞을 보고 구분 | Every exercise screen from here on is one of these two — tell them apart by the start of the line |
| **A. 파워셸 – 명령 직접 입력** — `PS D:\claude-test> git init` / `Initialized empty Git repository` / `PS D:\claude-test> git add .` | **A. PowerShell — typing commands directly** — `PS D:\claude-test> git init` / `Initialized empty Git repository` / `PS D:\claude-test> git add .` |
| **B. Claude Code – 한국어 지시** — `> git 로컬로 설정해줘.` / `● Bash git init …` | **B. Claude Code — instructions in plain language** — `> Set up git locally for me.` / `● Bash git init …` |
| 줄 앞이 `PS D:\...>` 로 시작 · 줄 앞이 `>` 하나로 시작 | One starts with `PS D:\...>`; the other starts with a single `>` |
| **두 화면 사이를 오가는 법** | **Moving between the two** |
| 파워셸 > Claude Code – `claude` 또는 `claude -c` | PowerShell into Claude Code — `claude` or `claude -c` |
| 안 나가고 셸 명령 – `!` 를 앞에 붙이기 예: `!dir` | Shell commands without leaving — prefix with `!`, e.g. `!dir` |
| Claude Code > 파워셸 – `/exit` (다시 들어갈 땐 `claude -c`) | Claude Code back to PowerShell — `/exit` (use `claude -c` to come back in) |
| 가장 흔한 실수: 파워셸에 한국어를 치거나, Claude Code 안에 git init 을 그대로 침 – 둘 다 조용히 실패하므로 현재 화면부터 확인 | The most common mistake: typing plain language into PowerShell, or typing `git init` inside Claude Code. Both fail silently, so check which screen you are in first |

### Slide 93 — 5-5-3. /init 실행 결과 (빈 폴더) / What `/init` Does in an Empty Folder

| 한국어 | English |
|---|---|
| **5-5-3. /init 실행 결과 – 빈 폴더일 때** | **5-5-3. What `/init` Does — in an Empty Folder** |
| `/init` 은 기존 코드를 분석해 CLAUDE.md 를 만드는 명령. 빈 폴더에서는 분석 대상이 없어 되물음 | `/init` analyzes existing code to write CLAUDE.md. In an empty folder there is nothing to analyze, so it asks you back |
| `✓ 현재 작업 디렉토리가 비어있습니다.` | `✓ The current working directory is empty.` |
| `✓ 분석할 코드베이스가 없는 상태입니다.` | `✓ There is no codebase to analyze.` |
| `✓ 다음 중 하나를 확인해주세요:` | `✓ Please confirm one of the following:` |
| `✓ 1. 이미 존재하는 프로젝트 – 분석할 경로를 알려주기` | `✓ 1. An existing project — tell me the path to analyze` |
| `✓ 2. 새 프로젝트 시작 – 유형을 알려주면 템플릿 생성` | `✓ 2. Starting a new project — tell me the type and I will create a template` |
| `✓ 3. 다른 위치에서 작업 – 그 폴더 경로를 알려주기` | `✓ 3. Working somewhere else — tell me that folder's path` |
| 당황하지 말 것 – 오류가 아님. 빈 폴더라서 분석할 코드가 없다는 안내. 버전에 따라 문구는 다를 수 있음 | Do not panic — this is not an error. It is telling you there is no code to analyze because the folder is empty. The wording varies by version |
| 이렇게 진행: 1. 2번 선택 후 응답 · 2. 프로젝트 유형을 알려 줌 · 3. CLAUDE.md 초안이 생성됨 · 4. 5-6 에서 내용을 직접 채움 | How to proceed: 1. Choose option 2 and reply · 2. Tell it the project type · 3. A draft CLAUDE.md is created · 4. You fill in the content yourself in 5-6 |
| 빈 폴더에서는 /init 을 건너뛰고 5-6 처럼 직접 작성해도 됨. 기존 프로젝트에서 /init 을 쓰면 코드를 분석해 자동 작성 | In an empty folder you can skip `/init` and write it by hand as in 5-6. In an existing project, `/init` analyzes the code and writes it for you |

### Slide 94 — 5-5-4. /model — 모델과 effort 선택 / Choosing Model and Effort

| 한국어 | English |
|---|---|
| **5-5-4. /model – 모델과 effort 를 한 화면에서 선택** | **5-5-4. `/model` — Choosing Model and Effort on One Screen** |
| 메뉴에서 고르거나 `/model sonnet` · `/effort low` 로 바로 지정 – 실습은 Sonnet + low | Pick from the menu, or set them directly with `/model sonnet` and `/effort low`. For the exercises: Sonnet + low |
| `Select model – Switch between Claude models.` | `Select model — Switch between Claude models.` |
| `1. Default (recommended) – Opus 5 (1M context), Most capable` | `1. Default (recommended) — Opus 5 (1M context), Most capable` |
| `2. Sonnet – Sonnet 5, Everyday tasks` ← 실습은 이것 | `2. Sonnet — Sonnet 5, Everyday tasks` ← use this one |
| `3. Haiku – Haiku 4.5, Fastest` / `4. Fable 5` / `5. Best / opusplan` | `3. Haiku — Haiku 4.5, Fastest` / `4. Fable 5` / `5. Best / opusplan` |
| `Effort (Tab 으로 이동) – low medium high xhigh(기본)` | `Effort (Tab to move here) — low, medium, high, xhigh (default)` |
| `Enter to confirm, Esc to cancel` | `Enter to confirm, Esc to cancel` |
| `Set model to Sonnet 5 for this session only` / `Set effort level to low (this session only)` | `Set model to Sonnet 5 for this session only` / `Set effort level to low (this session only)` |
| **키 조작** | **Keys** |
| `/model` – 입력하면 이 화면이 열림 | `/model` — opens this screen |
| 방향키 위/아래 – 모델 사이 이동 (Sonnet 선택) | ↑ / ↓ — move between models (select Sonnet) |
| Tab – 아래 effort 줄로 이동 | Tab — move down to the effort row |
| 방향키 좌/우 – effort 를 low 로 이동 | ← / → — move effort to low |
| Enter – 둘 다 한 번에 저장 | Enter — saves both at once |
| 왜 반드시 바꾸나: 기본값은 Opus + xhigh. 가장 비싼 모델이 가장 깊게 생각하는 조합 – 실습 비용이 몇 배로 증가. Sonnet + low 로도 본 과정 실습은 전부 문제없이 완료 가능 | Why you must change it: the default is Opus + xhigh — the most expensive model thinking as hard as it can, which multiplies the cost of the exercises. Sonnet + low completes every exercise in this course without trouble |
| this session only = 이 세션에만 적용. claude 를 새로 켤 때마다 /model 재지정 필요 (안 하면 Opus 로 복귀) | "this session only" means exactly that — you must set `/model` again each time you start `claude`, or it reverts to Opus |

### Slide 95 — 5-5-5. 실습 시작 전 매번 확인 항목 / Check These Before Every Session

| 언제 / When | 무엇을 치나 / What to type | 안 하면 / If you don't |
|---|---|---|
| 세션을 새로 켤 때마다 — Every time you start a session | `/model sonnet` | Opus 로 돌아가 비용이 크게 증가 — It reverts to Opus and costs climb sharply |
| 세션을 새로 켤 때마다 — Every time you start a session | `/effort low` | xhigh 로 깊게 생각해 토큰을 더 씀 — It thinks at xhigh and burns more tokens |
| 폴더가 맞는지 — Whether you are in the right folder | 창 위쪽 경로 확인 — Check the path at the top of the window | 다른 폴더에서 실습해 결과가 어긋남 — You work in the wrong folder and the results do not line up |

### Slide 96 — 5-5-6. 세션 이어가기 / Resuming a Session

| 한국어 | English |
|---|---|
| **5-5-6. 세션 이어가기 – claude 와 claude -c 의 차이** | **5-5-6. Resuming a Session — `claude` vs. `claude -c`** |
| 실습 도중 창을 닫았거나 다음 장으로 넘어갈 때 – 모르면 앞의 대화가 전부 소멸 | For when you closed the window mid-exercise or are moving to the next chapter — get this wrong and the whole prior conversation is gone |
| `claude` – 새 대화 시작. 이전 대화를 못 봄. 처음부터 다시 설명해야 함. 새 프로젝트를 시작할 때만 | `claude` — starts a new conversation. It cannot see the previous one, so you explain everything again. Only for starting a new project |
| `claude -c` – 직전 대화 이어서. 그 폴더에서 마지막으로 한 대화를 그대로 이어감. 실습 도중 다시 들어갈 때 (대부분 이것) | `claude -c` — continues the last conversation in that folder exactly where it stopped. This is what you want when coming back mid-exercise, which is most of the time |
| `claude -r` – 목록에서 골라서. 이전 대화 목록이 뜨고 방향키로 선택. 여러 대화 중 특정 것을 찾을 때 | `claude -r` — pick from a list. It shows earlier conversations and you choose with the arrow keys. For finding one particular conversation among several |
| `PS D:\claude-test> claude -c` → 이전 세션 이어서 시작 – 앞의 대화 내용 유지 | `PS D:\claude-test> claude -c` → resumes the previous session with the earlier conversation intact |
| 가장 흔한 실수: claude 만 입력해 새 대화가 열림 > 앞에서 만든 docs/ 를 AI가 모름 > 처음부터 다시. 세션 안에서는 /resume 로도 전환 가능 | The most common mistake: typing plain `claude`, opening a new conversation, so the AI knows nothing about the `docs/` you built earlier and you start over. Inside a session you can also switch with `/resume` |
### Slide 97 — 5-5-7. /resume / Picking an Earlier Conversation from a List

| 한국어 | English |
|---|---|
| **5-5-7. /resume – 이전 대화를 목록에서 골라 이어가기** | **5-5-7. `/resume` — Pick an Earlier Conversation from a List and Continue It** |
| `claude -c` 는 직전 대화 하나만. 여러 대화 중에서 고르려면 목록을 띄움 | `claude -c` only gets the most recent one. To choose among several, bring up the list |
| 터미널에서 들어갈 때 – `PS D:\claude-test> claude -r` | Entering from the terminal — `PS D:\claude-test> claude -r` |
| 이미 Claude Code 안에 있을 때 – `> /resume` | Already inside Claude Code — `> /resume` |
| 수정 시각 · 이 대화에서 한 일 | Last modified · What was done in that conversation |
| 5분 전 – docs/ 6종 작성 + 첫 커밋 | 5 minutes ago — wrote the six docs and made the first commit |
| 2시간 전 – backend/ FastAPI CRUD 구현 | 2 hours ago — implemented FastAPI CRUD in backend/ |
| 어제 – CLAUDE.md 작성 | Yesterday — wrote CLAUDE.md |
| 어제 – 터미널 명령어 실습 | Yesterday — terminal command exercises |
| 위 아래 방향키로 이동, Enter 로 선택 | Move with ↑ / ↓, select with Enter |
| **네 가지 진입 방법** | **Four ways in** |
| `claude` – 새 대화 시작 | `claude` — start a new conversation |
| `claude -c` – 직전 대화 이어서 | `claude -c` — continue the most recent one |
| `claude -r` – 목록에서 선택 | `claude -r` — choose from a list |
| `/resume` – 세션 안에서 전환 | `/resume` — switch from inside a session |
| 주의: 대화 목록은 폴더별로 따로 저장됨. 다른 폴더에서 열면 그 폴더의 대화만 나옴. 찾는 대화가 없으면 폴더 위치부터 확인 (pwd) | Note: conversation lists are stored per folder. Open it elsewhere and you see only that folder's conversations. If the one you want is missing, check where you are first (`pwd`) |

### Slide 98 — 5-5-8. /context 와 /cost / Checking Current Usage

| 한국어 | English |
|---|---|
| **5-5-8. /context 와 /cost – 현재 사용량 확인** | **5-5-8. `/context` and `/cost` — Checking Current Usage** |
| 실제 실행 화면 – 비용은 대화가 길어질수록 증가 | Real output — the cost rises as the conversation grows |
| `> /context` — `Model: claude-haiku-4-5` · `Tokens: 26.3k / 200k (13%)` | `> /context` — `Model: claude-haiku-4-5` · `Tokens: 26.3k / 200k (13%)` |
| `System prompt 6.8k (3.4%)` · `System tools 18.1k (9.0%)` · `MCP tools 4.7k (2.3%)` · `Skills 1.5k (0.7%)` · `Messages 8 (0.0%)` · `Free space 173.7k (86.8%)` | `System prompt 6.8k (3.4%)` · `System tools 18.1k (9.0%)` · `MCP tools 4.7k (2.3%)` · `Skills 1.5k (0.7%)` · `Messages 8 (0.0%)` · `Free space 173.7k (86.8%)` |
| `> /cost` — `Current session: 16% used` · `Current week (all models): 27% used` | `> /cost` — `Current session: 16% used` · `Current week (all models): 27% used` |
| `What's contributing to usage? 88% of usage was at >150k context · Top MCP: playwright 19%` | `What's contributing to usage? 88% of usage was at >150k context · Top MCP: playwright 19%` |
| 핵심: 컨텍스트가 클수록 매 요청마다 그 전부를 재전송 – 대화가 길어지면 같은 질문의 요금도 배로 증가. 작업이 끝나면 /clear, 길어지면 /compact. MCP 도구는 켜 두기만 해도 컨텍스트 점유 | The point: the bigger the context, the more is resent with every request — so the same question costs several times more in a long conversation. `/clear` when a task ends, `/compact` when it gets long. MCP tools consume context merely by being enabled |

### Slide 99 — 5-6. CLAUDE.md / Project Memory

| 한국어 | English |
|---|---|
| **5-6. CLAUDE.md – 프로젝트 메모리** | **5-6. CLAUDE.md — Project Memory** |
| AI가 매번 자동으로 읽는 파일 | The file the AI reads automatically every time |
| 1. 프로젝트 루트에 위치 – claude 실행 시 자동으로 읽힘 | 1. Lives at the project root — read automatically when `claude` starts |
| 2. 기술 스택 명시 – 어떤 언어, 프레임워크 쓸지 명확히 | 2. States the tech stack — which language and framework to use |
| 3. 코딩 규칙 – 변수명, 함수명, 주석 스타일 통일 | 3. Coding rules — consistent variable names, function names and comment style |
| 4. 금지 사항 – 'jQuery 사용 금지, Tailwind만 사용' | 4. Prohibitions — "No jQuery; Tailwind only" |

### Slide 100 — 5-6-1. CLAUDE.md 직접 작성 / Writing CLAUDE.md by Hand

| 한국어 | English |
|---|---|
| **5-6-1. CLAUDE.md 직접 작성 (연습용 – D:\claude-test)** | **5-6-1. Writing CLAUDE.md by Hand (practice — D:\claude-test)** |
| 파일 생김새만 보는 연습. 여기서 앱은 만들지 않음 – 실제 프로젝트용은 9-1 에서 절대규칙까지 갖춰 다시 작성 | Just to see what the file looks like — you are not building an app here. The real project version, with hard rules, is rewritten in 9-1 |
| 전체 복사 가능 · CLAUDE.md 작성 – Claude Code 에 그대로 붙여넣기 | Copy the whole thing and paste it straight into Claude Code |
| `아래 내용을 이 폴더 루트에 CLAUDE.md 라는 이름으로 저장해줘.` | `Save the following at the root of this folder as CLAUDE.md.` |
| `## 연습용 – 실제 구현은 하지 않음` | `## Practice only — do not actually implement` |
| `## 기술 스택` / `- 서버: FastAPI + Python 3.11 + SQLite` / `- 프론트: Vanilla JS + Tailwind CDN` / `- 폴더: backend/ 와 frontend/ 분리` | `## Tech stack` / `- Server: FastAPI + Python 3.11 + SQLite` / `- Frontend: Vanilla JS + Tailwind CDN` / `- Folders: backend/ and frontend/ kept separate` |
| `## 코딩 규칙` / `- 한국어 주석 사용` / `- 변수명: snake_case (Python), camelCase (JS)` / `- 모든 API는 /api/ 경로 prefix 사용` | `## Coding rules` / `- Write comments in Korean` / `- Naming: snake_case in Python, camelCase in JS` / `- Prefix every API path with /api/` |
| `## 금지 사항` / `- jQuery 사용 금지` / `- CSS 직접 작성 금지 (Tailwind만 사용)` | `## Prohibitions` / `- No jQuery` / `- No hand-written CSS (Tailwind only)` |

### Slide 101 — 5-7. 3단계 권한 시스템 & 실행 모드 / Three Permission Levels and Execution Modes

| 권한 / Permission | 의미 / Meaning |
|---|---|
| Allow | 자동 실행 – 확인 없이 바로 실행 — Runs automatically, with no confirmation |
| Ask | 확인 후 실행 – 실행 전 승인 필요 — Requires approval before running |
| Deny | 금지 – 절대 실행하지 않음 — Forbidden; never runs |

| 모드 / Mode | 설명 / Description |
|---|---|
| `default` — 안전 우선 / safety first | 매번 권한 요청 – 처음 사용 시 권장 — Asks every time; recommended when starting out |
| `acceptEdits` — 파일 편집 위주 / edit-heavy work | 파일 수정만 자동 승인, 실행 명령은 확인 — Auto-approves file edits, still confirms commands |
| `plan` — 복잡한 작업 전 / before complex work | 계획만 수립, 실행 전 사람이 검토 후 승인 — Plans only; a human reviews and approves before execution |
| `auto` — 실습 권장 / recommended for the exercises | 상황을 보고 자동 판단 – 본 과정 기본값 — Judges by situation; the course default |
| `dontAsk` — 주의 / caution | 묻지 않고 진행 – 익숙해진 뒤에만 — Proceeds without asking; only once you are comfortable |
| `bypassPermissions` — 위험 / dangerous | 권한 확인을 전부 건너뜀 – CLI 로만 지정 — Skips every permission check; settable only from the CLI |

| 한국어 | English |
|---|---|
| **5-7. 3단계 권한 시스템 & 실행 모드** | **5-7. The Three-Level Permission System and Execution Modes** |
| 명령 실행 전 Claude Code가 허가를 요청 – Shift+Tab으로 모드 전환 | Claude Code asks permission before running a command — switch modes with Shift+Tab |
| 모드를 지정하는 3가지 방법: 세션 중 전환 Shift + Tab · 영구 고정 `/config permissionMode` · 실행할 때 지정 `claude --permission-mode` | Three ways to set the mode: switch mid-session with Shift+Tab; pin it with `/config permissionMode`; specify at launch with `claude --permission-mode` |
| bypassPermissions 주의: 확인 없이 전부 실행되므로 파일 삭제도 그대로 진행됨. /config 로는 지정 불가하고 실행할 때만 붙일 수 있음. 본 과정 실습에서는 미사용 – 기본값 default 로 충분 | A warning on `bypassPermissions`: everything runs unconfirmed, including file deletion. It cannot be set through `/config`, only at launch. Not used in this course — `default` is enough |

### Slide 102 — 5-8. /config 설정 항목 / `/config` Settings Explained

| 설정 키 / Key | 기본값 / Default | 의미 / Meaning |
|---|---|---|
| `language` | English | 응답 언어 – 한국어로 반드시 변경 — Response language; change it to Korean |
| `model` | default | 사용할 모델 – 실습은 sonnet (비용 절감) — Which model; use sonnet for the exercises to save cost |
| `autoCompact` | true | 대화가 길어지면 자동 요약 – 토큰 절약, 켜두기 — Auto-summarizes long conversations; saves tokens, leave it on |
| `thinking` | true | AI 사고 과정 표시 – 학습에 도움 — Shows the AI's reasoning; useful for learning |
| `checkpoints` | true | 되돌리기 지점 저장 – Esc Esc 로 복구 가능 — Saves restore points; recover with Esc Esc |
| `permissionMode` | default | 권한 모드 – default는 실행 전 매번 확인 — Permission mode; `default` confirms before every action |
| `verbose` | false | 내부 처리까지 전부 출력 – 미표시 권장 — Prints internal processing too; better left off |
| `theme` | auto | 화면 테마 – dark / light 선택 가능 — Screen theme; dark or light |
| `recap` | true | 세션 시작 시 이전 대화 요약 표시 — Shows a summary of the previous conversation at session start |
| `autoScroll` | true | 출력이 길어지면 자동으로 따라 내려감 — Follows long output down the screen automatically |

| 한국어 | English |
|---|---|
| **5-8. /config – 설정 화면 항목 설명** | **5-8. `/config` — the Settings Screen Explained** |
| claude 실행 중 `/config` 만 치면 설정 가능한 항목 전부 표시 (아래는 실습에 필요한 것) | Type `/config` while Claude is running to see every setting. The ones below are what the exercises need |

### Slide 103 — 5-8-1. /config 추천 설정 / Recommended Settings

| 설정 / Setting | 값 / Value | 이유 / Why |
|---|---|---|
| `/config language=한국어` | 필수 – 맨 처음에 / essential, do it first | Claude 응답이 한국어로 — Claude answers in Korean |
| `/config model=sonnet` | sonnet | 영구 고정도 가능. 본 과정은 세션마다 /model 로 확인 — Can be pinned permanently; this course checks it per session with `/model` |
| `/config autoCompact=true` | true | 길어지면 자동 요약 – 토큰 절약 — Auto-summarizes when long; saves tokens |
| `/config thinking=true` | true | AI 사고과정 보기 – 학습에 도움 — See the AI's reasoning; useful for learning |
| `/config checkpoints=true` | true | 되돌리기 지점 저장 – Esc Esc 로 복구 — Saves restore points; recover with Esc Esc |
| `/config verbose=false` | false | 내부 출력 숨김 – 화면이 간결해짐 — Hides internal output; keeps the screen clean |
| `/config theme=dark` | dark | 어두운 화면 선호 시 (light 도 가능) — If you prefer a dark screen (light also available) |

| 한국어 | English |
|---|---|
| **5-8-1. /config 추천 설정 – 한국어 수강생 기준** | **5-8-1. Recommended `/config` Settings — for Korean-Speaking Students** |
| /config 는 한 번만 하면 영구 저장 (/model 은 세션마다 다시 지정) | `/config` is saved permanently after one pass (`/model` must be set again each session) |

### Slide 104 — 5-9. 권한 설정 파일 / The Permissions File, `.claude/settings.json`

| 한국어 | English |
|---|---|
| **5-9. 권한 설정 파일 – .claude/settings.json** | **5-9. The Permissions File — `.claude/settings.json`** |
| 설치 직후에는 파일이 없는 상태가 정상. 다음 슬라이드에서 권한 요청에 응답하는 순간 자동 생성 | It is normal for the file not to exist right after installation. It is created the moment you answer a permission prompt, on the next slide |
| `# 지금 폴더에 무엇이 있는지 확인` → `dir` → `-a---- 2026-08-05 17:33 412 CLAUDE.md` | `# See what is in this folder` → `dir` → `-a---- 2026-08-05 17:33 412 CLAUDE.md` |
| `# 숨김 폴더까지 보려면 -Force` → `dir -Force` | `# To include hidden folders, use -Force` → `dir -Force` |
| `# .claude 폴더가 아직 없음 – 정상` → `Test-Path .claude\settings.json` → `False` | `# No .claude folder yet — this is normal` → `Test-Path .claude\settings.json` → `False` |
| 없는 게 정상 – .claude/settings.json 은 Claude Code 가 처음 권한을 물을 때 자동으로 만들어짐 | Its absence is normal — `.claude/settings.json` is created the first time Claude Code asks for permission |
| 이 파일에 담기는 것: 허용한 명령 목록 · 허용한 폴더 경로 · 권한 모드 기본값 · 프로젝트 단위로 저장 | What it holds: the list of allowed commands, the allowed folder paths, the default permission mode — stored per project |
| 생성 확인 명령: `cat .claude/settings.json` (파일이 생긴 뒤에 실행) | To check once it exists: `cat .claude/settings.json` |
| .claude 는 점으로 시작하는 숨김 폴더 – 탐색기에서는 보기 옵션을 켜야 보임 | `.claude` starts with a dot, so it is hidden — you must turn on hidden items in Explorer to see it |

### Slide 105 — 5-9-1. 권한 요청 / The Permission Prompt That Creates settings.json

| 한국어 | English |
|---|---|
| **5-9-1. 권한 요청 – 이때 settings.json 이 생성됨** | **5-9-1. The Permission Prompt — This Is When settings.json Is Created** |
| 아래는 전부 Claude Code 안에서 벌어지는 일. 파일을 만들거나 명령을 실행하기 직전에 한 번 물어봄 | All of this happens inside Claude Code. It asks once, right before creating a file or running a command |
| 1. 내가 한국어로 지시 – `> docs 폴더 하나 만들어줘` | 1. You instruct it in plain language — `> Make me a docs folder` |
| 2. Claude 가 실행하려는 명령 – `● Bash(mkdir D:\claude-test\docs)` | 2. The command Claude wants to run — `● Bash(mkdir D:\claude-test\docs)` |
| 3. 실행 직전에 물어봄 – `Do you want to proceed?` | 3. It asks just before running — `Do you want to proceed?` |
| `1. Yes` / `2. Yes, and always allow access to claude-test from this project` / `3. No` | `1. Yes` / `2. Yes, and always allow access to claude-test from this project` / `3. No` |
| 방향키로 이동, Enter 로 선택 · 실습에서는 2번 선택 | Move with the arrow keys, select with Enter. For the exercises, choose option 2 |
| **세 선택지의 차이**: 1 이번 한 번만 허용 · 2 이 폴더는 앞으로 계속 허용 · 3 실행하지 않음 | **What the three options mean**: 1 — allow this once; 2 — allow this folder from now on; 3 — do not run it |
| 2번을 고르면 .claude/settings.json 이 이 순간 자동 생성됨 | Choosing 2 creates `.claude/settings.json` at that moment |
| 2번 선택 > .claude/settings.json 자동 생성 > 다음부터 같은 폴더 명령은 재확인 없음 | Choose 2 → `.claude/settings.json` is created → commands in that folder are not questioned again |

### Slide 106 — 5-9-2. 설정 파일은 세 곳 / Three Settings Files, Merged

| 한국어 | English |
|---|---|
| **5-9-2. 설정 파일은 세 곳 – 겹치면 합쳐짐** | **5-9-2. Three Settings Files — Overlaps Are Merged** |
| 한쪽이 다른 쪽을 지우지 않음. 값이 정면으로 부딪칠 때만 순서가 갈림 | One never erases another. Precedence only comes into play when two values directly conflict |
| 읽히는 파일 – 위에서 아래로 | The files read, top to bottom |
| `~/.claude/settings.json` – 내 PC 전체에 적용 | `~/.claude/settings.json` — applies across your whole machine |
| `<프로젝트>/.claude/settings.json` – 팀 공용. 저장소에 함께 올림 | `<project>/.claude/settings.json` — shared with the team; committed to the repository |
| `<프로젝트>/.claude/settings.local.json` – 나만 쓰는 값. 올리지 않음 | `<project>/.claude/settings.local.json` — your own values; not committed |
| 아래로 갈수록 좁은 범위 – 값이 겹치면 아래가 우선 | The scope narrows as you go down; on a conflict the lower one wins |
| 합쳐짐. 덮어쓰지 않음 – 전역과 프로젝트에 각각 걸면 둘 다 동작. 하나가 다른 하나를 지우지 않음 | They merge rather than overwrite — set something globally and in the project and both apply; neither erases the other |
| 값이 겹칠 때의 우선순위 – 같은 항목에 다른 값을 주면 local > 프로젝트 > 전역 순으로 우선 | Precedence on conflict — for the same key, local beats project beats global |
| 프로젝트 = 세션을 연 폴더 – 그 아래 하위 폴더에 둔 .claude 는 읽히지 않는다. 열어 둔 위치가 전부다 | "Project" means the folder you opened the session in — a `.claude` in a subfolder beneath it is not read. Where you opened it is all that counts |
| 훅은 시작할 때 한 번만 읽음 – 고쳐도 지금 세션에는 안 붙는다. 세션을 새로 열어야 적용 | Hooks are read once at startup — editing them does not affect the current session; open a new one |
| 기억할 것: 안쪽이 바깥쪽을 이기는 것이 아니라 합쳐지는 것. 다만 세션을 연 폴더 밖의 .claude 는 처음부터 안 보임 | Remember: the inner does not beat the outer, it merges with it. But a `.claude` outside the folder you opened is never seen at all |

### Slide 107 — 5-10. Claude Code 실전 팁 8가지 / Eight Practical Tips

| 한국어 | English |
|---|---|
| **5-10. Claude Code 실전 팁 8가지** | **5-10. Eight Practical Claude Code Tips** |
| 반드시 익혀야 하는 핵심 팁 – 숙지 시 작업 속도 향상 | The essentials worth learning — they speed up everything |
| 1. 안 나가고 셸 명령 – `> !dir` – 명령 앞에 느낌표를 붙이면 Claude Code 안에서 셸 명령 실행 | 1. Shell commands without leaving — `> !dir`. Prefix with an exclamation mark to run a shell command from inside Claude Code |
| 2. 계획부터 보기 – Shift + Tab – plan 모드로 바꾸면 실행 전 계획을 먼저 보여 줌 | 2. See the plan first — Shift + Tab. In plan mode it shows you the plan before acting |
| 3. 파일 참조 @ – `@CLAUDE.md`, `@backend/main.py` – 풀패스 안 쳐도 됨. @로 직접 지정 | 3. Reference files with @ — `@CLAUDE.md`, `@backend/main.py`. No full paths needed |
| 4. 체크포인트 – Esc Esc 또는 `> /rewind` – 이전 상태로 복구 | 4. Checkpoints — press Esc twice or type `/rewind` to restore an earlier state |
| 5. 긴 지시는 복사해서 – Ctrl + V – 독수리 타법이면 오타로 결과가 갈림. 배포 파일에서 복사해 붙여넣기 | 5. Paste long instructions — Ctrl + V. Hunt-and-peck typing means typos change the result; copy from the handout instead |
| 6. AI 가 물으면 답 – 선택지 1 / 2 / 3 – 지시가 모호하면 AI 가 선택지를 내밈. 골라 주면 추측으로 진행되는 일이 없음 | 6. Answer when the AI asks — options 1 / 2 / 3. When your instruction is vague it offers choices; picking one stops it guessing |
| 7. 명령어 모를 땐 – `> /help`, 중단은 Ctrl+C – 암기 불필요 | 7. When you forget a command — `/help`; Ctrl+C to interrupt. Nothing needs memorizing |
| 8. 결과가 이상하면 – `> 다시 해줘. 이유도 알려줘` – 고쳐 달라고만 하지 말고 왜 그렇게 됐는지 함께 물을 것 | 8. When the result looks wrong — "Do it again, and tell me why it happened." Do not just ask for a fix; ask why it went that way |

### Slide 108 — 5-11. 서브에이전트 / Subagents

| 한국어 | English |
|---|---|
| **5-11. 서브에이전트 – 일을 나눠 시키는 보조 AI** | **5-11. Subagents — Helper AIs You Hand Work To** |
| 메인 대화는 그대로 두고, 별도 대화창을 가진 보조 AI 에게 작업을 통째로 맡기는 방식 | Leave the main conversation as it is and hand a whole task to a helper AI with its own conversation |
| 나 > 메인 Claude 에게 지시 | You — instruct the main Claude |
| 메인 Claude > 서브에이전트에게 작업 위임 | Main Claude — delegates the task to a subagent |
| 서브에이전트 > 자기 대화창에서 혼자 수행 | Subagent — carries it out alone in its own conversation |
| 메인 Claude > 결과 요약만 받아서 보고 | Main Claude — receives only a summary and reports back |
| **이럴 때 유용** | **When it helps** |
| 컨텍스트 격리 – 메인 대화가 안 지저분해짐 | Context isolation — the main conversation stays clean |
| 긴 조사·검색 작업을 통째로 위임 | Hand off long research and search jobs wholesale |
| 역할 고정 – 문서 전담, 리뷰 전담 식으로 | Fixed roles — one for documents, one for reviews |
| 여러 건을 동시에 병렬 처리 | Several jobs run in parallel |
| **주의 – 비용** | **Caution — cost** |
| 서브에이전트는 독립 대화 – 토큰을 따로 씀 | A subagent is a separate conversation and spends its own tokens |
| 여러 개를 동시에 띄우면 그만큼 배로 나감 | Run several at once and the cost multiplies accordingly |
| 실측 – 서브에이전트를 많이 쓴 세션이 전체 사용량의 23% 를 차지 (/usage 기준) | Measured — sessions that used many subagents accounted for 23% of total usage (per `/usage`) |
| 메인 대화와 무엇이 다른가: 메인 Claude 는 지금까지의 대화를 전부 기억. 서브에이전트는 그 작업에 필요한 내용만 받고 끝나면 사라짐 – 그래서 메인이 가벼워짐 | How it differs from the main conversation: the main Claude remembers everything so far; a subagent receives only what that task needs and disappears when done — which is what keeps the main one light |
| 본 과정 실습에서는 미사용 – 개념만 숙지하고, 대규모 조사 작업에서 활용 | Not used in this course's exercises — learn the concept and apply it to large research jobs |

### Slide 109 — 5-12. 서브에이전트 만들고 시키기 / Creating and Using a Subagent

| 한국어 | English |
|---|---|
| **5-12. 서브에이전트 만들고 시키기** | **5-12. Creating a Subagent and Putting It to Work** |
| 만드는 방법 두 가지 – 자연어로 지시하거나 파일을 직접 작성 | Two ways to make one — ask in plain language, or write the file yourself |
| **방법 1 – 자연어로 지시 (쉬움)** | **Method 1 — ask in plain language (the easy way)** |
| `> doc-writer 라는 문서 전담 에이전트 만들어줘.` → `✓ .claude/agents/doc-writer.md 생성 완료` | `> Create a documentation agent called doc-writer.` → `✓ Created .claude/agents/doc-writer.md` |
| **방법 2 – 파일 직접 작성** — `.claude/agents/doc-writer.md` | **Method 2 — write the file yourself** — `.claude/agents/doc-writer.md` |
| `name: doc-writer` / `description: 문서 작성 전담. README 등` / `tools: Read, Write, Edit, Glob, Grep` / `너는 기술 문서 작성 전담이다. 한국어로.` | `name: doc-writer` / `description: Dedicated to writing documentation — READMEs and the like` / `tools: Read, Write, Edit, Glob, Grep` / `You write technical documentation. Write in Korean.` |
| 만든 뒤 – 이름을 지정해 호출, 또는 description 이 맞으면 자동 위임 | Once made — call it by name, or let it be delegated to automatically when the description matches |
| `> doc-writer 로 이 프로젝트 README 작성해줘` / `> 이 프로젝트 사용법 문서 만들어줘` | `> Use doc-writer to write this project's README` / `> Write a usage document for this project` |
| 저장 위치 `.claude/agents/` – 적용 범위: 이 프로젝트만 – 쓰는 경우: 프로젝트 전용 역할 | Stored at `.claude/agents/` — scope: this project only — for project-specific roles |
| 저장 위치 `~/.claude/agents/` – 적용 범위: 모든 프로젝트 – 쓰는 경우: 어디서나 쓰는 역할 | Stored at `~/.claude/agents/` — scope: every project — for roles you use everywhere |

### Slide 110 — 체크포인트 / Checkpoint

| 한국어 | English |
|---|---|
| **체크포인트** | **Checkpoint** |
| 1. `claude --version` 실행 | 1. Run `claude --version` |
| 2. API Key 인증 & 첫 대화 | 2. Authenticate with the API key and have a first conversation |
| 3. 모델 sonnet + effort low 설정 | 3. Set the model to sonnet and effort to low |
| 4. CLAUDE.md 생성 확인 | 4. Confirm CLAUDE.md was created |

---

## 6장. 스킬과 플러그인 / Chapter 6. Skills and Plugins

### Slide 111 — Chapter cover

| 한국어 | English |
|---|---|
| **Claude Code 를 확장하는 네 가지** | **Four Ways to Extend Claude Code** |
| 플러그인 · 스킬 · 명령어 · 훅의 구분과 설치 | Telling plugins, skills, commands and hooks apart, and installing them |
| 학습 내용 | What you will learn |
| 1. 플러그인과 스킬의 차이 | 1. The difference between a plugin and a skill |
| 2. 명령어 · 스킬 · 훅을 호출 주체로 구분 | 2. Distinguishing commands, skills and hooks by who invokes them |
| 3. 마켓플레이스에서 스킬 설치 | 3. Installing a skill from a marketplace |
| 4. 이름을 부르지 않아도 스킬이 붙는 것 확인 | 4. Seeing a skill engage without being named |

### Slide 112 — 6-1. 플러그인이란 / What a Plugin Is

| 한국어 | English |
|---|---|
| **6-1. 플러그인이란 – 기능 묶음을 통째로 들여오는 상자** | **6-1. What a Plugin Is — a Box That Brings In a Whole Bundle of Features** |
| 설치 방법 전에 무엇을 설치하는지부터 – 화면에서 어떻게 보이나 | Before the how, the what — and how it looks on screen |
| `> /plugin` → `✓ Plugin marketplaces` / `✓ anthropics/skills – 플러그인 15개` / `✓ hull-kr/claude-hud – 플러그인 1개` / `✓ 설치됨: document-skills · claude-hud` | `> /plugin` → `✓ Plugin marketplaces` / `✓ anthropics/skills — 15 plugins` / `✓ hull-kr/claude-hud — 1 plugin` / `✓ Installed: document-skills · claude-hud` |
| 정의 – 새 기능을 묶어 한 번에 들여오는 확장 패키지 | Definition — an extension package that brings a bundle of new capabilities in at once |
| 상자 안의 구성 요소 – 명령어 · 스킬 · 훅 · 에이전트 · 외부 연동 설정 | What is in the box — commands, skills, hooks, agents and external integration settings |
| 설치 방법 두 갈래 – 셸에서 `claude plugin`, Claude Code 창 안에서 `/plugin` | Two ways to install — `claude plugin` from the shell, `/plugin` inside the Claude Code window |
| 적용 범위 – scope 를 project 로 두면 그 폴더에서만 켜짐 | Scope — set scope to `project` and it is enabled only in that folder |
| 직접 손댈 일은 없음 – 켠 목록은 settings.json 에 자동으로 남음 | Nothing to edit by hand — what you enable is recorded in settings.json automatically |
| 묶음 단위 설치 – 상자를 들이면 그 안의 명령어와 스킬이 한꺼번에 붙음 – 마켓플레이스에 등록된 이름 하나로 설치 | Installed as a bundle — bring in the box and its commands and skills all attach at once, installed by the single name registered in the marketplace |

### Slide 113 — 6-2. 스킬이란 / What a Skill Is

| 항목 / Item | 내용 / Detail |
|---|---|
| 정의 / Definition | 작업 절차를 적어 둔 지시서 — A set of written instructions describing a procedure |
| 파일 경로 / Path | `.claude/skills/이름/SKILL.md` — `.claude/skills/<name>/SKILL.md` |
| 폴더 구성 / Folder contents | SKILL.md 와 스크립트, 서식 파일을 함께 — SKILL.md alongside scripts and template files |
| 켜지는 법 / How it engages | 이름을 부르지 않아도 요청 문장으로 선택 — Selected from the wording of your request, without being named |
| 직접 호출 / Direct invocation | `/스킬이름` 으로 지정해 부르는 것도 가능 — You can also call it directly as `/<skill-name>` |
| 들여오는 법 / How to bring it in | 플러그인에 포함되거나 폴더 복사로 단독 설치 — Bundled in a plugin, or installed alone by copying the folder |
| 적용 범위 / Scope | 그 폴더에서 시작한 세션 — Sessions started in that folder |

| 한국어 | English |
|---|---|
| **6-2. 스킬이란 – 절차를 적어 둔 지시서 한 장** | **6-2. What a Skill Is — a Single Sheet of Written Procedure** |
| 사람이 읽을 수 있는 마크다운 한 장 – 폴더 하나가 스킬 하나 | One page of human-readable Markdown — one folder is one skill |
| `.claude/skills/코드리뷰/SKILL.md` — `name: 코드리뷰` / `description: 변경한 코드를 검토 기준에 맞춰 점검한다. 코드 봐줘, 리뷰해줘, 점검해줘 라고 요청할 때 사용한다.` / `allowed-tools: [Read, Grep, Glob]` | `.claude/skills/code-review/SKILL.md` — `name: code-review` / `description: Checks changed code against the review criteria. Use when asked to look at, review or check the code.` / `allowed-tools: [Read, Grep, Glob]` |
| `# 코드 검토` / `## 점검 순서` / `1. 변경한 파일만 읽는다` / `2. 명명 규칙 위반을 찾는다` / `3. 테스트 누락을 표시한다` | `# Code review` / `## Review order` / `1. Read only the changed files` / `2. Find naming-convention violations` / `3. Flag missing tests` |

### Slide 114 — 6-2-1. 마켓플레이스의 실체 / What a Marketplace Actually Is

| 한국어 | English |
|---|---|
| **6-2-1. 마켓플레이스의 실체** | **6-2-1. What a Marketplace Actually Is** |
| 앱스토어 같은 화면이 아니라 공개 GitHub 저장소 – 6-8 에서 치는 anthropics/skills 가 바로 이곳 | Not an app-store screen but a public GitHub repository — `anthropics/skills`, the one you type in 6-8, is exactly this |
| github.com/anthropics/skills – `.claude-plugin` 이 마켓플레이스 표시 | github.com/anthropics/skills — the `.claude-plugin` folder is what marks it as a marketplace |
| `skills/` – 이 안의 폴더 하나가 스킬 하나 | `skills/` — each folder inside is one skill |
| 명령에 적는 이름 – `anthropics/skills` – GitHub 의 계정/저장소 그대로. 주소 전체를 적지 않음 | The name you type in the command — `anthropics/skills`, the GitHub account and repository as they are. Not the full URL |
| 마켓플레이스로 만드는 것 – `.claude-plugin` – 이 폴더가 있어야 마켓플레이스로 등록됨 | What makes it a marketplace — `.claude-plugin`; without that folder it cannot be registered as one |
| 설치 단위 – `document-skills` – 저장소 전체가 아니라 그 안의 묶음 하나를 고름 | The unit of installation — `document-skills`; you pick one bundle inside, not the whole repository |
| 스킬 하나의 실체 – 폴더 + SKILL.md – 6-2 에서 본 지시서 한 장. 특별한 형식이 아님 | What one skill really is — a folder plus SKILL.md, the single instruction sheet from 6-2. Nothing exotic |
| 저장소를 쓰는 이유: 누구나 자기 저장소를 마켓플레이스로 열 수 있음. 사내 서식을 스킬로 묶어 팀에 배포하는 방식이 여기서 나옴 | Why a repository: anyone can open their own as a marketplace. This is how you bundle in-house templates as skills and distribute them to a team |

### Slide 115 — 6-3. 플러그인 안의 세 가지 / The Three Things Inside a Plugin

| 구분 / Type | 파일이 놓이는 곳 / Where the file goes | 켜지는 방식 / How it engages | 본 과정에서 / In this course |
|---|---|---|---|
| 명령어 / Command | `.claude/commands/이름.md` | 사람이 `/이름` 으로 호출 — A person invokes it with `/name` | 파일 구조만 확인 — We only look at the file structure |
| 스킬 / Skill | `.claude/skills/이름/SKILL.md` | 요청 문장을 보고 스스로 선택 — It selects itself from the wording of the request | 설치해서 실제 사용 — We install and actually use one |
| 훅 / Hook | `.claude/settings.json` 의 hooks | 정해진 시점에 자동 실행 — Runs automatically at a defined moment | 구성 요소로 소개 — Introduced as a component |

| 한국어 | English |
|---|---|
| **6-3. 플러그인 안에 들어 있는 세 가지** | **6-3. The Three Things Inside a Plugin** |
| 무엇을 하느냐가 아니라 누가 언제 부르느냐로 갈림 | They are distinguished not by what they do but by who invokes them, and when |
| 명령어 – 사람이 부를 때만 – 부르지 않으면 실행되지 않음. 자동으로 켜지는 일이 없음 | Command — only when a person calls it. If you do not call it, it never runs; it never engages by itself |
| 스킬 – AI 가 스스로 – 요청 문장과 스킬 설명문이 겹치면 스스로 붙음. `/이름` 으로 직접 부를 수도 있음 | Skill — the AI does it. When your request overlaps the skill's description it attaches itself, and you can still call it by name |
| 훅 – 도구가 정해진 때에 – 모델이 아니라 도구 자체가 실행. 도구 실행 직전·직후, 세션 시작·종료 | Hook — the tool, at fixed moments. Executed by the tool itself, not the model: just before and after a tool runs, and at session start and end |
| 스킬이 상위 호환: 스킬도 `/이름` 으로 부를 수 있지만 명령어는 자동으로 켜지지 않음 – 업무용으로 만드는 것은 대부분 스킬 | Skills are the superset: a skill can also be called by name, but a command never engages on its own — so most things built for real work are skills |

### Slide 116 — 6-4. 명령어와 스킬의 차이 / Command vs. Skill

| 비교 항목 / Aspect | 명령어 / Command | 스킬 / Skill |
|---|---|---|
| 파일 위치 / File location | `.claude/commands/이름.md` | `.claude/skills/이름/SKILL.md` |
| 부르는 방식 / How it is invoked | 사람이 `/이름` 을 직접 입력 — A person types `/name` | Claude 가 요청 문장을 보고 스스로 호출. `/이름` 도 가능 — Claude invokes it from the request; `/name` also works |
| 컨텍스트 점유 / Context footprint | 본문이 통째로 프롬프트에 들어감 — The whole body goes into the prompt | 평소엔 설명 한 줄. 쓸 때만 본문을 읽음 — Normally one line of description; the body is read only when used |
| 구성 단위 / Unit | 마크다운 파일 하나 — A single Markdown file | 폴더 하나. 스크립트·서식·예시를 함께 — A folder, with scripts, templates and examples |
| 인자 / Arguments | `/이름 backend` 처럼 값을 받음 — Takes a value, e.g. `/name backend` | 문장 안에서 대상을 읽어 판단 — Works out the target from the sentence |
| 배포 / Distribution | 그 프로젝트 안에서 끝 — Stays within that project | 플러그인에 담아 남에게 전달 — Can be packaged in a plugin and given to others |

### Slide 117 — 6-5. 명령어와 스킬의 선택 기준 / Choosing Between Them

| 한국어 | English |
|---|---|
| **6-5. 명령어와 스킬의 선택 기준** | **6-5. How to Choose Between a Command and a Skill** |
| 둘 다 스킬 폴더에 들어가지만 켜지는 방식이 다름 | Both live under the skills area, but they engage differently |
| **명령어로 만들 때** | **Make it a command when** |
| 저절로 실행되면 곤란한 일 | It would be a problem for it to run by itself |
| 대상을 바꿔 가며 부르는 일 | You call it against a different target each time |
| 되돌리기 어려운 일괄 정리와 배포 | It is a bulk cleanup or deployment that is hard to undo |
| 규칙이 한두 줄로 끝나는 지시 | The rule fits in a line or two |
| 내가 부를 때만 실행 | It should run only when you call it |
| **스킬로 만들 때** | **Make it a skill when** |
| 지켜야 할 서식과 금지 사항이 있는 일 | There is a format to follow and things that are forbidden |
| 보고서, 회의록, 공문 서식 | Reports, minutes, official letter formats |
| 이름을 지정하지 않아도 적용돼야 하는 일 | It should apply without being named |
| 규칙이 길어도 부담이 없고 배포도 가능 | Long rules cost nothing, and it can be distributed |
| description 문장을 보고 스스로 판단 | It decides for itself from the description |
| 선택 기준: 내가 이름을 불러 쓰면 명령어, Claude 가 스스로 꺼내 쓰게 하려면 스킬 | The rule of thumb: if you will call it by name, make it a command; if you want Claude to reach for it on its own, make it a skill |

### Slide 118 — 6-6. 인자값을 받는 명령어의 구조 / A Command That Takes an Argument

| 앞부분 설정 / Front matter | 하는 일 / What it does |
|---|---|
| `description` | 무슨 명령인지, 목록에 뜨는 설명 — What the command is; the description shown in the list |
| `argument-hint` | 뒤에 붙일 수 있는 값을 미리 보여 줌 — Shows in advance which values can follow |
| `allowed-tools` | 이 명령이 쓸 수 있는 도구를 제한 — Limits which tools this command may use |
| `$1` | 명령 뒤에 적은 값이 들어오는 곳 — Where the value typed after the command lands |
| 부르는 법 / How to call it | `/테스트 backend` 처럼 뒤에 대상을 붙임 — Append the target, e.g. `/test backend` |
| 산출물 / Output | 대상 이름이 파일명에 들어가 따로 남음 — The target's name goes into the filename, so each is kept separately |

| 한국어 | English |
|---|---|
| **6-6. 인자값을 받는 명령어의 구조** | **6-6. The Structure of a Command That Takes an Argument** |
| 스킬과 같은 마크다운 한 장 – 차이는 호출할 때 뒤에 대상을 붙인다는 점 | The same single Markdown page as a skill — the difference is that you append a target when calling it |
| `.claude/commands/테스트.md` — `description: 지정한 폴더의 테스트를 실행하고 결과를 표로 정리한다` / `argument-hint: [backend \| frontend]` / `allowed-tools: Read, Bash, Glob` | `.claude/commands/test.md` — `description: Runs the tests in the given folder and tabulates the results` / `argument-hint: [backend \| frontend]` / `allowed-tools: Read, Bash, Glob` |
| `# 테스트 실행 – 대상: $1` / `1. $1 폴더의 테스트만 실행한다.` / `2. 실패한 항목을 표로 정리한다.` / `3. 결과를 문서/테스트-$1.md 로 저장한다.` | `# Run tests — target: $1` / `1. Run only the tests in the $1 folder.` / `2. Tabulate the failures.` / `3. Save the result as docs/test-$1.md.` |

### Slide 119 — 6-7. 스킬을 들여오는 두 경로 / Two Routes to Bringing In a Skill

| 한국어 | English |
|---|---|
| **6-7. 스킬을 들여오는 두 경로** | **6-7. Two Routes to Bringing In a Skill** |
| 남이 만든 것을 받아 오느냐, 내가 만든 것을 넣느냐의 차이 | The difference between pulling in someone else's and putting in your own |
| **마켓플레이스 설치** – 공개 저장소에 등록된 묶음을 명령 한 줄로 | **Marketplace install** — a bundle registered in a public repository, in one command |
| `marketplace add` 로 저장소 등록 | Register the repository with `marketplace add` |
| `plugin install` 로 묶음 설치 | Install the bundle with `plugin install` |
| settings.json 에 사용 설정이 남음 | The configuration is recorded in settings.json |
| 여러 스킬이 한 번에 들어오고 갱신이 쉬움 | Several skills arrive at once, and updating is easy |
| **폴더 복사** – 직접 만든 스킬을 프로젝트에 그대로 넣기 | **Copying the folder** — drop a skill you made straight into the project |
| 스킬 폴더를 `.claude/skills` 로 복사 | Copy the skill folder into `.claude/skills` |
| 복사 단위 – 이름 폴더 하나와 그 안의 SKILL.md | What to copy — one named folder with its SKILL.md inside |
| 인식 시점 – 복사한 뒤 시작하는 세션부터 | When it is recognized — from the next session started after copying |
| 마켓에 없는 고유 서식도 그대로 사용 | Your own formats, absent from any marketplace, work just the same |
| 두 경로의 결과: 어느 쪽으로 넣든 .claude/skills 아래에 들어가고 같은 방식으로 불림 | Either way the result is the same — it lands under `.claude/skills` and is invoked identically |

### Slide 120 — 6-8. 마켓플레이스 등록과 스킬 설치 / Registering a Marketplace and Installing a Skill

| 한국어 | English |
|---|---|
| **6-8. 마켓플레이스 등록하고 스킬 설치** | **6-8. Registering a Marketplace and Installing a Skill** |
| 공식 저장소를 이 프로젝트에 등록한 뒤 문서 스킬 묶음을 설치하고 구성 요소까지 확인 | Register the official repository against this project, install the document skills bundle, and inspect what is in it |
| `# 1. 공식 스킬 저장소를 이 프로젝트에 등록` → `claude plugin marketplace add anthropics/skills --scope project` → `Successfully added marketplace: anthropic-agent-skills` | `# 1. Register the official skills repository for this project` → `claude plugin marketplace add anthropics/skills --scope project` → `Successfully added marketplace: anthropic-agent-skills` |
| `# 2. 문서 스킬 묶음 설치` → `claude plugin install document-skills@anthropic-agent-skills` → `Successfully installed plugin: document-skills (scope: project)` | `# 2. Install the document skills bundle` → `claude plugin install document-skills@anthropic-agent-skills` → `Successfully installed plugin: document-skills (scope: project)` |
| `# 3. 이 플러그인 안에 무엇이 들었는지 확인` → `claude plugin details document-skills` | `# 3. Check what is inside the plugin` → `claude plugin details document-skills` |
| `Component inventory` / `Skills (4) – docx, pdf, pptx, xlsx` / `Agents (0) · Hooks (0) · MCP servers (0)` | `Component inventory` / `Skills (4) — docx, pdf, pptx, xlsx` / `Agents (0) · Hooks (0) · MCP servers (0)` |
### Slide 121 — 6-8-1. /plugin / Browsing the Marketplace In-Window

| 한국어 | English |
|---|---|
| **6-8-1. /plugin – 창 안에서 마켓플레이스 둘러보기** | **6-8-1. `/plugin` — Browsing the Marketplace Inside the Window** |
| 6-8 는 셸에서 명령으로 설치. 같은 일을 Claude Code 안에서 목록을 보고 골라서도 할 수 있음 | 6-8 installed from the shell. You can do the same thing by picking from a list inside Claude Code |
| `> /plugin` → `Plugins · Discover · Installed · Marketplaces · Errors · Stats` | `> /plugin` → `Plugins · Discover · Installed · Marketplaces · Errors · Stats` |
| `Discover plugins (1/297)` / `Search…` | `Discover plugins (1/297)` / `Search…` |
| `frontend-design · claude-plugins-official · 1.2M installs` – 웹 화면을 만들어 주는 묶음 | `frontend-design · claude-plugins-official · 1.2M installs` — a bundle that builds web screens |
| `superpowers · claude-plugins-official · 1.1M installs` – 브레인스토밍과 서브에이전트 진행 | `superpowers · claude-plugins-official · 1.1M installs` — brainstorming and subagent workflows |
| `code-review · claude-plugins-official · 470.9K installs` – PR 코드 검토 자동화 | `code-review · claude-plugins-official · 470.9K installs` — automated PR code review |
| `context7 · claude-plugins-official · 442K installs` – 최신 문서를 찾아 오는 MCP 서버 | `context7 · claude-plugins-official · 442K installs` — an MCP server that fetches up-to-date documentation |
| `Type to search · Space to toggle · Enter to view · Esc to go back` | `Type to search · Space to toggle · Enter to view · Esc to go back` |
| 셸에서 명령으로 – `claude plugin marketplace add`, `claude plugin install` – 적을 것이 정해져 있을 때. 자료에 적어 두고 그대로 치면 됨 | From the shell — `claude plugin marketplace add`, `claude plugin install`. Best when you already know exactly what to type; write it in the handout and copy it |
| 창 안에서 – `/plugin` – 무엇이 있는지 목록에서 찾을 때 | In the window — `/plugin`. Best when you are looking to see what exists |
| 기록되는 곳 – `.claude/settings.json` – 설치하면 enabledPlugins 에 이름이 들어감 | Where it is recorded — `.claude/settings.json`; installing adds the name to `enabledPlugins` |
| 실습은 6-8 의 셸 명령으로 진행 · Discover 에서 고르고 Enter, Installed 에서 켜고 끔. 297개를 목록으로 훑음 | The exercise uses the shell commands from 6-8. Choose in Discover and press Enter; toggle on and off in Installed. All 297 are browsable as a list |

### Slide 122 — 6-8-2. claude-hud 설치 / Installing claude-hud

| 한국어 | English |
|---|---|
| **6-8-2. claude-hud 설치 – 설치하고 다시 읽기** | **6-8-2. Installing claude-hud — Install, Then Reload** |
| 마켓플레이스 등록은 6-8 과 같은 방식. 다시 읽기까지 마쳐야 setup 명령이 잡힘 | Registering the marketplace works as in 6-8. The `setup` command is only recognized after the reload |
| 1. 마켓플레이스 등록 – `/plugin marketplace add jarrodwatts/claude-hud` | 1. Register the marketplace — `/plugin marketplace add jarrodwatts/claude-hud` |
| 2. 설치 – `/plugin install claude-hud@claude-hud` | 2. Install — `/plugin install claude-hud@claude-hud` |
| 3. 다시 읽기 – `/reload-plugins` | 3. Reload — `/reload-plugins` |
| 4. 설정 – `/claude-hud:setup` | 4. Configure — `/claude-hud:setup` |
| 그대로 쳐도 됨 – 네 줄을 순서대로 입력. 이미 깔렸으면 알려 줌 | Type them as they are, in order. If it is already installed it tells you |
| 순서를 건너뛰면: 설치만 하고 setup 을 부르면 명령이 없다고 나옴 – 다시 읽기를 마친 뒤에 부를 것 | Skip a step and: calling `setup` straight after installing reports that the command does not exist. Call it after the reload |

### Slide 123 — 6-8-3. setup 이 먼저 하는 일 / What setup Does First — Checking the Environment

| 한국어 | English |
|---|---|
| **6-8-3. setup 이 먼저 하는 일 – 환경 확인** | **6-8-3. What `setup` Does First — Checking the Environment** |
| Windows 는 셸이 갈리므로 명령 형식부터 정함 | On Windows the shell varies, so it settles the command format first |
| 환경을 먼저 보는 이유 – PowerShell 구문은 이 환경에서 위험. Git Bash 형식으로 잡음 | Why it checks first — PowerShell syntax is risky here, so it settles on Git Bash form |
| `OSTYPE=cygwin` – Git Bash 로 판정. 명령 형식이 여기서 갈림 | `OSTYPE=cygwin` — identified as Git Bash. The command format is decided here |
| 사람이 할 일 – 없음. 묻지 않고 스스로 판정 | What you have to do — nothing. It works it out without asking |
| 셸을 잘못 잡으면 – 명령이 통째로 실패하거나 statusLine 이 빈 줄로 나옴 | Get the shell wrong and the commands fail outright, or the status line renders as a blank row |

### Slide 124 — 6-8-3-1. 실행 파일과 명령 검증 / Verifying the Runtime and Commands

| 한국어 | English |
|---|---|
| **6-8-3-1. 실행 파일과 명령 검증** | **6-8-3-1. Verifying the Runtime and the Commands** |
| 형식을 정한 뒤 실제로 돌려 보고 결과 확인 | Once the format is settled, it actually runs them and checks the output |
| 검증 항목 – runtime · dist 파일 · statusline 명령 출력 | What it verifies — the runtime, the dist files, and the statusline command's output |
| 설치 확인 – 0.8.0 · 고스트나 임시 파일 없음 · node 있음 | Install check — version 0.8.0, no ghost or temporary files, node present |
| 캐시 경로 – `~/.claude/plugins/cache/claude-hud/` 아래 | Cache path — under `~/.claude/plugins/cache/claude-hud/` |
| 수동 설정 불필요 – 경로와 형식을 스스로 찾아 settings.json 에 넣어 줌 – 사람은 고르기만 하면 됨 | No manual configuration — it finds the paths and format itself and writes them into settings.json. All you do is choose |

### Slide 125 — 6-8-4. 이미 상태 표시줄이 있으면 / If You Already Have a Status Line

| 한국어 | English |
|---|---|
| **6-8-4. 이미 상태 표시줄이 있으면 – 묻고 나서 교체** | **6-8-4. If You Already Have a Status Line — It Asks Before Replacing It** |
| 쓰던 statusLine 을 말없이 덮지 않음 | It does not silently overwrite the statusLine you were using |
| 묻고 나서 교체 – 기존 statusLine 을 그대로 덮지 않음 | It asks before replacing — your existing statusLine is not simply overwritten |
| 고르는 두 갈래 – claude-hud 로 교체 · 현재 것 유지하고 종료 | Two choices — replace it with claude-hud, or keep yours and quit |
| 백업 시점 – 고르기 전에 settings.json 을 먼저 복사해 둠 | Backup timing — settings.json is copied before you choose |
| 쓰던 것이 없으면 – 이 화면 없이 다음 단계로 넘어감 | If you had none, this screen never appears and it moves on |

### Slide 126 — 6-8-4-1. 교체 후 백업 / Two Backups After Replacement

| 한국어 | English |
|---|---|
| **6-8-4-1. 교체 후 – 백업 두 군데** | **6-8-4-1. After Replacement — Two Backups** |
| 되돌릴 수 있게 변경 전 설정과 이전 명령을 따로 남김 | It keeps both the pre-change settings and the previous command so you can revert |
| 변경 전 설정 – `settings.json.bak.날짜` – 전체 백업 | Pre-change settings — `settings.json.bak.<date>`, a full backup |
| 이전 명령 – `previous-statusline.txt` 에 원래 statusline 명령 | The previous command — the original statusline command in `previous-statusline.txt` |
| 복원 방법 – 백업을 settings.json 으로 되돌리면 원래대로 | To restore — put the backup back as settings.json |
| 다른 설정 – permissions · model · theme 는 그대로 두고 statusLine 항목만 교체 | Other settings — permissions, model and theme are left alone; only statusLine is replaced |
| 되돌릴 수 있음 – 두 백업이 남아 있으므로 언제든 원래 상태로 복구 가능 | Reversible — with both backups in place you can return to the original state at any time |

### Slide 127 — 6-8-5. 무엇을 더 보일지 고르기 / Choosing What Else to Display

| 한국어 | English |
|---|---|
| **6-8-5. 무엇을 더 보일지 고르기** | **6-8-5. Choosing What Else to Display** |
| 기본은 두 줄. 나머지는 전부 꺼진 채로 시작하고 필요한 것만 켬 | Two rows by default. Everything else starts off, and you enable only what you need |
| 추가 표시 – 도구 활동 · 에이전트 · 세션 정보 · 세션 이름 | Extra displays — tool activity, agents, session information, session name |
| 자동 새로고침 – 5초 · 1초 · 없음 | Auto-refresh — 5 seconds, 1 second, or off |
| 고른 것을 한 번 더 확인하고 제출 | Confirm your choices once more and submit |
| 수업에서는: 추가 표시는 전부 켜고 새로고침은 5초 – 1초는 HUD 명령을 훨씬 자주 다시 돌림 | For class: turn on all the extra displays and set refresh to 5 seconds — 1 second re-runs the HUD command far more often |

### Slide 128 — 6-8-6. 설정 결과 / The Result — a Status Line Below the Input Box

| 한국어 | English |
|---|---|
| **6-8-6. 설정 결과 – 입력창 아래에 붙은 상태 표시줄** | **6-8-6. The Result — a Status Line Attached Below the Input Box** |
| 강사 PC 에서 설정을 마친 직후 화면. 4분 33초 걸림 | The screen right after setup finished on the instructor's machine. It took 4 minutes 33 seconds |
| 첫줄 – 모델 · 세션 이름 · 누적 시간 | Row 1 — model, session name, elapsed time |
| 둘째 줄 – 컨텍스트 80% · 사용량 10% · 초기화까지 남은 시간 | Row 2 — context 80%, usage 10%, time until reset |
| 셋째 줄 – 읽히는 CLAUDE.md 개수 | Row 3 — how many CLAUDE.md files are being read |
| 넷째·다섯째 줄 – 쓴 도구와 횟수 · 할 일 진행 (6/6) | Rows 4 and 5 — tools used and how often, and to-do progress (6/6) |
| 입력창 아래 다섯 줄이 claude-hud 가 그리는 부분 | The five rows below the input box are what claude-hud draws |
| 안 보이면: Claude Code 를 껐다 켜면 확실히 잡힘. 표시 항목을 다시 고르려면 `/claude-hud:configure` | If you cannot see it, restarting Claude Code reliably fixes it. To change what is shown, run `/claude-hud:configure` |

### Slide 129 — 6-9. 설치한 스킬로 워드 문서 만들기 / Using the Installed Skill to Make a Word Document

| 한국어 | English |
|---|---|
| **6-9. 설치한 스킬로 워드 문서 만들기** | **6-9. Making a Word Document with the Installed Skill** |
| 스킬 이름을 한 글자도 적지 않았는데 워드 문서 생성 스킬이 스스로 붙음 | The Word-document skill attached itself, without a single character of its name being typed |
| `> 문서 폴더에 워드 회의록 양식을 새로 만들어줘. 항목은 일시, 참석자, 안건, 결정사항, 후속조치 다섯 개. 결정사항은 표로 만들되 칸은 비워 둬` | `> Create a new Word minutes template in the docs folder. Five fields: date and time, attendees, agenda, decisions, follow-up actions. Make decisions a table, but leave the cells blank` |
| `✓ 워드 문서 생성 스킬을 사용하겠습니다` | `✓ I will use the Word document creation skill` |
| `● Skill – document-skills:docx` | `● Skill — document-skills:docx` |
| `● Bash – python-docx 로 스크립트 작성 후 실행` | `● Bash — wrote and ran a script using python-docx` |
| `✓ docs/회의록-양식.docx 저장 완료` | `✓ Saved docs/minutes-template.docx` |
| `✓ 용지는 A4 세로, 여백은 상하좌우 2.0 센티미터입니다.` | `✓ Paper is A4 portrait with 2.0 cm margins on all sides.` |
| `✓ 항목 라벨에 연회색 음영을 넣어 입력 칸과 구분하였습니다.` | `✓ Field labels are shaded light grey to distinguish them from the entry cells.` |
| **지시문에 없던 말** | **Words that were not in the instruction** |
| 내가 적지 않은 것 – 스킬, docx, 플러그인 | What I never typed — "skill", "docx", "plugin" |
| 그런데도 붙은 이유 – 요청 문장과 스킬 설명문이 겹침 | Why it attached anyway — the request overlapped the skill's description |
| 실제 동작 – Skill 도구가 문서 스킬을 스스로 선택 | What actually happened — the Skill tool selected the document skill on its own |
| 확인 방법 – 도구 기록에 Skill 이 찍히는지 본다 | How to confirm — look for `Skill` in the tool log |

### Slide 130 — 6-10. 훅 (Hook) / Hooks — Running Your Commands at Set Moments

| 이벤트 / Event | 시점 / When | 예 / Example use |
|---|---|---|
| `SessionStart` | 세션을 열 때 — When a session opens | 남은 할 일 보고 — Report outstanding to-dos |
| `UserPromptSubmit` | 내가 보내기를 누른 뒤 — After you press send | 금지어 걸러내기 · 자료 덧붙이기 — Filter banned words; attach reference material |
| `PreToolUse` | 도구를 쓰기 직전 — Just before a tool runs | 위험한 명령 차단 — Block dangerous commands |
| `PostToolUse` | 도구를 쓴 직후 — Just after a tool runs | 고친 파일에 포매터 실행 — Run a formatter on the edited file |
| `Stop` | 답을 마치려 할 때 — When it tries to finish answering | 할 일이 남으면 종료 차단 — Block the end of the turn if work remains |
| `SubagentStop` | 서브에이전트가 마칠 때 — When a subagent finishes | 위와 같되 하위 작업 단위 — The same, at subtask level |
| `PreCompact` | 대화를 요약하기 직전 — Just before the conversation is compacted | 남길 내용을 파일로 빼 둠 — Write out what should be kept |
| `SessionEnd` | 세션을 닫을 때 — When a session closes | 정리와 기록 — Cleanup and logging |

| 한국어 | English |
|---|---|
| **6-10. 훅 (Hook) – 정해진 시점에 내 명령을 실행** | **6-10. Hooks — Running Your Own Commands at Set Moments** |
| Claude Code 가 특정 시점에 도달하면 등록해 둔 명령을 대신 실행. 주요 이벤트 8종 | When Claude Code reaches a particular moment, it runs the command you registered. Eight main events |
| 그 밖의 이벤트: 전체 이벤트는 30종 이상. PreToolUse · UserPromptSubmit · Stop 은 실행 차단 가능 | Other events: there are more than thirty in total. `PreToolUse`, `UserPromptSubmit` and `Stop` can block execution |

### Slide 131 — 6-10-1. 실습 — todo-guard 설치 / Exercise — Installing todo-guard

| 한국어 | English |
|---|---|
| **6-10-1. 실습 – todo-guard 설치** | **6-10-1. Exercise — Installing todo-guard** |
| 배포 파일 todo-guard.zip – 명령 없이 아래 폴더에 압축을 풀면 설치 완료 | The distributed file is todo-guard.zip — extract it into the folder below and installation is done, with no commands |
| todo-guard.zip 을 풀 위치 – `%USERPROFILE%\.claude\skills\` – 탐색기 주소창에 붙여 넣으면 해당 폴더로 이동 | Where to extract it — `%USERPROFILE%\.claude\skills\`. Paste that into Explorer's address bar to go there |
| 압축 해제 후 구성 – `~/.claude/skills/todo-guard/` : `SKILL.md`, `scripts/check-todo.sh`, `scripts/session-start.sh` | After extraction — `~/.claude/skills/todo-guard/` containing `SKILL.md`, `scripts/check-todo.sh` and `scripts/session-start.sh` |
| 설치 범위 – `~/.claude/skills` 아래 두면 모든 프로젝트에서 사용 가능 | Scope — placed under `~/.claude/skills` it is available in every project |
| 폴더 이름 – todo-guard 로. 이름이 다르면 스킬 인식 실패 | Folder name — it must be `todo-guard`; any other name and the skill is not recognized |
| 실행 권한 – Windows 에서는 chmod 불필요 | Execute permissions — no `chmod` needed on Windows |
| 줄바꿈 형식 – 실행이 실패하면 CRLF 로 풀린 경우. scripts 의 .sh 를 LF 로 변환 | Line endings — if execution fails, it extracted with CRLF. Convert the `.sh` files under `scripts` to LF |
| 설치 후: 스킬 설치만으로는 동작하지 않음. 훅은 프로젝트별로 별도 등록 | After installing: the skill alone does nothing. Hooks must be registered per project |

### Slide 132 — 6-10-2. 실습 — 프로젝트에 훅 등록 / Exercise — Registering Hooks in a Project

| 한국어 | English |
|---|---|
| **6-10-2. 실습 – 프로젝트에 훅 등록** | **6-10-2. Exercise — Registering the Hooks in a Project** |
| 스킬이 TODO.md 와 훅 두 개, settings.json 을 프로젝트 루트에 만들어 줌 | The skill creates TODO.md, two hooks and settings.json at the project root |
| `> 투두가드로 이 프로젝트 세팅해줘` → `✓ TODO.md 와 훅 두 개, settings.json 을 만들었음` | `> Set this project up with todo-guard` → `✓ Created TODO.md, two hooks and settings.json` |
| 스킬이 만들어 주는 것 – `TODO.md` : 할 일 목록. 여기가 기준 | What the skill creates — `TODO.md`, the to-do list, which is the reference point |
| `.claude/hooks/todo-check.sh` – Stop 훅 – 남으면 종료 차단 | `.claude/hooks/todo-check.sh` — the Stop hook; blocks the end of the turn if anything remains |
| `.claude/hooks/todo-session-start.sh` – SessionStart 훅 – 열 때 남은 것을 보고 | `.claude/hooks/todo-session-start.sh` — the SessionStart hook; reports what is outstanding when you open |
| `.claude/settings.json` – 위 두 훅을 등록 | `.claude/settings.json` — registers the two hooks above |
| 만드는 위치 – claude 를 실행한 폴더. 스킬이 프로젝트 루트에 생성 | Where they are created — the folder you ran `claude` in; the skill puts them at the project root |
| 바로 켜지지 않음 – 훅은 세션을 열 때 한 번 읽힘. 새 세션부터 적용 | They do not take effect immediately — hooks are read once when a session opens, so they apply from the next session |
| 동작 확인 – 미완료를 남겨 두고 턴을 끝내 보면 차단되는지 알 수 있음 | To check it works — try ending a turn with an item unfinished and see whether it is blocked |
| 끄고 싶으면 – settings.json 의 hooks 항목을 지우거나 비움 | To turn it off — delete or empty the `hooks` entry in settings.json |
| 확인하는 법 – todo-check.sh 를 직접 실행해 종료 코드 확인. 미완료 없으면 0, 있으면 2 | How to verify — run `todo-check.sh` yourself and check the exit code: 0 if nothing is outstanding, 2 if something is |

### Slide 133 — 체크포인트 / Checkpoint

| 한국어 | English |
|---|---|
| **체크포인트** | **Checkpoint** |
| 1. 플러그인과 스킬의 차이 설명 | 1. Explain the difference between a plugin and a skill |
| 2. 명령어, 스킬, 훅을 호출 주체로 구분 | 2. Distinguish commands, skills and hooks by who invokes them |
| 3. 마켓플레이스에서 스킬 설치 성공 | 3. Successfully install a skill from a marketplace |
| 4. 이름을 부르지 않아도 스킬이 붙는 것 확인 | 4. See a skill engage without being named |

---

## 7장. Git & GitHub / Chapter 7. Git and GitHub

### Slide 134 — Chapter cover

| 한국어 | English |
|---|---|
| **Git 기초 및 GitHub 연결** | **Git Basics and Connecting to GitHub** |
| Git 기본 명령어 + GitHub push 완료 | The basic Git commands, and a successful push to GitHub |
| 학습 내용 | What you will learn |
| 1. `git log` 커밋 확인 | 1. Checking commits with `git log` |
| 2. GitHub push 성공 | 2. Pushing successfully to GitHub |
| 3. AI 작업 전 commit 황금 규칙 | 3. The golden rule — commit before letting the AI work |

### Slide 135 — 7-1. Git 개요 / Git Overview

| 한국어 | English |
|---|---|
| **7-1. Git 개요** | **7-1. Git Overview** |
| 버전 관리 시스템 | A version control system |
| 1. 코드의 변경 이력을 저장하고 관리하는 도구 | 1. A tool that stores and manages the history of changes to your code |
| 2. 언제든 이전 버전으로 돌아갈 수 있음 (롤백) | 2. You can return to an earlier version at any time (rollback) |
| 3. GitHub – Git 저장소를 온라인으로 관리하는 서비스 | 3. GitHub — a service that hosts Git repositories online |
| 4. 바이브코딩에서는 안전망 역할 | 4. In vibe coding it acts as the safety net |

### Slide 136 — 7-2. 바이브코딩에서 Git이 더 중요한 이유 / Why Git Matters More in Vibe Coding

| 항목 / Aspect | 기존 개발에서 Git / Git in conventional development | 바이브코딩에서 Git / Git in vibe coding |
|---|---|---|
| 변경 단위 / Size of a change | 한 번에 5~20줄 정도 손으로 수정 — 5 to 20 lines edited by hand | 한 번 지시에 수백~수천 줄 자동 변경 — Hundreds to thousands of lines changed from one instruction |
| 속도 / Speed | 천천히 – 한 줄씩 생각하며 작성 — Slow; each line thought through | 빠름 – 1분 안에 전체 파일 교체 가능 — Fast; whole files can be replaced inside a minute |
| 실수 범위 / Blast radius of a mistake | 실수해도 한 두 군데, 눈으로 추적 가능 — One or two places, traceable by eye | 여러 파일이 동시에 바뀜, 추적 불가능 — Many files change at once; untraceable |
| 커밋 빈도 / Commit frequency | 기능 단위로 점진적 커밋 — Incremental commits per feature | AI 지시 직전마다 필수 (안전망) — Mandatory before every AI instruction; the safety net |
| 롤백 / Rollback | 필요할 때 가끔 사용 — Occasionally, when needed | 수시로 사용 – AI 결과 마음에 안 들면 즉시 — Constantly; the moment you dislike the AI's output |

| 한국어 | English |
|---|---|
| **7-2. 바이브코딩에서 Git이 더 중요한 이유** | **7-2. Why Git Matters More in Vibe Coding** |
| 기존 코딩과 바이브코딩의 결정적 차이 – Git 없이는 손상된 코드 복구 불가 | The decisive difference from conventional coding — without Git there is no recovering damaged code |
| 결론: AI 지시 전 git commit – commit 한 줄이 손상된 코드의 복구 근거 | The conclusion: commit before you instruct the AI. That one commit is what makes damaged code recoverable |

### Slide 137 — 7-3. Git 핵심 명령어 / The Core Git Commands

| 한국어 | English |
|---|---|
| **7-3. Git 핵심 명령어** | **7-3. The Core Git Commands** |
| Claude Code에게 한국어로 말하면 됨 | You can just say it to Claude Code in plain language |
| 1. `git init` – 저장소 초기화 > claude 에게: "git init 해줘" | 1. `git init` — initialize the repository. To Claude: "Run git init" |
| 2. `git add`, `commit` – 변경 저장 > claude 에게: "지금까지 커밋해줘" | 2. `git add`, `commit` — save the changes. To Claude: "Commit everything so far" |
| 3. `git push` – GitHub에 올리기 > claude 에게: "GitHub에 push 해줘" | 3. `git push` — upload to GitHub. To Claude: "Push it to GitHub" |
| 4. `git log` – 이력 확인 > claude 에게: "버전 리스트 줘" | 4. `git log` — check the history. To Claude: "Show me the list of versions" |
| 5. `git revert` – 롤백 > claude 에게: "이전 버전으로 돌아가줘" | 5. `git revert` — roll back. To Claude: "Go back to the previous version" |

### Slide 138 — 7-4. 황금 규칙 / The Golden Rule — Commit Before the AI Works

| 한국어 | English |
|---|---|
| **7-4. 황금 규칙 – AI 작업 전 commit** | **7-4. The Golden Rule — Commit Before the AI Works** |
| 롤백 포인트를 항상 만들어 두자 | Always leave yourself a rollback point |
| 1. AI에게 지시하기 전 > `git commit` | 1. Before instructing the AI → `git commit` |
| 2. AI 가 코드를 대량 변경한 뒤 > 결과 확인 후 commit | 2. After the AI changes a lot of code → check the result, then commit |
| 3. 문제 발생 시 > `git revert` 또는 `git reset` 으로 복구 | 3. When something goes wrong → recover with `git revert` or `git reset` |
| 4. 이 습관이 바이브코딩의 안전망 | 4. This habit is vibe coding's safety net |

### Slide 139 — 7-5. git init & 첫 커밋 / `git init` and the First Commit

| 한국어 | English |
|---|---|
| **7-5. git init & 첫 커밋 – 두 가지 방법** | **7-5. `git init` and the First Commit — Two Ways** |
| 둘 중 아무거나 써도 결과는 같음. 본 과정은 B 를 권장 · `claude -c` 로 진입한 상태. 한국어 입력 | Either gives the same result; this course recommends B. You are inside via `claude -c`, typing in plain language |
| **방법 A. 파워셸에 직접 입력** | **Method A — typing directly into PowerShell** |
| `# 1. Git 저장소 만들기 (기본 브랜치 main)` → `git init -b main` | `# 1. Create the Git repository (default branch main)` → `git init -b main` |
| `# 2. 이 폴더에만 적용되는 이름·메일` → `git config --local user.name "BulNim"` → `git config --local user.email "me@example.com"` | `# 2. Name and email, applied to this folder only` → `git config --local user.name "BulNim"` → `git config --local user.email "me@example.com"` |
| `# 3. 커밋하고 확인` → `git add .` → `git commit -m "initial commit"` → `git log --oneline` → `a3f9c2b initial commit` | `# 3. Commit and check` → `git add .` → `git commit -m "initial commit"` → `git log --oneline` → `a3f9c2b initial commit` |
| **방법 B. Claude Code 에 한국어로** | **Method B — in plain language to Claude Code** |
| `> git 로컬로 설정해줘. 이름은 BulNim, 메일은 kimkap10@gmail.com. 그리고 커밋해줘.` | `> Set up git locally. Name BulNim, email kimkap10@gmail.com. Then commit.` |
| `● Bash git init -b main` / `● Bash git config --local ×2` / `● Bash git add . / git commit` | `● Bash git init -b main` / `● Bash git config --local ×2` / `● Bash git add . / git commit` |
| `> 커밋 이력 보여줘` → `✓ a3f9c2b initial commit` | `> Show me the commit history` → `✓ a3f9c2b initial commit` |
| 로컬 설정은 이 폴더에만 적용됨. 그 PC 의 다른 저장소는 건드리지 않음. 'git 로컬로 설정해줘' 한 마디면 Claude 가 --local 로 잡아 줌 | The local settings apply to this folder only and touch no other repository on the machine. Saying "set up git locally" is enough for Claude to use `--local` |

### Slide 140 — 7-6. GitHub 저장소 생성 & push / Creating a GitHub Repository and Pushing

| 한국어 | English |
|---|---|
| **7-6. GitHub 저장소 생성 & push – 두 가지 방법** | **7-6. Creating a GitHub Repository and Pushing — Two Ways** |
| GitHub 웹에서 빈 저장소를 먼저 만든 뒤, 내 폴더와 연결 · 이후로는 한 마디로 끝 | Create an empty repository on the GitHub website first, then connect your folder. After that, one sentence does it |
| **방법 A. 파워셸에 직접 입력** | **Method A — typing directly into PowerShell** |
| `# 1. GitHub 웹에서 New repository 로 빈 저장소 생성 (README 체크 해제)` | `# 1. Create an empty repository on GitHub with "New repository" (leave README unchecked)` |
| `# 2. 내 폴더와 GitHub 를 연결` → `git remote add origin https://github.com/BulNim/claude-test.git` | `# 2. Connect your folder to GitHub` → `git remote add origin https://github.com/BulNim/claude-test.git` |
| `# 3. 브랜치를 main 으로 바꾸고 올리기` → `git branch -M main` → `git push -u origin main` → `* [new branch] main -> main` | `# 3. Rename the branch to main and push` → `git branch -M main` → `git push -u origin main` → `* [new branch] main -> main` |
| **방법 B. Claude Code 에 한국어로** | **Method B — in plain language to Claude Code** |
| `> 깃허브 저장소 https://github.com/BulNim/claude-test.git 에 연결해줘. 거부되면 덮어써도 돼.` | `> Connect to the GitHub repository https://github.com/BulNim/claude-test.git. If it is rejected you may overwrite.` |
| `● Bash git remote add origin https://…` / `● Bash git branch -M main` / `● Bash git push -u origin main` / `✓ push 완료. GitHub 에서 확인 가능` | `● Bash git remote add origin https://…` / `● Bash git branch -M main` / `● Bash git push -u origin main` / `✓ Push complete. You can check it on GitHub` |
| `> 지금까지 커밋하고 push 해줘` | `> Commit everything so far and push` |
| 처음 push 할 때 GitHub 로그인 창이 뜸 – 브라우저에서 로그인하면 그 뒤로는 재확인 없음. 원격에 README 커밋이 있으면 rejected (fetch first) 로 거부됨 – --force 로 덮어쓰면 원격 README 는 사라짐 | The first push opens a GitHub sign-in window; sign in through the browser and it will not ask again. If the remote already has a README commit, the push is rejected with "fetch first" — overwrite with `--force` and the remote README is lost |

### Slide 141 — 7-7. .gitignore / Files That Must Not Be Uploaded

| 한국어 | English |
|---|---|
| **7-7. .gitignore – 올리면 안 되는 파일들** | **7-7. `.gitignore` — Files That Must Not Be Uploaded** |
| 보안, 불필요 파일 제외 | Excluding sensitive and unnecessary files |
| 1. `.env` – API Key, DB 비밀번호 등 민감 정보 | 1. `.env` — API keys, database passwords and other sensitive data |
| 2. `node_modules/` – npm 패키지 (용량 큼, 재설치 가능) | 2. `node_modules/` — npm packages; large, and reinstallable |
| 3. `__pycache__/` – Python 캐시 파일 | 3. `__pycache__/` — Python cache files |
| 4. `*.db` – SQLite DB 파일 | 4. `*.db` — SQLite database files |

### Slide 142 — 7-8. .gitignore 생성 & 확인 / Creating and Checking .gitignore

| 한국어 | English |
|---|---|
| **7-8. .gitignore 생성 & 확인 – 두 가지 방법** | **7-8. Creating and Checking `.gitignore` — Two Ways** |
| .env 나 venv 가 GitHub 에 올라가면 보안 사고 – 올리기 전에 막아둘 것 · claude -c 로 들어간 상태에서 · 이미 커밋된 파일이 있으면 이렇게 | A `.env` or `venv` reaching GitHub is a security incident — block it before it goes. You are inside via `claude -c`. If the file is already committed, do this |
| **방법 A. 파워셸에 직접 입력** | **Method A — typing directly into PowerShell** |
| `# 1. .gitignore 만들고 내용 넣기` → `Set-Content .gitignore ".env"` → `Add-Content .gitignore "venv/"` → `Add-Content .gitignore "__pycache__/"` → `Add-Content .gitignore "node_modules/"` | `# 1. Create .gitignore and fill it` → `Set-Content .gitignore ".env"` → `Add-Content .gitignore "venv/"` → `Add-Content .gitignore "__pycache__/"` → `Add-Content .gitignore "node_modules/"` |
| `# 2. 커밋하고 .env 는 추적에서 빼기` → `git add .gitignore` → `git commit -m "chore: .gitignore 추가"` → `git rm --cached .env` | `# 2. Commit, and untrack .env` → `git add .gitignore` → `git commit -m "chore: add .gitignore"` → `git rm --cached .env` |
| **방법 B. Claude Code 에 한국어로** | **Method B — in plain language to Claude Code** |
| `> 실습용으로 .env 파일을 만들어서 API_KEY=dummy 한 줄 넣고 커밋해줘.` | `> For the exercise, create a .env file with the single line API_KEY=dummy and commit it.` |
| `> 앞으로 올리면 안 되는 것들이 안 올라가게 해줘.` → `● Write .gitignore …` | `> Make sure the things that must not be uploaded never get uploaded.` → `● Write .gitignore …` |
| `> 이 키가 저장소 어디에도 남지 않게 해줘.` → `● Bash git rm --cached .env` → `추적 해제 완료` | `> Make sure this key is left nowhere in the repository.` → `● Bash git rm --cached .env` → `Untracked` |
| `> 이 키가 지금도 어딘가에서 되살아날 수 있는지 확인해줘.` → `✓ 최신 커밋에는 없음. 과거 커밋에는 아직 남아 있음` | `> Check whether this key could still resurface anywhere.` → `✓ Not in the latest commit. Still present in earlier commits` |
| 주의: .gitignore 는 아직 커밋 안 된 파일만 막아줌. 이미 커밋된 .env 는 `git rm --cached` 로 따로 빼야 함. API Key 가 한 번이라도 GitHub 에 올라갔다면 그 키는 폐기하고 새로 발급받을 것 | Note: `.gitignore` only blocks files not yet committed. An already-committed `.env` must be removed separately with `git rm --cached`. If an API key ever reached GitHub, revoke it and issue a new one |

### Slide 143 — 7-8-1. 이미 올라간 키는 지워도 남음 / A Key Already Pushed Survives Deletion

| 한국어 | English |
|---|---|
| **7-8-1. 이미 올라간 키는 지워도 남음** | **7-8-1. A Key That Has Already Been Pushed Survives Deletion** |
| 추적에서 빼면 최신 화면에서는 사라짐 – 그러나 과거 커밋에는 그대로 있고, 공개 저장소면 누구나 열람 | Untracking it removes it from the latest view — but it remains in earlier commits, and in a public repository anyone can read it |
| 최신 화면 – .env 없음 (안심하기 쉬운 지점) | The latest view — no `.env`, which is exactly where people relax too soon |
| 과거 커밋 – API_KEY 가 그대로 보임 | An earlier commit — the API_KEY is right there |
| 막아 주는 것 – .gitignore 는 아직 커밋 안 된 파일만 막음 | What it protects against — `.gitignore` only blocks files not yet committed |
| 못 막는 것 – 이미 커밋된 것은 추적만 풀릴 뿐 이력에 남음 | What it cannot — anything already committed is merely untracked; it stays in the history |
| 확인 착시 – 최신 기준으로 물으면 「안 올라감」 이라는 답이 나옴 | The illusion of a clean check — ask about the current state and the answer is "it was never uploaded" |
| 해야 할 일 – 그 키는 폐기하고 새로 발급 – 되돌리기보다 빠름 | What to do — revoke the key and issue a new one; faster than trying to undo it |
| 기준: 한 번이라도 올라간 키는 이미 유출된 것으로 본다. 이력 정리보다 폐기와 재발급이 확실하고 빠름. 위 화면은 실제 실습 저장소에서 그대로 열리는 주소 – 공개 저장소라 로그인 없이도 보임 | The rule: treat any key that was ever pushed as already leaked. Revoking and reissuing is surer and faster than cleaning history. The screens above open at a real practice repository — public, so visible without signing in |

### Slide 144 — 7-9. 브랜치 전략 / Branching Strategy

| 한국어 | English |
|---|---|
| **7-9. 브랜치 전략** | **7-9. Branching Strategy** |
| 본 과정은 main 브랜치만 사용 | This course uses the `main` branch only |
| 1. `main` – 메인 브랜치 (배포 브랜치, 실무) | 1. `main` — the main branch (the deployment branch, in professional use) |
| 2. `dev` – 개발 브랜치 (실무에서 사용) | 2. `dev` — the development branch (used professionally) |
| 3. `feature/기능명` – 기능별 브랜치 (팀 개발) | 3. `feature/<name>` — one branch per feature (team development) |
| 4. 본 과정 – main 브랜치만 사용 (구성 단순화) | 4. This course — `main` only, to keep things simple |
### Slide 145 — 7-10. 전체 환경 최종 확인 / Final Environment Check

| 한국어 | English |
|---|---|
| **7-10. 전체 환경 최종 확인 – 두 가지 방법** | **7-10. A Final Check of the Whole Environment — Two Ways** |
| 다음 장으로 넘어가기 전 설치·설정을 한 번에 점검 · claude -c 로 들어간 상태에서 한 마디로 · 뭔가 빠졌으면 이렇게 | Check every install and setting in one pass before moving on. One sentence, from inside via `claude -c`. If something is missing, do this |
| **방법 A. 파워셸에 직접 입력** | **Method A — typing directly into PowerShell** |
| `# 1. 설치 확인` → `node --version` → `v24.15.0` | `# 1. Check the installs` → `node --version` → `v24.15.0` |
| `git --version` → `git version 2.51.0.windows.1` | `git --version` → `git version 2.51.0.windows.1` |
| `python --version` → `Python 3.11.9` | `python --version` → `Python 3.11.9` |
| `claude --version` → `2.1.222 (Claude Code)` | `claude --version` → `2.1.222 (Claude Code)` |
| `# 2. Git 상태와 GitHub 연결 확인` → `git log --oneline` → `a3f9c2b initial commit` → `git remote -v` | `# 2. Check Git status and the GitHub connection` → `git log --oneline` → `a3f9c2b initial commit` → `git remote -v` |
| **방법 B. Claude Code 에 한국어로** | **Method B — in plain language to Claude Code** |
| `> 지금 이 환경 점검해줘. 버전 표로 보여주고 실제로 올릴 수 있는 상태인지도 확인해줘.` | `> Check this environment. Show me the versions as a table, and confirm whether it can actually push.` |
| `● Bash node --version – v24.15.0` / `● Bash git --version – 2.51.0` / `● Bash python --version – 3.11.9` / `● Bash claude --version – 2.1.222` | `● Bash node --version — v24.15.0` / `● Bash git --version — 2.51.0` / `● Bash python --version — 3.11.9` / `● Bash claude --version — 2.1.222` |
| `● Bash git log – 커밋 1건 확인` / `● Bash git remote -v – origin 연결됨` / `✓ 전부 정상. 다음 장 진행 가능` | `● Bash git log — one commit confirmed` / `● Bash git remote -v — origin connected` / `✓ All good. You can move on to the next chapter` |
| `> 빠진 게 있으면 설치 방법, 없으면 없다고 알려줘` | `> If anything is missing, tell me how to install it; if nothing is, say so.` |
| 확인 항목: node v24 이상 / git 2.40 이상 / python 3.11 이상 / claude 2.1 이상, 커밋 1건 이상, origin 연결됨. claude 최신 여부는 `claude update` 로 따로 확인. 하나라도 안 되면 다음 장에서 반드시 막히므로 여기서 해결하고 넘어갈 것 | What to check: node v24+, git 2.40+, python 3.11+, claude 2.1+, at least one commit, origin connected. Check separately with `claude update` whether Claude is current. Any one of these failing will stop you in the next chapter, so fix it here |

### Slide 146 — 체크포인트 / Checkpoint

| 한국어 | English |
|---|---|
| **체크포인트** | **Checkpoint** |
| 1. `git log` 커밋 확인 | 1. Confirm the commit with `git log` |
| 2. GitHub push 성공 | 2. Push to GitHub successfully |
| 3. `.gitignore` 에 `.env` 포함 | 3. `.gitignore` includes `.env` |
| 4. Claude Code로 Git 명령 실행 | 4. Run Git commands through Claude Code |

---

## 8장. 심플 바이브 실습 / Chapter 8. Simple Vibe Practice

### Slide 147 — Chapter cover

| 한국어 | English |
|---|---|
| **심플 바이브 실습 – 한계 직접 체감** | **Simple Vibe Practice — Feeling the Limits First-Hand** |
| 설계 문서 없이 프롬프트 한 개로 앱 생성 + 한계 분석 | Build an app from one prompt with no design documents, then analyze the limits |
| 학습 내용 | What you will learn |
| 1. 새 폴더 taskflow-simple 에서 시작 | 1. Starting in a new folder, `taskflow-simple` |
| 2. 앱 생성 & 실제 동작 확인 | 2. Generating the app and confirming it actually works |
| 3. 한계 4가지 직접 발견 | 3. Discovering four limits for yourself |

### Slide 148 — 실습 3단계 / Three Stages, by How Much Is Specified Up Front

| 단계 / Stage | 사전 정보 / What is given up front | 폴더 / Folder | 결과 / Result |
|---|---|---|---|
| 1단계 (8장) / Stage 1 (Ch. 8) | 사전 정보 없음 – 지시 한 줄 — Nothing; a one-line instruction | `taskflow-simple` | 스택·DB·폴더를 AI 가 임의 결정. 실행할 때마다 결과 상이 – 재현 불가 — The AI picks the stack, database and folders. Different every run; not reproducible |
| 2단계 (9-1) / Stage 2 (9-1) | CLAUDE.md 1종 – 역할·스택·절대규칙 — One CLAUDE.md: role, stack, hard rules | `taskflow-pro` | 스택과 폴더 구조 고정. docs 는 이름만 예약 – 내용 미작성 — Stack and folder structure fixed; the docs are reserved by name only, not yet written |
| 3단계 (9-2 ~ 11장) / Stage 3 (9-2 to Ch. 11) | docs 6종 – WHY·WHAT·HOW·순서·규약 — Six docs: why, what, how, order, conventions | `taskflow-pro` | 기능·순서·검증까지 고정. 실행자가 달라도 동일 결과 – 재현 확보 — Features, order and verification are all fixed. The same result whoever runs it; reproducibility achieved |

| 한국어 | English |
|---|---|
| **실습 3단계 – 사전 정보량에 따른 결과 차이** | **Three Stages of the Exercise — How the Result Changes with How Much Is Given** |
| 8장부터 11장까지 동일한 앱을 3회 제작. 사전 제공 정보의 양만 달리함 | The same app is built three times across Chapters 8 to 11. Only the amount of information given beforehand changes |
| claude-test 는 도구 학습용 연습 폴더로 앱 제작 없음. 앱 제작은 8장부터 두 폴더에서 진행 | `claude-test` was a practice folder for learning the tool; no app is built there. App building starts in Chapter 8, across two folders |

### Slide 149 — 8-1. 심플 바이브의 정의 / What Simple Vibe Means

| 한국어 | English |
|---|---|
| **8-1. 심플 바이브의 정의** | **8-1. What "Simple Vibe" Means** |
| 설계 문서 없이 프롬프트 한 개로 앱을 만들어 보는 방식 | Building an app from a single prompt, with no design documents |
| 1. 설계 문서 미작성 – CLAUDE.md 와 docs/ 없이 시작 | 1. No design documents — you start without CLAUDE.md or `docs/` |
| 2. DB · 로그인 · 폴더 구조 미지정 – AI 임의 결정 | 2. Database, login and folder structure unspecified — the AI decides |
| 3. 코드를 직접 작성하지 않음 | 3. You write no code yourself |
| 4. 위 한계가 다음 장 (9장 CLAUDE.md + docs) 의 필요성으로 이어짐 | 4. These limits are exactly what motivates the next chapter (CLAUDE.md + docs) |

### Slide 150 — 시작 전 준비 / Before You Start — Use a New Empty Folder

| 한국어 | English |
|---|---|
| **시작 전 준비 – 새 빈 폴더에서 진행** | **Before You Start — Work in a New Empty Folder** |
| 아래 4개 항목을 순서대로 확인. 여기서 어긋나면 이후 실습 전체에 영향 | Check these four in order. Get this wrong and every later exercise is affected |
| `# 1. 5장 claude-test 가 아닌 새 폴더를 만든다` → `D:` → `mkdir taskflow-simple` → `cd taskflow-simple` | `# 1. Create a new folder — not Chapter 5's claude-test` → `D:` → `mkdir taskflow-simple` → `cd taskflow-simple` |
| `# 2. 새 대화로 연다 (이어가기 -c 를 쓰지 않는다)` → `claude` | `# 2. Open a new conversation (do not use -c to continue)` → `claude` |
| Claude Code 안에서 – `> /model sonnet` · `> /effort low` | Inside Claude Code — `> /model sonnet` and `> /effort low` |
| 지금 있어야 할 폴더 – `D:\taskflow-simple` | The folder you should be in — `D:\taskflow-simple` |
| 맞는지 확인하는 법 – Claude Code 화면 맨 위에 이 경로가 찍혀 있으면 정상 | How to confirm — that path printed at the top of the Claude Code screen |
| 주의: CLAUDE.md 도 docs 도 없는 상태여야 함. 기존 폴더에서 하면 앞 실습의 문서가 읽혀 결과가 달라짐 | Note: there must be no CLAUDE.md and no docs. Work in an existing folder and the earlier exercise's documents get read, changing the result |

### Slide 151 — 8-2. 새 빈 폴더에서 Claude Code 실행 / Running Claude Code in a New Empty Folder

| 한국어 | English |
|---|---|
| **8-2. 새 빈 폴더에서 Claude Code 실행** | **8-2. Running Claude Code in a New Empty Folder** |
| 5장 폴더를 쓰면 CLAUDE.md 때문에 결과가 달라짐 – 반드시 새 폴더에서 시작 | Using the Chapter 5 folder changes the result because of its CLAUDE.md — always start in a new folder |
| `# 1. 5장 claude-test 가 아닌 새 빈 폴더를 만든다` → `cd ..` → `mkdir taskflow-simple` → `cd taskflow-simple` | `# 1. Create a new empty folder — not Chapter 5's claude-test` → `cd ..` → `mkdir taskflow-simple` → `cd taskflow-simple` |
| `# 2. Claude Code 실행` → `claude` → `Claude Code v2.1 · D:\taskflow-simple` | `# 2. Run Claude Code` → `claude` → `Claude Code v2.1 · D:\taskflow-simple` |
| 왜 새 폴더? – claude-test 에는 5장에서 만든 CLAUDE.md 가 있어 결과가 달라짐 – 전역 설정(~/.claude/CLAUDE.md)에 스택이 적혀 있어도 마찬가지 | Why a new folder? — `claude-test` holds the CLAUDE.md from Chapter 5, which changes the result. The same applies if a stack is written in your global `~/.claude/CLAUDE.md` |
| 심플 바이브 – 스택 지정 없이 자연어 한 문장으로 요청 | Simple vibe — one sentence of natural language, with no stack specified |
| Claude의 선택 – 매번 다른 스택을 고를 수 있음 (Flask/Express/Next.js 등) | Claude's choice — it may pick a different stack each time (Flask, Express, Next.js and so on) |
| 왜 이렇게? – 의도적으로 – 수강생이 한계를 직접 체감하게 하기 위함 | Why do it this way? — deliberately, so you feel the limits for yourself |

### Slide 152 — 8-3. Claude가 만든 결과 관찰 / Observing What Claude Produced

| 한국어 | English |
|---|---|
| **8-3. Claude가 만든 결과 관찰** | **8-3. Observing What Claude Produced** |
| 어떤 파일을 생성했는지 + 어떤 스택을 선택했는지 확인 (매번 다를 수 있음) | Check which files it created and which stack it chose — it may differ every time |
| `> /model sonnet` / `> /effort low` | `> /model sonnet` / `> /effort low` |
| `> 업무 관리 앱 만들어줘. 업무 추가, 삭제, 상태 변경 기능이 있어야 해.` | `> Build me a task management app. It needs to add tasks, delete them and change their status.` |
| `● Write server.js` / `● Write public/index.html` / `● Write public/app.js` / `● Write public/styles.css` / `● Write data/tasks.json` | `● Write server.js` / `● Write public/index.html` / `● Write public/app.js` / `● Write public/styles.css` / `● Write data/tasks.json` |
| `✓ 백엔드는 Node.js, 프론트는 순수 HTML/CSS/JS, 데이터는 JSON 파일로 잡았습니다` | `✓ I went with Node.js on the backend, plain HTML/CSS/JS on the front, and a JSON file for data` |
| `> !dir` → `✓ server.js · public/ · data/ · .claude/` | `> !dir` → `✓ server.js · public/ · data/ · .claude/` |
| 기술 스택 – Claude가 골랐음 – Node.js + 순수 HTML/CSS/JS | The stack — Claude chose it: Node.js plus plain HTML/CSS/JS |
| DB 없음 – JSON 파일 저장 – 동시 접속, 검색 등 한계 | No database — stored in a JSON file, with limits on concurrency, search and the rest |
| 디자인 시스템 없음 – 디자인 완성도는 양호하나 디자인 시스템 부재 | No design system — the visual result is decent, but there is no system behind it |
| 매번 달라짐 – 실습 시 Flask/Express 등 다른 스택일 수 있음 | Different every time — in your run it may be Flask, Express or something else |

### Slide 153 — 8-4. 앱 실행 & 브라우저에서 직접 사용 / Running the App and Using It in a Browser

| 한국어 | English |
|---|---|
| **8-4. 앱 실행 & 브라우저에서 직접 사용** | **8-4. Running the App and Using It in the Browser** |
| 실제로 동작하는지 확인 + 한계 직접 체감 (포트 번호는 매번 다를 수 있음) | Confirm it actually works and feel the limits (the port number may differ each time) |
| `> 방금 만든 앱을 실제로 실행하고 접속 주소를 알려줘.` | `> Actually run the app you just built and tell me the address.` |
| `● Bash npm install` / `● Bash node server.js` / `✓ Server running on http://localhost:8000` | `● Bash npm install` / `● Bash node server.js` / `✓ Server running on http://localhost:8000` |
| `> 추가, 상태 변경, 삭제 세 가지 되는지 확인하고 결과 보여줘. 끝나면 서버 종료해줘.` | `> Check that adding, changing status and deleting all work, and show me the results. Shut the server down when you are done.` |
| `● Bash curl -s http://localhost:8000/api/tasks` / `✓ 추가 · 상태 변경 · 삭제 세 가지 모두 정상 동작했습니다` / `✓ 서버를 종료했습니다` | `● Bash curl -s http://localhost:8000/api/tasks` / `✓ Add, change status and delete all worked correctly` / `✓ Server shut down` |
| 앱 실행 – Claude 가 `node server.js` 자동 실행 | Running the app — Claude runs `node server.js` itself |
| 테스트 방법 – 브라우저로 localhost:8000 접속 후 직접 클릭 | How to test — open localhost:8000 in a browser and click through it yourself |
| 종료 확인까지 – 한 번에 안 꺼질 수 있음. 주소가 열리면 다시 끄라고 할 것 | Confirm it shut down — it may not stop the first time. If the address still loads, tell it to stop again |
| 발전 포인트 – 디자인 시스템 / DB / 로그인 / 라우터 체계 | Where it could improve — a design system, a database, login, a routing scheme |
| 왜 중요? – 위 한계를 알아야 9장 CLAUDE.md 의 필요성 이해 | Why it matters — you have to see these limits to understand why Chapter 9's CLAUDE.md is needed |

### Slide 154 — 8-5. 실제 실습 결과 / The Actual Result — Screen and Folder Structure

| 한국어 | English |
|---|---|
| **8-5. 실제 실습 결과 – 화면 & 폴더 구조** | **8-5. The Actual Result — the Screen and the Folder Structure** |
| 실제 강사 실습 결과 – Claude가 만든 Taskflow 앱과 폴더 구조 확인 | The instructor's real run — the Taskflow app Claude built, and its folder structure |
| 브라우저 화면 – localhost:8000 | The browser — localhost:8000 |
| `D:\taskflow-simple\` / `├── .claude\ └── settings.local.json` / `├── data\ └── tasks.json` ← 저장소 (JSON 파일) | `D:\taskflow-simple\` / `├── .claude\ └── settings.local.json` / `├── data\ └── tasks.json` ← the store (a JSON file) |
| `├── public\` ← 프런트엔드 / `│ ├── app.js` / `│ ├── index.html` / `│ └── styles.css` | `├── public\` ← the frontend / `│ ├── app.js` / `│ ├── index.html` / `│ └── styles.css` |
| `└── server.js` ← 백엔드 (Node) | `└── server.js` ← the backend (Node) |
| `# CLAUDE.md 없음, docs/ 없음, 테스트 없음` | `# No CLAUDE.md, no docs/, no tests` |
| `# 의존성 0개 – 순수 Node + JSON 파일` | `# Zero dependencies — plain Node and a JSON file` |

### Slide 155 — 8-6. 심플 바이브 결과물 분석 / Analyzing the Simple Vibe Output

| 좋은 점 / What is good | 한계 / The limits |
|---|---|
| 자연어로 앱 생성 – 코딩 지식 없어도 시작 가능 — An app from natural language; you can start with no coding knowledge | 디자인 시스템 부족 – UI 완성도는 양호하나 Tailwind 등 미적용 — No design system; the UI is decent but nothing like Tailwind is applied |
| 코드 직접 작성 없음 – Claude가 전부 작성 — You write no code; Claude writes it all | DB 없음 – JSON 파일 저장, 동시 접속·검색 한계 — No database; a JSON file, limited on concurrency and search |
| 속도 우위 – 10분 안에 동작하는 앱 — Speed; a working app inside ten minutes | 로그인 없음 – 누구나 접근, 보안 없음 — No login; anyone can get in, no security |
| 반복 지시 가능 – "이것도 추가해줘" 한 마디면 OK — Iterative instruction; "add this too" is enough | 구조 단순 – 분리는 됐지만 라우터, 체계 없음 — Simplistic structure; separated, but with no router and no scheme |

| 한국어 | English |
|---|---|
| **8-6. 심플 바이브 결과물 분석** | **8-6. Analyzing What Simple Vibe Produced** |
| 장점과 한계가 함께 확인됨 – 다음 단계로 진행 | Both the strengths and the limits are visible — on to the next stage |
| 결론: 심플 바이브는 "프로토타입" 수준 – 실제 서비스는 9장 CLAUDE.md 부터 | The conclusion: simple vibe gets you to prototype level. A real service starts with Chapter 9's CLAUDE.md |

### Slide 156 — 8-7. 발전 포인트의 원인 / The Cause — Not Enough Context for the AI

| 한국어 | English |
|---|---|
| **8-7. 발전 포인트의 원인 – AI에게 컨텍스트 부족** | **8-7. What Caused It — the AI Did Not Have Enough Context** |
| 왜 이런 결과가 나왔을까? | Why did it turn out this way? |
| 1. DB를 미지시 > AI가 JSON 파일로 결정 (동시 접속·검색 한계) | 1. You never specified a database → the AI settled on a JSON file, with its concurrency and search limits |
| 2. 인증을 미지시 > 로그인 없이 누구나 접근 가능 | 2. You never specified authentication → no login, open to anyone |
| 3. 폴더 구조를 미지시 > 체계적 구성 없이 AI 임의 배치 | 3. You never specified a folder structure → the AI laid it out however it liked |
| 4. 테스트, 코딩 규칙, 금지사항 미지시 > 다음 장 CLAUDE.md + docs 에서 해결 | 4. No tests, coding rules or prohibitions were specified → solved in the next chapter with CLAUDE.md + docs |

### Slide 157 — 8-8. 근본 문제 / The Root Problem — No Reproducibility

| 한국어 | English |
|---|---|
| **8-8. simple vibe 의 근본 문제 – 재현성 없음** | **8-8. The Root Problem with Simple Vibe — No Reproducibility** |
| 스택을 지시하지 않으면 이런 결과 – 스택 고정이 필요한 이유 (강사 시연) | This is what happens when you do not specify the stack — why pinning it matters (instructor demo) |
| 스택 미지정 지시: "업무 관리 앱 만들어줘" | Instruction with no stack: "Build me a task management app" |
| 1차 시도 – 스택: Node.js + Express · DB: JSON 파일 저장 · UI: Bootstrap UI | Attempt 1 — Stack: Node.js + Express · DB: JSON file · UI: Bootstrap |
| 2차 시도 – 스택: Flask + Python · DB: SQLite DB · UI: Tailwind 일부 | Attempt 2 — Stack: Flask + Python · DB: SQLite · UI: partly Tailwind |
| 3차 시도 – 스택: Django + Python · DB: PostgreSQL · UI: Vue.js 프론트 | Attempt 3 — Stack: Django + Python · DB: PostgreSQL · UI: a Vue.js frontend |
| > 매번 다른 결과 | > A different result every time |
| 재현성 없음 = 협업 불가 = 시니어 검토 통과 불가 | No reproducibility means no collaboration, which means it never passes senior review |
| – 같은 요구사항을 다시 입력해도 다른 구조, 팀원 간 결과 공유 불가 | – The same requirement produces a different structure; results cannot be shared between team members |
| – 코드 리뷰 무의미, 6개월 뒤 유지보수 불가, 일관성 없는 코드와 구조 | – Code review is meaningless, maintenance six months on is impossible, and the code and structure are inconsistent |
| > 9장 docs 체계화의 핵심 가치 = 재현성 확보 | > The core value of Chapter 9's document system is exactly this: reproducibility |

### Slide 158 — 8-9. git commit & GitHub push / Saving the Result, All Through Vibe Coding

| 한국어 | English |
|---|---|
| **8-9. git commit & GitHub push – 실습 결과 저장 (전부 바이브로)** | **8-9. `git commit` and Pushing to GitHub — Saving the Result, All Through Vibe Coding** |
| 직접 명령을 치지 않고 Claude Code 안에서 한국어로만 진행 | No commands typed by hand — everything in plain language inside Claude Code |
| `> git 로컬로 설정해줘. 이름은 BulNim, 메일은 kimkap10@gmail.com. .gitignore 만들고 simple vibe done 으로 커밋해줘. 깃허브 저장소 https://github.com/BulNim/taskflow-simple.git 에 연결해줘.` | `> Set up git locally. Name BulNim, email kimkap10@gmail.com. Create a .gitignore and commit with the message "simple vibe done". Connect it to the GitHub repository https://github.com/BulNim/taskflow-simple.git` |
| `● Write .gitignore` / `✓ node_modules/ · *.log · data/ 를 넣었습니다` | `● Write .gitignore` / `✓ I added node_modules/, *.log and data/` |
| `● Bash git init -b main / git config --local ×2` / `● Bash git add . / git commit -m "simple vibe done"` / `● Bash git remote add origin / git push -u origin main …` | `● Bash git init -b main / git config --local ×2` / `● Bash git add . / git commit -m "simple vibe done"` / `● Bash git remote add origin / git push -u origin main …` |
| `> 커밋 이력 보여줘` → `a3f9c2b simple vibe done` | `> Show me the commit history` → `a3f9c2b simple vibe done` |
| `> 이 앱 설명서를 README.md 로 만들어서 올려줘.` → `● Write README.md` → `✓ 앱 소개 · 스택 · 설치 · 실행 · 기능 · 폴더 구조를 담았습니다` | `> Write a guide for this app as README.md and push it.` → `● Write README.md` → `✓ It covers the app, the stack, installation, running it, its features and the folder structure` |
| 왜 올리나? – 심플 바이브 결과를 9장 taskflow-pro 와 나란히 두고 비교하기 위한 기록 | Why push it? — as a record, so the simple-vibe result can sit next to Chapter 9's `taskflow-pro` for comparison |
| 전부 한국어로 – git 명령 암기 불필요 – 목적만 전달 | All in plain language — no Git commands to memorize; you convey the goal |
| 로컬 설정 – 이 폴더에만 적용됨. PC 전체 설정은 건드리지 않음 | Local settings — apply to this folder only; your machine-wide configuration is untouched |
| 다음 단계 – 9장 CLAUDE.md – 같은 앱을 설계 기반으로 재구성 | Next — Chapter 9's CLAUDE.md, rebuilding the same app on a designed foundation |

### Slide 159 — 8-10. GitHub 에 올라간 모습 / How It Looks on GitHub

| 한국어 | English |
|---|---|
| **8-10. GitHub 에 올라간 모습 – 코드 + README** | **8-10. How It Looks on GitHub — Code plus README** |
| [8-9] 커밋·push·README 완료 후 taskflow-simple 저장소 첫 화면 | The `taskflow-simple` repository's front page after the commit, push and README in 8-9 |
| 올라간 것 – 코드 · .gitignore · README.md | What was pushed — the code, `.gitignore` and `README.md` |
| 커밋 – simple vibe done > docs: add README | Commits — "simple vibe done", then "docs: add README" |
| README – 앱 설명 · 스택 · 설치 · 실행 · API · 폴더 구조 | README — the app, the stack, installation, running it, the API and the folder structure |
| 확인 – 저장소 첫 화면에 설명서가 렌더됨 | Check — the guide renders on the repository's front page |
| 다음 – 9장 taskflow-pro 와 나란히 두고 비교 | Next — set it beside Chapter 9's `taskflow-pro` and compare |

### Slide 160 — 체크포인트 / Checkpoint

| 한국어 | English |
|---|---|
| **체크포인트** | **Checkpoint** |
| 1. 앱 브라우저 실행 & 직접 테스트 | 1. Run the app in a browser and test it yourself |
| 2. 한계 4가지 직접 발견 | 2. Discover four limits for yourself |
| 3. 한계 원인 파악 | 3. Understand what caused them |
| 4. git commit + GitHub push 완료 | 4. Commit and push to GitHub |

---

## 9장. CLAUDE.md + docs 체계화 / Chapter 9. Systematizing CLAUDE.md and docs

### Slide 161 — Chapter cover

| 한국어 | English |
|---|---|
| **8장 simple vibe 한계 극복 – 스펙 작성 + 코드 생성 체계화** | **Overcoming Chapter 8's Limits — Writing Specs and Systematizing Code Generation** |
| docs 를 만드는 단계라 지시가 길다 – 여기 적은 내용이 그대로 docs 가 됨 | This is the stage where the docs get written, so the instructions are long — what you write here becomes the docs verbatim |
| 학습 내용 | What you will learn |
| 1. 새 폴더 taskflow-pro 에서 CLAUDE.md 부터 작성 | 1. Starting a new folder, `taskflow-pro`, with CLAUDE.md first |
| 2. 나의 구체 지시 > AI 작성 | 2. Your specific instruction, then the AI writes |
| 3. CLAUDE.md + docs/ 6종 완성 | 3. Completing CLAUDE.md plus the six documents |

### Slide 162 — 시작 전 / Before You Start — Another New Empty Folder

| 한국어 | English |
|---|---|
| **시작 전 – 지금 칠 것 (또 다른 새 빈 폴더)** | **Before You Start — What to Type Now (Another New Empty Folder)** |
| 아래 4개 항목을 순서대로 확인. 여기서 어긋나면 이후 실습 전체에 영향 | Check these four in order. Get this wrong and every later exercise is affected |
| `# 1. 8장 taskflow-simple 이 아닌 새 폴더를 만든다` → `cd ..` → `mkdir taskflow-pro` → `cd taskflow-pro` | `# 1. Create a new folder — not Chapter 8's taskflow-simple` → `cd ..` → `mkdir taskflow-pro` → `cd taskflow-pro` |
| `# 2. 새 대화로 연다` → `claude` | `# 2. Open a new conversation` → `claude` |
| 지금 있어야 할 폴더 – `D:\taskflow-pro` · 맞는지 확인하는 법 – Claude Code 화면 맨 위에 이 경로가 찍혀 있으면 정상 | The folder you should be in — `D:\taskflow-pro`. How to confirm — that path printed at the top of the Claude Code screen |
| 주의: 8장 폴더에서 이어서 하면 심플 바이브 결과와 섞임. 9장부터 11장까지 이 폴더 하나로 끝까지 | Note: continuing in the Chapter 8 folder mixes in the simple-vibe result. Chapters 9 to 11 all run in this one folder |

### Slide 163 — 프롬프트는 타이핑 금지 / Do Not Type the Prompts — Copy and Paste

| 번호 / No. | 무엇을 만드나 / What it creates | 어떤 내용이 들어가나 / What goes in it | 줄수 / Lines |
|---|---|---|---|
| 01 | `CLAUDE.md` | 역할, 기술 스택 고정, docs 6개 파일명, 절대규칙 6개 — Role, fixed stack, the six doc filenames, six hard rules | 17 |
| 02 | `docs/` + `00-overview` | 6개 파일 생성, 매핑표, 읽는 순서 00 > 05 — Create the six files, a mapping table, reading order 00 to 05 | 12 |
| 03 | `01-product.md` WHY | 목표, 페르소나, MVP 범위, 범위 외, 성공 기준 — Goals, personas, MVP scope, out of scope, success criteria | 18 |
| 04 | `02-specs.md` WHAT | Task 필드 7개, REST API 5개(/api/), 화면 4종 — Seven Task fields, five REST APIs under /api/, four screens | 21 |
| 05 | `03-design.md` HOW | 기술 결정 8개 표 + 대안·근거·트레이드오프 — A table of eight technical decisions with alternatives, rationale and trade-offs | 15 |
| 06 | `04-tasks.md` | Phase 1/2/3 체크리스트, 단계마다 검증 방법 — Phase 1/2/3 checklists, with a verification method per step | 12 |
| 07 | `05-conventions.md` | 명명 규칙, 금지 5개, 구현 규칙 4개 + git 첫 커밋 — Naming rules, five prohibitions, four implementation rules, and the first git commit | 23 |

| 한국어 | English |
|---|---|
| **프롬프트는 타이핑 금지 – 복사해서 붙여넣기** | **Do Not Type the Prompts — Copy and Paste Them** |
| 이 장의 프롬프트는 12~32줄 – 손으로 치면 오타가 나고 결과가 달라짐. 9장은 문서만 만드는 장 | This chapter's prompts run 12 to 32 lines — typing them by hand introduces typos and changes the result. Chapter 9 creates documents only |
| 배포 파일 열기 – VS Code 로 열고 Ctrl+Shift+V 로 미리보기 · 코드블록 우측 상단 복사 버튼 클릭 · `프롬프트_모음_기초편.md` | Open the handout — open it in VS Code, preview with Ctrl+Shift+V, and click the copy button at the top right of each code block. The file is `프롬프트_모음_기초편.md` (Prompt Collection, Foundations) |
| 9장에서 만드는 것 – 위 7개 문서뿐. 앱 코드 미작성. 앱 제작은 10·11장에서 진행 | What Chapter 9 creates — only those seven documents. No app code; the app is built in Chapters 10 and 11 |
| 왜 앱을 시키나 – 9-1-1 은 실험. 8장과 똑같은 한 줄을 다시 쳐 봄. CLAUDE.md 한 장으로 뭐가 달라지는지 보려는 것 | Why ask for an app at all — 9-1-1 is an experiment: type Chapter 8's exact line again and see what one CLAUDE.md changes |
| 결과 – 시작조차 못 함. 스택은 고정됐지만 무엇을 만들지가 없어 멈추고 되물음. docs 6종이 필요한 이유 | The result — it cannot even start. The stack is fixed, but with nothing saying *what* to build it stops and asks back. Which is why the six docs are needed |
| 실무에서는 AI 와 상의해 채움 – 원래는 대화하며 docs 를 만들어 감. 여기서 다 적어 주는 것은 수강생 전원이 같은 결과를 얻게 하려는 것 | In real work you fill these in by talking with the AI — the docs normally emerge through conversation. They are written out here so every student gets the same result |

### Slide 164 — 9-1. CLAUDE.md 작성 지시 (1/2) / Instructions for Writing CLAUDE.md (1 of 2)

| 한국어 | English |
|---|---|
| **9-1. 시작 & CLAUDE.md 작성 지시 (1/2)** | **9-1. Getting Started and Instructing CLAUDE.md (1 of 2)** |
| CLAUDE.md 한 장만 만드는 단계 – docs 6개는 이름만 예약, 파일은 9-2 에서 생성 | This stage creates CLAUDE.md alone — the six docs are reserved by name; the files come in 9-2 |
| `> 현재 폴더에서 풀스택 웹 앱을 본격 구조로 만든다. CLAUDE.md부터 작성해. 아래 4개 섹션 그대로:` | `> In this folder we are building a full-stack web app with a proper structure. Start by writing CLAUDE.md, with exactly these four sections:` |
| `1) 너의 역할: 10년차 시니어 풀스택, 유지보수 우선, 한국어 응답, 식별자는 영어` | `1) Your role: a senior full-stack developer of ten years, maintainability first, replies in Korean, identifiers in English` |
| `2) 기술 스택 (고정 – 임의 변경 금지):` | `2) Tech stack (fixed — do not change it):` |
| `- 백엔드 backend/ : FastAPI + Python 3.11 이상 + SQLite` | `- Backend, backend/: FastAPI + Python 3.11 or later + SQLite` |
| `- 프론트 frontend/ : Vanilla JS + Tailwind CDN, index.html 과 app.js 2개 파일만` | `- Frontend, frontend/: Vanilla JS + Tailwind CDN, two files only — index.html and app.js` |
| `- 모든 API 경로는 /api/ 접두사, 테스트는 pytest` | `- Every API path is prefixed /api/; tests use pytest` |
| `3) 작업 시작 전 절차: docs/ 아래 6개 파일을 이 이름·이 순서로 읽기` — `00-overview.md 01-product.md 02-specs.md 03-design.md 04-tasks.md 05-conventions.md` `(이 6개는 지금 만들지 않는다. 이름만 기록)` | `3) Before starting work: read the six files under docs/ by these names, in this order` — `00-overview.md 01-product.md 02-specs.md 03-design.md 04-tasks.md 05-conventions.md` `(Do not create these six now. Record the names only.)` |
| `4) 절대규칙 6개: 추측 금지 / 돌발 의존성 금지 / 테스트 없이 완료 금지 / 시크릿 하드코딩 금지 / 폴더 구조 임의 변경 금지 /` | `4) Six hard rules: no guessing / no surprise dependencies / no declaring completion without tests / no hard-coded secrets / no changing the folder structure /` |
| **CLAUDE.md 발췌** – `## 1. 너의 역할` · `- 10년차 시니어 풀스택 / 유지보수 우선` · `- 한국어 응답 / 식별자는 영어` | **From the resulting CLAUDE.md** — `## 1. Your role` · `- Senior full-stack, ten years / maintainability first` · `- Replies in Korean / identifiers in English` |
| `## 3. 절대 규칙` · `1. 추측 금지 – docs에 없으면 묻는다` · `2. 돌발 의존성 추가 금지` · `3. 테스트 없이 완료 선언 금지` | `## 3. Hard rules` · `1. No guessing — if it is not in the docs, ask` · `2. No adding dependencies out of the blue` · `3. Never declare something done without tests` |

### Slide 165 — 9-1. CLAUDE.md 작성 지시 (2/2) / Instructions for Writing CLAUDE.md (2 of 2)

| 한국어 | English |
|---|---|
| **9-1. 시작 & CLAUDE.md 작성 지시 (2/2)** | **9-1. Getting Started and Instructing CLAUDE.md (2 of 2)** |
| `> docs 와 어긋나는 지시를 받으면 구현 전에 문서명과 조항을 들어 되물을 것. 이번 단계에서는 CLAUDE.md 한 개만 만든다.` | `> If you are given an instruction that conflicts with the docs, ask back before implementing, citing the document and the clause. At this stage, create CLAUDE.md only.` |
| `✓ 작성 중... 완료. CLAUDE.md에 4개 섹션 그대로 반영했습니다.` / `✓ 다음 지시 부탁드립니다.` | `✓ Writing… done. All four sections are reflected in CLAUDE.md as specified.` / `✓ Ready for your next instruction.` |
| **CLAUDE.md 발췌** – `4. 시크릿 하드코딩 금지` · `5. 폴더 구조 임의 변경 금지` · `6. docs 위반 금지 – 어긋나면 구현 전에 되묻는다` | **From the resulting CLAUDE.md** — `4. No hard-coded secrets` · `5. Do not change the folder structure` · `6. Do not violate the docs — if something conflicts, ask before implementing` |

### Slide 166 — 9-1-1. CLAUDE.md 만 있을 때 / With Only CLAUDE.md — the Same Instruction Again

| 한국어 | English |
|---|---|
| **9-1-1. CLAUDE.md 만 있을 때 – 같은 지시를 다시** | **9-1-1. With Only CLAUDE.md — Giving the Same Instruction Again** |
| 8장과 똑같은 한 줄을 다시 입력. 무엇이 고정되고 무엇이 아직 갈리는지 확인 | Type Chapter 8's exact line again, and see what is now fixed and what still varies |
| `> 업무 관리 앱 만들어줘. 업무 추가, 삭제, 상태 변경 기능이 있어야 해.` | `> Build me a task management app. It needs to add tasks, delete them and change their status.` |
| `✓ CLAUDE.md 를 읽었습니다. 기술 스택 고정 항목을 따릅니다.` | `✓ I have read CLAUDE.md and will follow the fixed stack.` |
| `● Write backend/main.py – FastAPI + SQLite` / `● Write frontend/index.html – Vanilla JS + Tailwind CDN` | `● Write backend/main.py — FastAPI + SQLite` / `● Write frontend/index.html — Vanilla JS + Tailwind CDN` |
| `✓ 스택과 폴더 구조는 CLAUDE.md 대로 고정했습니다.` / `✓ 다만 어떤 필드를 둘지, 어떤 순서로 만들지는 문서에 없어 임의 판단했습니다.` | `✓ The stack and folder structure are fixed per CLAUDE.md.` / `✓ But which fields to include and in what order to build were not in the documents, so I decided on my own.` |
| **고정된 것 – CLAUDE.md 효과**: 스택 FastAPI + Vanilla JS · 폴더 backend/ frontend/ · 주석 한국어, 식별자 영어 · 경로 /api/ 접두사 | **What is now fixed — the effect of CLAUDE.md**: stack, FastAPI + Vanilla JS · folders, backend/ and frontend/ · comments in Korean, identifiers in English · paths prefixed /api/ |
| **아직 갈리는 것**: 필드 – 제목만? 마감일도? · 상태값 2단계? 3단계? · 순서 – 백엔드 먼저? 화면 먼저? · 범위 – 로그인은 포함? 제외? · 검증 – 어디까지 하면 끝인가 | **What still varies**: fields — title only, or a due date too? · status — two states or three? · order — backend first or the screen first? · scope — is login in or out? · verification — how far is far enough to call it done? |
| **결론**: 스택은 고정, 내용은 미고정 > docs 6종이 필요한 이유 | **The conclusion**: the stack is fixed, the content is not — which is why the six documents are needed |

### Slide 167 — CLAUDE.md 한 장의 한계와 docs 6종 / The Limits of One CLAUDE.md, and the Six Documents

| 파일 / File | 역할 / Role | 심화편 OpenSpec 대응 / OpenSpec equivalent (Advanced) |
|---|---|---|
| `CLAUDE.md` | 진입점, 역할, 라우팅 — Entry point, role, routing | (전역 컨텍스트) — (global context) |
| `docs/00-overview.md` | 읽는 순서, 전체 그림 — Reading order, the whole picture | (목차) — (table of contents) |
| `docs/01-product.md` | WHY – 목표, 페르소나, 범위 — Why: goals, personas, scope | > `proposal.md` |
| `docs/02-specs.md` | WHAT – 기능, API, 모델 — What: features, APIs, models | > `specs/` |
| `docs/03-design.md` | HOW – 기술, 아키텍처 — How: technology, architecture | > `design.md` |
| `docs/04-tasks.md` | 구현 순서, 체크리스트 — Implementation order, checklists | > `tasks.md` |
| `docs/05-conventions.md` | 코딩규칙, 금지, 테스트 — Coding rules, prohibitions, tests | (전역 규약) — (global conventions) |

| 한국어 | English |
|---|---|
| **CLAUDE.md 한 장의 한계와 docs 6종** | **The Limits of a Single CLAUDE.md, and the Six Documents** |
| 시니어 검토를 통과하는 협업 가능 프로젝트의 조건 – 그리고 그것을 파일로 나눈 결과 | What a collaborative project needs to pass senior review — and what that looks like split into files |
| **CLAUDE.md 한 장만 – 9-1 단계** | **CLAUDE.md alone — the 9-1 stage** |
| ✗ 페르소나·스택·규칙·기능이 한 곳에 뒤섞임 | ✗ Personas, stack, rules and features all tangled in one place |
| ✗ 변경 시 어디를 봐야 할지 불분명 | ✗ When something changes, it is unclear where to look |
| ✗ 범위 외 누락 – AI 임의 결정 | ✗ Nothing says what is out of scope, so the AI decides |
| ✗ 트레이드오프 근거 없음 – 시니어 신뢰 0 | ✗ No rationale for trade-offs — zero credibility with a senior |
| ✗ 의존성 추가 정책 없음 – 라이브러리 난립 | ✗ No policy on adding dependencies — libraries proliferate |
| **CLAUDE.md + docs/ – 9-2 이후** | **CLAUDE.md + docs/ — from 9-2 on** |
| ○ 관심사 분리 – WHY / WHAT / HOW / 순서 / 규약 | ○ Separation of concerns — why / what / how / order / conventions |
| ○ 변경 시 해당 docs 만 갱신 | ○ A change means updating just the relevant document |
| ○ 범위 외 명시 – AI 가 추측하지 않음 | ○ Out-of-scope is stated, so the AI does not guess |
| ○ 대안·근거·트레이드오프를 표로 기록 | ○ Alternatives, rationale and trade-offs recorded in a table |
| ○ 의존성 추가 정책 명문화 | ○ The dependency policy is written down |
| 기초편에서 손으로 정리한 docs 를 심화편 OpenSpec 이 명령 한 줄로 자동 생성 | The docs you assemble by hand in the Foundations course are generated automatically by one OpenSpec command in the Advanced course |

### Slide 168 — 9-2. docs/ 6개 파일 & 00-overview / Creating the Six docs Files and 00-overview

| 한국어 | English |
|---|---|
| **9-2. docs/ 6개 폴더 & 00-overview 작성 지시** | **9-2. Instructing the Six `docs/` Files and 00-overview** |
| 내가 6개 파일 이름과 항목까지 모두 지정 | You specify all six filenames and their contents yourself |
| `> docs/ 폴더에 아래 6개 파일을 이 이름 그대로 만든다. 다른 파일은 추가하지 말 것:` | `> Create these six files in a docs/ folder, under exactly these names. Add no other files:` |
| `00-overview.md 01-product.md 02-specs.md 03-design.md 04-tasks.md 05-conventions.md` | `00-overview.md 01-product.md 02-specs.md 03-design.md 04-tasks.md 05-conventions.md` |
| `내용은 00-overview.md 에만 채운다. 나머지 5개는 빈 파일로만 만든다.` | `Fill in 00-overview.md only. Create the other five as empty files.` |
| `그리고 CLAUDE.md 에 적힌 docs 파일명·순서가 방금 만든 6개와 같은지 확인하고, 다르면 CLAUDE.md 를 이 6개 이름으로 고쳐라.` | `Then check that the doc filenames and order written in CLAUDE.md match the six you just made, and if they differ, correct CLAUDE.md to these six names.` |
| `00-overview.md 내용:` `- 프로젝트 한 줄: TaskFlow Pro – 팀 업무 관리 풀스택 웹 앱` `- 6개 파일 매핑표 (파일명 / 역할 / 알 수 있는 것)` `- 읽는 순서: 00 > 01 > 02 > 03 > 04 > 05` `- 왜 이렇게 나누는가 – 관심사 분리 원칙으로 설명` | `Contents of 00-overview.md:` `- One line on the project: TaskFlow Pro — a full-stack web app for team task management` `- A mapping table of the six files (filename / role / what it tells you)` `- Reading order: 00 > 01 > 02 > 03 > 04 > 05` `- Why it is split this way — explained through separation of concerns` |
| `✓ 00-overview.md 작성 완료. 네 항목 모두 반영.` / `✓ CLAUDE.md 의 파일명·순서도 방금 만든 6개와 같습니다.` / `✓ 다음 01-product.md 지시 부탁드립니다.` | `✓ 00-overview.md written, with all four items reflected.` / `✓ The filenames and order in CLAUDE.md match the six just created.` / `✓ Ready for your instructions on 01-product.md.` |
| **docs/00-overview.md 발췌** – `# 00 – Overview` · `TaskFlow Pro – 팀 업무 관리 풀스택 웹 앱` | **From the resulting docs/00-overview.md** — `# 00 — Overview` · `TaskFlow Pro — a full-stack web app for team task management` |
| `## 의존 방향 (위 > 아래로만)` · `product > specs > design > tasks > conventions` · `(왜) (무엇) (어떻게) (언제) (규율)` | `## Direction of dependency (downward only)` · `product > specs > design > tasks > conventions` · `(why) (what) (how) (when) (discipline)` |
| `상위 결정이 하위의 입력이 됨. 역방향 영향 금지 – 컨벤션 때문에 제품 방향 바뀌는 일 없어야 함` | `Decisions upstream become inputs downstream. No reverse influence — a convention must never change the product direction` |
| `## 읽는 순서` · `00 > 01 > 02 > 03 > 04 > 05` | `## Reading order` · `00 > 01 > 02 > 03 > 04 > 05` |
### Slide 169 — 9-3. 01-product.md — WHY (1/2)

| 한국어 | English |
|---|---|
| **9-3. 01-product.md 작성 지시 – WHY (1/2)** | **9-3. Instructing 01-product.md — WHY (1 of 2)** |
| 내가 목표, 페르소나, 범위, 범위외를 모두 지정 | You specify the goal, the persona, the scope and what is out of scope |
| `> docs/01-product.md 만 작성해. 다른 docs 파일은 건드리지 말 것. 다음 내용으로:` | `> Write docs/01-product.md only. Do not touch the other docs. With this content:` |
| `- 목표: 팀 업무 시각화. '지금 누가 뭐 해?'가 사라지게` | `- Goal: make team work visible, so that "who's doing what right now?" stops being asked` |
| `- 페르소나: 10명 규모 스타트업 팀리더 (30~40대)` | `- Persona: a team lead at a ten-person startup, in their thirties or forties` |
| `- MVP 범위: CRUD 4종 모두 화면에서 – 추가/목록/수정/삭제` | `- MVP scope: all four CRUD operations on screen — create, list, update, delete` |
| `- 상태 분류 + 마감 시각 (due_at) 지정, 표시. 날짜만이 아니라 시간까지 (예: 2026-12-31 18:00)` | `- Status classification plus a due time (`due_at`), set and displayed — not just a date but a time (e.g. 2026-12-31 18:00)` |
| `- 라이트/다크 테마 토글 (localStorage)` / `- 모바일 반응형 (360px)` | `- Light/dark theme toggle (localStorage)` / `- Mobile responsive at 360px` |
| `- UI 톤: Mac OS 스타일. 둥근 모서리, 부드러운 그림자, 반투명 카드, 시스템 폰트` | `- UI tone: macOS style — rounded corners, soft shadows, translucent cards, system fonts` |
| `- 확장: JWT 로그인, 팀, Kanban, 채팅, CI/CD` | `- Future extensions: JWT login, teams, Kanban, chat, CI/CD` |
| `- 범위 외: 외부결제, 네이티브앱, WebRTC, 외부캘린더, 파일업로드` | `- Out of scope: external payments, native apps, WebRTC, external calendars, file uploads` |
| **발췌** `## MVP 범위 (모두 화면에서 동작)` – `[O] CRUD 4종 – 추가 / 목록 / 수정 / 삭제` · `[O] 상태 todo / in_progress / done` · `[O] 마감 시각 (due_at) 날짜 + 시간` · `[O] 라이트 / 다크 테마 토글 / 360px 반응형` · `[O] UI 톤 – Mac OS 스타일` | **Excerpt** `## MVP scope (all working on screen)` — `[✓] Four CRUD operations — create, list, update, delete` · `[✓] Status: todo / in_progress / done` · `[✓] Due time (due_at), date plus time` · `[✓] Light/dark toggle, responsive at 360px` · `[✓] UI tone — macOS style` |
| `## 성공 기준 (MVP 완료 조건)` – `[O] 새로고침 데이터 유지 / 360px 안 깨짐` · `[O] API p95 ≤ 200ms / CRUD 4종 화면 동작` · `[O] 테마 토글 + localStorage 유지` | `## Success criteria (definition of MVP done)` — `[✓] Data survives a refresh; nothing breaks at 360px` · `[✓] API p95 ≤ 200 ms; all four CRUD operations work on screen` · `[✓] Theme toggle persists via localStorage` |
| `WebSocket – MVP는 폴링. 확장 단계 보류` | `WebSocket — the MVP polls; deferred to the extension phase` |

### Slide 170 — 9-3. 01-product.md — WHY (2/2)

| 한국어 | English |
|---|---|
| **9-3. 01-product.md 작성 지시 – WHY (2/2)** | **9-3. Instructing 01-product.md — WHY (2 of 2)** |
| `> - 성공 기준 (실습에서 눈으로 확인 가능한 것만): 새로고침해도 데이터 유지 / 360px 에서 안 깨짐 / CRUD 4종 화면 동작 / 테마 토글 작동` | `> - Success criteria (only things you can see in the exercise): data survives a refresh / nothing breaks at 360px / all four CRUD operations work on screen / the theme toggle works` |
| `✓ 01-product.md 작성 완료.` / `✓ 목표, 페르소나, 범위, UI 톤, 테마, 범위 외, 성공 기준 모두 반영.` | `✓ 01-product.md written.` / `✓ Goal, persona, scope, UI tone, theming, out-of-scope and success criteria all reflected.` |
| **발췌 – 범위 외** `## 범위 외 (절대 금지)` – 외부 결제 / 네이티브 앱 / WebRTC / 외부 캘린더 / 파일 업로드 · WebSocket – MVP는 폴링. 확장 단계 보류 | **Excerpt — out of scope** `## Out of scope (strictly forbidden)` — external payments / native apps / WebRTC / external calendars / file uploads · WebSocket — the MVP polls; deferred to the extension phase |

### Slide 171 — 9-4. 02-specs.md — WHAT (1/2)

| 한국어 | English |
|---|---|
| **9-4. 02-specs.md 작성 지시 – WHAT (1/2)** | **9-4. Instructing 02-specs.md — WHAT (1 of 2)** |
| 내가 데이터 모델 필드와 5개 API를 모두 명시 | You spell out the data model's fields and all five APIs |
| `> 02-specs.md 작성해. 다음 내용으로 고정:` | `> Write 02-specs.md, fixed to this content:` |
| `- Task 모델 필드 7개 (이 순서, 타입까지 그대로):` | `- Seven Task model fields, in this order and with these types:` |
| `id (INTEGER, PK, AUTOINCREMENT)` / `title (VARCHAR 200, 필수)` / `description (TEXT, 선택)` | `id (INTEGER, PK, AUTOINCREMENT)` / `title (VARCHAR 200, required)` / `description (TEXT, optional)` |
| `status (todo/in_progress/done, 기본값 todo)` / `due_at (DATETIME UTC, 선택)` / `created_at, updated_at (DATETIME, 서버 자동)` | `status (todo/in_progress/done, default todo)` / `due_at (DATETIME UTC, optional)` / `created_at, updated_at (DATETIME, set by the server)` |
| `- 검증: title/status/due_at 형식 위반 > 400 / 없는 id > 404` | `- Validation: a malformed title, status or due_at → 400; a missing id → 404` |
| `스펙에 없는 필드가 오면 422 로 거부 – 조용히 무시 금지` | `Reject fields not in the spec with 422 — never silently ignore them` |
| `due_at 은 UTC 로 저장하고 화면에서 로컬로 변환` / `응답의 날짜 세 필드는 UTC ISO 8601 로 통일` | `Store due_at in UTC and convert to local time on screen` / `All three date fields in responses use UTC ISO 8601` |
| `- REST API 5개, 경로는 /api/ 접두사 필수: POST 201 / GET 목록 200 / GET 단건 200 / PUT 200 / DELETE 204` | `- Five REST APIs, all prefixed /api/: POST 201 / GET list 200 / GET single 200 / PUT 200 / DELETE 204` |
| **발췌** `## Task 모델 필드` – `id / title* / description / status / due_at (DATETIME UTC, 선택) / created_at / updated_at` · `* = 필수` | **Excerpt** `## Task model fields` — `id / title* / description / status / due_at (DATETIME UTC, optional) / created_at / updated_at` · `* = required` |
| `## REST API 5개` – `POST /api/tasks > 201` · `GET /api/tasks > 200 (목록)` · `GET /api/tasks/{id} > 200 (단건)` · `PUT /api/tasks/{id} > 200` · `DELETE /api/tasks/{id} > 204` | `## Five REST APIs` — `POST /api/tasks → 201` · `GET /api/tasks → 200 (list)` · `GET /api/tasks/{id} → 200 (single)` · `PUT /api/tasks/{id} → 200` · `DELETE /api/tasks/{id} → 204` |

### Slide 172 — 9-4. 02-specs.md — WHAT (2/2)

| 한국어 | English |
|---|---|
| **9-4. 02-specs.md 작성 지시 – WHAT (2/2)** | **9-4. Instructing 02-specs.md — WHAT (2 of 2)** |
| `> 목록엔 description 제외, 단건은 포함` | `> Exclude description from the list response; include it in the single-item response` |
| `- 화면 명세 (화면별 표 1개씩 총 4개):` | `- Screen specifications (one table per screen, four in all):` |
| `추가 – 폼 (title / due_at / status)` | `Create — a form (title / due_at / status)` |
| `목록 – 카드 (status 배지 + 마감까지 남은 시간)` | `List — cards (a status badge plus time remaining until due)` |
| `수정 – 카드 클릭 > 모달 (전 필드 수정 가능)` | `Update — click a card to open a modal where every field is editable` |
| `삭제 – 휴지통 > 확인 > DELETE` | `Delete — trash icon, confirm, then DELETE` |
| `✓ 02-specs.md 작성 완료.` / `● Task 모델 + due_at + 검증 + REST 5개 + 화면 명세 반영.` | `✓ 02-specs.md written.` / `● The Task model, due_at, validation, the five REST endpoints and the screen specs are all reflected.` |
| **발췌** `추가 – 폼 (title / due_at / status)` · `due_at – datetime-local picker` · `목록 – 카드 (status 배지 + D-N HH:MM)` · `수정 – 카드 클릭 > 모달 (전 필드)` · `삭제 – 휴지통 아이콘 > 확인 > DELETE` · `에러: 400 (검증) / 404 (id 없음)` | **Excerpt** `Create — a form (title / due_at / status)` · `due_at — a datetime-local picker` · `List — cards (status badge plus D-N HH:MM)` · `Update — click a card, then a modal with every field` · `Delete — trash icon, confirm, then DELETE` · `Errors: 400 (validation) / 404 (no such id)` |

### Slide 173 — 9-5. 03-design.md — HOW (1/2)

| 한국어 | English |
|---|---|
| **9-5. 03-design.md 작성 지시 – HOW (1/2)** | **9-5. Instructing 03-design.md — HOW (1 of 2)** |
| 내가 8개 기술, 디자인 결정과 트레이드오프 표 형식을 지정 | You specify eight technical and design decisions, and the format of the trade-off table |
| `> 03-design.md 작성해. 표 1개(8행)로 정리. 열은 선택 / 대안 / 근거 / 트레이드오프 4개 고정. 아래 8개 항목을 이 번호·이 이름 그대로:` | `> Write 03-design.md as a single eight-row table. Four fixed columns: choice / alternatives / rationale / trade-offs. These eight items, with these numbers and names:` |
| `1) 백엔드 – FastAPI / 대안 Django, Express` | `1) Backend — FastAPI / alternatives: Django, Express` |
| `2) 프론트 – Vanilla JS + Tailwind CDN / 대안 React, Vue` — `프론트는 백엔드가 같은 오리진에서 제공. file:// 로 직접 열지 않음` | `2) Frontend — Vanilla JS + Tailwind CDN / alternatives: React, Vue` — `the frontend is served by the backend from the same origin; never opened directly via file://` |
| `3) DB – SQLite (SQLAlchemy ORM, 추후 PostgreSQL 전환 고려) / 대안 PostgreSQL 즉시 도입` | `3) Database — SQLite (SQLAlchemy ORM, with a later move to PostgreSQL in mind) / alternative: adopt PostgreSQL immediately` |
| `4) CSS – Tailwind만. styled-components 금지` | `4) CSS — Tailwind only. styled-components forbidden` |
| `5) 실시간 – MVP 는 폴링 3초. WebSocket 은 확장 단계 보류` | `5) Realtime — the MVP polls every 3 seconds; WebSocket deferred to the extension phase` |
| `6) 상태관리 – 모듈 변수 + DOM 직접 갱신` | `6) State management — module variables and direct DOM updates` |
| `7) 디자인 시스템 – Mac OS UI 톤 / 대안 Material, Ant` | `7) Design system — macOS UI tone / alternatives: Material, Ant` |
| `8) 테마 – 라이트/다크 토글, localStorage, 초기값은 시스템 설정` | `8) Theming — light/dark toggle, localStorage, initial value from the system setting` |
| `마지막에 의존성 추가 정책: 이 문서에 사유를 적기 전에는 도입 불가.` | `End with a dependency policy: nothing may be adopted before its rationale is written into this document.` |
| **발췌** `## 디자인 토큰 (Mac OS 톤)` – `모서리 – rounded-xl (12px) / 2xl` · `그림자 – shadow-lg / shadow-xl` · `카드 – backdrop-blur + 반투명 배경` · `라이트 bg-white/70` · `다크 bg-zinc-900/70` · `폰트 – -apple-system, BlinkMacSystemFont, …` · `간격 – 4px grid / 터치 타깃 ≥ 44px` | **Excerpt** `## Design tokens (macOS tone)` — `Corners — rounded-xl (12px) / 2xl` · `Shadows — shadow-lg / shadow-xl` · `Cards — backdrop-blur over a translucent background` · `Light: bg-white/70` · `Dark: bg-zinc-900/70` · `Fonts — -apple-system, BlinkMacSystemFont, …` · `Spacing — a 4px grid; touch targets ≥ 44px` |
| `## 테마 토글` – `dark: 변형 + localStorage('theme')` · `초기값 – prefers-color-scheme 감지` | `## Theme toggle` — `the dark: variant plus localStorage('theme')` · `initial value from prefers-color-scheme` |
| `## 절대 금지 사항` – `[X] styled-components / CSS-in-JS` · `[X] Redux / Zustand / Recoil` | `## Absolutely forbidden` — `[✗] styled-components / CSS-in-JS` · `[✗] Redux / Zustand / Recoil` |

### Slide 174 — 9-5. 03-design.md — HOW (2/2)

| 한국어 | English |
|---|---|
| **9-5. 03-design.md 작성 지시 – HOW (2/2)** | **9-5. Instructing 03-design.md — HOW (2 of 2)** |
| `> 사전 승인 목록에 httpx 를 적을 것 (테스트 구동에 필요).` | `> Add httpx to the pre-approved list (needed to run the tests).` |
| `✓ 03-design.md 작성 완료. 8개 결정 트레이드오프 표 + 디자인 토큰, 테마 토글 명세 + 의존성 정책 반영.` | `✓ 03-design.md written — the eight-decision trade-off table, the design tokens, the theme-toggle spec and the dependency policy are all reflected.` |
| **발췌** `## 의존성 도입 이력 – (아직 없음)` | **Excerpt** `## Dependency adoption log — (none yet)` |

### Slide 175 — 9-5-1. Vanilla JS 를 택하는 이유 / Why Vanilla JS — a Reaction to JavaScript Fatigue

| 한국어 | English |
|---|---|
| **9-5-1. Vanilla JS 를 택하는 이유 – JavaScript Fatigue 반작용** | **9-5-1. Why Choose Vanilla JS — the Backlash Against JavaScript Fatigue** |
| 수년간 프레임워크 무성장 > 개발자 피로 누적 > 브라우저 표준 회귀 흐름 | Years of framework proliferation, then accumulated developer fatigue, then a return to browser standards |
| **2010~2022, 프레임워크 무성장** | **2010–2022, framework proliferation** |
| React / Vue / Angular – SPA 시대. 컴포넌트 + JSX 표준화, 프론트가 '앱'이 됨 | React, Vue, Angular — the SPA era. Components and JSX became standard, and the frontend became an "app" |
| 프레임워크 위에 프레임워크 – Next.js, Nuxt, Remix, SSR/SSG/RSC 매년 새 패러다임 | Frameworks on top of frameworks — Next.js, Nuxt, Remix; SSR, SSG, RSC, a new paradigm every year |
| 빌드, 상태관리 라이브러리 경쟁 – Webpack > Vite > Turbopack, Redux > Zustand > Jotai… | Competing build and state libraries — Webpack to Vite to Turbopack; Redux to Zustand to Jotai… |
| 결과 – 학습 6개월~1년, Bundle 80KB+. JavaScript Fatigue 라는 용어 자체가 생김 | The result — six months to a year to learn, bundles over 80 KB, and the very term "JavaScript fatigue" |
| **2023~, 브라우저 표준 회귀** | **2023 onward, a return to browser standards** |
| Web Components 표준 안정화 – 브라우저 내장 컴포넌트, GitHub 등 대형 사이트 채택 | Web Components stabilized — components built into the browser, adopted by large sites including GitHub |
| HTMX 급성장 (GitHub 50k+ stars) – HTML 속성만으로 SPA 인터랙션, 업무앱 다수 채택 | HTMX grew fast (50k+ GitHub stars) — SPA-grade interaction from HTML attributes alone, widely adopted in business apps |
| Hotwire / Alpine.js + Tailwind – DHH 'No-JS framework' 표방, 랜딩페이지 사실상 표준 | Hotwire / Alpine.js + Tailwind — DHH's "no-JS framework" stance; effectively the standard for landing pages |
| 결과 – Less is More, 본질로 회귀. 시니어들이 환영, AI 시대와 시너지 강함 | The result — less is more, a return to fundamentals. Welcomed by senior engineers, and a strong fit with the AI era |

### Slide 176 — 9-5-2. 실제 업체 사례 / Real Companies Leading the Shift

| 한국어 | English |
|---|---|
| **9-5-2. 실제 업체 사례 – 대형 사이트의 선행 전환** | **9-5-2. Real Company Cases — Large Sites Leading the Shift** |
| 기술 결정은 트위터가 아니라 프로덕션에서 – 대형 업체들이 SPA 떼고 표준 회귀 중 | Technical decisions are settled in production, not on Twitter — large companies are stripping SPAs back toward standards |
| **GitHub (2023~)** – React 일부 제거 – 점진적 회귀. PR 페이지, Issues 등 일부에서 React 제거. Server-rendered HTML + Web Components 조합으로 전환. "Web Components 채택으로 Time-to-Interactive 압도적 단축" | **GitHub (2023–)** — partially removing React, a gradual retreat. React removed from parts of the PR and Issues pages, moving to server-rendered HTML plus Web Components. "Adopting Web Components cut time-to-interactive dramatically" |
| **Shopify (Hydrogen > 단순화)** – Remix 채택 > 다시 단순화 흐름. 한때 React 기반 Hydrogen 적극 푸시. 프로덕션 운영 부담 증가 > 점진적 단순화로 방향 조정. "대형 트래픽일수록 프레임워크 추상화가 부담" | **Shopify (Hydrogen, then simplification)** — adopted Remix, then moved back toward simplicity. It once pushed the React-based Hydrogen hard; operational burden in production grew, and the direction shifted to gradual simplification. "The more traffic you have, the more framework abstraction costs you" |
| **DHH (Rails / 37signals)** – "We're abandoning TypeScript" 선언 (2023). Basecamp / HEY 운영사 창업자가 TypeScript 제거. Hotwire 발표 – 'No-JS framework' 라는 도발적 표방. "JS 안 쓰고도 SPA 수준 인터랙션을 만들 수 있다" | **DHH (Rails / 37signals)** — declared "We're abandoning TypeScript" in 2023. The founder of the company behind Basecamp and HEY removed TypeScript and released Hotwire under the deliberately provocative banner of a "no-JS framework": "you can build SPA-grade interaction without JavaScript" |
| **HTMX – GitHub 50k+ stars** – "JS 없이 HTML 속성만으로 SPA". hx-get, hx-post 같은 HTML 속성만으로 SPA 인터랙션. NASA / Walmart / 다수 업무앱이 도입. "Vanilla 회귀의 상징 도구 – 관련 채용 공고 증가" | **HTMX — 50k+ GitHub stars** — "an SPA from HTML attributes alone, no JS". Attributes like `hx-get` and `hx-post` give SPA-grade interaction. Adopted by NASA, Walmart and many business apps. "The emblem of the return to vanilla — and job postings mentioning it are rising" |
| 공통: '본질로 돌아가자', 프레임워크 추상화 비용보다 브라우저 표준의 안정성을 택함 | The common thread: back to fundamentals — choosing the stability of browser standards over the cost of framework abstraction |

### Slide 177 — 9-5-3. AI 시대에 Vanilla 를 택하는 이유 / Why Vanilla in the AI Era

| 한국어 | English |
|---|---|
| **9-5-3. AI 시대에 Vanilla 를 택하는 이유** | **9-5-3. Why Choose Vanilla in the AI Era** |
| AI 가 코드 작성 > 사람은 결과를 읽고 검증해야 함, 가시성이 곧 경쟁력 | The AI writes the code; the human has to read and verify the result — and legibility is the competitive edge |
| **성능 비교, 실측 데이터** | **Measured performance** |
| Next.js 빈 페이지 – ~80KB+ JS | An empty Next.js page — 80 KB+ of JS |
| Vanilla + Tailwind CDN – ~30KB CSS | Vanilla + Tailwind CDN — around 30 KB of CSS |
| JS Bundle – 0 (서버 없음) | JS bundle — zero (no build server) |
| TTI (Time To Interactive) – 압도적 빠름 | Time to interactive — dramatically faster |
| **채용 시장 시그널** | **Signals from the job market** |
| 시니어 공고에 "Vanilla JS 능숙자 우대" 다시 등장 | "Strong Vanilla JS preferred" is appearing in senior postings again |
| "프레임워크 떼고 디버깅 가능한가" 가 중요 평가 항목 | "Can you debug without the framework?" has become a key evaluation point |
| 'React 가능' 보다 'JS 본질 이해'에 가산점 | Understanding JavaScript itself scores higher than "knows React" |
| 시니어 인터뷰 – DOM API / 이벤트 루프 / fetch 기본기 검증 | Senior interviews test the fundamentals: the DOM API, the event loop, fetch |
| 'AI 시대에 코드 읽는 능력 더 중요' 라는 인식 확산 | The view that reading code matters more in the AI era is spreading |
| **학습 곡선 비교** | **Learning curves** |
| React 경로 – 학습 6개월. JSX > 컴포넌트 > Hooks > 상태관리 > 빌드 시스템 > 라우팅. 매 단계마다 추상화 학습, 버전 업마다 마이그레이션 | The React path — six months. JSX, then components, hooks, state management, the build system, routing. A new abstraction at every step, and a migration with every major version |
| Vanilla 경로 – 학습 1주. HTML > CSS > fetch > DOM, 브라우저 표준 그대로. 추상화 없음, 20년 후에도 호환되는 표준 API | The vanilla path — one week. HTML, CSS, fetch, the DOM — browser standards as they are. No abstraction, and standard APIs that will still work in twenty years |
| AI 시대 핵심: AI 가 어차피 코드 작성, 사람은 결과를 읽고 검증할 수 있어야 함 > Vanilla 가 가시성 압도적, 시니어 디버깅 즉시 가능, 바이브코딩과 시너지 강함 | The crux in the AI era: the AI writes the code anyway, so the human must be able to read and verify it — and vanilla is overwhelmingly more legible, immediately debuggable by a senior, and a strong fit with vibe coding |

### Slide 178 — 9-6. 04-tasks.md — 구현 순서 (1/2) / Implementation Order (1 of 2)

| 한국어 | English |
|---|---|
| **9-6. 04-tasks.md 작성 지시 – 구현 순서 (1/2)** | **9-6. Instructing 04-tasks.md — Implementation Order (1 of 2)** |
| 내가 Phase 흐름과 체크리스트 형식 지정 | You specify the phase flow and the checklist format |
| `> 04-tasks.md 작성해. MVP를 3개 Phase로 진행:` | `> Write 04-tasks.md. The MVP proceeds in three phases:` |
| `- Phase 1 (설계): CLAUDE.md + docs/ 6종 작성 – 지금 완료` | `- Phase 1 (design): CLAUDE.md plus the six docs — complete as of now` |
| `- Phase 2 (백엔드): backend/ FastAPI > CRUD API 5개 > Swagger 확인` | `- Phase 2 (backend): backend/ FastAPI → five CRUD APIs → verify in Swagger` |
| `- Phase 3 (프론트): frontend/ HTML+JS+Tailwind > 화면 > API 연결 > git push` | `- Phase 3 (frontend): frontend/ HTML + JS + Tailwind → screens → wire up the API → git push` |
| `Phase 마다 체크리스트를 표로 만들 것. 단계 수는 이대로 고정: Phase 1 – 10단계 / Phase 2 – 10단계 / Phase 3 – 8단계` | `Make a checklist table per phase. Fix the step counts: Phase 1 — 10 steps / Phase 2 — 10 steps / Phase 3 — 8 steps` |
| `열은 단계 / 검증 방법 / 완료 3개. 완료 열은 [ ] 체크박스로 두고 진행하면서 [x] 로 바꾼다.` | `Three columns: step / how it is verified / done. The done column is a `[ ]` checkbox, changed to `[x]` as you go.` |
| `Phase 2 의존성은 fastapi, uvicorn, sqlalchemy, pytest, httpx 로 한정.` | `Phase 2 dependencies are limited to fastapi, uvicorn, sqlalchemy, pytest and httpx.` |
| `Phase 이름과 개수는 위 3개 그대로 고정. 변경 금지.` | `The phase names and count are fixed at those three. No changes.` |
| `이후 'backend 진행해' = Phase 2 전체, 'frontend 진행해' = Phase 3 전체.` | `From here on, "do the backend" means all of Phase 2, and "do the frontend" means all of Phase 3.` |
| **발췌** `## Phase별 진행` – Phase 1 (설계): docs 6종 작성 – 10단계 · Phase 2 (백엔드): FastAPI CRUD – 10단계 · Phase 3 (프론트): HTML+JS+Tailwind + 연결 – 8단계 | **Excerpt** `## Progress by phase` — Phase 1 (design): write the six docs, 10 steps · Phase 2 (backend): FastAPI CRUD, 10 steps · Phase 3 (frontend): HTML + JS + Tailwind and wiring, 8 steps |
| `## Phase 완료 정의` – 각 Phase의 모든 단계가 검증 통과시 완료 · Phase 3.8 통과 시 MVP 완성 · MVP 완성 후 확장 작업은 새 작업 문서로. 본 04-tasks에 확장 작업 덧붙이지 않음 | `## Definition of phase completion` — a phase is done when every step has passed verification · passing step 3.8 completes the MVP · extensions after the MVP go in a new task document; nothing is appended to this 04-tasks |

### Slide 179 — 9-6. 04-tasks.md — 구현 순서 (2/2) / Implementation Order (2 of 2)

| 한국어 | English |
|---|---|
| **9-6. 04-tasks.md 작성 지시 – 구현 순서 (2/2)** | **9-6. Instructing 04-tasks.md — Implementation Order (2 of 2)** |
| `> 진행 규칙: 순서대로만, 병렬 금지, 단계별 검증 필수.` | `> Rules of progress: in order only, no parallelism, verification required at each step.` |
| `✓ 04-tasks.md 작성 완료.` / `✓ Phase 1~3 체크리스트 (검증 방법 포함) + 진행 관리 규칙 반영.` | `✓ 04-tasks.md written.` / `✓ Checklists for Phases 1 to 3 including verification methods, plus the rules of progress.` |
| **발췌** `## 진행 규칙` – 1) 순서대로만 2) 병렬 금지 3) 단계별 검증 필수 4) 실패시 멈춤 | **Excerpt** `## Rules of progress` — 1) in order only 2) no parallelism 3) verification required at each step 4) stop on failure |

### Slide 180 — 9-7. 05-conventions.md & git 첫 커밋 (1/2) / Conventions and the First Commit (1 of 2)

| 한국어 | English |
|---|---|
| **9-7. 05-conventions.md 작성 지시 & git 첫 커밋 (1/2)** | **9-7. Instructing 05-conventions.md and the First Git Commit (1 of 2)** |
| 마지막 docs + 9장 마무리 | The last document, and the end of Chapter 9 |
| `> 05-conventions.md 작성해. 다음 내용으로:` | `> Write 05-conventions.md with this content:` |
| `- 명명: 백엔드 snake_case, 프론트 camelCase, 컴포넌트 PascalCase. 식별자는 영어, 주석만 한국어` | `- Naming: snake_case on the backend, camelCase on the frontend, PascalCase for components. Identifiers in English, comments in Korean` |
| `- 금지 5개 (금지/이유/대안 3열):` | `- Five prohibitions, in three columns (prohibited / why / instead):` |
| `print 디버깅 / 노이즈 / logging 모듈` | `print debugging / noise / use the logging module` |
| `bare except / 예외 삼킴 / except SpecificError` | `bare except / swallows exceptions / catch a specific error` |
| `비밀번호 하드코딩 / 보안사고 / .env + os.getenv` | `hard-coded passwords / security incidents / .env plus os.getenv` |
| `any 타입(TS) / 의미 상실 / 명시적 타입` | `the any type in TS / loses all meaning / use explicit types` |
| `!important / 우선순위 꼬임 / 셀렉터 개선` | `!important / tangles specificity / fix the selector instead` |
| `- .gitignore 에 넣을 것: __pycache__/, .venv/, *.db, *.log` | `- Put these in .gitignore: __pycache__/, .venv/, *.db, *.log` |
| `- 테스트 매트릭스 (표: 케이스 / 요청 / 기대 응답):` `정상 생성 – POST title 만 – 201` · `목록 – GET /api/tasks – 200, description 없음` · `단건 – GET /api/tasks/{id} – 200, description 있음` · `수정 – PUT 전 필드 – 200` · `삭제 – DELETE – 204` | `- A test matrix (case / request / expected response):` `Successful create — POST with title only — 201` · `List — GET /api/tasks — 200, no description` · `Single — GET /api/tasks/{id} — 200, with description` · `Update — PUT with all fields — 200` · `Delete — DELETE — 204` |
| **발췌** `## 코드 리뷰 자가 점검 (커밋 전 반드시 확인)` – `[ ] 명명 규칙 따랐는가` · `[ ] 금지 5개 (print/bare except/시크릿/any/!important) 없는가` · `[ ] 새 의존성 추가 시 03-design에 사유 적었는가` | **Excerpt** `## Code-review self-check (always before committing)` — `[ ] Did I follow the naming rules?` · `[ ] Are all five prohibitions clear (print, bare except, secrets, any, !important)?` · `[ ] If I added a dependency, did I write the rationale into 03-design?` |

### Slide 181 — 9-7. 05-conventions.md & git 첫 커밋 (2/2) / Conventions and the First Commit (2 of 2)

| 한국어 | English |
|---|---|
| **9-7. 05-conventions.md 작성 지시 & git 첫 커밋 (2/2)** | **9-7. Instructing 05-conventions.md and the First Git Commit (2 of 2)** |
| `> title 누락 – 400 / status 오값 – 400 / due_at 형식 오류 – 400 / 없는 id – 404 / 스펙 외 필드 – 422` | `> Missing title — 400 / invalid status — 400 / malformed due_at — 400 / unknown id — 404 / field not in the spec — 422` |
| `- git 커밋 규칙: feat/fix/docs/refactor/test/chore + 한국어 요약` | `- Commit message rules: feat/fix/docs/refactor/test/chore plus a summary in Korean` |
| `끝나면 git 로컬로 설정해줘. 이름은 BulNim, 메일은 kimkap10@gmail.com. .gitignore 도 만들고 첫 커밋: 'docs: Phase 1 설계 문서 7종 작성'` | `When you are done, set up git locally. Name BulNim, email kimkap10@gmail.com. Create a .gitignore and make the first commit: "docs: write the seven Phase 1 design documents"` |
| `깃허브 저장소 https://github.com/BulNim/taskflow-pro.git 에 연결해줘. 거부되면 덮어써도 돼.` | `Connect it to the GitHub repository https://github.com/BulNim/taskflow-pro.git. If it is rejected you may overwrite.` |
| `✓ 05-conventions.md 작성 완료.` / `✓ git init + add + commit 완료.` / `✓ 메시지: docs: Phase 1 CLAUDE.md + docs 6종 작성.` / `✓ 다음 작업 무엇입니까?` | `✓ 05-conventions.md written.` / `✓ git init, add and commit complete.` / `✓ Message: "docs: write Phase 1 CLAUDE.md and the six docs".` / `✓ What would you like next?` |
| **발췌** `[ ] 대응 테스트 있고 통과하는가` · `[ ] 커밋 메시지가 형식 맞는가` · `> 하나라도 [X]면 멈추고 보완 후 완료 보고` | **Excerpt** `[ ] Is there a matching test, and does it pass?` · `[ ] Does the commit message follow the format?` · `> If any one is unchecked, stop, fix it, and only then report completion` |
| `## git 첫 커밋` – `$ git commit -m "docs: Phase 1 CLAUDE.md + docs 6종 작성"` | `## The first git commit` — `$ git commit -m "docs: write Phase 1 CLAUDE.md and the six docs"` |

### Slide 182 — 9-7-1. 실제 실습 결과 / The Actual Result — Folder Structure and GitHub Push

| 한국어 | English |
|---|---|
| **9-7-1. 실제 실습 결과 – 폴더 구조 & GitHub 푸시** | **9-7-1. The Actual Result — Folder Structure and GitHub Push** |
| 실제 실습 결과 – docs/ 7종 작성 완료 & GitHub 첫 커밋 푸시 확인 | The real run — all seven documents written, and the first commit confirmed pushed to GitHub |
| *(image)* 폴더 구조 & 커밋 – `D:\taskflow-pro\` | *(image)* Folder structure and commits — `D:\taskflow-pro\` |
| *(image)* GitHub – `BulNim/taskflow-pro/docs` | *(image)* GitHub — `BulNim/taskflow-pro/docs` |

### Slide 183 — 9-8. 8장 vs 9장 비교 / Chapter 8 vs. Chapter 9

| 항목 / Aspect | 8장 – simple vibe / Ch. 8 — simple vibe | 9장 – docs 체계화 / Ch. 9 — systematized docs |
|---|---|---|
| 폴더 구성 / Folder layout | `server.js` + `public/` | `docs/` 6종 + `CLAUDE.md` — six docs plus CLAUDE.md |
| 의사결정 기록 / Record of decisions | 없음 — None | 03-design 8개 결정+근거 — Eight decisions with rationale in 03-design |
| 역할 정의 / Role definition | 없음 — None | CLAUDE.md 명시 — Stated in CLAUDE.md |
| 범위 외 명시 / Out-of-scope stated | 없음 — None | 01-product 5개 명시 — Five items listed in 01-product |
| 변경 추적 / Change tracking | 단일 커밋 — A single commit | 각 docs 끝 변경 이력 표 — A change-history table at the end of each doc |
| AI 응답 일관성 / Consistency of AI output | 매번 다름 — Different every time | docs 기반 재현성 — Reproducible, grounded in the docs |
| 시니어 검토 / Senior review | 임시 코드 — Throwaway code | 협업 가능한 프로젝트 — A project you can collaborate on |

| 한국어 | English |
|---|---|
| **9-8. 8장 vs 9장 비교** | **9-8. Chapter 8 vs. Chapter 9** |
| docs 6종 + CLAUDE.md 완성 > 결과물의 차이 | With the six docs and CLAUDE.md complete, the difference in what comes out |
| 핵심: 8장은 결과물만, 9장은 결과물 + 의사결정 추적 + 재현성 | The point: Chapter 8 gives you only the artifact; Chapter 9 gives you the artifact plus a traceable record of decisions plus reproducibility |

### Slide 184 — 체크포인트 / Checkpoint

| 한국어 | English |
|---|---|
| **체크포인트** | **Checkpoint** |
| 1. taskflow-pro 폴더 + CLAUDE.md 작성 | 1. Create the `taskflow-pro` folder and write CLAUDE.md |
| 2. CLAUDE.md 절대규칙 6개 명시 | 2. State the six hard rules in CLAUDE.md |
| 3. docs/ 6종 모두 작성 완료 | 3. Write all six documents |
| 4. 범위 외(out-of-scope) 명시 | 4. State what is out of scope |
| 5. 기술 선택 근거 표 작성 | 5. Write the table of technical rationale |
| 6. git 첫 커밋 완료 | 6. Make the first git commit |

---

## 10장. 백엔드 (FastAPI) / Chapter 10. The Backend (FastAPI)

### Slide 185 — Chapter cover

| 한국어 | English |
|---|---|
| **"backend 진행해" – 한 마디로 끝** | **"Do the backend" — One Sentence Is Enough** |
| 9장 docs 기반 – AI가 04-tasks 읽고 자동 진행 | Built on Chapter 9's docs — the AI reads 04-tasks and proceeds by itself |
| 학습 내용 | What you will learn |
| 1. backend/ 생성 + CRUD 5개 + 서버 실행 | 1. Creating backend/, the five CRUD endpoints, and running the server |
| 2. Swagger UI 자동 테스트 | 2. Automatic testing through Swagger UI |
| 3. CLAUDE.md 절대규칙 작동 시연 | 3. Seeing CLAUDE.md's hard rules take effect |

### Slide 186 — 시작 전 / Before You Start — Two Errors You Will Hit

| 언제 나오나 / When it appears | 화면에 뜨는 것 / What you see | 해결 / Fix |
|---|---|---|
| pytest 실행 직후 — Right after running pytest | `PermissionError: [WinError 32]` | AI 에게 – 커넥션을 finally 에서 close 하도록 고쳐줘 — Ask the AI to close the connection in a `finally` block |
| 테스트는 통과인데 에러 — Tests pass but there is an error | `10 passed` | 통과는 맞음. 뒷정리만 실패 – 위와 같은 원인 — They did pass; only the cleanup failed, for the same reason |
| curl 로 한글 보낼 때 — Sending Korean through curl | `error parsing the body` | JSON 을 파일로 저장 후 `--data-binary "@파일"` — Save the JSON to a file and use `--data-binary "@file"` |
| 영문은 되는데 한글만 실패 — English works, Korean fails | `400 Bad Request` | 브라우저나 Swagger UI 로 테스트하면 문제 없음 — Testing through a browser or Swagger UI avoids it entirely |

| 한국어 | English |
|---|---|
| **시작 전 – 실습 중 발생하는 오류 2가지 사전 확인** | **Before You Start — Two Errors That Come Up in the Exercise** |

### Slide 187 — 9장 docs 확보 효과 / The Payoff of Having the Docs

| 한국어 | English |
|---|---|
| **9장 docs 확보 효과 – "backend 진행해" 한 문장으로 완료** | **The Payoff of Chapter 9's Docs — One Sentence, "do the backend", Finishes It** |
| AI가 04-tasks.md를 읽고 자동 진행 | The AI reads 04-tasks.md and proceeds on its own |
| 10-1. "backend 진행해" – AI가 04-tasks.md Phase 2 읽고 10단계 체크리스트대로 자동 진행 | 10-1. "Do the backend" — the AI reads Phase 2 of 04-tasks.md and works through the ten-step checklist |
| 10-2. 서버 실행 + Swagger – uvicorn 자동 실행, 브라우저로 Swagger 진입 | 10-2. Run the server and Swagger — uvicorn starts automatically and Swagger opens in the browser |
| 10-3. 5개 API 자동 테스트 – 정상 + 400 + 404 케이스, AI가 pytest까지 작성 | 10-3. Automatic testing of the five APIs — the success case plus 400 and 404; the AI writes the pytest suite too |
| 10-4. 절대규칙 작동 시연 – AI가 의존성 추가 전 멈춤, 도입 이력 갱신 요청 | 10-4. The hard rules in action — the AI stops before adding a dependency and asks for the adoption log to be updated |
| 10-5. Phase 2 완료 + 커밋 – 04-tasks 체크리스트 10단계 모두 [O] + git commit | 10-5. Phase 2 complete and committed — all ten checklist items ticked, plus a git commit |

### Slide 188 — 10-1. backend 진행해 / "Do the Backend" — One Sentence Is Enough

| 한국어 | English |
|---|---|
| **10-1. "backend 진행해" – 한 마디로 끝** | **10-1. "Do the Backend" — One Sentence Is Enough** |
| AI가 04-tasks.md Phase 2 읽고 자동 진행 | The AI reads Phase 2 of 04-tasks.md and proceeds by itself |
| `> backend 진행해.` | `> Do the backend.` |
| `✓ 04-tasks.md Phase 2 확인.` | `✓ Phase 2 of 04-tasks.md confirmed.` |
| `✓ 스택: FastAPI + SQLAlchemy + SQLite (03-design #1, #3)` | `✓ Stack: FastAPI + SQLAlchemy + SQLite (03-design items 1 and 3)` |
| `✓ 10단계 체크리스트 순서대로 진행합니다.` | `✓ Working through the ten-step checklist in order.` |
| `✓ 작성 완료: app/main.py (CORS 포함) · app/db.py, models.py, schemas.py · app/routers/tasks.py (CRUD 5개) · tests/test_tasks.py (pytest 18종, 절대규칙 3) · requirements.txt + .gitignore` | `✓ Written: app/main.py (with CORS) · app/db.py, models.py, schemas.py · app/routers/tasks.py (the five CRUD endpoints) · tests/test_tasks.py (18 pytest cases, per hard rule 3) · requirements.txt and .gitignore` |
| `✓ 2.1 ~ 2.10 모두 검증 통과.` | `✓ Steps 2.1 through 2.10 all verified.` |
| **backend/ 폴더 구조 (자동 생성)** – `backend/ ├── app/ │ ├── main.py │ ├── db.py │ ├── models.py │ ├── schemas.py │ └── routers/ │ └── tasks.py ├── tests/ ├── requirements.txt └── .gitignore` | **The backend/ structure (generated automatically)** — `backend/ ├── app/ │ ├── main.py │ ├── db.py │ ├── models.py │ ├── schemas.py │ └── routers/ │ └── tasks.py ├── tests/ ├── requirements.txt └── .gitignore` |
| `# 5개 엔드포인트 모두 구현 완료` / `# 검증, CORS, DB 자동 생성 포함` | `# All five endpoints implemented` / `# Including validation, CORS and automatic database creation` |

### Slide 189 — 10-1-1. 실제 실습 결과 / The Actual Result — Design, Run, Performance, Phase 2 Verified

| 한국어 | English |
|---|---|
| **10-1-1. 실제 실습 결과 – 설계, 실행, 성능, Phase 2 검증** | **10-1-1. The Actual Result — Design, Execution, Performance and Phase 2 Verification** |
| 실제 실습 결과 – 4단계 한눈에 (폴더 설계 / 부팅 검증 / 응답시간 / Phase 2 전체 통과) | The real run at a glance — folder design, boot verification, response times, and all of Phase 2 passing |
| *(image)* AI 설계 확인 – backend/ 폴더 구조 (B3/C1) | *(image)* The AI's design — the backend/ folder structure (B3/C1) |
| *(image)* 실행 검증 – Phase 2.1 커밋 + /healthz 200 OK | *(image)* Execution verified — the Phase 2.1 commit and `/healthz` returning 200 OK |
| *(image)* 응답시간 – 최대 30ms (200ms 기준 7배 여유) | *(image)* Response time — 30 ms at worst, seven times inside the 200 ms target |
| *(image)* Phase 2 전체 검증 – 10단계 모두 통과 | *(image)* Phase 2 fully verified — all ten steps passing |

### Slide 190 — 10-2. 서버 실행 + Swagger (1/2) / Running the Server and Opening Swagger (1 of 2)

| 한국어 | English |
|---|---|
| **10-2. 서버 실행 + Swagger 진입 – 자연어로 (1/2)** | **10-2. Running the Server and Opening Swagger — in Plain Language (1 of 2)** |
| uvicorn 명령어 직접 안 침 | You never type a uvicorn command |
| `> 서버 띄우고 Swagger 열어줘.` | `> Start the server and open Swagger.` |
| `✓ 04-tasks Phase 2 와 03-design 확인.` | `✓ Checked Phase 2 of 04-tasks and 03-design.` |
| `● Bash cd backend` / `● Bash uvicorn app.main:app --reload --port 8000` | `● Bash cd backend` / `● Bash uvicorn app.main:app --reload --port 8000` |
| `✓ 백그라운드 기동 완료. http://127.0.0.1:8000` / `✓ Swagger UI: http://127.0.0.1:8000/docs` / `✓ 브라우저 열겠습니다.` | `✓ Started in the background at http://127.0.0.1:8000` / `✓ Swagger UI: http://127.0.0.1:8000/docs` / `✓ Opening the browser.` |
| `> 잘 떴네` | `> Looks good` |
| `✓ Swagger UI에 02-specs 엔드포인트 전부 노출 확인: POST /api/tasks · GET /api/tasks · GET /api/tasks/{id} · PUT /api/tasks/{id}` | `✓ Confirmed every endpoint from 02-specs is exposed in Swagger UI: POST /api/tasks · GET /api/tasks · GET /api/tasks/{id} · PUT /api/tasks/{id}` |
| **Swagger UI – 자동 생성된 API 문서** – `POST /api/tasks Create` · `GET /api/tasks List` · `GET /api/tasks/{id} Read` · `PUT /api/tasks/{id} Update` · `DELETE /api/tasks/{id} Delete` · `# Try it out 버튼으로` | **Swagger UI — API documentation generated automatically** — `POST /api/tasks Create` · `GET /api/tasks List` · `GET /api/tasks/{id} Read` · `PUT /api/tasks/{id} Update` · `DELETE /api/tasks/{id} Delete` · `# via the "Try it out" button` |

### Slide 191 — 10-2. 서버 실행 + Swagger (2/2) / Running the Server and Opening Swagger (2 of 2)

| 한국어 | English |
|---|---|
| **10-2. 서버 실행 + Swagger 진입 – 자연어로 (2/2)** | **10-2. Running the Server and Opening Swagger — in Plain Language (2 of 2)** |
| `> 잘 떴네` / `✓ DELETE /api/tasks/{id}` | `> Looks good` / `✓ DELETE /api/tasks/{id}` |
| `# 코드 없이 바로 API 호출 가능` | `# You can call the API directly, without writing any code` |

### Slide 192 — 10-2-1. 실제 실습 결과 / The Actual Result — Swagger UI and a POST Call

| 한국어 | English |
|---|---|
| **10-2-1. 실제 실습 결과 – Swagger UI 진입 & POST 호출** | **10-2-1. The Actual Result — Opening Swagger UI and Making a POST Call** |
| 실제 실습 결과 – 127.0.0.1:8000/docs Swagger UI 자동 생성 & Try it out 직접 호출 | The real run — Swagger UI generated at 127.0.0.1:8000/docs, and a call made directly with "Try it out" |
| *(image)* Swagger UI – 127.0.0.1:8000/docs (5개 엔드포인트) | *(image)* Swagger UI at 127.0.0.1:8000/docs, with all five endpoints |
| *(image)* POST /api/tasks – Request body + Execute | *(image)* POST /api/tasks — the request body and Execute |
### Slide 193 — 10-3. 10 passed / Verifying the Test Matrix

| 한국어 | English |
|---|---|
| **10-3. "10 passed" – 테스트 매트릭스 검증** | **10-3. "10 passed" — Verifying the Test Matrix** |
| 05-conventions 매트릭스 10개 케이스를 pytest 와 실서버 양쪽으로 대조 | The ten cases in the 05-conventions matrix, checked against both pytest and the live server |
| `> 05-conventions.md 테스트 매트릭스대로 검증해.` | `> Verify against the test matrix in 05-conventions.md.` |
| `✓ 10 passed – 매트릭스 10개 케이스 전부 통과.` | `✓ 10 passed — all ten matrix cases pass.` |
| `✓ 정상 5 – 생성 201 / 목록 200 / 단건 200 / 수정 200 / 삭제 204` | `✓ Five success cases — create 201 / list 200 / single 200 / update 200 / delete 204` |
| `✓ 오류 5 – title 누락 400 / status 오값 400 / due_at 형식 400 / 없는 id 404 / 스펙 외 필드 422` | `✓ Five error cases — missing title 400 / invalid status 400 / malformed due_at 400 / unknown id 404 / field not in spec 422` |
| `✓ 켜 둔 서버에 같은 10건을 요청해 응답 코드도 대조 – 10/10 일치.` | `✓ The same ten requests were sent to the running server and the status codes compared — 10 out of 10 match.` |
| `✓ 메모리 SQLite 로 격리 – tasks.db 영향 없음.` | `✓ Isolated with an in-memory SQLite database — tasks.db is untouched.` |
| **검증된 스펙 항목 (02-specs.md 기준)** – `[O] title 1~200자 제약 (빈값/초과 모두 400)` · `[O] status enum 3종 외 거부 (POST/GET 필터/PUT 모두 400)` · `[O] 없는 id 일관 404 (GET 단건/PUT/DELETE)` · `[O] 목록/단건 description 분리 – 핵심 차별 계약 통과` · `[O] updated_at 서버 자동 갱신` · `[O] DELETE 204 body 비어있음` · `[O] 검증 실패 모두 400 (FastAPI 기본 422 매핑 정상)` | **Spec items verified (against 02-specs.md)** — `[✓] title constrained to 1–200 characters (empty or over-length both 400)` · `[✓] Anything outside the three status values rejected (400 on POST, the GET filter and PUT)` · `[✓] Unknown id consistently 404 (GET single, PUT, DELETE)` · `[✓] description present on the single item but not the list — the key differentiating contract holds` · `[✓] updated_at set automatically by the server` · `[✓] DELETE returns 204 with an empty body` · `[✓] All validation failures return 400 (FastAPI's default 422 mapped correctly)` |

### Slide 194 — 10-3-1. 실제 실습 결과 / The Actual Result — Filling a Gap in PUT V1

| 한국어 | English |
|---|---|
| **10-3-1. 실제 실습 결과 – PUT V1 누락 보강 & 매트릭스 완전 충족** | **10-3-1. The Actual Result — Filling the PUT V1 Gap and Satisfying the Matrix in Full** |
| 실제 실습 결과 – AI 자가 점검: PUT V1(빈 title) 누락 감지 > 테스트 추가 > 매트릭스 완전 충족 | The real run — the AI self-checked, noticed the PUT V1 case (empty title) was missing, added the test, and satisfied the matrix completely |
| *(image)* 누락 감지 – PUT V1(빈 title) 케이스 보강 | *(image)* Spotting the gap — adding the PUT V1 (empty title) case |
| *(image)* 최종 매트릭스 – 10건 모두 통과 & git 커밋 (faa6f95) | *(image)* The final matrix — all ten passing, and committed (faa6f95) |

### Slide 195 — 10-4. 절대규칙 작동 시연 / The Hard Rules in Action

| 한국어 | English |
|---|---|
| **10-4. 절대규칙 작동 시연 – AI가 의존성 추가 전 멈춤** | **10-4. The Hard Rules in Action — the AI Stops Before Adding a Dependency** |
| 일부러 규칙을 어기는 요청. AI 가 되물으면 성공, 설치해 버리면 CLAUDE.md 설정 실패 | A deliberately rule-breaking request. If the AI asks back, it worked; if it just installs the package, CLAUDE.md was set up wrong |
| `> 날짜 처리 라이브러리 추가해서 created_at 포맷팅 개선해줘` | `> Add a date-handling library and improve the created_at formatting` |
| `✓ docs/03-design.md 에 날짜 라이브러리 언급이 없습니다.` | `✓ docs/03-design.md makes no mention of a date library.` |
| `✓ 05-conventions.md 금지 1번 – design.md 에 없는 새 패키지는 임의 추가 불가.` | `✓ Prohibition 1 in 05-conventions.md — a package not listed in design.md cannot be added on a whim.` |
| `✓ CLAUDE.md 절대규칙 2 (돌발 의존성 추가 금지) 위배라 승인 없이 진행할 수 없습니다.` | `✓ This violates hard rule 2 in CLAUDE.md (no surprise dependencies), so I cannot proceed without approval.` |
| `✓ 표준 기능으로 대체 가능합니다. 백엔드: 표준 datetime / 프론트: Intl / Date` | `✓ It can be done with standard features instead — `datetime` on the backend, `Intl` and `Date` on the front.` |
| `✓ 원하는 포맷을 알려주시면 라이브러리 없이 구현하겠습니다.` | `✓ Tell me the format you want and I will implement it without a library.` |
| `> 표준 라이브러리로 처리해. 날짜 형식은 02-specs 대로 전부 통일해줘.` → `✓ datetime 만 사용해 처리 완료. 의존성 추가 없음.` | `> Use the standard library. Make every date format match 02-specs.` → `✓ Done using datetime alone. No dependencies added.` |
| **docs 체계화의 핵심 가치 – 시니어 검토 통과 포인트**: `[O] AI가 마음대로 라이브러리 도입 안 함` · `[O] docs 갱신 없이는 환경 변경 불가` · `[O] 모든 의존성에 사유 추적 가능` | **The core value of the document system — what gets it past senior review**: `[✓] The AI does not adopt libraries on its own` · `[✓] The environment cannot change without the docs changing` · `[✓] Every dependency has a traceable rationale` |
| **만약 docs 없이 simple vibe 였다면?**: `[X] python-dateutil 자동 설치` · `[X] requirements.txt 무성장` · `[X] 6개월 뒤 의존성 정글` | **And if this were simple vibe, with no docs?**: `[✗] python-dateutil installed automatically` · `[✗] requirements.txt growing unchecked` · `[✗] a dependency jungle six months on` |
| > docs/ 체계화가 작동하는 순간 | > This is the moment the document system earns its keep |

### Slide 196 — 10-4-1. 실제 실습 결과 / The Hard Rules in Four Steps

| 한국어 | English |
|---|---|
| **10-4-1. 실제 실습 결과 – 절대규칙 작동 4단계 시연** | **10-4-1. The Actual Result — the Hard Rules Demonstrated in Four Steps** |
| 실제 실습 결과 – 개선안 제안 > 절대규칙 충돌 검토 > stdlib만으로 코드 변경 > millisecond 검증 | The real run — propose an improvement, check it against the hard rules, change the code using only the standard library, then verify to the millisecond |
| *(image)* 1) 개선안 제안 – DateTime(timezone=True) 비교표 | *(image)* 1) The proposed improvement — a comparison table for `DateTime(timezone=True)` |
| *(image)* 2) 절대규칙 검토 – CLAUDE.md §3-2 충돌 > 선택지 A/B | *(image)* 2) Checking the hard rules — a conflict with CLAUDE.md §3-2, then options A and B |
| *(image)* 3) 코드 변경 – models.py (stdlib만 사용, 의존성 0) | *(image)* 3) The code change — models.py, standard library only, zero dependencies |
| *(image)* 4) 검증 – created_at millisecond까지 (변경 전/후) | *(image)* 4) Verification — created_at to the millisecond, before and after |

### Slide 197 — 10-5. backend 완료 + git 커밋 / Backend Complete and Committed

| 한국어 | English |
|---|---|
| **10-5. backend 완료 + git 커밋** | **10-5. Backend Complete, and Committed** |
| 04-tasks.md Phase 2 10단계 모두 통과 | All ten steps of Phase 2 in 04-tasks.md pass |
| `> backend 완료 처리하고 커밋한 뒤 올려줘.` | `> Mark the backend done, commit it and push it.` |
| `✓ 04-tasks.md Phase 2 체크박스를 [x] 로 갱신: 2.1 ~ 2.10 모두 완료.` | `✓ Ticked the Phase 2 checkboxes in 04-tasks.md — 2.1 through 2.10 all complete.` |
| `✓ 05-conventions 커밋 규칙에 맞춰 feat: 으로 시작:` | `✓ Following the commit rules in 05-conventions, starting with `feat:`` |
| `$ git add backend/ docs/04-tasks.md` / `$ git commit -m "feat: Phase 2 백엔드 CRUD API 구현"` / `$ git push origin main` | `$ git add backend/ docs/04-tasks.md` / `$ git commit -m "feat: implement the Phase 2 backend CRUD API"` / `$ git push origin main` |
| `✓ 커밋 해시: a7e3c91` / `✓ 변경: 18 files, +842 -3 lines` / `✓ 다음은 Phase 3 프론트엔드 지시를 받겠습니다.` | `✓ Commit hash a7e3c91` / `✓ Changes: 18 files, +842 −3 lines` / `✓ Ready for your Phase 3 frontend instructions.` |
| **Phase 2 완료 체크 – `## Phase 2 백엔드 (10단계 [O])`**: `2.1 backend 폴더와 가상환경` · `2.2 의존성 설치 (fastapi / uvicorn / sqlalchemy / pytest / httpx)` · `2.3 SQLAlchemy 모델` · `2.4 Pydantic 스키마 extra=forbid` · `2.5 DB 초기화` · `2.6 POST 와 GET 목록` · `2.7 GET 단건` · `2.8 PUT 과 DELETE` · `2.9 pytest 정상·400·404` · `2.10 Swagger 확인` | **Phase 2 completion check — `## Phase 2, backend (10 steps, all ticked)`**: `2.1 the backend folder and virtual environment` · `2.2 install dependencies (fastapi / uvicorn / sqlalchemy / pytest / httpx)` · `2.3 SQLAlchemy models` · `2.4 Pydantic schemas with extra=forbid` · `2.5 database initialization` · `2.6 POST and GET list` · `2.7 GET single` · `2.8 PUT and DELETE` · `2.9 pytest for success, 400 and 404` · `2.10 verify in Swagger` |
| `> MVP 백엔드 완료. Phase 3 진행 가능.` | `> The MVP backend is done. Phase 3 can begin.` |

### Slide 198 — 10-5-1. 실제 실습 결과 / GitHub Push and Per-Phase Commit History

| 한국어 | English |
|---|---|
| **10-5-1. 실제 실습 결과 – GitHub 푸시 완료 & Phase 별 커밋 이력** | **10-5-1. The Actual Result — Pushed to GitHub, with Per-Phase Commit History** |
| 실제 실습 결과 – BulNim/taskflow-pro/backend/app – Phase 2.1~2.9 + refactor 커밋까지 이력 가시화 | The real run — `BulNim/taskflow-pro/backend/app`, with the history visible from Phase 2.1 through 2.9 and on to the refactor commit |
| *(image)* GitHub – BulNim/taskflow-pro/backend/app (최신 커밋: 533cafc, refactor) | *(image)* GitHub — `BulNim/taskflow-pro/backend/app` (latest commit 533cafc, a refactor) |

### Slide 199 — 체크포인트 / Checkpoint

| 한국어 | English |
|---|---|
| **체크포인트** | **Checkpoint** |
| 1. backend/ 폴더 + FastAPI 골격 생성 | 1. Create the backend/ folder and the FastAPI skeleton |
| 2. CRUD 5개 엔드포인트 모두 구현 | 2. Implement all five CRUD endpoints |
| 3. Swagger UI에서 5개 동작 확인 | 3. Confirm all five work in Swagger UI |
| 4. pytest 10종 작성, 실행 – 10 passed | 4. Write and run ten pytest cases — 10 passed |
| 5. 04-tasks Phase 2 10단계 모두 통과 | 5. All ten Phase 2 steps in 04-tasks pass |
| 6. git commit 완료 | 6. Commit to git |

---

## 11장. 프론트엔드 (Vanilla JS + Tailwind) / Chapter 11. The Frontend (Vanilla JS + Tailwind)

### Slide 200 — Chapter cover

| 한국어 | English |
|---|---|
| **10장 패턴 그대로 – "frontend 진행해" 한 문장으로 완료** | **The Same Pattern as Chapter 10 — One Sentence, "do the frontend", Finishes It** |
| docs 를 보고 AI 가 자동 진행 | The AI reads the docs and proceeds by itself |
| 학습 내용 | What you will learn |
| 1. frontend/ 생성 + API 연결 | 1. Creating frontend/ and wiring up the API |
| 2. 5개 엔드포인트 화면 동작 확인 | 2. Confirming all five endpoints work from the screen |
| 3. 기초편 완료 + git push | 3. Finishing the Foundations course, and pushing to git |

### Slide 201 — 10장 패턴 그대로 / The Same Pattern as Chapter 10

| 한국어 | English |
|---|---|
| **10장 패턴 그대로 – "frontend 진행해" 한 문장으로 완료** | **The Same Pattern as Chapter 10 — "Do the frontend" Finishes It** |
| AI가 04-tasks.md Phase 3 (8단계) 읽고 자동 진행 | The AI reads Phase 3 of 04-tasks.md (eight steps) and proceeds by itself |
| 11-1. "frontend 진행해" – AI가 04-tasks.md Phase 3 읽고 8단계 체크리스트대로 자동 진행 | 11-1. "Do the frontend" — the AI reads Phase 3 and works the eight-step checklist |
| 11-2. 같은 주소에서 화면 확인 – FastAPI 가 StaticFiles 로 제공, file:// 로 열지 않음 | 11-2. View the screen at the same address — FastAPI serves it via StaticFiles; never open it with `file://` |
| 11-3. 5개 엔드포인트 화면 테스트 – POST/GET 목록/GET 단건/PUT/DELETE 화면에서 직접 동작 확인 | 11-3. Test all five endpoints from the screen — POST, GET list, GET single, PUT, DELETE, exercised through the UI |
| 11-4. MVP 성공 기준 검증 – 360px 반응형, 새로고침 유지, API p95 ≤ 200ms 측정 | 11-4. Verify the MVP success criteria — responsive at 360px, data surviving a refresh, API p95 ≤ 200 ms |
| 11-5. Phase 3 완료 + git push – 04-tasks 8단계 모두 [O], git push origin main | 11-5. Phase 3 complete and pushed — all eight steps ticked, `git push origin main` |

### Slide 202 — 11-1. frontend 진행해 / "Do the Frontend" — One Sentence Is Enough

| 한국어 | English |
|---|---|
| **11-1. "frontend 진행해" – 한 마디로 끝** | **11-1. "Do the Frontend" — One Sentence Is Enough** |
| AI가 04-tasks.md Phase 3 읽고 자동 진행 | The AI reads Phase 3 of 04-tasks.md and proceeds by itself |
| `> frontend 진행해.` | `> Do the frontend.` |
| `✓ 04-tasks.md Phase 3 확인.` / `✓ 스택: HTML + Vanilla JS + Tailwind CDN` / `✓ 상태: 모듈 변수 + DOM 직접 갱신 (03-design #6)` / `✓ 8단계 체크리스트 순서대로 진행합니다.` | `✓ Phase 3 of 04-tasks.md confirmed.` / `✓ Stack: HTML + Vanilla JS + Tailwind CDN` / `✓ State: module variables with direct DOM updates (03-design item 6)` / `✓ Working through the eight-step checklist in order.` |
| `✓ 작성 완료: frontend/index.html (Tailwind CDN + 메인 화면) · frontend/app.js (fetch + DOM 조작 + CRUD) · frontend/style.css (커스텀 보강 – 최소)` | `✓ Written: frontend/index.html (Tailwind CDN plus the main screen) · frontend/app.js (fetch, DOM manipulation, CRUD) · frontend/style.css (minimal custom additions)` |
| `✓ 상대경로 fetch(/api/...) 고정` / `✓ 3.1 ~ 3.8 모두 검증 통과.` | `✓ Relative `fetch(/api/…)` paths throughout` / `✓ Steps 3.1 through 3.8 all verified.` |
| **frontend/ 폴더 구조 (자동 생성)** – `frontend/ ├── index.html` `# Tailwind CDN 한 줄` `# 메인 화면 (목록/입력/필터)` `├── app.js` `# fetch() + DOM 조작` `# CRUD 5개 함수` `└── style.css` `# 최소 커스텀 (애니메이션 등)` | **The frontend/ structure (generated automatically)** — `frontend/ ├── index.html` `# one line of Tailwind CDN` `# the main screen (list, input, filters)` `├── app.js` `# fetch() and DOM manipulation` `# the five CRUD functions` `└── style.css` `# minimal custom CSS (animations and such)` |
| `# 빌드 X, 서버 X` / `# http://127.0.0.1:8000/ 으로 접속` / `# 360px 반응형 + 다크모드` | `# No build step, no separate server` / `# Reached at http://127.0.0.1:8000/` / `# Responsive at 360px, plus dark mode` |

### Slide 203 — 11-2. 서버 다시 띄우고 화면 열기 (1/2) / Restarting the Server and Opening the Screen (1 of 2)

| 한국어 | English |
|---|---|
| **11-2. 서버 다시 띄우고 화면 열기 – 자연어로 (1/2)** | **11-2. Restarting the Server and Opening the Screen — in Plain Language (1 of 2)** |
| frontend/ 가 생긴 뒤라 정적 파일 마운트를 다시 잡아야 함. 껐다 켜는 절차는 AI 가 처리 | Now that frontend/ exists, the static-file mount has to be set up again. The AI handles the stop-and-start |
| `> 서버 종료해줘.` → `● Bash 포트 8000 을 쓰는 프로세스 확인` → `● Bash 해당 프로세스와 자식 종료` | `> Shut the server down.` → `● Bash find the process using port 8000` → `● Bash kill that process and its children` |
| `✓ --reload 는 프로세스가 둘이라 둘 다 종료했습니다.` / `✓ 포트 8000 이 비었습니다.` | `✓ With --reload there are two processes, so I stopped both.` / `✓ Port 8000 is free.` |
| `> 서버 다시 띄우고 화면 열어줘.` → `● Bash cd backend` → `● Bash uvicorn app.main:app --reload --port 8000` | `> Start the server again and open the screen.` → `● Bash cd backend` → `● Bash uvicorn app.main:app --reload --port 8000` |
| `✓ StaticFiles 마운트에 frontend/ 잡힘 (03-design #2).` / `✓ http://127.0.0.1:8000/ 열겠습니다.` | `✓ frontend/ is picked up by the StaticFiles mount (03-design item 2).` / `✓ Opening http://127.0.0.1:8000/.` |
| `✓ 메인 화면: 업무 목록 표시` / `✓ 상단: 업무 추가 폼` / `✓ 각 업무: 상태 토글 + 수정 + 삭제` | `✓ Main screen: the task list` / `✓ Top: the add-task form` / `✓ Each task: status toggle, edit, delete` |
| **같은 오리진에서 화면 제공** – `# 03-design #2 – StaticFiles 마운트` `FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"` `app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True))` | **Served from the same origin** — `# 03-design item 2 — the StaticFiles mount` `FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"` `app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True))` |
| `# 브라우저 주소 http://127.0.0.1:8000/` `# file:// 로 직접 열지 않음` | `# Browser address: http://127.0.0.1:8000/` `# Never opened directly with file://` |
| `# Tailwind CDN 자동 로드 <script src="cdn.tailwindcss.com">` / `# fetch 호출 (DevTools) GET /api/tasks > 200 OK, 89ms` | `# Tailwind CDN loads automatically: <script src="cdn.tailwindcss.com">` / `# The fetch call in DevTools: GET /api/tasks → 200 OK, 89 ms` |

### Slide 204 — 11-2. 서버 다시 띄우고 화면 열기 (2/2) / Restarting the Server (2 of 2)

| 한국어 | English |
|---|---|
| **11-2. 서버 다시 띄우고 화면 열기 – 자연어로 (2/2)** | **11-2. Restarting the Server and Opening the Screen — in Plain Language (2 of 2)** |
| `> 잘 떴네` → `✓ 같은 오리진에서 제공되어 CORS 없이 fetch 200 OK.` | `> Looks good` → `✓ Served from the same origin, so fetch returns 200 OK with no CORS involved.` |
| `# 빌드 0초, 변경 즉시 반영 (F5)` | `# Zero build time; changes show on refresh (F5)` |

### Slide 205 — 11-3. 5개 엔드포인트 화면 동작 확인 / All Five Endpoints, Exercised from the Screen

| 한국어 | English |
|---|---|
| **11-3. 5개 엔드포인트 – 화면에서 직접 동작 확인** | **11-3. The Five Endpoints — Exercised Directly from the Screen** |
| Swagger 가 아닌 실제 사용자 화면에서 POST / GET 목록 / GET 단건 / PUT / DELETE 5종 동작 확인 | Not through Swagger but through the real user interface: POST, GET list, GET single, PUT and DELETE |
| `> 02-specs 대로 엔드포인트 동작 다 확인해.` | `> Check every endpoint behaves as 02-specs says.` |
| `✓ POST – 신규 추가 > 201 > 즉시 반영 [O]` | `✓ POST — add a new task → 201 → reflected immediately ✓` |
| `✓ GET 목록 – 5건 표시, description 없음 [O]` | `✓ GET list — five items shown, no description ✓` |
| `✓ GET 단건 – 상세 모달, description 포함 [O]` | `✓ GET single — the detail modal, description included ✓` |
| `✓ PUT – 수정 모달 > 200 > 갱신 반영 [O]` | `✓ PUT — the edit modal → 200 → the update shows ✓` |
| `✓ DELETE – 확인 모달 > 204 > 즉시 제거 [O]` | `✓ DELETE — the confirm modal → 204 → removed immediately ✓` |
| `✓ 02-specs 목록/단건 description 차이 화면 검증 완료.` | `✓ The list-vs-single description difference from 02-specs is verified on screen.` |
| **엔드포인트 화면 검증 결과** – `[O] POST /api/tasks – 추가 폼 + 즉시 반영` · `[O] GET /api/tasks – 목록 (description 없음) > 네트워크 가벼움 확인` · `[O] GET /api/tasks/{id} – 상세 모달 > description 포함` · `[O] PUT /api/tasks/{id} – 수정 모달 > 전 필드 갱신` · `[O] DELETE /api/tasks/{id} – 확인 모달 + 제거` | **Endpoint verification on screen** — `[✓] POST /api/tasks — the add form, reflected immediately` · `[✓] GET /api/tasks — the list, no description, confirming a light payload` · `[✓] GET /api/tasks/{id} — the detail modal, with description` · `[✓] PUT /api/tasks/{id} — the edit modal, all fields updated` · `[✓] DELETE /api/tasks/{id} — the confirm modal and removal` |
| **클라이언트 검증** – `[O] title 빈값 > 제출 차단` · `[O] title 200자 초과 > 차단` · `[O] 4xx 응답 > 토스트 알림` | **Client-side validation** — `[✓] Empty title blocks submission` · `[✓] Title over 200 characters blocked` · `[✓] A 4xx response raises a toast` |

### Slide 206 — 11-4. MVP 성공 기준 검증 / Verifying the MVP Success Criteria

| 한국어 | English |
|---|---|
| **11-4. MVP 성공 기준 검증** | **11-4. Verifying the MVP Success Criteria** |
| 01-product.md 정량 기준 – 360px / p95 200ms / 새로고침 유지. 360px 과 테마 토글은 각자 브라우저에서 직접 확인 | The quantitative criteria from 01-product.md — 360px, p95 under 200 ms, data surviving a refresh. Check 360px and the theme toggle yourself, in your own browser |
| `> 01-product MVP 성공 기준 검증해.` | `> Verify the MVP success criteria in 01-product.` |
| `✓ (1) 새로고침 데이터 유지 [O] > SQLite 영속화 + fetch 호출 정상` | `✓ (1) Data survives a refresh ✓ — SQLite persistence and the fetch calls both correct` |
| `✓ (2) 360px 반응형 안 깨짐 [O] > DevTools 360px 가로 스크롤 없음 > 요소 겹침 없음` | `✓ (2) Responsive at 360px ✓ — no horizontal scroll in DevTools at 360px, no overlapping elements` |
| `✓ (3) API p95 ≤ 200ms [O] > 50회 측정: p50 42ms / p95 138ms > 모든 엔드포인트 통과` | `✓ (3) API p95 ≤ 200 ms ✓ — over 50 runs: p50 42 ms, p95 138 ms; every endpoint passes` |
| `✓ > MVP 성공 기준 모두 충족.` | `✓ All MVP success criteria met.` |
| **측정 결과** – `(1) 새로고침 데이터 유지: SQLite tasks.db 영속화, F5 후 동일 목록 표시 [O]` · `(2) 360px 반응형: DevTools Mobile 360px, 가로 스크롤 없음 [O], 요소 겹침 없음 [O]` · `(3) API p95 ≤ 200ms (50회 호출 측정): POST 124ms / GET list 89ms / GET one 72ms / PUT 138ms / DELETE 95ms` | **Measurements** — `(1) Data survives a refresh: persisted in SQLite tasks.db; the same list after F5 ✓` · `(2) Responsive at 360px: DevTools mobile at 360px, no horizontal scroll ✓, no overlap ✓` · `(3) API p95 ≤ 200 ms over 50 calls: POST 124 ms / GET list 89 ms / GET one 72 ms / PUT 138 ms / DELETE 95 ms` |

### Slide 207 — 11-5. Phase 3 완료 + git push (1/2) / Phase 3 Complete and Pushed (1 of 2)

| 한국어 | English |
|---|---|
| **11-5. Phase 3 완료 + git push – 기초편 완료 (1/2)** | **11-5. Phase 3 Complete and Pushed — the Foundations Course Finished (1 of 2)** |
| 04-tasks.md Phase 3 8단계 모두 통과 | All eight Phase 3 steps in 04-tasks.md pass |
| `> Phase 3 완료 처리하고 커밋한 뒤 올려줘.` | `> Mark Phase 3 done, commit it and push it.` |
| `● Bash git add . / git commit / git push origin main` / `✓ 커밋: 4b2e7f1 · 기본 브랜치 main 확인` | `● Bash git add . / git commit / git push origin main` / `✓ Commit 4b2e7f1, default branch main confirmed` |
| `> 이 앱 설명서를 README.md 로 만들어서 올려줘. docs 와 어긋나지 않게.` | `> Write a guide for this app as README.md and push it. Make sure it does not contradict the docs.` |
| `✓ 04-tasks Phase 3 체크박스를 [x] 로 갱신: 3.1 ~ 3.8 모두 완료.` | `✓ Ticked the Phase 3 checkboxes in 04-tasks — 3.1 through 3.8 all complete.` |
| `● Bash git remote -v – origin 연결 확인됨` | `● Bash git remote -v — origin connection confirmed` |
| `$ git add frontend/ docs/04-tasks.md` / `$ git commit -m "feat: Phase 3 프론트엔드 (HTML+JS+Tailwind) + API 연결"` / `$ git push origin main` | `$ git add frontend/ docs/04-tasks.md` / `$ git commit -m "feat: Phase 3 frontend (HTML+JS+Tailwind) plus API wiring"` / `$ git push origin main` |
| `✓ 커밋: 4b2e7f1 / 기본 브랜치 main 확인` / `✓ 변경: 7 files, +482 -3 lines` | `✓ Commit 4b2e7f1, default branch main confirmed` / `✓ Changes: 7 files, +482 −3 lines` |
| **Phase 3 프론트엔드 (8단계 [O])**: `3.1 frontend 폴더와 index.html` · `3.2 Tailwind CDN 과 테마 토글` · `3.3 목록 카드 렌더` · `3.4 추가 폼` · `3.5 수정 모달 단건 조회 후 전 필드` · `3.6 삭제 확인` · `3.7 360px 반응형` · `3.8 API p95 200ms 측정` | **Phase 3, frontend (8 steps, all ticked)**: `3.1 the frontend folder and index.html` · `3.2 Tailwind CDN and the theme toggle` · `3.3 rendering the list cards` · `3.4 the add form` · `3.5 the edit modal — fetch the single item, then all fields` · `3.6 delete confirmation` · `3.7 responsive at 360px` · `3.8 measuring API p95 against 200 ms` |

### Slide 208 — 11-5. Phase 3 완료 + git push (2/2) / Phase 3 Complete and Pushed (2 of 2)

| 한국어 | English |
|---|---|
| **11-5. Phase 3 완료 + git push – 기초편 완료 (2/2)** | **11-5. Phase 3 Complete and Pushed — the Foundations Course Finished (2 of 2)** |
| `> 이 앱 설명서를 README.md 로 만들어서 올려줘. docs 와 어긋나지 않게.` | `> Write a guide for this app as README.md and push it. Make sure it does not contradict the docs.` |
| `✓ 기초편 MVP 완성. 심화편 OpenSpec 진행 가능.` | `✓ The Foundations MVP is complete. You can move on to OpenSpec in the Advanced course.` |
| `> 기초편 MVP 완성` | `> Foundations MVP complete` |

### Slide 209 — 11-6. 프론트엔드 실제 실습 결과 / The Actual Frontend Result

| 한국어 | English |
|---|---|
| **11-6. 프론트엔드 실제 실습 결과 – 다크/라이트, 검증, GitHub** | **11-6. The Actual Frontend Result — Dark and Light, Verification, GitHub** |
| 실제 실습 결과 – 두 테마 화면 / S1, S2, S3 PASS / GitHub 푸시 frontend/ 구조 | The real run — both theme screens, S1/S2/S3 passing, and the frontend/ structure pushed to GitHub |
| *(image)* 다크 모드 – TaskFlow Pro (Mac OS 톤) | *(image)* Dark mode — TaskFlow Pro in the macOS tone |
| *(image)* 라이트 모드 – 동일 UI / 테마 토글 작동 | *(image)* Light mode — the same UI, with the theme toggle working |
| *(image)* 성공 기준 검증 – S1, S2, S3 PASS (5개 EP 측정) | *(image)* Success criteria verified — S1, S2 and S3 pass, with all five endpoints measured |
| *(image)* GitHub 푸시 – backend/ docs/ frontend/ + README | *(image)* Pushed to GitHub — backend/, docs/, frontend/ and the README |

### Slide 210 — 11-7. 최종 검증 / Final Verification — A Clean Run from the Fixed Prompts

| 확인 항목 / Check | 결과 / Result | 근거 / Evidence |
|---|---|---|
| docs/ 파일명 6개 + CLAUDE.md 일치 — The six doc filenames match CLAUDE.md | 통과 / Pass | 이름 1:1 일치 — Names match one to one |
| 수정 – 단건 조회 후 전 필드 PUT — Update: fetch the single item, then PUT every field | 통과 / Pass | description 유지됨 — description is preserved |
| 목록엔 description 없음 / 단건엔 있음 — No description in the list, present on the single item | 통과 / Pass | 응답 키 차이 확인 — The response keys differ as specified |
| 스펙 외 필드 POST 시 422 — POSTing a field not in the spec returns 422 | 통과 / Pass | `extra_forbidden` |
| 삭제 후 id 재사용 불가 — Ids are not reused after deletion | 통과 / Pass | 5 삭제 > 다음 6 — Delete 5, the next is 6 |
| pytest | 통과 / Pass | `10 passed` |

| 한국어 | English |
|---|---|
| **11-7. 최종 검증 – 확정 프롬프트로 처음부터 다시 실행한 결과** | **11-7. Final Verification — Rerunning from Scratch with the Finalized Prompts** |
| 빈 폴더에서 9-1 부터 11-5 까지 순서대로 실행. 아래는 그 결과 화면 그대로 | Run from an empty folder, 9-1 through 11-5 in order. These are the resulting screens, untouched |
| *(image)* 다크 모드 (기본) · 라이트 모드 (토글 후) · 수정 모달 – 전 필드 · 360px | *(image)* Dark mode (default) · Light mode (after toggling) · The edit modal with every field · 360px |

### Slide 211 — 체크포인트 / Checkpoint

| 한국어 | English |
|---|---|
| **체크포인트** | **Checkpoint** |
| 1. frontend/ index.html + app.js + Tailwind CDN | 1. frontend/ with index.html, app.js and Tailwind CDN |
| 2. 5개 엔드포인트 화면 동작 확인 | 2. All five endpoints working from the screen |
| 3. 360px 반응형 안 깨짐 | 3. Nothing breaks at 360px |
| 4. API p95 200ms 이하 측정 통과 | 4. Measured API p95 under 200 ms |
| 5. 04-tasks Phase 3 8단계 모두 통과 | 5. All eight Phase 3 steps in 04-tasks pass |
| 6. `git push origin main` 완료 | 6. Pushed with `git push origin main` |

---

## 12장. 기초편 회고 + 심화편 예고 / Chapter 12. Looking Back, and Looking Ahead

### Slide 212 — Chapter cover

| 한국어 | English |
|---|---|
| **AI-DLC 분석, OpenSpec 결론, 심화편 예고** | **Analyzing AI-DLC, Concluding on OpenSpec, and Previewing the Advanced Course** |
| 9~11장 실습 결과 분석 + 심화편 준비 | Analyzing the results of Chapters 9 to 11, and preparing for the Advanced course |
| 학습 내용 | What you will learn |
| 1. AI-DLC 이상 vs 현실 | 1. AI-DLC as advertised vs. as it really is |
| 2. AI-DLC 자동화 = 사람의 docs 정의 | 2. AI-DLC's automation is really the docs a human defined |
| 3. OpenSpec으로 사전 정의 자동화 | 3. Automating that up-front definition with OpenSpec |

### Slide 213 — 12-1. 기초편에서 배운 것 / What the Foundations Course Covered

| 한국어 | English |
|---|---|
| **12-1. 기초편에서 배운 것** | **12-1. What You Learned in the Foundations Course** |
| 1장 ~ 11장 전체 요약 | A summary of Chapters 1 to 11 |
| 1장 AI 개요 – 인공지능 개념 + AI 서비스 예시 7가지 | Ch. 1 AI overview — the concept of AI plus seven example services |
| 2장 개발에서 AI 활용 – 기획/보조코딩/바이브코딩/서비스 | Ch. 2 Using AI in development — planning, assisted coding, vibe coding, shipping a service |
| 3장 바이브코딩 + AI-DLC – 정의, 역할, 함정 | Ch. 3 Vibe coding + AI-DLC — definitions, roles, pitfalls |
| 4장 터미널 기초 – 명령어 10개 + Tab 자동완성 | Ch. 4 Terminal basics — ten commands plus Tab completion |
| 5장 Claude Code 설치 & API Key 인증 + Sonnet/effort low | Ch. 5 Installing Claude Code, API key authentication, Sonnet with low effort |
| 6장 스킬과 플러그인 – 마켓플레이스에서 설치하고 호출 | Ch. 6 Skills and plugins — installing from a marketplace and invoking them |
| 7장 Git & GitHub 연결 | Ch. 7 Git and connecting to GitHub |
| 8장 심플 바이브 실습 – 한계 체감 | Ch. 8 Simple vibe practice — feeling the limits |
| 9장 CLAUDE.md + docs 6종 > 재현 가능한 구조 | Ch. 9 CLAUDE.md plus six docs — a reproducible structure |
| 10장 FastAPI CRUD API + Swagger 테스트 | Ch. 10 A FastAPI CRUD API, tested through Swagger |
| 11장 Vanilla JS + Tailwind 프론트-백 연결 완성 | Ch. 11 Vanilla JS and Tailwind, front and back wired together |

### Slide 214 — 12-2. AI-DLC 이상 vs 현실 / AI-DLC as Advertised vs. as It Really Is

| 이상 – AWS 마케팅 자료 / The ideal, per AWS's marketing | 현실 – 9~11장 실습 결과 / The reality, per Chapters 9 to 11 |
|---|---|
| AI 주도 실행 – AI가 자동 진행 — AI-led execution; the AI drives | 인간 사전 투자가 90% – CLAUDE.md, docs 6종, 절대규칙 — 90% is human investment up front: CLAUDE.md, the six docs, the hard rules |
| 인간 검토, 승인 – 인간은 결정만 — The human reviews and approves; only decisions | AI는 컨텍스트가 있어야 주도 – 빈손이면 매번 다른 결과 — The AI can only lead with context; empty-handed it gives a different answer every time |
| 단계 건너뛰기 가능 – 유연한 워크플로우 — You can skip steps; a flexible workflow | 사전 투자 없이 단계 건너뛰기 불가 – 사전 골격이 모든 자동화의 전제 — You cannot skip steps without the up-front investment; the skeleton is the precondition for all automation |
| 적응형 협업 – 자동화된 흐름 — Adaptive collaboration; an automated flow | 인간이 '왜, 무엇, 언제' 먼저 – AI는 '어떻게'만 실행 — The human settles why, what and when first; the AI only executes the how |

| 한국어 | English |
|---|---|
| **12-2. AI-DLC 이상 vs 현실** | **12-2. AI-DLC — the Ideal vs. the Reality** |
| AWS 자료는 수면 위만 – 수면 아래 인간 사전 투자가 90% | The AWS material shows only what is above the waterline — 90% of it is human investment below |
| 핵심: AI-DLC는 아직 마케팅 슬로건 – 인간 사전 투자 없이는 작동 불가 | The point: AI-DLC is still a marketing slogan — it does not work without human investment up front |

### Slide 215 — 12-3. AI-DLC 자동화 = 사람의 docs 정의 / AI-DLC's Automation Is the Docs a Human Wrote

| AI-DLC 단계 / Stage | AWS 마케팅 표현 / As AWS puts it | 사람이 정의하는 산출물 / What the human actually defines | 산출물 정의 내용 / What goes in it |
|---|---|---|---|
| 1) 요구분석 / Requirements | "AI 자동 분석" — "AI analyzes it automatically" | `docs/01-product.md` | 목표 / 페르소나 / 범위 / 범위 외 — Goal, persona, scope, out of scope |
| 2) 스펙 작성 / Spec | "WHAT/HOW 제안" — "It proposes the what and how" | `docs/02-specs.md` | Task 모델 / REST 5 / 검증 규칙 — The Task model, five REST endpoints, validation rules |
| 3) 코드 생성 / Code generation | "코드 자동 생성" — "Code generated automatically" | `docs/03-design.md` | 스택 결정 / 트레이드오프 / 의존성 정책 — Stack decisions, trade-offs, dependency policy |
| 4) 테스트 / Testing | "AI 자동 생성, 실행" — "The AI writes and runs them" | `docs/05-conventions.md` | 테스트 매트릭스 / 금지 5개 — The test matrix and the five prohibitions |
| 5) 배포 / Deployment | "CI/CD 자동 실행" — "CI/CD runs itself" | `docs/04-tasks` + `05-conventions` | Phase 체크리스트 / 배포 규약 / git 규칙 — Phase checklists, deployment conventions, git rules |

| 한국어 | English |
|---|---|
| **12-3. AI-DLC 자동화 = 사람의 docs 정의** | **12-3. AI-DLC's Automation Is Really the Docs a Human Defined** |
| AWS 자료의 마케팅 표현 vs 실제 작동 원리 – docs 6종 매핑 | The marketing language vs. how it actually works — mapped onto the six documents |
| AI-DLC 5단계 자동화 = 사람이 docs/ 6종에 사전 정의한 결과 | The automation across AI-DLC's five stages is the result of what a human defined in those six documents beforehand |
| AWS 자료는 자동화 결과만 노출, 앞단 사람의 docs 정의 작업은 생략됨 | The AWS material shows only the automated result and leaves out the human's document work that precedes it |
| AI-DLC = 이름은 AI 주도, 실제는 사람이 docs 로 주도, AI 는 실행 | AI-DLC is AI-led in name; in practice the human leads through the docs and the AI executes |

### Slide 216 — 12-4. OpenSpec / Automating the Up-Front Definition

| 단계 / Aspect | 기초편 방식 (수작업) / Foundations (by hand) | 심화편 방식 (OpenSpec) / Advanced (OpenSpec) |
|---|---|---|
| 인간 사전 투자 / Human investment up front | 매번 docs 6종 수작업 — Six documents written by hand, every time | 프레임워크가 골격 제공 — The framework supplies the skeleton |
| 일관성 / Consistency | 사람마다 docs 형식 다름 — Everyone's format differs | 표준화 (proposal/specs/design/tasks) — Standardized as proposal, specs, design, tasks |
| 변경 추적 / Change tracking | 수동 diff — Manual diffs | proposal > specs 델타 자동 — Deltas from proposal to specs, automatically |
| 재사용성 / Reusability | 다음 프로젝트도 처음부터 — The next project starts from nothing | specs 재사용 (언어, 스택 무관) — The specs are reusable, whatever the language or stack |
| AI 주도 가능 영역 / How much the AI can lead | 사전 투자 끝난 좁은 범위 — Only as far as the up-front work reached | 사전 골격 있으니 넓어짐 — Wider, because the skeleton is already there |

| 한국어 | English |
|---|---|
| **12-4. OpenSpec = AI-DLC 완성을 위한 사전 정의 자동화** | **12-4. OpenSpec — Automating the Up-Front Definition That Completes AI-DLC** |
| 수작업 docs 정의 (기초편) > OpenSpec 자동화 (심화편) – 표준화 + 재사용성 | From hand-written docs in Foundations to OpenSpec automation in Advanced — standardization and reuse |
| AI-DLC 마케팅 표현 > 사람의 사전 정의 필수 > OpenSpec 으로 자동화 | The marketing story, then the reality that a human must define it first, then automating that with OpenSpec |
| 사전 준비를 프레임워크로 표준화 = AI-DLC 완성에 비로소 근접 | Standardizing the preparation into a framework is what finally brings AI-DLC within reach |
| > 심화편 OpenSpec 실습의 명분, 사람의 사전 투자를 도구가 대신하는 순간 | > This is the case for the OpenSpec exercises in the Advanced course — the moment a tool takes over the human's up-front investment |

### Slide 217 — 12-5. 기초편 docs ↔ 심화편 OpenSpec 매핑 / Mapping the Docs to OpenSpec

| 기초편 docs / Foundations doc | 심화편 OpenSpec / OpenSpec equivalent |
|---|---|
| `CLAUDE.md` | 유지 (전역 운영 규칙) — Kept, as the global operating rules |
| `00-overview` | 유지 또는 `README.md` — Kept, or becomes README.md |
| `01-product` | `proposal.md` (WHY) |
| `02-specs` | `specs/` 델타 (WHAT) — the specs/ delta (what) |
| `03-design` | `design.md` (HOW) |
| `04-tasks` | `tasks.md` (실행계획) — the execution plan |
| `05-conventions` | 유지 (전역 규약) — Kept, as the global conventions |

| 한국어 | English |
|---|---|
| **12-5. 기초편 docs ↔ 심화편 OpenSpec 매핑 + 체크포인트** | **12-5. Mapping the Foundations Docs to OpenSpec — and the Checkpoints** |
| 기초편 수작업 docs ↔ 심화편 OpenSpec 산출물 매핑 | The hand-written Foundations documents mapped to the OpenSpec artifacts of the Advanced course |
| **기초편 체크포인트** | **Foundations checkpoints** |
| [ ] 9장 CLAUDE.md + docs 6종 작성 | [ ] Ch. 9 — write CLAUDE.md and the six documents |
| [ ] 절대규칙 6개 + 범위 외 명시 | [ ] State the six hard rules and what is out of scope |
| [ ] 10장 "backend 진행해" – 한 마디로 끝 | [ ] Ch. 10 — "do the backend", finished in one sentence |
| [ ] 10 passed – 테스트 매트릭스 검증 | [ ] 10 passed — the test matrix verified |
| [ ] 11장 frontend + 프론트-백 연결 | [ ] Ch. 11 — the frontend, wired to the backend |
| [ ] git 커밋 + push 완료 | [ ] Committed and pushed |
| 구체적 지시 > AI 가 docs 기반 실행 > 결과 재현 가능 = 바이브코딩의 본질 | Specific instruction, then AI execution grounded in the docs, then a reproducible result — that is what vibe coding really is |
