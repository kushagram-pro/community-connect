def classify_need(text: str):
    # temporary mock response
    return {
        "category": "food",
        "urgency": 4,
        "summary": text[:50],
        "confidence": 0.8
    }