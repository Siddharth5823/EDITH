from pygame import mixer
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
audio_path = os.path.join(current_dir, 'Audios')

ss=0
mixer.init()
shutdown = mixer.Sound(os.path.join(audio_path, 'shutdown.mp3'))
bruh = mixer.Sound(os.path.join(audio_path, '_bruh.mp3'))
augh = mixer.Sound(os.path.join(audio_path, '_aughhhh.mp3'))
ting = mixer.Sound(os.path.join(audio_path, 'discord-notification.mp3'))