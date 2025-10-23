import re

def analyze_structure(text: str) -> str:
    headings = re.findall(r'^\s*(#{1,6}|\b[A-Z ]{3,}\b)', text, re.MULTILINE)
    paragraphs = text.split('\n\n')
    list_items = re.findall(r'^\s*[-*]\s+', text, re.MULTILINE)

    suggestions = []
    if len(headings) < 3:
        suggestions.append("Add more headings for better navigation.")
    if any(len(p.split()) > 150 for p in paragraphs):
        suggestions.append("Break long paragraphs into shorter ones.")
    if not list_items:
        suggestions.append("Use bullet or numbered lists to improve readability.")

    return " ".join(suggestions) if suggestions else "Structure and flow look good."
