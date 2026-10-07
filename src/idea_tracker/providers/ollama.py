
from pydantic import BaseModel

from idea_tracker.providers.base import LLMProvider


class OllamaProvider(LLMProvider):
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url
        self._supports_tool_calling = False
        self._context_window = 4096
        self._cost_per_token = 0.0

    @property
    def supports_tool_calling(self) -> bool:
        return self._supports_tool_calling

    @property
    def context_window(self) -> int:
        return self._context_window

    @property
    def cost_per_token(self) -> float:
        return self._cost_per_token

    def generate_structured(self, prompt: str, schema: type[BaseModel]) -> BaseModel:
        # MVP stub: for Phase 1, return empty instance or raise.
        # Real implementation calls /api/generate with JSON schema enforcement.
        return schema()
