import imaplib
import email
import re
import wikipedia
from math import *
import sys
import string
import speech_recognition as sr
import os
import numpy as np
import datetime
from time import sleep
import random as rand
import pyjokes 
import requests
from bs4 import BeautifulSoup
from gnewsclient import gnewsclient
from time import sleep
#PYTHONPATH='C:\Python\Machine-Learning\Files\Bots\EDITH\dependencies'
import os 
import win32com.client as wincom

def speak(text):
    say = wincom.Dispatch("SAPI.SpVoice")
    say.Speak(text)

'''
def mail_read(username,password,host):
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    _, search_data = mail.search(None, 'UNSEEN')
    my_message = []
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        for header in ['subject', 'to', 'from', 'date']:
            email_data[header] = email_message[header]
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                email_data['body'] = body.decode()
            elif part.get_content_type() == "text/html":
                html_body = part.get_payload(decode=True)
                email_data['html_body'] = html_body.decode()
        my_message.append(email_data)
    desp = 'empty'
    if bool(my_message) == False:
        return desp
    elif bool(my_message) == True:
        return my_message

def details_change(text):  
    Personal['name'] = text
    with open('details.py','w') as file:
        file.write('Personal = '+str(Personal))
    file.close()
'''

def greet():
    global ohh
    global x
    x = datetime.datetime.now()
    a = int(x.strftime('%H'))
    if a < 12:
        ohh = "Good Morning"
    if (a <15) and (a >= 12):
        ohh = "Good afternoon"

    if (a >= 15) and (a <= 18):
        ohh = "Good Evening"

    if a>18:
        ohh = "Good Night"
    print(ohh)
    speak(ohh)
'''
def mail():
    speak('Yo Mister Siddharth! Good to see you!')
    mail = mail_read(Personal['mail'],Personal['mailpasswd'],'imap.gmail.com')
    if type(mail) == list:
        if len(mail) > 1:
            speak('you have got %s recent emails!'%len(mail))
        else:
            speak('you have got 1 recent email!')
        
    elif mail == 'empty':
        print('No Recent Emails Found!')
        speak('No Recent Emails Found!')
'''
def appereciate():
    speak('thank you!')

def maths(query):
    try:
        answere = eval(' '.join(query))
        print(answere)
        speak(answere)
    except:
        print('cant find')
        speak('no ans available!')
def news():
    # top = 'World : Nation : Business\nTech : Ent. : Sports : Sc : Health'
    # speak('News on which topic?')
    # inputt = ' '.join(listen())
    # if 'topic' in inputt:
    #     speak('World , Nation , Business , Tech , Entertainment , Sports , Science , Health')
    #     speak('Now tell me the topic!')
    #     topic = ' '.join(listen())
    # else:
    #     topic = inputt
    # print(topic)
    client = gnewsclient.NewsClient(language='english', 
                                    location='india', 
                                    topic='health', 
                                    max_results=2)  
    news_list = client.get_news()
    speak('Top 2 news are')
    for item in news_list:
        print("Title : ",item['title'])
        speak(item['title'])
        sleep(0.5)

def weather(query):
    city = " ".join(query)
    print(city)
    url = "https://www.google.com/search?q="+city
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    data = str.split('\n')
    sky = data[1]
    print("its a %s day"%sky+" with %s temperature"%temp)
    speak("its a %s day"%sky+" with %s temperature"%temp)
    

def joke():
    jokes = pyjokes.get_jokes(language="en", category="all")
    random_num = rand.randrange(len(jokes))
    speak(jokes[random_num])
'''    
def remind(query):
    remind = open("Machine-Learning/Files/Bots/EDITH/dependencies/Reminders.txt","a")
    for i in range(2): query.pop(0)
    remind.write(" ".join(query)+"\n")
    remind.close()

def clear_reminder():
    remind = open("Machine-Learning\Files\Bots\EDITH\dependencies\Reminders.txt","w")
    remind.write("")
    remind.close()
    
def read_reminder():
    remind = open("Machine-Learning/Files/Bots/EDITH/dependencies/Reminders.txt","r")
    reminders = remind.read()
    reminders = reminders.split("\n")
    speak("There are %s"%len(reminders)+" reminders in your reminders list!")
    for i in reminders:
        print(i)
        speak(i)
    speak("only these are there!")

def change_name(query):
    for i in range(4): query.pop(0)
    details_change(' '.join(query))
'''

def time():
    x = datetime.datetime.now()
    time = x.strftime('%I:%M %p')
    speak("its "+time)
    
def wiki(query):
    query.remove("wikipedia")
    q = " ".join(query)
    try:
        w = wikipedia.summary(q,sentences=1)
        print(w) 
        speak(w)
    except:
        speak("no matching content available")

