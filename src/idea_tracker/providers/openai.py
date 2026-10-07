
from pydantic import BaseModel

from idea_tracker.providers.base import LLMProvider


class OpenAIProvider(LLMProvider):
    def __init__(self, api_key: str = ""):
        self.api_key = api_key
        self.supports_tool_calling = True
        self.context_window = 128000
        self.cost_per_token = 0.00001

    def generate_structured(self, prompt: str, schema: type[BaseModel]) -> BaseModel:
        raise NotImplementedError("Phase 1 stub")
