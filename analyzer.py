import argparse
import json
from scraper import fetch_article_text
from readability import analyze_readability

def analyze_structure_and_style(text):
    # Simple heuristic example
    result = {}

    # Structure: count headings and lists
    headings = text.count('\n#') + text.count('\n##')  # crude markdown style assumption
    lists = text.count('\n- ') + text.count('\n* ') + text.count('\n1. ')

    structure_assessment = []
    if headings < 3:
        structure_assessment.append("Add more headings for better navigation.")
    if lists < 3:
        structure_assessment.append("Use bullet or numbered lists to improve readability.")

    result['assessment'] = " ".join(structure_assessment) if structure_assessment else "Good structure."

    # Completeness (placeholder)
    if "example" not in text.lower():
        result['completeness'] = "No clear examples or step-by-step instructions detected. Consider adding some."
    else:
        result['completeness'] = "Examples detected."

    # Style (placeholder)
    style_assessment = "Style is clear, concise, and user-friendly."
    result['style'] = style_assessment

    return result

def main():
    parser = argparse.ArgumentParser(description="AI Documentation Analyzer")
    parser.add_argument("url", help="URL of the documentation article")
    parser.add_argument("-o", "--output", default="report.json", help="Output JSON file")
    args = parser.parse_args()

    print(f"Fetching content from: {args.url}")
    text = fetch_article_text(args.url)
    print(f"Pulled {len(text)} characters")

    readability = analyze_readability(text)
    structure_style = analyze_structure_and_style(text)

    report = {
        "url": args.url,
        "readability": readability,
        "structure_and_flow": {
            "assessment": structure_style['assessment']
        },
        "completeness_and_examples": {
            "assessment": structure_style['completeness']
        },
        "style_guidelines": {
            "assessment": structure_style['style']
        }
    }

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"Report saved to {args.output}")

if __name__ == "__main__":
    main()
