import numpy as np
import librosa
import soundfile as sf

def add_noise(input_file, output_file="adv.wav"):
    audio, sr = librosa.load(input_file, sr=16000)
    noise = 0.001 * np.random.randn(len(audio))
    adv_audio = audio + noise
    sf.write(output_file, adv_audio, sr)
    return output_file