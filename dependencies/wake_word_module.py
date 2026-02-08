import struct
from threading import local
import pyaudio
import pvporcupine

porcupine = None
pa = None
audio_stream = None
file = "C:\Python\Machine-Learning\Files\Bots\Porcupine-wake-word\Hey-Edith_en_windows_v2_2_0.ppn"
porcupine = pvporcupine.create(keyword_paths=[file], access_key='c76xtiYegZhM593n5rNDM/94pIZ/NElfthtCpqjlCEDIAMy5isLVuA==')

pa = pyaudio.PyAudio()

audio_stream = pa.open(
                rate=porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=porcupine.frame_length)
def detect(exec):
    if exec == 1:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        keyword_index = porcupine.process(pcm)

        if keyword_index >= 0:
            print("Hotword Detected")
            return 1
    
    if exec == 0:
        if porcupine is not None:
            porcupine.delete()

        if audio_stream is not None:
            audio_stream.close()

        if pa is not None:
            pa.terminate()