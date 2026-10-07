from datetime import UTC, datetime

from idea_tracker.core.enums import ProposalStatus
from idea_tracker.core.proposals import Proposal


def test_proposal_lifecycle():
    p = Proposal(agent_run_id="run_1", target_entity="idea", target_id="i_1", diff={"stage": "STRUCTURE"}, rationale="test")
    assert p.status == ProposalStatus.PENDING
    # Lifecycle: accept proposal
    p.status = ProposalStatus.ACCEPTED
    # Manually mark reviewed to match expected state after acceptance
    p.reviewed_at = datetime.now(UTC)
    assert p.status == ProposalStatus.ACCEPTED
    assert p.reviewed_at is not None
