"""앱 진입점. 검증 실패를 02-specs 가 정한 코드로 바꿔 돌려준다."""
import logging
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from .db import Base, engine
from .routers import tasks

# print 디버깅 금지 (05-conventions). logging 모듈을 쓴다.
logger = logging.getLogger(__name__)

app = FastAPI(title="TaskFlow Pro API", version="0.1.0")

Base.metadata.create_all(bind=engine)
app.include_router(tasks.router)


@app.exception_handler(RequestValidationError)
async def on_validation_error(request: Request, exc: RequestValidationError):
    """스펙 외 필드는 422, 나머지 형식 위반은 400 으로 돌려준다."""
    errors = exc.errors()
    extra = any(e.get("type") == "extra_forbidden" for e in errors)
    code = 422 if extra else 400
    logger.info("검증 실패 %s %s -> %s", request.method, request.url.path, code)
    detail = [
        {"loc": list(e.get("loc", [])), "msg": e.get("msg"), "type": e.get("type")}
        for e in errors
    ]
    return JSONResponse(status_code=code, content={"detail": detail})


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


# 03-design 2번 - 프론트는 백엔드가 같은 오리진에서 제공한다.
# file:// 로 직접 열지 않는다. API 라우트 뒤에 붙여야 /api 가 가려지지 않는다.
FRONTEND_DIR = Path(__file__).resolve().parent.parent.parent / "frontend"
if FRONTEND_DIR.is_dir():
    app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
