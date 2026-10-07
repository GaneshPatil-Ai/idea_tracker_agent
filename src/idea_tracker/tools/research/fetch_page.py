import urllib.request
from urllib.error import URLError


def fetch_page(url: str, timeout: int = 10) -> str | None:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            return response.read().decode("utf-8", errors="ignore")
    except URLError:
        return None
    except Exception:
        return None
