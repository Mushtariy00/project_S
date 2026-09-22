"""05-conventions 테스트 매트릭스 10건. 메모리 SQLite 로 격리한다."""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.db import Base, get_db
from app.main import app

engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestSession = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def override_get_db():
    db = TestSession()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture()
def client():
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c
    Base.metadata.drop_all(bind=engine)


def make(client, **kwargs):
    payload = {"title": "샘플"}
    payload.update(kwargs)
    return client.post("/api/tasks", json=payload)


# 1. 정상 생성 - POST title 만 - 201
def test_create_with_title_only(client):
    res = make(client)
    assert res.status_code == 201
    assert res.json()["status"] == "todo"


# 2. 목록 - GET /api/tasks - 200, description 없음
def test_list_has_no_description(client):
    make(client, description="설명")
    res = client.get("/api/tasks")
    assert res.status_code == 200
    assert "description" not in res.json()[0]


# 3. 단건 - GET /api/tasks/{id} - 200, description 있음
def test_detail_has_description(client):
    task_id = make(client, description="설명").json()["id"]
    res = client.get(f"/api/tasks/{task_id}")
    assert res.status_code == 200
    assert res.json()["description"] == "설명"


# 4. 수정 - PUT 전 필드 - 200
def test_update_all_fields(client):
    task_id = make(client).json()["id"]
    res = client.put(
        f"/api/tasks/{task_id}",
        json={
            "title": "고친 제목",
            "description": "고친 설명",
            "status": "in_progress",
            "due_at": "2026-12-31T18:00:00Z",
        },
    )
    assert res.status_code == 200
    assert res.json()["status"] == "in_progress"


# 5. 삭제 - DELETE - 204
def test_delete(client):
    task_id = make(client).json()["id"]
    assert client.delete(f"/api/tasks/{task_id}").status_code == 204
    assert client.get(f"/api/tasks/{task_id}").status_code == 404


# 6. title 누락 - 400
def test_missing_title(client):
    assert client.post("/api/tasks", json={"description": "x"}).status_code == 400


# 7. status 오값 - 400
def test_bad_status(client):
    assert make(client, status="wrong").status_code == 400


# 8. due_at 형식 오류 - 400
def test_bad_due_at(client):
    assert make(client, due_at="nope").status_code == 400


# 9. 없는 id - 404
def test_missing_id(client):
    assert client.get("/api/tasks/9999").status_code == 404


# 10. 스펙 외 필드 - 422
def test_unknown_field(client):
    assert make(client, hacker="x").status_code == 422
