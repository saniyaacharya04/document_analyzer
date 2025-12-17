# DocLens AI

DocLens AI is a production-grade documentation analysis platform that evaluates technical documentation for **readability, structure, completeness, and writing style**.
It provides a **CLI tool**, a **REST API**, and **Dockerized deployment**, backed by automated testing and CI.

This project is designed to demonstrate **real-world software engineering practices**, not a demo or toy project.

---

## Key Features

* Analyze documentation from a public URL
* Readability scoring using linguistic metrics
* Structural analysis (headings, lists, flow)
* Completeness checks (examples, instructions)
* Writing style assessment
* Command Line Interface (CLI)
* FastAPI-based REST API
* Docker & Docker Compose support
* End-to-end validation script
* CI pipeline with automated tests

---

## Tech Stack

* Python 3.10
* FastAPI
* Pydantic
* Requests, BeautifulSoup
* textstat, nltk
* Pytest
* Docker, Docker Compose
* GitHub Actions CI

---

## Project Structure

```
document_analyzer/
├── docker/                 # Docker & Compose files
├── scripts/                # Validation scripts
├── src/doclens/             # Application source
│   ├── api/                # FastAPI layer
│   ├── cli/                # CLI interface
│   ├── core/               # Core analysis logic
│   ├── services/           # Independent analyzers
│   ├── utils/              # Utility helpers
│   ├── config/             # Logging & config
│   └── premium/            # Premium feature placeholders
├── tests/                  # Unit tests
├── reports/                # Output reports
├── Makefile
├── requirements.txt
├── requirements-dev.txt
├── ARCHITECTURE.md
└── README.md
```

---

## Installation (Local)

### Using Conda (recommended)

```bash
conda create -n doclens python=3.10
conda activate doclens
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

---

## CLI Usage

Run the documentation analyzer from the command line:

```bash
make cli
```

Or directly:

```bash
PYTHONPATH=src python -m doclens.cli.analyze \
"https://example.com/docs" \
-o reports/report.json
```

---

## API Usage

### Start the API server

```bash
make api
```

API runs at:

```
http://127.0.0.1:8000
```

### Health Check

```
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

### Analyze Documentation

```
POST /analyze
```

Request body:

```json
{
  "url": "https://example.com/docs"
}
```

Response (example):

```json
{
  "url": "...",
  "readability": {...},
  "structure_and_flow": {...},
  "completeness_and_examples": {...},
  "style_guidelines": {...}
}
```

---

## Docker Usage

### Build and run with Docker Compose

```bash
docker compose -f docker/docker-compose.yml up --build
```

API will be available at:

```
http://localhost:8000
```

Health check is automatically configured.

---

## Testing

Run unit tests:

```bash
make test
```

Run full end-to-end validation (CLI + API):

```bash
make validate
```

This script verifies:

* Dependencies
* Unit tests
* CLI execution
* API startup
* Health endpoint
* JSON output validation

---

## CI Pipeline

GitHub Actions CI automatically:

* Installs dependencies
* Runs unit tests
* Validates the project structure

CI configuration lives in:

```
.github/workflows/ci.yml
```

---

## Architecture

A detailed system design is documented in:

```
ARCHITECTURE.md
```

It covers:

* Layered architecture
* Data flow
* Service boundaries
* Extensibility design
* Premium feature placeholders

---

## Premium Features (Planned)

Premium capabilities are intentionally stubbed and clearly marked:

* AI-powered revision suggestions
* Automatic doc rewriting
* Export to multiple formats
* Team analytics dashboards

These are placeholders only and do not contain business logic.

---

## Versioning

Current release:

```
v1.0.0
```

Tagged and published.

---

## License

MIT License. See `LICENSE` for details.

