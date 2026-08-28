from datetime import datetime, timezone
from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    success: bool
    message: str
    data: T | None = None
    error: str | dict[str, Any] | list[Any] | None = None
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
