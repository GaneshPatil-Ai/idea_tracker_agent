from pydantic import BaseModel


class GroundingCheck(BaseModel):
    claim: str
    source: str
    verified: bool
    notes: str = ""


def compute_risk_score(impact: float, uncertainty: float) -> float:
    return impact * uncertainty


def verify_quote(url: str, quote: str, content: str) -> GroundingCheck:
    verified = quote in content
    return GroundingCheck(
        claim=quote,
        source=url,
        verified=verified,
        notes="Quote verified in fetched content." if verified else "Quote NOT found in fetched content.",
    )
