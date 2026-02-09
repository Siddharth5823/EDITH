import re
import wikipedia
from math import *
import sys
import string
import os
import numpy as np
import datetime
import random as rand
import pyjokes 
import requests
from time import sleep
from bs4 import BeautifulSoup
from gnewsclient import gnewsclient
import win32com.client as wincom

def speak(text):
    say = wincom.Dispatch("SAPI.SpVoice")
    say.Speak(text)

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

