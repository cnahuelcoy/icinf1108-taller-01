from datetime import datetime, timezone
from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")


class ApiError(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: str
    detail: str


class ApiResponse(BaseModel, Generic[T]):
    success: bool
    message: str
    data: T | None = None
    error: ApiError | None = None
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
