import speech_recognition as sr
import pyttsx3
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
def takenotes():
    with sr.Microphone() as source:
        f=open("myfile1.txt","w")
        print("Continue saying to take notes")
        audio1=r1.listen(source)
        order1=r1.recognize_google(audio1,language="en")
        f.write(order1)
        f.close()
        f=open("myfile1.txt","r")
        print(f.read())
def openb():
    print("Opening Browser")
    speaktext("say the text to search in google")
    print("say the text to search in google")
    with sr.Microphone() as source:
        audio2=r2.listen(source)
        order2=r2.recognize_google(audio2,language="en")    
    cd ='E:\python\chromedriver.exe'
    browser = webdriver.Chrome(cd)
    browser.get("https://google.co.in/search?q ="+order2)
    print("Opened Browser")
    
def speaktext(command):
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait()

r=sr.Recognizer()
r1=sr.Recognizer()
r2=sr.Recognizer()
with sr.Microphone() as source:
    print("listening")
    speaktext("HI MOHIT Say something")
    audio=r.listen(source)
    order=r.recognize_google(audio,language="en")
    speaker="Did You say"+order
    speaktext(speaker)
    if "quit" in order:
        print("closing")
    if "take notes" in order:
        takenotes()   
    if "google" in order:
        openb()
'''
engine=pyttsx3.init()
engine.say(order)
engine.runAndWait()
'''
