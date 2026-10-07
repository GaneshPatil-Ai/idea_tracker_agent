from idea_tracker.agents.base import Agent, AgentContext, AgentResult
from idea_tracker.core.proposals import Proposal
from idea_tracker.core.enums import ProposalStatus, DecisionChoice


class DecisionAdvisorAgent:
    name = "decision_advisor"

    def run(self, context: AgentContext) -> AgentResult:
        recommendation = DecisionChoice.PURSUE
        proposal = Proposal(
            agent_run_id="stub_decision_advisor",
            target_entity="decision",
            target_id=context.idea_id or "idea_unknown",
            diff={
                "recommendation": recommendation.value,
                "confidence": 0.6,
                "tradeoffs": ["Low evidence; high risk score; pursue only after validation experiment."],
                "what_would_change": "If customer interviews refute demand assumption (supported < 2/5), recommend KILL.",
            },
            rationale="AI recommends PURSUE with 60% confidence given current evidence. Human must select final choice.",
            evidence_ids=[],
            status=ProposalStatus.PENDING,
        )
        return AgentResult(proposal=proposal, agent_run_id="stub_decision_advisor")
