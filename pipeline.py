from preprocess import clean_audio
from lid_model import detect_language
from ipa_translate import to_ipa, translate
from tts_generate import generate_audio
from spoof_detection import classify_audio
from adversarial import add_noise

clean_file = clean_audio("original_segment.wav")
print("Audio cleaned:", clean_file)

text = "this is a sample speech in english aur yeh hindi ka part hai"
print("Transcript:", text)

lid_result = detect_language(text)
print("LID:", lid_result)

ipa_text = to_ipa(text)
print("IPA:", ipa_text)

translated = translate(text)
print("Translated:", translated)

output_audio = generate_audio(translated)
print("Generated Audio:", output_audio)

status = classify_audio(output_audio)
print("Audio Type:", status)

adv_file = add_noise(clean_file)
print("Adversarial file:", adv_file)