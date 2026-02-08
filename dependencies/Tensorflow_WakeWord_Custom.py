######## IMPORTS ##########
import sounddevice as sd
from scipy.io.wavfile import write
import librosa
import Speech_to_Text as SR
import numpy as np
print('importing tensorflow!!')
from tensorflow import keras 
from keras.models import load_model #type: ignore
print('tensorflow imported!!')
####### ALL CONSTANTS #####
fs = 16000
seconds = 1
history = 0
output = 0
##### LOADING OUR SAVED MODEL and PREDICTING ###
model = load_model('Machine-Learning/Files/Bots/Custom-Wake-Word/Neural-network-Model/Custom-model.h5')

print("Say Now: ")
def Prediction():
    global history
    fs = 16000
    if history == 1:
        output = 0
        history = 0
    else:
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()
        write("sample.wav", fs, myrecording)
        audio, sample_rate = librosa.load("sample.wav")
        mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=16)
        mfcc_processed = np.mean(mfcc.T, axis=0)
        prediction = model.predict(np.expand_dims(mfcc_processed, axis=0))
        if prediction[:, 1] > 0.99:
            history = 1
            output = 1
        else:
            output = 0
    return output
ii = 0
def DATA():
    global ii
    if Prediction():
        return 1