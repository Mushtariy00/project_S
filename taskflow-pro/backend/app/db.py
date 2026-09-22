"""DB 연결. 03-design 3번 결정에 따라 SQLite + SQLAlchemy ORM 을 쓴다."""
import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# 시크릿 하드코딩 금지 (05-conventions). 경로는 환경변수로 덮어쓸 수 있다.
DEFAULT_URL = f"sqlite:///{Path(__file__).resolve().parent.parent / 'tasks.db'}"
DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_URL)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass


def get_db():
    """요청 하나에 세션 하나. 끝나면 반드시 닫는다."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
