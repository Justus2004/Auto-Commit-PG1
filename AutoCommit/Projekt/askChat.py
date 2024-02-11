import pyautogui
import time

from utils import *

def perform_login():
    time.sleep(2)
    click_at_position(1400, 550)
    time.sleep(2)
    click_at_position(926, 550)

    type_with_shortcut("vier.drei1", ["ctrl", "alt", "q"])
    pyautogui.typewrite("web.de")
    press_key("enter")

    click_at_position(926, 675, duration=1)
    pyautogui.typewrite("python.Auto.Commit.2023")
    press_key("enter")
    time.sleep(5)
    
def ask_chat_gpt(ideas):
    click_at_position(685, 950, duration=1)

    # Verwende die erste Idee, wenn vorhanden
    if ideas:
        pyautogui.typewrite("write a code in python for " + ideas)
        press_key("enter")
    else:
        print("No ideas available.")
        
    
def clickOnCopy():
    time.sleep(20)
    click_at_position(720, 843)
    time.sleep(2)