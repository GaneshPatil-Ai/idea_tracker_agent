from typing import Protocol

from pydantic import BaseModel


class LLMProvider(Protocol):
    def generate_structured(self, prompt: str, schema: type[BaseModel]) -> BaseModel:
        ...

    @property
    def supports_tool_calling(self) -> bool:
        ...

    @property
    def context_window(self) -> int:
        ...

    @property
    def cost_per_token(self) -> float:
        ...
