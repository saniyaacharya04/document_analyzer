from doclens.services.completeness import analyze_completeness

def test_completeness_no_examples():
    text = "This document contains only description without guidance."
    result = analyze_completeness(text)

    assert "No clear examples" in result
