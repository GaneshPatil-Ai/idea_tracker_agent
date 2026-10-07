from idea_tracker.agents.base import Agent, AgentContext, AgentResult
from idea_tracker.core.enums import EvidenceStance, ProposalStatus
from idea_tracker.core.models import Evidence
from idea_tracker.core.proposals import Proposal


class ResearcherAgent:
    name = "researcher"
    # Strict bounds per spec
    max_steps = 3
    max_sources = 5
    max_duration = 300  # seconds

    def run(self, context: AgentContext) -> AgentResult:
        # Bounded research: returns evidence proposals with verified stance
        evidence_items = [
            Evidence(
                idea_id=context.idea_id or "idea_unknown",
                url="https://example.com/source1",
                title="Example source supporting assumption",
                source="web_search",
                quote="Direct evidence quote.",
                stance=EvidenceStance.SUPPORTING,
                reliability=0.8,
            ),
            Evidence(
                idea_id=context.idea_id or "idea_unknown",
                url="https://example.com/source2",
                title="Counter-evidence source",
                source="web_search",
                quote="Contradictory claim.",
                stance=EvidenceStance.CONTRADICTING,
                reliability=0.7,
            ),
        ]
        proposal = Proposal(
            agent_run_id="stub_researcher",
            target_entity="evidence",
            target_id="evidence_bundle",
            diff={"evidence_items": [e.id for e in evidence_items]},
            rationale=f"Collected {len(evidence_items)} sources within bounds (max_steps={self.max_steps}, max_sources={self.max_sources}).",
            evidence_ids=[],
            status=ProposalStatus.PENDING,
        )
        return AgentResult(proposal=proposal, agent_run_id="stub_researcher")
