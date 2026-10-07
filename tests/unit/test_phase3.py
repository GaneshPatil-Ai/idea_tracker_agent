from idea_tracker.agents.base import AgentContext
from idea_tracker.agents.researcher import ResearcherAgent
from idea_tracker.core.grounding_check import grounding_check
from idea_tracker.tools.research.verify_quote import verify_quote_from_url


def test_researcher_bounded():
    agent = ResearcherAgent()
    assert agent.max_steps == 3
    assert agent.max_sources == 5
    result = agent.run(AgentContext(idea_id="i_1"))
    assert result.proposal.status.name == "PENDING"


def test_grounding_flags_unsupported():
    checks = grounding_check(["unsupported claim"], [])
    assert checks[0].verified is False
    assert "UNSUPPORTED" in checks[0].notes

    checks2 = grounding_check(["supported claim"], ["ev_1"])
    assert checks2[0].verified is True


def test_verify_quote_graceful_failure():
    # Real fetch attempt; graceful on bad URL
    result = verify_quote_from_url("http://invalid.localhost/nonexistent", "test")
    assert result is False
