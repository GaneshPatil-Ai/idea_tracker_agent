from datetime import datetime, UTC
from typing import Any

from pydantic import BaseModel, Field


class AgentRun(BaseModel):
    id: str = Field(default_factory=lambda: f"run_{datetime.now(UTC).strftime('%Y%m%d%H%M%S%f')}")
    agent: str
    provider: str
    model: str
    prompt_hash: str | None = None
    input_hash: str | None = None
    input_payload: Any | None = None
    output_payload: Any | None = None
    tokens_in: int | None = None
    tokens_out: int | None = None
    duration_ms: int | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))