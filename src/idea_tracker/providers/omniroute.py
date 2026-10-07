import os
from typing import Type
from pydantic import BaseModel
import urllib.request, json
from idea_tracker.providers.base import LLMProvider


class OmniRouteProvider(LLMProvider):
    def __init__(self):
        self.base_url = os.getenv("OMNIROUTE_URL", "http://localhost:20128/v1")
        self.api_key = os.getenv("OMNIROUTE_API_KEY", "")
        self._supports_tool_calling = True
        self._context_window = 128000
        self._cost_per_token = 0.00001

    @property
    def supports_tool_calling(self) -> bool:
        return self._supports_tool_calling

    @property
    def context_window(self) -> int:
        return self._context_window

    @property
    def cost_per_token(self) -> float:
        return self._cost_per_token

    def generate_structured(self, prompt: str, schema: Type[BaseModel]) -> BaseModel:
        req = urllib.request.Request(
            f"{self.base_url}/chat/completions",
            data=json.dumps({
                "model": os.getenv("LLM_MODEL", "BOT2"),
                "messages": [{"role": "user", "content": prompt}],
            }).encode(),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read())
                content = data.get("choices", [{}])[0].get("message", {}).get("content", "{}")
                return schema.parse_raw(content)
        except Exception as exc:
            # Graceful: if endpoint down, return empty or raise with context
            raise RuntimeError(f"OmniRoute call failed: {exc}")
