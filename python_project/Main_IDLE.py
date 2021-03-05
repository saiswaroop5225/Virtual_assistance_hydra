import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS

r=sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            hydra_speak(ask)
        audio=r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            hydra_speak('sorry,I did not get That')
        except sr.RequestError:
            hydra_speak('Sorry, My speech Service is down')
        return voice_data
def hydra_speak(audio_string):
    tts = gTTS(text=audio_string,lang='en')
    r = random.randint(1,10000000)
    audio_file = 'audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name'in voice_data:
        hydra_speak('My name is Hydra')
    if 'what is your age'in voice_data:
        hydra_speak('My age is 1 day Old')
    if 'where are you from'in voice_data:
        hydra_speak('Im from Swaroop Workspace')
    if 'who created you'in voice_data:
        hydra_speak('Swaroop Created me.')
    if 'what time is it'in voice_data:
        hydra_speak(ctime())
    if 'what is your age'in voice_data:
        hydra_speak('My age is 1 day Old')
    if 'search' in voice_data:
        search = record_audio('what do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        hydra_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('what location you are searching for?')
        url = 'https://google.nl/maps/place/' +location +'/&amp;'
        webbrowser.get().open(url)
        hydra_speak('Here is what I found for ' + location)
    if 'exit' in voice_data:
        exit()
time.sleep(1)
hydra_speak("Hi! Im hydra, your virtual assistance")
hydra_speak('How Can I help You?')
while 1:
    voice_data =record_audio()
    respond(voice_data)
