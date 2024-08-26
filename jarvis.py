import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclib
rec = sr.Recognizer()
engine=pyttsx3.init()
def speak(text, s):
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate+s)
    engine.say(text)
    engine.runAndWait()

def process(c):
    
    if ("open google") in c.lower():
        webbrowser.open("https://google.com")
    elif ("open chatgpt") in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif ("my mails") in c.lower():
        webbrowser.open("https://gmail.com")
    elif ("open facebook") in c.lower():
        webbrowser.open("https://facebook.com")
    elif ("open youtube") in c.lower():
        webbrowser.open("https://youtube.com")
    elif ("watch videos") in c.lower():
        webbrowser.open("https://youtube.com")
    elif ("watch anime") in c.lower():
        webbrowser.open("https://gogoanimeapp.com")
    elif ("say something") in c.lower():
        speak("This project is dedicated to all my superiors and little ones who believed in me",s=-0)
    elif ("about yourself") in c.lower():
        speak('''I am the first humble creation of my master who is a human named "Sudipto Saha". 
        I am named after the virtual assistant of the science fiction character "iron man". Though I am nothing compared to the Jarvis 
        you may know . But even still try to carry out your commands , no pun intended''', s=0)
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclib.music[song]
        webbrowser.open(link)
    elif c.lower()=="list":
        print(musiclib.lst())
    elif c.lower()=="commands":
        print('''open google\nopenchatgpt\nmy mails(opens gmail)\n
        open facebook\nopen youtube\nwatch videos\nabout yourself\nplay(name of your song)\n''')



if(__name__== "__main__"):
    speak("Jarvis at your service.", s= -50)
    while True:
        rec=sr.Recognizer()
        print("( 0^0 )")
        try:
            with sr.Microphone() as source:
                print("listening")
                audio=rec.listen(source,timeout=3,phrase_time_limit=3)
            c = rec.recognize_google(audio)
            print(c)
            
            if(c.lower()=="Jarvis"):
                print("At your service")
            
            with sr.Microphone() as source:
                print("ready ")
                speak("At your service, sir", s=0)
                audio = rec.listen(source,timeout=5,phrase_time_limit=5)
                command = rec.recognize_google(audio).lower()
                
                process(command)

        
        except Exception as e:
            print(f"I apologize. Would you repeat, please? Error :{e} ".format(e))