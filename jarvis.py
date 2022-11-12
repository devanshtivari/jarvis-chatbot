import pyttsx3
import speech_recognition as sr
import datetime
engine = pyttsx3.init('sapi5') #initializing the engine
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice'  , voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<=17:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am assistant. Please tell me how can I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
    

if __name__ == '__main__':
    wishMe()
    