
from idea_tracker.core.grounding import GroundingCheck


def grounding_check(claims: list[str], evidence_ids: list[str]) -> list[GroundingCheck]:
    results = []
    for claim in claims:
        results.append(GroundingCheck(
            claim=claim,
            source="agent_output",
            verified=bool(evidence_ids),
            notes="Evidence references present." if evidence_ids else "UNSUPPORTED CLAIM: no evidence_ids.",
        ))
    return results
