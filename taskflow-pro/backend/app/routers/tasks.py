"""CRUD API 5개. 경로는 /api/ 접두사를 쓴다 (02-specs)."""
from datetime import timezone

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import Task
from ..schemas import TaskCreate, TaskDetail, TaskListItem, TaskUpdate

router = APIRouter(prefix="/api/tasks", tags=["tasks"])


def strip_tz(value):
    """due_at 은 UTC 로 저장한다. 들어온 오프셋을 UTC 로 맞춘 뒤 naive 로 둔다."""
    if value is None:
        return None
    if value.tzinfo is not None:
        value = value.astimezone(timezone.utc).replace(tzinfo=None)
    return value


def find_or_404(db: Session, task_id: int) -> Task:
    task = db.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="없는 업무다")
    return task


@router.post("", response_model=TaskDetail, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate, db: Session = Depends(get_db)) -> Task:
    task = Task(
        title=payload.title,
        description=payload.description,
        status=payload.status,
        due_at=strip_tz(payload.due_at),
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.get("", response_model=list[TaskListItem])
def list_tasks(db: Session = Depends(get_db)) -> list[Task]:
    return list(db.scalars(select(Task).order_by(Task.id)))


@router.get("/{task_id}", response_model=TaskDetail)
def read_task(task_id: int, db: Session = Depends(get_db)) -> Task:
    return find_or_404(db, task_id)


@router.put("/{task_id}", response_model=TaskDetail)
def update_task(
    task_id: int, payload: TaskUpdate, db: Session = Depends(get_db)
) -> Task:
    task = find_or_404(db, task_id)
    data = payload.model_dump(exclude_unset=True)
    if "due_at" in data:
        data["due_at"] = strip_tz(data["due_at"])
    for key, value in data.items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)) -> Response:
    task = find_or_404(db, task_id)
    db.delete(task)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
