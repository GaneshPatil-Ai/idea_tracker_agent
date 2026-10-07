from idea_tracker.providers.ollama import OllamaProvider


def test_provider_interface():
    p = OllamaProvider()
    assert not p.supports_tool_calling
    assert p.context_window > 0
