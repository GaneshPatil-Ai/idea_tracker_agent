from typing import Protocol

from pydantic import BaseModel

from idea_tracker.core.proposals import Proposal


class AgentContext(BaseModel):
    idea_id: str = ""
    stage: str = "CAPTURE"


class AgentResult(BaseModel):
    proposal: Proposal
    agent_run_id: str = ""


class Agent(Protocol):
    name: str
    def run(self, context: AgentContext) -> AgentResult:
        ...
