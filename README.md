# AI Documentation Analyzerb [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/saniyaacharya04/document_analyzer/blob/main/LICENSE)


This tool analyzes MoEngage documentation (or any public web documentation) and provides a structured report evaluating:

1. **Readability**
2. **Structure & Flow**
3. **Completeness & Examples**
4. **Style Guidelines**

Optionally, it can also revise the content based on the suggestions generated.

---

## Features

* Analyze documentation for marketing readability using metrics like Flesch Reading Ease and Gunning Fog Index.
* Assess structural quality (headings, paragraph flow, list usage).
* Evaluate completeness of explanations and presence of examples.
* Compare writing style against Microsoft Style Guide recommendations.
* Optionally rewrite content to improve readability and clarity.

---

## Project Structure

ai_analyser/
│
│   analyzer.py               # Main CLI script to run the analysis
│   analyzer_logic.py         # Orchestrates various assessment modules
│   completeness.py           # Completeness & examples checker
│   example_report.json       # Sample output report
│   readability.py            # Readability metrics calculator
│   README.md                 # Project documentation
│   report.json               # Generated report from live analysis
│   report_generator.py       # Aggregates results into structured output
│   requirements.txt          # Python package dependencies
│   revision_agent.py         # Optional bonus agent to revise text
│   scraper.py                # Scrapes content using Selenium
│   structure.py              # Checks structure and flow
│   style.py                  # Evaluates style guideline adherence
│   utils.py                  # Helper functions (e.g., text cleaner)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/saniyaacharya04/document_analyzer.git
cd ai_analyser
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Analyze a Documentation URL

```bash
python analyzer.py "https://help.moengage.com/hc/en-us/articles/4415622460948-Push-Templates" -o report.json
```

This will:

* Fetch the article via Selenium
* Analyze it across the 4 criteria
* Save a structured JSON report to `report.json`

---

## Example Output

```json
{
  "url": "https://help.moengage.com/hc/en-us/articles/4415622460948-Push-Templates",
  "readability": {
    "flesch_reading_ease": 47.43,
    "gunning_fog_index": 9.47,
    "feedback": "Moderate difficulty."
  },
  "structure_and_flow": {
    "assessment": "Add more headings for better navigation. Use bullet or numbered lists to improve readability."
  },
  "completeness_and_examples": {
    "assessment": "No clear examples or step-by-step instructions detected. Consider adding some."
  },
  "style_guidelines": {
    "assessment": "Style is clear, concise, and user-friendly."
  }
}
```

---

## Optional: Content Rewriting Agent

You can use `revision_agent.py` to rewrite documentation with the suggested improvements:

```bash
python revision_agent.py input_article.txt suggestions.json -o revised_output.md
```

---

## Notes

* The tool uses **Selenium with headless Chrome** for scraping content that blocks requests.
* Ensure you have **Google Chrome installed** and `chromedriver` is properly configured.

---

## Style Guide

Style recommendations are based on:

* Microsoft Writing Style Guide:

  * Clear and concise writing
  * Friendly, conversational tone
  * Step-by-step instructions over passive descriptions

---

## License

This project is licensed under the [MIT License](LICENSE).

---
