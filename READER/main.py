import pyttsx3 
import pyperclip as pc
import keyboard
from pyautogui import hotkey
from time import sleep

def say(s):
    engine=pyttsx3.init()
    engine.setProperty("rate",139)
    engine.say(s)
    engine.runAndWait()


sleep(4)

hotkey("ctrl","c")

sentence=pc.paste()


say(sentence)
print(sentence)