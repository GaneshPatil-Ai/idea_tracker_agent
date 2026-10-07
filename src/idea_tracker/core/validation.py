from idea_tracker.core.proposals import Proposal


def validate_proposal(p: Proposal, target_exists: bool = True) -> list[str]:
    errors = []
    if p.target_entity not in ("idea", "assumption", "evidence"):
        errors.append("Invalid target_entity")
    if not target_exists:
        errors.append("Target does not exist")
    for ev in p.evidence_ids:
        # Evidence reference check stub
        pass
    return errors
