import speech_recognition as sr
from pydub import AudioSegment
import os
import io


def speech_to_text(audio_data):
    ogg_file = io.BytesIO(audio_data)
    audio = AudioSegment.from_file(ogg_file, format="ogg")

    wav_file = io.BytesIO()
    audio.export(wav_file, format="wav")
    wav_file.seek(0)

    r = sr.Recognizer()
    with sr.AudioFile(wav_file) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language="en")
    return text


