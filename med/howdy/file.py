def main():
  import pyttsx3 
  import pytesseract
  import cv2
  pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
  ctx = ssl.create_default_context()
  ctx.check_hostname = False
  ctx.verify_mode = ssl.CERT_NONE
  result = pytesseract.image_to_string('test_images\\1.jpg',lang='eng')
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
                if words == 'hydrocortisone':
                 print (words)
                 return('hydrocortison.mp3',"mp3")
                elif words == 'paracetamol':
                 print (words)
                 return('paracetamol.mp3',"mp3")
                elif words == 'decil':
                 print (words)
                 return('decil.mp3',"mp3")
                elif words == 'arnica':
                 print (words)
                 return('arnica.mp3',"mp3")
                else :
                  return(0,0)

if __name__ == "__main__":
    main()
