from typing import Protocol

from idea_tracker.core.models import Evidence


class SearchProvider(Protocol):
    def search(self, query: str, max_results: int = 5) -> list[Evidence]:
        ...
    def fetch_page(self, url: str) -> str | None:
        ...
