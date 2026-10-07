from enum import Enum


class Stage(str, Enum):
    CAPTURE = "CAPTURE"
    STRUCTURE = "STRUCTURE"
    UNDERSTAND = "UNDERSTAND"
    VALIDATE = "VALIDATE"
    DECIDE = "DECIDE"
    EXECUTE = "EXECUTE"
    REVIEW = "REVIEW"
    LEARN = "LEARN"


class AssumptionType(str, Enum):
    DESIRABILITY = "DESIRABILITY"
    VIABILITY = "VIABILITY"
    FEASIBILITY = "FEASIBILITY"
    USABILITY = "USABILITY"


class AssumptionStatus(str, Enum):
    UNVERIFIED = "UNVERIFIED"
    SUPPORTED = "SUPPORTED"
    REFUTED = "REFUTED"
    MIXED = "MIXED"


class EvidenceStance(str, Enum):
    SUPPORTING = "SUPPORTING"
    CONTRADICTING = "CONTRADICTING"
    NEUTRAL = "NEUTRAL"


class ProposalStatus(str, Enum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    EDITED = "EDITED"
    REJECTED = "REJECTED"


class DecisionChoice(str, Enum):
    PURSUE = "PURSUE"
    PIVOT = "PIVOT"
    PARK = "PARK"
    KILL = "KILL"
