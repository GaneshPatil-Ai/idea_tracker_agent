from idea_tracker.agents.base import AgentContext, AgentResult
from idea_tracker.core.enums import ProposalStatus
from idea_tracker.core.proposals import Proposal


def resolve_next_action(assumption_id: str, risk_score: float, has_active_experiment: bool = False) -> str:
    explanation = (
        f"Next action: Design cheapest experiment for assumption {assumption_id}.\n"
        f"Why: Risk score {risk_score} is highest among unverified assumptions.\n"
        f"Experiment: Customer interview (lowest cost to reduce uncertainty).\n"
        f"Expected result: Clarify demand; if supported, reduce uncertainty."
    )
    return explanation


class NextActionResolver:
    name = "next_action_resolver"

    def run(self, context: AgentContext) -> AgentResult:
        proposal = Proposal(
            agent_run_id="stub_next_action",
            target_entity="idea",
            target_id=context.idea_id or "idea_unknown",
            diff={"next_action": "Interview 5 target users.", "explanation": resolve_next_action("asm_001", 6.0)},
            rationale="Highest-risk unverified assumption selected; cheapest meaningful experiment proposed.",
            evidence_ids=[],
            status=ProposalStatus.PENDING,
        )
        return AgentResult(proposal=proposal, agent_run_id="stub_next_action")
