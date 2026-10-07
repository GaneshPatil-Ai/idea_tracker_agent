# Idea Tracker

**Idea Tracker** is a local-first, deterministic workflow engine with narrow, schema-constrained AI specialists, human approval gates, and complete traceability.

It is designed to help software engineers, product managers, and builders move raw ideas through a rigorous validation pipeline without handing decision-making authority to autonomous LLM loops.

---

## Key Invariant: Agents Propose, Humans Decided

AI agents in Idea Tracker **never directly mutate canonical database entities**. Every AI-generated output is produced as a strictly validated `Proposal`.

```text
       ┌──────────────────────┐
       │   Deterministic      │
       │    Orchestrator      │
       └──────────┬───────────┘
                  │
 ┌────────────────┼────────────────┐
 ▼                ▼                ▼
Structurer    Researcher      Risk Analyst ... (Specialist Agents)
 │                │                │
 └────────────────┼────────────────┘
                  ▼
            Proposal Inbox
                  │
          HUMAN APPROVAL GATE
                  │
    ┌─────────────┴─────────────┐
    ▼                           ▼
Accept / Edit                 Reject
    │
    ▼
Canonical SQLite State
```

1. **Deterministic Orchestration**: Workflow state, stage gates, risk scores, and tool boundaries are managed by deterministic Python code.
2. **Schema-Constrained Agents**: Each agent operates with tight input/output Pydantic schemas.
3. **Traceability**: Every execution creates an immutable `AgentRun` audit record.
4. **Deterministic Risk Scoring**: Risk score is strictly calculated by application code (`risk_score = impact × uncertainty`), never hallucinated or directly output by an LLM.
5. **Grounding & Quote Verification**: Factual claims require cited evidence IDs. Quotes are verified directly against source page content.

---

## Workflow Stages

Idea Tracker guides an idea through eight lifecycle stages:

```text
CAPTURE ──► STRUCTURE ──► UNDERSTAND ──► VALIDATE ──► DECIDE ──► EXECUTE ──► REVIEW ──► LEARN
```

| Stage | Responsible Component | Output / Purpose |
|---|---|---|
| **CAPTURE** | User / CLI | Raw text problem statement & initial idea notes |
| **STRUCTURE** | `StructurerAgent` | Structured problem, target user, solution, value prop, max 3 open questions |
| **UNDERSTAND** | `RiskAnalystAgent` & `ResearcherAgent` | Identified assumptions, impact/uncertainty scoring, web evidence gathering |
| **VALIDATE** | `ValidationDesignerAgent` | Bounded, low-cost experiment specs with predefined success/failure criteria |
| **DECIDE** | `CriticAgent` & `DecisionAdvisorAgent` | Independent flaw identification & decision recommendations (`PURSUE`, `PIVOT`, `PARK`, `KILL`) |
| **EXECUTE** | `PlannerAgent` | Milestone & task generation linked directly to de-risking assumptions |
| **REVIEW** | `ReviewerAgent` | Experiment result evaluation & assumption status updates |
| **LEARN** | `NextActionResolver` | Deterministic resolution of the highest-risk unverified assumption |

---

## Architecture & Repository Structure

```text
idea-tracker/
├── pyproject.toml              # UV / Hatchling dependency & tool definitions
├── .env.example                # Example environment variable configuration
├── README.md
├── src/
│   └── idea_tracker/
│       ├── core/               # Domain models, enums, proposals, grounding & risk calculation
│       ├── storage/            # SQLAlchemy 2.x SQLite persistence layer
│       ├── agents/             # Specialist agents (Structurer, Researcher, Risk, etc.)
│       ├── tools/              # Research, fetch, and verification tools
│       ├── providers/          # LLM provider abstractions (Ollama, OmniRoute, OpenAI)
│       └── cli/                # Command-line interface
└── tests/
    └── unit/                   # Comprehensive unit test suite
```

---

## Tech Stack

* **Language**: Python 3.12+
* **Package Manager**: `uv`
* **Data Models & Validation**: Pydantic v2
* **Persistence**: SQLAlchemy 2.x with SQLite
* **CLI**: Typer
* **Quality & Testing**: pytest, Ruff, mypy
* **LLM Providers**: Pluggable architecture supporting local models (Ollama, OmniRoute) and cloud APIs (OpenAI).

---

## Getting Started

### Prerequisites

Install `uv` (Fast Python package installer and resolver):

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Installation

1. Clone the repository and navigate into the project root:
   ```bash
   cd idea-tracker
   ```

2. Sync dependencies and create the virtual environment using `uv`:
   ```bash
   uv sync --dev
   ```

3. Configure environment variables:
   ```bash
   cp .env.example .env
   ```

   Edit `.env` to configure your preferred LLM provider and settings:
   ```env
   LLM_PROVIDER=omniroute
   LLM_MODEL=BOT2
   OMNIROUTE_URL=http://localhost:20128/v1
   OMNIROUTE_API_KEY=your_api_key_here
   DATABASE_URL=sqlite:///data/idea_tracker.db
   ```

---

## Verification & Testing

Run the full suite of unit tests via `uv`:

```bash
uv run pytest tests/unit/ -v
```

Run linting checks:

```bash
uv run ruff check src/ tests/
```

---

## Usage Example

### Running the End-to-End Pipeline Programmatically

```python
from idea_tracker.core.models import Idea
from idea_tracker.agents.base import AgentContext
from idea_tracker.agents.structurer import StructurerAgent
from idea_tracker.agents.risk import RiskAnalystAgent
from idea_tracker.agents.next_action import resolve_next_action

# 1. Capture an Idea
idea = Idea(
    title="Local-first Note Graph",
    raw_text="A tool for linking markdown notes locally with automated summary nodes."
)

# 2. Structure the Idea via Structurer Agent
context = AgentContext(idea_id=idea.id)
structurer = StructurerAgent()
structure_proposal = structurer.run(context).proposal

print("Structure Proposal Status:", structure_proposal.status)  # PENDING
print("Proposed Problem:", structure_proposal.diff["problem"])

# 3. Analyze Risks
risk_agent = RiskAnalystAgent()
risk_proposal = risk_agent.run(context).proposal

# 4. Resolve Next Action Deterministically
next_action_text = resolve_next_action(
    assumption_id="asm_001",
    risk_score=risk_proposal.diff["impact"] * risk_proposal.diff["uncertainty"]
)
print(next_action_text)
```

---

## License

MIT License.
