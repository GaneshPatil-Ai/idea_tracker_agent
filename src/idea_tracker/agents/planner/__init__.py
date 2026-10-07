from idea_tracker.agents.base import AgentContext, AgentResult
from idea_tracker.core.proposals import Proposal
from idea_tracker.core.enums import ProposalStatus
from idea_tracker.core.models import Milestone, Task


class PlannerAgent:
    name = "planner"

    def run(self, context: AgentContext) -> AgentResult:
        milestone = Milestone(
            idea_id=context.idea_id or "idea_unknown",
            name="Validate demand assumption",
            description="Interview 5 target users to verify demand.",
            acceptance_criteria="4/5 confirm need; assumption status updated.",
            assumption_ids=["asm_highest_risk"],
            estimate="1 week",
        )
        task = Task(
            milestone_id=milestone.id,
            name="Conduct interviews",
            description="Reach 5 users; record responses.",
            depends_on=[],
            acceptance_criteria="Notes recorded; evidence references added.",
            estimate="2 days",
            status="NOT_STARTED",
        )
        proposal = Proposal(
            agent_run_id="stub_planner",
            target_entity="milestone",
            target_id=milestone.id,
            diff={
                "milestone": milestone.name,
                "tasks": [task.name],
                "assumption_ids": milestone.assumption_ids,
                "dependencies": task.depends_on,
            },
            rationale="Plan connects milestone to specific assumption (de-risking), with deterministic topological dependency (none for first task).",
            evidence_ids=[],
            status=ProposalStatus.PENDING,
        )
        return AgentResult(proposal=proposal, agent_run_id="stub_planner")
