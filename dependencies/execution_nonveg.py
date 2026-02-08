from pygame import mixer
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
audio_path = os.path.join(current_dir, 'Audios')
#sys.path.insert(1, current_dir)
from Execution import *
intent_list = {
    '1' : ['on','1','open',]
    ,
    '0' : ['off','0','close']
    ,
    'negative': ['not',"don't",'wont',"does'nt",'no','neither',"didn't"]

}
ss=0
mixer.init()
choke = mixer.Sound(os.path.join(audio_path, 'chokeme.wav'))
hoon = mixer.Sound(os.path.join(audio_path, 'hoonyeahh.wav'))
song = mixer.Sound(os.path.join(audio_path, 'soaringhoonyeah.wav'))
chalaja = mixer.Sound(os.path.join(audio_path, 'chala-ja.mp3'))
shutdown = mixer.Sound(os.path.join(audio_path, 'shutdown.mp3'))
bruh = mixer.Sound(os.path.join(audio_path, '_bruh.mp3'))
augh = mixer.Sound(os.path.join(audio_path, '_aughhhh.mp3'))
puneet = mixer.Sound(os.path.join(audio_path, 'puneet.mp3'))
chal = mixer.Sound(os.path.join(audio_path, 'Chal.mp3'))
somebody = mixer.Sound(os.path.join(audio_path, 'somebody.wav'))
dametu = mixer.Sound(os.path.join(audio_path, 'Dametucasito.mp3'))
ting = mixer.Sound(os.path.join(audio_path, 'discord-notification.mp3'))
aryannight = mixer.Sound(os.path.join(audio_path, 'Aryannightout.wav'))

def nonveg(query):
    if (('love' in query) or ('like' in query) or ('f***' in query)) and ('you' in query):
        for j in intent_list['negative']:
            if j in ' '.join(query):
                chalaja.play()
                return ss
                exit
        else:
            choke.play()
            return ss

    elif ('song' in query) and ('sing' in query):
        print('At your service Master')
        speak('At your service Master')
        song.play()
        return ss

    elif (('gf'in query) or ('girlfriend' in query) or ('bandi'in query)) and ('broke' in query) and ('up' in query):
        for j in intent_list['negative']:
            if j in ' '.join(query):
                augh.play()
                chalaja.play()
                return ss
                exit
        else:
            puneet.play()
            return ss

    elif ('favour' in query) and ('do' in query):
        chal.play()
        return ss

    elif ('somebody'in query) and ('give' in query) and ('me' in query):
        somebody.play()
        return ss
    
    elif ('where'in query) and ('were' in query) and ('you' in query) and ('last'in query) and ('night' in query):
        aryannight.play()
        return ss

    elif ('orgasm' in query):
        for j in intent_list['negative']:
            if j in ' '.join(query):
                augh.play()
                sleep(1)
                chalaja.play()
                return ss
                exit
        else:
            dametu.play()
            return ss
