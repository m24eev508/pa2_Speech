from gtts import gTTS

def generate_audio(text, filename="output_LRL_cloned.wav"):
    tts = gTTS(text)
    tts.save(filename)
    return filename