import os
from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_URL = os.getenv("DATABASE_URL", "sqlite:///data/idea_tracker.db")
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


class IdeaDB(Base):
    __tablename__ = "ideas"
    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    raw_text = Column(Text)
    problem = Column(Text)
    target_user = Column(String)
    solution = Column(Text)
    value_proposition = Column(Text)
    stage = Column(String, default="CAPTURE")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class AssumptionDB(Base):
    __tablename__ = "assumptions"
    id = Column(String, primary_key=True)
    idea_id = Column(String, ForeignKey("ideas.id"), nullable=False)
    statement = Column(Text, nullable=False)
    type = Column(String, default="DESIRABILITY")
    status = Column(String, default="UNVERIFIED")
    impact = Column(Float, default=0.0)
    uncertainty = Column(Float, default=0.0)
    risk_score = Column(Float, default=0.0)
    justification = Column(Text)
    evidence_ids = Column(Text, default="")  # JSON list
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class EvidenceDB(Base):
    __tablename__ = "evidence"
    id = Column(String, primary_key=True)
    idea_id = Column(String, ForeignKey("ideas.id"), nullable=False)
    url = Column(String)
    title = Column(String)
    source = Column(String)
    quote = Column(Text)
    retrieved_at = Column(DateTime, default=datetime.utcnow)
    stance = Column(String, default="NEUTRAL")
    reliability = Column(Float, default=1.0)
    content_hash = Column(String)


class ProposalDB(Base):
    __tablename__ = "proposals"
    id = Column(String, primary_key=True)
    agent_run_id = Column(String, nullable=False)
    target_entity = Column(String, nullable=False)
    target_id = Column(String, nullable=False)
    diff = Column(Text)  # JSON
    rationale = Column(Text)
    evidence_ids = Column(Text, default="")
    status = Column(String, default="PENDING")
    created_at = Column(DateTime, default=datetime.utcnow)
    reviewed_at = Column(DateTime)


class AgentRunDB(Base):
    __tablename__ = "agent_runs"
    id = Column(String, primary_key=True)
    agent = Column(String, nullable=False)
    provider = Column(String, nullable=False)
    model = Column(String, nullable=False)
    prompt_hash = Column(String)
    input_hash = Column(String)
    input_payload = Column(Text)
    output_payload = Column(Text)
    tokens_in = Column(Integer)
    tokens_out = Column(Integer)
    duration_ms = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)


def init_db():
    Base.metadata.create_all(bind=engine)
