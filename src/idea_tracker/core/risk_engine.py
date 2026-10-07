from idea_tracker.core.risk import compute_risk_score


def compute_risk_for_assumption(impact: float, uncertainty: float) -> float:
    return compute_risk_score(impact, uncertainty)
