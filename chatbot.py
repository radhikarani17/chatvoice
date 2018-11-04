#Author sumeer@unixindia.com
# this code works with python3.5

import re
import random
import datetime
import webbrowser
import pyttsx3
import wikipedia
from pygame import mixer
import speech_recognition as sr
import pyowm
HOUNDIFY_CLIENT_ID = "PjWoG9bD7j9AZhx9xT-fmQ=="  # Houndify client IDs are Base64-encoded strings
HOUNDIFY_CLIENT_KEY = "tz_XwYCu54Yw4II_pBSVOE1WaU878JErw_fn-HBychmJV1EM6eDlt7oa1cZMWiHL15rEeNncTOlUEBZn4fNO1A=="
newRate = 110
engine = pyttsx3.init()
voices = engine.getProperty('voice')
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', newRate)
some = 'xxxxx'
seme = 'yyyyy'
greetings = ['hello', 'hi', 'Hai', 'hey!', 'hey']
answers = ['hey i am Khan', 'hi i am Khan', 'Hai i am Khan']
question = ['How are you?', 'How are you doing?']
responses = ['Okay', "I'm fine"]
var1 = ['who made you', 'who created you']
var2 = ['created by sumeer', 'sumeer']
var3 = ['what time is it', 'what is the time', 'time']
var4 = ['who are you', 'what is your name']
cmd1 = ['open browser', 'open Google']
maps = ['take' and 'me' and 'to']
music = 'play'
cmd2 = ['play music', 'open music player']
cmd4 = ['open YouTube', 'I want to watch a video']
cmd5 = ['tell me the weather', 'weather', 'what about the weather']
cmd6 = ['exit', 'close', 'goodbye', 'nothing']
cmd7 = ['facebook', 'Facebook', 'open Facebook', 'Fb', 'fb', 'open FB', 'FB']
cmd8 = ['instagram','Instagram', 'open Instagram']
cmd3 = ['thank you']
repfr9 = ['youre welcome', 'glad i could help you']
while True:
    now = datetime.datetime.now()
    r = sr.Recognizer() 
    with sr.Microphone(device_index = 6, sample_rate = 48000, chunk_size = 2048) as source:#check for python3 -m sounddevices if problem aries in device_index 
        r.adjust_for_ambient_noise(source); print ("Say Something"); audio = r.listen(source) 
        try:
            print("You said:- " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
            engine.say('I didnt get that. Rerun the code')
            engine.runAndWait()
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    saidData = r.recognize_google(audio);
    if r.recognize_google(audio) is not seme:
        words = r.recognize_google(audio).split();
        if 'take' and 'me' and 'to' in words:
            engine.say("opening maps"); engine.runAndWait(); webbrowser.open_new('https://www.google.co.in/maps/dir/13.0642874,80.275344/' + r.recognize_google(audio).split(" ",)[3]);
    elif r.recognize_google(audio) in greetings:
        random_greeting = random.choice(answers)
        print(random_greeting)
        engine.say(random_greeting)
        engine.runAndWait()
    elif r.recognize_google(audio) in question:
        engine.say('I am fine, how about you?')
        engine.runAndWait()
        print('I am fine, how about you?')
    elif r.recognize_google(audio) in var1:
        engine.say('I was made by sumeer')
        engine.runAndWait()
        reply = random.choice(var2)
        print(reply)
    elif r.recognize_google(audio) in cmd3:
        print(random.choice(repfr9))
        engine.say(random.choice(repfr9))
        engine.runAndWait()
    elif r.recognize_google(audio) in cmd2:
        mixer.init()
        mixer.music.load("song.wav")
        mixer.music.play(); 
    elif r.recognize_google(audio) is not some:
        words = r.recognize_google(audio).split();
        if music in words:
            engine.say("opening song in youtube"); engine.runAndWait(); webbrowser.open_new('https://www.youtube.com/results?search_query=' + r.recognize_google(audio).lstrip(music));
    elif r.recognize_google(audio) in var4:
        engine.say('my name is khan , i am a bot')
        engine.runAndWait()
    elif r.recognize_google(audio) in cmd7:
        webbrowser.open('http://www.facebook.com')
    elif r.recognize_google(audio) in cmd8:
        webbrowser.open('http://www.instagram.com')
    elif r.recognize_google(audio) in cmd4:
        webbrowser.open('http://www.youtube.com')
    elif r.recognize_google(audio) in cmd6:
        print('see you later')
        engine.say('see you later')
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio) in cmd5:
        owm = pyowm.OWM('601a44c4523a544a4cdc0578cdc6721a')
        observation = owm.weather_at_place('Chennai, IN')
        observation_list = owm.weather_around_coords(13.0878, 80.2785)
        w = observation.get_weather()
        w.get_wind()
        w.get_humidity()
        w.get_temperature('celsius')
        print(w)
        print(w.get_wind())
        print(w.get_humidity())
        print(w.get_temperature('celsius'))
        engine.say(w.get_wind())
        engine.runAndWait()
        engine.say('humidity')
        engine.runAndWait()
        engine.say(w.get_humidity())
        engine.runAndWait()
        engine.say('temperature')
        engine.runAndWait()
        engine.say(w.get_temperature('celsius'))
        engine.runAndWait()
    elif r.recognize_google(audio) in var3:
        print("Current date and time : ")
        print(now.strftime("The time is %H:%M"))
        engine.say(now.strftime("The time is %H:%M"))
        engine.runAndWait()
    elif r.recognize_google(audio) in cmd1:
        webbrowser.open('http://www.google.com')
    else:
        
        engine.say("loading info please wait");
        engine.runAndWait();
        print(wikipedia.summary(r.recognize_google(audio)));
        engine.say(wikipedia.summary(r.recognize_google(audio)));
        engine.runAndWait();
        engine.say("opening search in new tab"); engine.runAndWait();
        webbrowser.open_new('http://www.google.com/search?q=' + r.recognize_google(audio));
# if need for choices uncomment below and comment above lines after else
        #engine.say("say the correct option listed below")
        #engine.runAndWait(); print(" say google or say wiki for choice of your selection:- "); engine.say(" say google or say wiki for choice of your selection:- "); engine.runAndWait();         
        #try:
        #    print("Houndify thinks you said " + r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))
        #except sr.UnknownValueError:
        #    print("Houndify could not understand audio")
        #except sr.RequestError as e:
        #    print("Could not request results from Houndify service; {0}".format(e))
        #if r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY) == 'wiki':
        #    print(wikipedia.summary(r.recognize_google(audio)))
        #    engine.say(wikipedia.summary(r.recognize_google(audio)))
        #    engine.runAndWait()
        #elif r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY) == 'google':
        #	 engine.say("opening search in new tab"); engine.runAndWait(); webbrowser.open_new('http://www.google.com/search?q=' + r.recognize_google(audio)); 
        #else:
        #    engine.say("entered option wrong");
        #    engine.runAndWait()

