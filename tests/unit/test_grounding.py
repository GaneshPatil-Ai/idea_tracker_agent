from idea_tracker.core.grounding import verify_quote


def test_verify_quote():
    result = verify_quote("http://example.com", "hello", "hello world")
    assert result.verified is True
    result_bad = verify_quote("http://example.com", "goodbye", "hello world")
    assert result_bad.verified is False
