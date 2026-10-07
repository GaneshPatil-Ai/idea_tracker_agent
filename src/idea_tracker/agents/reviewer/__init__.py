from idea_tracker.agents.base import AgentContext, AgentResult
from idea_tracker.core.proposals import Proposal
from idea_tracker.core.enums import ProposalStatus, AssumptionStatus


class ReviewerAgent:
    name = "reviewer"

    def run(self, context: AgentContext) -> AgentResult:
        # Review experiment result; canonical state changed only through proposal
        updated = AssumptionStatus.SUPPORTED
        proposal = Proposal(
            agent_run_id="stub_reviewer",
            target_entity="assumption",
            target_id="asm_highest_risk",
            diff={"status": updated.value},
            rationale="Experiment result entered; 4/5 users confirmed. Assumption updated to SUPPORTED via proposal only.",
            evidence_ids=["ev_12"],
            status=ProposalStatus.PENDING,
        )
        return AgentResult(proposal=proposal, agent_run_id="stub_reviewer")
