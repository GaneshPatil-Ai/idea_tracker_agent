from idea_tracker.agents.base import Agent, AgentContext, AgentResult
from idea_tracker.core.agent_run import AgentRun
from idea_tracker.core.enums import AssumptionStatus, AssumptionType, ProposalStatus
from idea_tracker.core.models import Assumption
from idea_tracker.core.proposals import Proposal


class RiskAnalystAgent:
    name = "risk_analyst"

    def run(self, context: AgentContext) -> AgentResult:
        # Deterministic risk: LLM proposes impact/uncertainty; code computes score
        assumption = Assumption(
            idea_id=context.idea_id,
            statement="Core value proposition is desired by target users.",
            type=AssumptionType.DESIRABILITY,
            impact=8.0,
            uncertainty=0.75,
            risk_score=8.0 * 0.75,
            justification="No direct customer interviews yet; high impact, high uncertainty.",
            evidence_ids=[],
            status=AssumptionStatus.UNVERIFIED,
        )
        proposal = Proposal(
            agent_run_id="stub_risk_analyst",
            target_entity="assumption",
            target_id=assumption.id,
            diff={
                "impact": assumption.impact,
                "uncertainty": assumption.uncertainty,
                "status": assumption.status,
                "justification": assumption.justification,
                "evidence_ids": assumption.evidence_ids,
            },
            rationale=f"Risk score computed deterministically: {assumption.risk_score}. Evidence IDs remain empty (UNVERIFIED).",
            evidence_ids=[],
            status=ProposalStatus.PENDING,
        )
        return AgentResult(proposal=proposal, agent_run_id="stub_risk_analyst")
