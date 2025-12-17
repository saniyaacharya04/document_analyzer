from doclens.services.readability import analyze_readability

def test_readability_basic():
    text = "This is a simple sentence. It is easy to read."
    result = analyze_readability(text)

    assert "flesch_reading_ease" in result
    assert "gunning_fog_index" in result
    assert isinstance(result["flesch_reading_ease"], float)
