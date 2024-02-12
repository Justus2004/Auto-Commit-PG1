import time
import pyautogui
import webbrowser

def open_your_git():
    webbrowser.open('https://github.com/jonasDHBW/codespaces-jupyter/discussions/categories/general')
    
def new_disc():
    new_disc = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\newDiscussion.png')
    
    if new_disc is not None:
        pyautogui.moveTo(new_disc)
        pyautogui.click()
    else:
        print("didn't work")

def type_theme(theme):
    
    pyautogui.typewrite(theme)
    
    text_Field = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\textField.png')
    
    if text_Field is not None:
        pyautogui.moveTo(text_Field)
        pyautogui.click()
    else:
        print("click on text field didn't work")
        
    pyautogui.typewrite("this time i wrote a programm about: " + theme)
    
    startDiscussion = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\startDiscussion.png')
    
    if startDiscussion is not None:
        pyautogui.moveTo(startDiscussion)
        pyautogui.click()
    else:
        print("start Discussion didn't work")

def new_discussion_main(theme):
    open_your_git()
    time.sleep(1)
    new_disc()
    time.sleep(1)
    type_theme(theme)
