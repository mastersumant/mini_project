import pyttsx3 
import numpy as np
import pytesseract
from PIL import Image
import cv2
import ssl
import urllib
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



image=Image.open('med.jpg')
result = pytesseract.image_to_string(image,lang='eng')
result=result.lower()
print(result)

def onStart(): 
   print('starting') 
  
def onWord(name, location, length): 
   print('word', name, location, length) 
  
def onEnd(name, completed): 
   print('finishing', name, completed) 

engine = pyttsx3.init() 
  
engine.connect('started-utterance', onStart) 
engine.connect('started-word', onWord) 
engine.connect('finished-utterance', onEnd) 
def main():
 f1 = open('file1.txt',"w")
 f1.writelines(result) 
 f1.close()
 f1 = open('file1.txt').readlines()
 f2 = open('file2.txt').readlines()
 if len(f1) != 0 | len(f2) != 0:
    uniq1 = set(words for line in f1 for words in line.strip('\n\t').split(" "))
    uniq2 = set(wordss for lines in f2 for wordss in lines.strip('\n\t').split(" "))
    for words in uniq1:
        for wordds in uniq2:
            if words == wordds:
                if words == 'hydrocortison':
                 print (words)
                 pres="one tablet in the morning and one tablet at the night"
                 engine.say(words)
                 engine.say(pres)
                 engine.runAndWait()
                 engine.save_to_file(words, "med.wav")
                 engine.save_to_file(pres, "pres.wav")
                 return engine.say(words)
                if words == 'paracetamol':
                 print (words)
                 pres="one tablet in the morning and one tablet at the night"
                 engine.say(words)
                 engine.say(pres)
                 engine.runAndWait()
                if words == 'decil':
                 print (words)
                 pres="one tablet in the morning and one tablet at the night"
                 engine.say(words)
                 engine.say(pres)
                 engine.runAndWait()
                if words == 'arnica':
                 print (words)
                 pres="Appply it on the effected area after washing it by hot water"
                 engine.say(words)
                 engine.say(pres)
                 engine.runAndWait()
cv2.destroyAllWindows()
if __name__ == "__main__":
    main()