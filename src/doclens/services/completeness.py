def analyze_completeness(text: str) -> str:
    keywords = ["example", "step", "instruction", "how to", "tutorial", "guide"]
    found = any(k in text.lower() for k in keywords)
    if not found:
        return "No clear examples or step-by-step instructions detected. Consider adding some."
    return "Examples and instructions appear sufficient."
