# utils.py
import pyautogui
import webbrowser
import time

def open_browser(url):
    webbrowser.open(url)

def click_at_position(x, y, duration=0.5):
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.click()

def click_right(x, y, duration=0.5):
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.rightClick()
    
def type_with_shortcut(text, shortcut):
    pyautogui.typewrite(text)
    pyautogui.hotkey(*shortcut)

def press_key(key):
    pyautogui.press(key)

