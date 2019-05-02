import pygame
import json
import requests
import webbrowser
import urllib3
import sys
import os
import random
from threading import Thread
import copypaste
import speech_recognition as sr
from selenium import webdriver
import datetime
import pyttsx3
import wolframalpha
import smtplib
import urllib.request
import urllib.parse
import re

weat = "hava durumu"
ara = "internette ara"
youtube = "youtube"
bye = "güle güle"



engine = pyttsx3.init('sapi5')


urllib3.disable_warnings()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)



def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()
    


speak('Merhaba efendim, ben sizin dijital asistanınızım Jarvis!')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='tr-TR')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Üzgünüm Efendim ,Tekrar Deneyin')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':
 while True:
    deneme = True
    while deneme == True:
        speak("Size nasıl yardım edebilirim?")
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            audio = r.listen(source,timeout=None)
            try:
                metin = r.recognize_google(audio,language="tr-TR")
                print("Sen söyledin: " + metin)
                if weat in metin.lower():
                    
                    speak("Hangi şehrin hava durumunu merak ediyorsun?")
                    audio2 = r.listen(source,timeout=None,phrase_time_limit=5)
                    try:
                        metin = r.recognize_google(audio2,language="tr-TR")
                        print("Söyledin: " + metin)
                        appid = "APPID" ## Openweather sitesine kayıt olup alabilirsiniz.
                        url = "http://api.openweathermap.org/data/2.5/weather?q=" + metin + "&appid=" + appid
                        istek = requests.get(url,verify=False)
                        try:
                            istek = istek.json()
                            name = istek["name"]
                            istek = istek["main"]
                            istek = istek["humidity"]
                            istek = (istek - 32) / 1.8
                            print(name,"hava durumu:",int(istek),"derece")
                        except:
                            print("Böyle bir yer yok.")
                    except sr.UnknownValueError:
                        print("Anlamadım.")
                    except sr.RequestError:
                        print("Bad Request")
                elif "güle güle" in metin.lower():
                    speak("Sistem: Asistan arka plana alındı.\n")
                    os.chdir(yer)
                    main()
                elif ara in metin.lower():
                    speak("İnternette ne aramamı istiyorsun?")
                    audio2 = r.listen(source,timeout=None)
                    try:
                        metin = r.recognize_google(audio2,language="tr-TR")
                        print("Bunu mu arayayım?: " + metin)
                        print("Evet/Hayır")
                        audio3 = r.listen(source,timeout=None)
                        try:
                            metin2 = r.recognize_google(audio3,language="tr-TR")
                            print("Söyledin: " + metin2)
                            url = "https://www.google.com/search?q=" + metin
                            if "evet" in metin2.lower():
                                webbrowser.open_new(url)
                        except sr.UnknownValueError:
                            print("Anlamadım.")
                        except sr.RequestError:
                            print("Bad request.")
                    except sr.UnknownValueError:
                        print("Anlamadım.")
                    except sr.RequestError:
                        print("Bad request.")
                elif youtube in metin.lower():
                    print("Youtube'da ne aramamı istiyorsun?")
                    audio2 = r.listen(source,timeout=None)
                    try:
                        metin = r.recognize_google(audio2,language="tr-TR")
                        print("Bunu mu arayayım?: " + metin)
                        print("Evet/Hayır")
                        audio3 = r.listen(source,timeout=None)
                        try:
                            metin2 = r.recognize_google(audio3,language="tr-TR")
                            print(metin2)
                            query_string = urllib.parse.urlencode({"search_query" : input()})
                            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
                            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
                            print("http://www.youtube.com/watch?v=" + search_results[0])
                            url = "https://www.youtube.com/search?q=" + metin
                            if "evet" in metin2.lower():
                                webbrowser.open_new(url)
                        except sr.UnknownValueError:
                            print("Anlamadım.")
                        except sr.RequestError:
                            print("Bad request")
                    except sr.UnknownValueError:
                        print("Anlamadım.")
                    except sr.RequestError:
                        print("Bad request.")
                elif music in metin.lower():
                    t = Thread(target = Cal)
                    t.start()
                elif "durdur" in metin.lower():
                    pygame.mixer.init()
                    pygame.mixer.music.stop()
                    print("Şarkı durduruldu.")
                elif "kopyala" in metin.lower():
                    print("Neyi kopyalamamı istiyorsun?")
                    audio2 = r.listen(source,timeout=None)
                    try:
                        metin = r.recognize_google(audio2,language = "tr-TR")
                        print("Kopyalandı: " + metin)
                        copypaste.copy(metin)
                    except sr.UnknownValueError:
                        print("Anlamadım.")
                    except sr.RequestError:
                        print("Bad Request")
            except sr.UnknownValueError:
                print("Anlamadım.")
            except sr.RequestError:
                print("Bad Request")

   
