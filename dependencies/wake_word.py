import openwakeword
from openwakeword.model import Model
import openwakeword.utils as utils
import os
import sounddevice as sd
import numpy as np

MODEL_NAME = "alexa" 

try:
    print(f"Loading Wake Word Model: {MODEL_NAME}...")
    owwModel = Model(wakeword_models=[MODEL_NAME], inference_framework="onnx")

except Exception as e:

    print(f"⚠️ Model not found locally. Downloading default models now...")
    try:

        utils.download_models() 
        print("✅ Download Complete.")
        
        owwModel = Model(wakeword_models=[MODEL_NAME], inference_framework="onnx")
        
    except Exception as download_error:
        print(f"❌ CRITICAL: Could not download wake word model. Check internet.")
        print(f"Error details: {download_error}")
        owwModel = None

if owwModel:
    print("✅ Wake Word System Ready.")
else:
    print("⚠️ Wake Word System Disabled.")

FORMAT = np.int16
CHANNELS = 1
RATE = 16000
CHUNK = 1280 

def wake():
    print(f"\nListening for '{MODEL_NAME}'...")
    
    # We use a context manager to open the mic stream efficiently
    with sd.InputStream(samplerate=RATE, channels=CHANNELS, dtype='int16', blocksize=CHUNK) as stream:
        while True:
            # Read audio chunk
            data, overflowed = stream.read(CHUNK)
            
            # Feed to openWakeWord
            # Convert to numpy array (should be 1D)
            audio_data = np.frombuffer(data, dtype=np.int16)
            
            # Predict
            prediction = owwModel.predict(audio_data)
            
            # Check results
            for mdl in owwModel.prediction_buffer.keys():
                # Scores are 0.0 to 1.0. 
                # 0.5 is a good threshold (50% confidence)
                if prediction[mdl] > 0.5:
                    print(f"✅ Wake Word Detected: {mdl}")
                    return True # Break the loop and return to EDITH