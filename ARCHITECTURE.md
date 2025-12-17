# DocLens AI — System Architecture

## 1. Overview

**DocLens AI** is a modular, production-ready documentation analysis platform that evaluates technical documentation for:

* Readability
* Structure & flow
* Completeness & examples
* Style consistency

It supports:

* **CLI execution**
* **REST API (FastAPI)**
* **Dockerized deployment**
* **CI-validated end-to-end workflows**

The architecture is intentionally designed to be:

* Testable
* Extensible
* Cloud-ready
* Premium-feature friendly

---

## 2. High-Level Architecture

```
                  ┌───────────────┐
                  │     Client     │
                  │  (CLI / API)   │
                  └───────┬───────┘
                          │
                          ▼
                ┌───────────────────┐
                │   API / CLI Layer  │
                │  (FastAPI / CLI)   │
                └───────┬───────────┘
                        │
                        ▼
                ┌───────────────────┐
                │   Core Orchestrator│
                │  (Analyzer Engine) │
                └───────┬───────────┘
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
┌────────────┐  ┌──────────────┐  ┌──────────────┐
│ Readability│  │ Structure     │  │ Completeness │
│ Analyzer   │  │ Analyzer      │  │ Analyzer     │
└────────────┘  └──────────────┘  └──────────────┘
        │               │                │
        └───────────────┼────────────────┘
                        ▼
                ┌───────────────────┐
                │  Style Analyzer   │
                └─────────┬─────────┘
                          ▼
                ┌───────────────────┐
                │ Report Generator  │
                │   (JSON Output)   │
                └───────────────────┘
```

---

## 3. Directory Structure

```
document_analyzer/
├── src/doclens/
│   ├── api/            # FastAPI REST layer
│   ├── cli/            # Command-line interface
│   ├── core/           # Central orchestration logic
│   ├── services/       # Independent analyzers
│   ├── utils/          # Shared utilities
│   ├── config/         # Logging & configuration
│   └── premium/        # Premium feature placeholders
│
├── tests/              # Unit tests (pytest)
├── docker/             # Docker & Compose configs
├── scripts/            # Validation & automation
├── reports/            # Generated outputs
└── .github/workflows/  # CI pipeline
```

---

## 4. Component Responsibilities

### 4.1 API Layer (`doclens.api`)

* Built using **FastAPI**
* Exposes REST endpoints:

  * `GET /health`
  * `POST /analyze`
* Handles:

  * Request validation (Pydantic)
  * OpenAPI schema generation
  * Response serialization

> No business logic lives here.

---

### 4.2 CLI Layer (`doclens.cli`)

* Entry point for local analysis
* Calls the same core analyzer used by the API
* Outputs structured JSON reports

**Design principle:**
CLI and API share **100% of the core logic**.

---

### 4.3 Core Analyzer (`doclens.core`)

**System orchestrator.**

Responsibilities:

* Fetch content
* Invoke each analyzer
* Aggregate results
* Produce final analysis payload

This layer:

* Has no I/O assumptions
* Is fully testable
* Is reusable across interfaces

---

### 4.4 Services Layer (`doclens.services`)

Each service is:

* **Stateless**
* **Independent**
* **Single-responsibility**

| Service           | Responsibility            |
| ----------------- | ------------------------- |
| `readability.py`  | Text readability metrics  |
| `structure.py`    | Headings, flow, hierarchy |
| `completeness.py` | Missing sections/examples |
| `style.py`        | Tone, consistency checks  |
| `scraper.py`      | Safe content extraction   |

This makes adding new analyzers trivial.

---

### 4.5 Report Generator (`doclens.core.report_generator`)

* Converts analysis results into clean JSON
* Used by CLI and validation scripts
* Can later support:

  * PDF
  * HTML
  * Markdown exports

---

### 4.6 Premium Layer (`doclens.premium`)

**Intentional placeholder layer.**

Reserved for:

* LLM-based rewriting
* AI suggestions
* Auto-generated improvements

Currently stubbed to demonstrate **freemium architecture discipline**.

---

## 5. Data Flow

### API Flow

```
Client → FastAPI → Core Analyzer
       → Services → Aggregation → JSON Response
```

### CLI Flow

```
User → CLI → Core Analyzer
     → Services → Report Generator → JSON File
```

---

## 6. Validation & Quality Gates

### Automated Validation

* Unit tests (pytest)
* End-to-end validation script
* API health checks
* CLI execution verification

### CI Pipeline

* Runs on every push
* Fails on:

  * Import errors
  * Test failures
  * API startup issues

---

## 7. Deployment Architecture

### Docker

* Slim Python base image
* Explicit dependency install
* Health checks enabled
* Volume-mounted reports

### Docker Compose

* Single-service deployment
* Restart policies
* Observability-ready

---

## 8. Design Principles

* **Separation of Concerns**
* **Single Responsibility**
* **Interface-driven design**
* **No hidden side effects**
* **Production parity (local = CI = Docker)**

---

## 9. Scalability & Future Extensions

Planned / easy extensions:

* Async analyzers
* Background task execution
* API versioning (`/v1`)
* Authentication & rate limiting
* LLM integration
* Multi-document batch analysis

---

## 10. Why This Architecture Matters

This project demonstrates:

* Real-world backend architecture
* Clean modular design
* Test-driven development
* Deployment readiness
* Clear separation between free & premium logic

> **This is not a demo project.
> This is a production-capable system.**

