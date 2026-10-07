from idea_tracker.agents.validation import ValidationDesignerAgent
from idea_tracker.agents.critic import CriticAgent
from idea_tracker.agents.decision import DecisionAdvisorAgent
from idea_tracker.agents.base import AgentContext
from idea_tracker.core.enums import ProposalStatus


def test_validation_designer_proposes_experiment():
    agent = ValidationDesignerAgent()
    result = agent.run(AgentContext(idea_id="i_1"))
    assert result.proposal.status == ProposalStatus.PENDING
    assert result.proposal.diff.get("method") == "CUSTOMER_INTERVIEW"
    assert "success_criteria" in result.proposal.diff


def test_critic_produces_findings():
    agent = CriticAgent()
    result = agent.run(AgentContext(idea_id="i_1"))
    findings = result.proposal.diff.get("findings", [])
    assert any("counter-evidence" in f for f in findings)
    assert len(findings) >= 1


def test_decision_advisor_recommends():
    agent = DecisionAdvisorAgent()
    result = agent.run(AgentContext(idea_id="i_1"))
    assert result.proposal.diff.get("recommendation") == "PURSUE"
    assert "tradeoffs" in result.proposal.diff
