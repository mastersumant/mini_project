import datetime
from datetime import date
import cv2
import random
import matplotlib.pyplot as plt
import os
import pyaudio
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
#______________________________________________

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    hours = int(datetime.datetime.now().hour)
    minu=int(datetime.datetime.now().minute)
    if (hours >= 0 and hours <= 12):
        speak("good morning")
        speak("the time is")
        speak(hours)
        speak("hours")
        speak("and")
        speak(minu)
        speak("minutes")
    elif (hours >= 12 and hours <= 18):
        speak("good evening")
        speak("the time is")
        speak(hours)
        speak("hours")
        speak("and")
        speak(minu)
        speak("minutes")
    else:
        speak("good night")
        speak("the time is")
        speak(hours)
        speak("hours")
        speak("and")
        speak(minu)
        speak("minutes")
#______________________________________________
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognising")
        query = r.recognize_google(audio, language='en-in')
        print("user said ", query)
    except Exception as e:
        print(e)
        print("say that again")
        return "None"
    return query

#wish()
while(1):
 r=sr.Recognizer()
 with sr.Microphone() as source:
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    text = r.recognize_google(audio_data)
    print(text)
    if(text=='currency'):
        def main():
            cap=cv2.VideoCapture(0)
            if cap.isOpened():
                ret, frame= cap.read()
                print(ret)
                print(frame)
            else:
                ret=  False
        
            img=cv2.cvtColor(frame ,cv2.COLOR_BGR2RGB)
            plt.imshow(img)
            plt.xticks([])
            plt.yticks([])
            plt.show()
    
    
            output = "C:\\Users\\HP\\Desktop\\Python\\mini\\test_images\\1.jpg"
            cv2.imwrite(output,img)
   
            os.system("python test.py")
        if __name__=="__main__":
            main()
    if(text=='time'):
         wish()