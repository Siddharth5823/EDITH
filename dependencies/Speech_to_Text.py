import os
import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel
import numpy as np
import string 
from word2number import w2n

# Use a relative path for the temporary audio file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_AUDIO = os.path.join(BASE_DIR, "input.wav")

print("loading model")

MODEL_SIZE = "small.en"
model = WhisperModel(MODEL_SIZE, device="cpu", compute_type="int8")

def TEXT():
    fs = 44100
    seconds = 4
    print('Listening...')
    
    # Record as float32
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    
    #1 Check if the audio is empty
    if np.max(np.abs(recording)) < 0.01:
        print("Mic too quiet or not working!")
        return 0000

    recording = recording / np.max(np.abs(recording))
    
    audio_int16 = (recording * 32767).astype(np.int16)
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMP_AUDIO = os.path.join(BASE_DIR, "input.wav")
    write(TEMP_AUDIO, fs, audio_int16)

    segments, info = model.transcribe(TEMP_AUDIO, beam_size=5, vad_filter=True)
    
    text = "".join([segment.text for segment in segments]).strip()
    print(f"Result: {text}")
    
    if text:
        text = text.translate(str.maketrans('', '', string.punctuation)).lower()

    if not text: return 0000

    try:
        words = text.split()
        new_words = []
        for word in words:
            try:
                num = w2n.word_to_num(word)
                new_words.append(str(num))
            except ValueError:
                new_words.append(word)
        
        text = " ".join(new_words)
    except Exception as e:
        pass 
    text = text.lower().split()
    return text