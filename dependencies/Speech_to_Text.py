'''
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
    def Transcribe(Audio):
        # Record 4 seconds
        fs = 44100
        recc = sd.rec(int(4 * fs), samplerate=fs, channels=1)
        sd.wait()
        
        # Convert NumPy array to Raw bytes
        audio_int16 = (recc * 32767).astype(np.int16)
        raw_data = audio_int16.tobytes()
        
        # Create the AudioData object directly
        recognizer = sr.Recognizer()
        audio_data = sr.AudioData(raw_data, fs, 2) # 2 = 16-bit (2 bytes per sample)
        
        try:
            return recognizer.recognize_google(audio_data)
        except:
            return 0000

    print('Say: ')
    recc = sd.rec(int(4 * 44100), samplerate=44100, channels=1)
    sd.wait()
    text = Transcribe(recc)
    
    return text
'''

import os
import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel
import numpy as np

# Use a relative path for the temporary audio file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_AUDIO = os.path.join(BASE_DIR, "input.wav")

# Load the model once (use "tiny" for speed, "base" for better accuracy)
# 'int8' quantization makes it run fast even on older CPUs
print("loading model")
model = WhisperModel("base", device="cpu", compute_type="int8")

def TEXT():
    fs = 44100
    seconds = 4
    print('Listening...')
    
    # Record as float32
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    
    # 1. Check if the audio is empty
    if np.max(np.abs(recording)) < 0.01:
        print("Mic too quiet or not working!")
        return 0000

    # 2. Normalize the audio (Fixes the "you" hallucination)
    # This scales your voice to be clearly 'heard' by the AI
    recording = recording / np.max(np.abs(recording))
    
    # 3. Convert to 16-bit PCM
    audio_int16 = (recording * 32767).astype(np.int16)
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMP_AUDIO = os.path.join(BASE_DIR, "input.wav")
    write(TEMP_AUDIO, fs, audio_int16)

    # 4. Transcribe with 'vad_filter'
    # This tells Whisper to ignore silence and only look for human speech
    segments, info = model.transcribe(TEMP_AUDIO, beam_size=5, vad_filter=True)
    
    text = "".join([segment.text for segment in segments]).strip()
    
    print(f"Result: {text}")
    return text if text else 0000