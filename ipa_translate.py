def to_ipa(text):
    ipa = text.lower()
    ipa = ipa.replace("a", "ɑ").replace("e", "ɛ")
    return ipa

dictionary = {
    "hello": "namaskar",
    "speech": "bhashan",
    "system": "pranali",
    "teacher": "shikshak"
}

def translate(text):
    return " ".join([dictionary.get(w, w) for w in text.split()])