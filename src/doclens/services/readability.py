import textstat

def analyze_readability(text: str) -> dict:
    flesch = textstat.flesch_reading_ease(text)
    gunning = textstat.gunning_fog(text)

    if flesch > 60:
        feedback = "Easy to read."
    elif flesch > 30:
        feedback = "Moderate difficulty."
    else:
        feedback = "Hard to read for a general audience."

    return {
        "flesch_reading_ease": round(flesch, 2),
        "gunning_fog_index": round(gunning, 2),
        "feedback": feedback
    }
