from idea_tracker.agents.base import AgentContext
from idea_tracker.agents.next_action import resolve_next_action
from idea_tracker.agents.risk import RiskAnalystAgent
from idea_tracker.agents.structurer import StructurerAgent
from idea_tracker.core.enums import ProposalStatus


def test_structurer_proposes_structured_idea():
    agent = StructurerAgent()
    result = agent.run(AgentContext(idea_id="i_1"))
    assert result.proposal.target_entity == "idea"
    assert result.proposal.status == ProposalStatus.PENDING
    assert "problem" in result.proposal.diff
    assert len(result.proposal.diff.get("open_questions", [])) <= 3


def test_risk_analyst_computes_score_deterministically():
    agent = RiskAnalystAgent()
    result = agent.run(AgentContext(idea_id="i_1"))
    diff = result.proposal.diff
    # Deterministic: impact * uncertainty = 6.0
    assert diff["impact"] == 8.0
    assert diff["uncertainty"] == 0.75
    # Risk score computed by code
    assert diff["impact"] * diff["uncertainty"] == 6.0
    assert diff["status"] == "UNVERIFIED"


def test_next_action_explains_why():
    explanation = resolve_next_action("asm_001", 6.0)
    assert "Next action" in explanation
    assert "Why" in explanation
    assert "assumption" in explanation
