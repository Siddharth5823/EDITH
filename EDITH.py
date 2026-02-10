####################################  IMPORTS  ###################################
import random
import sys
import os
from time import sleep

current_dir = os.path.dirname(os.path.abspath(__file__))
dependencies_path = os.path.join(current_dir, 'dependencies')
sys.path.insert(1, dependencies_path)

from Execution import *
import Speech_to_Text as SR
from audios import *
from wake_word import wake

######################1##############  IMPORTS  ###################################


####################################  EDITH  #####################################
def EDITH(query):
    if ( ("good" in query) or ("amazing" in query) or ("best" in query) or ("intelligent" in query) or ("better" in query)) and ("you" in query):
        appereciate()
    elif "news" in query:
        news()
    elif ("weather" in query) or ("temperature" in query):
        weather(query)
    elif ("jokes" in query) or ("joke" in query):
        joke()
    elif (("hello" in query) or ("hi" in query) or ("hey" in query)) and (len(query) == 1):
        greet()
    elif ("time" in query) or ("date" in query):
        time()
    elif "wikipedia" in query:
        wiki(query)
    elif ('what' in query) and ('is' in query):
        query.remove('what')
        query.remove('is')
        maths(query)
    else:
        speak('No matching Skill available for command %s'%' '.join(query))
####################################  EDITH  #####################################


####################################  INPUT  #####################################
loop = 1
while loop:
    w = False
    w = wake()
    if w:
        print(wake)
        ting.play()
        text = SR.TEXT()
        if type(text) == str:
            text = text.lower().split()
            term = ['stop','terminate','kill']
            if any(x in ' '.join(text) for x in term):
                loop = 0
                speak('Terminating Sir, Have a good day!')
                shutdown.play()
                sleep(3)
            else:
                try:
                    text.remove('the')
                except: pass
                EDITH(text)

        elif text == 0000:
            print("DIDN'T UNDERSTOOD")
####################################  INPUT  #####################################