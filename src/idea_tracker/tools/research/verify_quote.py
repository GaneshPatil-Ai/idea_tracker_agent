from idea_tracker.core.grounding import verify_quote
from idea_tracker.tools.research.fetch_page import fetch_page


def verify_quote_from_url(url: str, quote: str) -> bool:
    content = fetch_page(url)
    if content is None:
        return False
    result = verify_quote(url, quote, content)
    return result.verified
