from idea_tracker.agents.base import Agent, AgentContext, AgentResult
from idea_tracker.core.agent_run import AgentRun
from idea_tracker.core.enums import ProposalStatus
from idea_tracker.core.proposals import Proposal


class StructurerAgent:
    name = "structurer"

    def run(self, context: AgentContext) -> AgentResult:
        proposal = Proposal(
            agent_run_id="stub_structurer",
            target_entity="idea",
            target_id=context.idea_id or "idea_unknown",
            diff={
                "problem": "structured problem from raw text",
                "target_user": "inferred user",
                "solution": "brief solution summary",
                "value_proposition": "value summary",
                "open_questions": ["clarify scope"],
            },
            rationale="Converted raw idea into structured fields. 3 clarification questions included.",
            evidence_ids=[],
            status=ProposalStatus.PENDING,
        )
        return AgentResult(proposal=proposal, agent_run_id="stub_structurer")
