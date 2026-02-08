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
from execution_nonveg import *

######################1##############  IMPORTS  ###################################


####################################  EDITH  #####################################
def EDITH(query):
    # EX = exec.gq(query)
    # gq(query).appericiate()

    # if (("mail" in query) or ('email' in query)) and ("read" in query):
    #     mail()
    if ( ("good" in query) or ("amazing" in query) or ("best" in query) or ("intelligent" in query) or ("better" in query)) and ("you" in query):
        appereciate()
    elif "news" in query:
        news()
    elif ("weather" in query) or ("temperature" in query):
        weather(query)
    elif ("jokes" in query) or ("joke" in query):
        joke()
    # elif ("remind" in query):
    #     remind(query)
    #elif ("clear" in query) and ("reminders" in query):
       # clear_reminder()
    # elif ("read" in query) and ("reminders" in query):
    #     read_reminder()
    # elif ('change' in query) and ('name' in query) and ('my' in query) and ('to' in query):
    #     change_name(query)
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


    #Home Automations
    '''
    elif ('turn' in query) or ('switch' in query) or ('open'in query) or ('close' in query):
        for inn in intent_list['1']:
            if inn in query:
                intent_binary = 1
                intent = 'open'
        for inn in intent_list['0']:
            if inn in query:
                intent_binary = 0   
                intent = 'close'
        if 'all' in query:
            location = query[-1]
            appliance = 'all'
            print(location,appliance,intent_binary)
            speak('{0} all the Appliances in {1}'.format(intent,location))
        else: 
            location = query[-1]
            appliance = query[-3]
            print(location,appliance,intent_binary)
            speak('{0} the {1} in {2}'.format(intent,appliance,location))
        '''
   





####################################  EDITH  #####################################


####################################  INPUT  #####################################
loop = 1
# EDITH('good')
while loop:
    
    #UNComment out if using Custom Model
    #wake = prd.DATA()
    
    #Comment out if using Picovoice
    wake = int(input("wake the bot by entering 1: "))
    
    if wake == 1:
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
                print(text)
                d = nonveg(text)
    
                if d != 0:
                    EDITH(text)
        elif text == 0000:
            print("DIDN'T UNDERSTOOD")
####################################  INPUT  #####################################