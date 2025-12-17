import json
import logging

logger = logging.getLogger(__name__)

def generate_report(data: dict, output_path: str) -> None:
    logger.info("Writing report to %s", output_path)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
