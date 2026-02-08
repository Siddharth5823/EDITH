import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import numpy as np

def TEXT():
    def Transcribe(Audio):
        reccc = (np.iinfo(np.int32).max * (Audio/np.abs(Audio).max())).astype(np.int32)
        write("sample.wav", 44100, reccc )
        recognizer = sr.Recognizer()
        with sr.AudioFile("sample.wav") as source:
            audio = recognizer.record(source)
            try:
                tex = recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                tex = 0000
        return tex

    print('Say: ')
    recc = sd.rec(int(4 * 44100), samplerate=44100, channels=1)
    sd.wait()
    text = Transcribe(recc)
    
    return text