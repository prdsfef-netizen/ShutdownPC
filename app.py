import pyttsx3
import speech_recognition as sr
import os
import time

def getCommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Escuhando')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print('Identificando')
            Query = r.recognize_google(audio)
            print("Mensaje='", Query, "'")
        except Exception as e:
            print(e)
            print("Intentalo otra vez")
            return ":C"
    time.sleep(2)
    return Query

def Speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

Speak("Quieres apagar la computadora Lizz?")
while True:
    command = getCommands()
    if "no" in command:
        Speak("La computadora no se apagara, ten un buen dia")
    if "yes" in command:
        Speak("Apagando equipo")
        break
    Speak("Hasta luego")
