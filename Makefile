# ===============================
# DocLens AI - Makefile
# ===============================

PYTHONPATH=src
PYTHON=python
PIP=pip
API_PORT=8000

.DEFAULT_GOAL := help

# -------------------------------
# Help
# -------------------------------
help:
	@echo "Available commands:"
	@echo ""
	@echo "Setup:"
	@echo "  make install        Install runtime dependencies"
	@echo "  make install-dev    Install dev dependencies"
	@echo ""
	@echo "Development:"
	@echo "  make cli            Run CLI analyzer"
	@echo "  make api            Run FastAPI server"
	@echo ""
	@echo "Testing & Validation:"
	@echo "  make test           Run unit tests"
	@echo "  make validate       Run end-to-end validation"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-build   Build Docker image"
	@echo "  make docker-up      Run Docker container"
	@echo "  make docker-down    Stop Docker container"
	@echo ""
	@echo "Utilities:"
	@echo "  make clean          Remove cache files"
	@echo "  make freeze         Freeze dependencies"
	@echo ""

# -------------------------------
# Dependency Management
# -------------------------------
install:
	$(PIP) install -r requirements.txt

install-dev:
	$(PIP) install -r requirements.txt -r requirements-dev.txt

freeze:
	$(PIP) freeze > requirements.lock.txt

# -------------------------------
# CLI
# -------------------------------
cli:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m doclens.cli.analyze \
	"https://help.moengage.com/hc/en-us/articles/4415622460948-Push-Templates" \
	-o reports/report.json

# -------------------------------
# API
# -------------------------------
api:
	PYTHONPATH=$(PYTHONPATH) uvicorn doclens.api.app:app --reload --port $(API_PORT)

# -------------------------------
# Testing
# -------------------------------
test:
	PYTHONPATH=$(PYTHONPATH) pytest -v

# -------------------------------
# End-to-End Validation
# -------------------------------
validate:
	bash scripts/validate_e2e.sh

# -------------------------------
# Docker
# -------------------------------
docker-build:
	docker compose -f docker/docker-compose.yml build

docker-up:
	docker compose -f docker/docker-compose.yml up

docker-down:
	docker compose -f docker/docker-compose.yml down

# -------------------------------
# Cleanup
# -------------------------------
clean:
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name ".pytest_cache" -type d -exec rm -rf {} +
	rm -f reports/validation_report.json
