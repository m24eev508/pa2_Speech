def detect_language(text):
    hindi_words = ["hai", "ka", "ki", "mein"]
    result = []

    for word in text.split():
        if word.lower() in hindi_words:
            result.append((word, "Hindi"))
        else:
            result.append((word, "English"))

    return result