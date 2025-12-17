#!/usr/bin/env bash
set -e

echo "======================================"
echo "DocLens AI – End-to-End Validation"
echo "======================================"

# Ensure no stale uvicorn processes
pkill -f uvicorn || true

PORT=8010

echo "[1/8] Checking Python version..."
python --version

echo "[2/8] Checking critical dependencies..."
PYTHONPATH=src python - << 'PYEOF'
import fastapi
import selenium
import textstat
import requests
print("✔ Core dependencies importable")
PYEOF

echo "[3/8] Running unit tests..."
PYTHONPATH=src pytest -q
echo "✔ Tests passed"

echo "[4/8] Running CLI analyzer..."
PYTHONPATH=src python -m doclens.cli.analyze \
"https://help.moengage.com/hc/en-us/articles/4415622460948-Push-Templates" \
-o reports/validation_report.json
echo "✔ CLI run successful"

echo "[5/8] Validating output JSON..."
python - << 'PYEOF'
import json

with open("reports/validation_report.json", encoding="utf-8") as f:
    data = json.load(f)

assert "readability" in data
assert "structure_and_flow" in data
assert "completeness_and_examples" in data
assert "style_guidelines" in data

print("✔ Output JSON structure valid")
PYEOF

echo "[6/8] Starting FastAPI server on port ${PORT}..."
PYTHONPATH=src uvicorn doclens.api.app:app --port ${PORT} --log-level error &
API_PID=$!
sleep 5

echo "[7/8] Validating API health endpoint..."
python - << PYEOF
import requests

resp = requests.get("http://127.0.0.1:${PORT}/health", timeout=5)
assert resp.status_code == 200
assert resp.json().get("status") == "ok"

print("✔ API health check passed")
PYEOF

echo "[8/8] Shutting down API server..."
kill ${API_PID}

echo "======================================"
echo "END-TO-END VALIDATION SUCCESSFUL"
echo "======================================"
