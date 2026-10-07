from idea_tracker.agents.base import Agent, AgentContext, AgentResult
from idea_tracker.core.proposals import Proposal
from idea_tracker.core.enums import ProposalStatus


class CriticAgent:
    name = "critic"

    def run(self, context: AgentContext) -> AgentResult:
        findings = [
            "No counter-evidence included for demand assumption.",
            "Experiment criteria are predefined but not linked to assumption status change.",
            "No unsupported claim check performed yet.",
        ]
        proposal = Proposal(
            agent_run_id="stub_critic",
            target_entity="idea",
            target_id=context.idea_id or "idea_unknown",
            diff={"findings": findings},
            rationale="Independent review completed. 3 findings: missing counter-evidence, criteria linkage, unsupported claims.",
            evidence_ids=[],
            status=ProposalStatus.PENDING,
        )
        return AgentResult(proposal=proposal, agent_run_id="stub_critic")
