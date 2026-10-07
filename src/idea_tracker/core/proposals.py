from datetime import datetime, UTC
from typing import Any

from pydantic import BaseModel, Field, model_validator

from idea_tracker.core.enums import ProposalStatus


class Proposal(BaseModel):
    id: str = Field(default_factory=lambda: f"prop_{datetime.now(UTC).strftime('%Y%m%d%H%M%S%f')}")
    agent_run_id: str
    target_entity: str  # e.g., "idea", "assumption", "evidence"
    target_id: str
    diff: dict[str, Any] = Field(default_factory=dict)
    rationale: str
    evidence_ids: list[str] = Field(default_factory=list)
    status: ProposalStatus = ProposalStatus.PENDING
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    reviewed_at: datetime | None = None

    @model_validator(mode="after")
    def compute_reviewed(self) -> "Proposal":
        if self.status != ProposalStatus.PENDING and self.reviewed_at is None:
            self.reviewed_at = datetime.now(UTC)
        return self
