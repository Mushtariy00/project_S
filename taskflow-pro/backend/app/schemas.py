"""요청과 응답 스키마. 스펙에 없는 필드는 받지 않는다 (extra=forbid)."""
from datetime import datetime, timezone

from pydantic import BaseModel, ConfigDict, Field, field_serializer

from .models import TaskStatus

STRICT = ConfigDict(extra="forbid")


def as_utc_iso(value: datetime | None) -> str | None:
    """응답의 날짜는 UTC ISO 8601 로 통일한다 (02-specs)."""
    if value is None:
        return None
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc).isoformat()


class TaskCreate(BaseModel):
    model_config = STRICT

    title: str = Field(min_length=1, max_length=200)
    description: str | None = None
    status: TaskStatus = TaskStatus.todo
    due_at: datetime | None = None


class TaskUpdate(BaseModel):
    model_config = STRICT

    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = None
    status: TaskStatus | None = None
    due_at: datetime | None = None


class TaskListItem(BaseModel):
    """목록 응답. description 을 뺀다 (02-specs)."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    status: TaskStatus
    due_at: datetime | None
    created_at: datetime
    updated_at: datetime

    @field_serializer("due_at", "created_at", "updated_at")
    def _iso(self, value: datetime | None) -> str | None:
        return as_utc_iso(value)


class TaskDetail(TaskListItem):
    """단건 응답. description 을 넣는다 (02-specs)."""

    description: str | None
