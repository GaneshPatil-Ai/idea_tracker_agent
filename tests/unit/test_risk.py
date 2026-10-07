from idea_tracker.core.risk import compute_risk_score


def test_risk_calculation():
    assert compute_risk_score(8.0, 0.5) == 4.0
    assert compute_risk_score(0.0, 1.0) == 0.0
