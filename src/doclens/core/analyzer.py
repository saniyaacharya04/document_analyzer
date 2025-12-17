import logging

from doclens.services.scraper import fetch_article_text
from doclens.services.readability import analyze_readability
from doclens.services.structure import analyze_structure
from doclens.services.completeness import analyze_completeness
from doclens.services.style import analyze_style

logger = logging.getLogger(__name__)

def analyze_url(url: str) -> dict:
    logger.info("Starting analysis for URL: %s", url)

    text = fetch_article_text(url)
    logger.info("Fetched %d characters", len(text))

    result = {
        "url": url,
        "readability": analyze_readability(text),
        "structure_and_flow": {
            "assessment": analyze_structure(text)
        },
        "completeness_and_examples": {
            "assessment": analyze_completeness(text)
        },
        "style_guidelines": {
            "assessment": analyze_style(text)
        }
    }

    logger.info("Analysis completed")
    return result
