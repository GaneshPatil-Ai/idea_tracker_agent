from idea_tracker.agents.planner import PlannerAgent
from idea_tracker.agents.reviewer import ReviewerAgent
from idea_tracker.agents.base import AgentContext
from idea_tracker.core.enums import ProposalStatus, AssumptionStatus


def test_planner_links_milestone_to_assumption():
    agent = PlannerAgent()
    result = agent.run(AgentContext(idea_id="i_1"))
    assert result.proposal.status == ProposalStatus.PENDING
    assert "assumption_ids" in result.proposal.diff
    assert result.proposal.diff["assumption_ids"] == ["asm_highest_risk"]


def test_reviewer_updates_assumption_via_proposal():
    agent = ReviewerAgent()
    result = agent.run(AgentContext(idea_id="i_1"))
    assert result.proposal.diff.get("status") == AssumptionStatus.SUPPORTED.value
    assert result.proposal.status == ProposalStatus.PENDING  # human accepts
