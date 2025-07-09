import speech_recognition as sr
import pyttsx3
import webbrowser as wb
import music_lib
import requests
import pyautogui
import time
import tkinter as tk

r= sr.Recognizer()
# Enter your API key for NewsAPI
apikey="" # Generate your own API key from https://newsapi.org
def say(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def mike_GUI():
    while True:
        ww=tk.Tk()
        ww.title("jarvis")
        ww.
        

def processcommand(command):
    print(f"request went:{command}")
    if "open google" in command.lower():
        wb.open("https://www.google.com/")
    
    elif "open youtube" in command.lower():
        wb.open("https://www.youtube.com/")
    
    elif "open ai" in command.lower():
        wb.open("https://chatgpt.com/")
    
    elif "open padh le" in command.lower():
        wb.open("https://live.padhle.in/s/courses/6678560b7ed11c6a45a853a8/take")
    
    elif "open amazon" in command.lower():
        wb.open("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=17760767577479957526&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9300507&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1")
    
    elif "open git" in command.lower():
        wb.open("https://github.com/")
    #play song:-
    elif command.lower().startswith("play"):
        songsplit=command.split()[1:]
        song=" ".join(songsplit).lower()
        try:
            findsong=music_lib.music[song]
            wb.open(findsong)
        except Exception as f:
            print(f"error;{f}")
          
    elif command.lower().startswith("search"):
        search_split=command.lower().replace("search","")
        print(search_split)
        wb.open("https://www.google.com/")
        time.sleep(3.5)
        pyautogui.typewrite(search_split)
        pyautogui.hotkey("enter")

    elif "news" in command.lower():
        fetch=requests.get(f"https://newsapi.org/v2/everything?q=India&apiKey={apikey}")
        news_data=fetch.json()
        articles=news_data.get("articles",[])
        for i in articles:
            print(i["title"])
            say(i["title"])
    
    elif "shutdown" in command.lower():
        global lo
        lo=lo+1
        say("jarvis shut downed")
         

if __name__=="__main__":
    say("Initializing Jarvis....")
    lo=1
    while lo!=2:
                                                  
        #listen for word jarvis
        with sr.Microphone() as source:
            print("listening...")
            audio_text = r.listen(source)
            print("recognising")
         
            try:
                a=r.recognize_google(audio_text)
            
            except Exception as f2:
                print("could not recognise;")
                print(f2)
                continue

            if a=="Jarvis":
                say("Yeah,jarvis activated")
                print("Jarvis active")
                #taking command as audio and coverting into text in order to send command in func parmeter
                lo=2

    while lo==2:
        # try:
            with sr.Microphone() as source2:
                print("how can i help you?,")
                print("listening...")
                window=tk.Tk()
                command_lis=r.listen(source2)
                command_text=r.recognize_google(command_lis)
                processcommand(command_text)

        # except Exception as e1:
        #     print(e1)
        #     print(f"sorry,could not get that")

                

