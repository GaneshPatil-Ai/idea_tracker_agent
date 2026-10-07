from idea_tracker.agents.base import Agent, AgentContext, AgentResult
from idea_tracker.core.proposals import Proposal
from idea_tracker.core.enums import ProposalStatus
from idea_tracker.core.models import Experiment


class ValidationDesignerAgent:
    name = "validation_designer"

    def run(self, context: AgentContext) -> AgentResult:
        experiment = Experiment(
            idea_id=context.idea_id or "idea_unknown",
            assumption_id="asm_highest_risk",
            method="CUSTOMER_INTERVIEW",
            hypothesis="Target users value the proposed solution.",
            success_criteria="4 out of 5 interviewed users confirm need.",
            failure_criteria="Fewer than 2 confirm; demand unverified.",
        )
        proposal = Proposal(
            agent_run_id="stub_validation_designer",
            target_entity="experiment",
            target_id=experiment.id,
            diff={
                "method": experiment.method,
                "hypothesis": experiment.hypothesis,
                "success_criteria": experiment.success_criteria,
                "failure_criteria": experiment.failure_criteria,
            },
            rationale="Cheapest experiment (customer interview) selected for highest-risk unverified assumption to reduce uncertainty.",
            evidence_ids=[],
            status=ProposalStatus.PENDING,
        )
        return AgentResult(proposal=proposal, agent_run_id="stub_validation_designer")
