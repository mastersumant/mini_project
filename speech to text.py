#import speech_recognition as sr

#filename = "100.wav"
#r = sr.Recognizer()

#with sr.AudioFile(filename) as source:
#    audio_data = r.record(source)
#    text = r.recognize_google(audio_data)
#    print(text)
import cv2
import random
import matplotlib.pyplot as plt
import os
import pyaudio
import speech_recognition as sr


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
    
    
            output = "C:\\Users\\Abhinav\\Desktop\\mini\\test_images\\1.jpg"
            cv2.imwrite(output,img)
   
            os.system("python test.py")
if __name__=="__main__":
   main()