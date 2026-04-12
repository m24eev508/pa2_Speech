import librosa
import soundfile as sf
import os

def clean_audio(file):
    audio, sr = librosa.load(file, sr=16000)

    audio = audio / max(abs(audio))

    output = "clean.wav"
    sf.write(output, audio, sr)

    print("Clean audio saved:", os.path.abspath(output))
    return output