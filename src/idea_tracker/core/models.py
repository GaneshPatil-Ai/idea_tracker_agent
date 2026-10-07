from datetime import datetime, UTC

from pydantic import BaseModel, Field

from idea_tracker.core.enums import (
    AssumptionStatus,
    AssumptionType,
    DecisionChoice,
    EvidenceStance,
    Stage,
)


class Idea(BaseModel):
    id: str = Field(default_factory=lambda: f"idea_{datetime.now(UTC).strftime('%Y%m%d%H%M%S%f')}")
    title: str
    raw_text: str
    problem: str | None = None
    target_user: str | None = None
    solution: str | None = None
    value_proposition: str | None = None
    stage: Stage = Stage.CAPTURE
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class Assumption(BaseModel):
    id: str = Field(default_factory=lambda: f"asm_{datetime.now(UTC).strftime('%Y%m%d%H%M%S%f')}")
    idea_id: str
    statement: str
    type: AssumptionType
    status: AssumptionStatus = AssumptionStatus.UNVERIFIED
    impact: float = 0.0
    uncertainty: float = 0.0
    risk_score: float = Field(default=0.0)
    justification: str | None = None
    evidence_ids: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class Evidence(BaseModel):
    id: str = Field(default_factory=lambda: f"ev_{datetime.now(UTC).strftime('%Y%m%d%H%M%S%f')}")
    idea_id: str
    url: str | None = None
    title: str | None = None
    source: str | None = None
    quote: str | None = None
    retrieved_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    stance: EvidenceStance = EvidenceStance.NEUTRAL
    reliability: float = 1.0
    content_hash: str | None = None


class Experiment(BaseModel):
    id: str = Field(default_factory=lambda: f"exp_{datetime.now(UTC).strftime('%Y%m%d%H%M%S%f')}")
    idea_id: str
    assumption_id: str
    method: str
    hypothesis: str
    success_criteria: str
    failure_criteria: str
    deadline: datetime | None = None
    result: str | None = None
    status: str = "PENDING"
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    completed_at: datetime | None = None


class Milestone(BaseModel):
    id: str = Field(default_factory=lambda: f"ms_{datetime.now(UTC).strftime('%Y%m%d%H%M%S%f')}")
    idea_id: str
    name: str
    description: str
    acceptance_criteria: str
    assumption_ids: list[str] = Field(default_factory=list)
    estimate: str = ""


class Task(BaseModel):
    id: str = Field(default_factory=lambda: f"tsk_{datetime.now(UTC).strftime('%Y%m%d%H%M%S%f')}")
    milestone_id: str
    name: str
    description: str
    depends_on: list[str] = Field(default_factory=list)
    acceptance_criteria: str
    estimate: str = ""
    status: str = "NOT_STARTED"


class Decision(BaseModel):
    id: str = Field(default_factory=lambda: f"dec_{datetime.now(UTC).strftime('%Y%m%d%H%M%S%f')}")
    idea_id: str
    choice: DecisionChoice
    rationale: str | None = None
    evidence_ids: list[str] = Field(default_factory=list)
    decided_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    review_date: datetime | None = None