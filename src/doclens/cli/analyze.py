import argparse
import logging

from doclens.core.analyzer import analyze_url
from doclens.core.report_generator import generate_report
from doclens.config.logging_config import setup_logging

def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description="DocLens AI – Documentation Analyzer")
    parser.add_argument("url", help="Documentation URL to analyze")
    parser.add_argument(
        "-o",
        "--output",
        default="reports/report.json",
        help="Path to output JSON report"
    )
    args = parser.parse_args()

    logger.info("CLI started")
    result = analyze_url(args.url)
    generate_report(result, args.output)
    logger.info("Report saved to %s", args.output)

if __name__ == "__main__":
    main()
