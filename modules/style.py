def analyze_style(text: str) -> str:
    passive_voice_indicators = ["was", "were", "is being", "are being"]
    if any(pv in text.lower() for pv in passive_voice_indicators):
        return "Passive voice detected; use more active voice for clarity."
    jargon_words = ["leverage", "synergy", "robust", "ecosystem"]
    if any(j in text.lower() for j in jargon_words):
        return "Consider reducing jargon for wider understanding."
    return "Style is clear, concise, and user-friendly."
