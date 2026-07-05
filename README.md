# Contract Review Agent

[![CI](https://github.com/kogunlowo123/contract-review-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/contract-review-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Legal | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Contract review agent that analyzes legal agreements, identifies risky clauses, compares against standard terms, flags deviations from playbook, and generates redline suggestions.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `analyze_contract` | Analyze a contract for key terms, obligations, and risks |
| `identify_risks` | Identify risky or unusual clauses in a contract |
| `compare_to_playbook` | Compare contract terms against company standard playbook |
| `generate_redlines` | Generate redline suggestions for non-standard terms |
| `extract_obligations` | Extract key obligations, deadlines, and renewal terms |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/contract-review/analyze` | Analyze |
| `POST` | `/api/v1/contract-review/search` | Search |
| `POST` | `/api/v1/contract-review/generate` | Generate document |
| `GET` | `/api/v1/contract-review/track` | Track status |
| `POST` | `/api/v1/contract-review/report` | Generate report |

## Features

- Contract
- Review
- Compliance
- Audit Trail

## Integrations

- Relativity
- Logikcull
- Ironclad
- Docusign Clm
- Westlaw

## Architecture

```
contract-review-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── contract_review_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Legal Tech Platform + LLM + Document Management**

---

Built as part of the Enterprise AI Agent Platform.
