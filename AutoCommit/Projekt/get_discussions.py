import random
from utils import *
import pyautogui
from clipboard_extractor import *
def pull_disscusion_link():
    dateiName = 'Auto-Commit-PG1\AutoCommit\Projekt\Git-Hub-Acc.txt'

    # Zähle die Anzahl der Zeilen in der Datei
    with open(dateiName, 'r') as f:
        zeilen = f.readlines()

    # Wähle eine zufällige Zeilennummer
    zufalls_zeilennummer = random.randint(0, len(zeilen) - 1)

    # Lies die zufällige Zeile
    with open(dateiName, 'r') as f:
        zufalls_zeile = f.readlines()[zufalls_zeilennummer]

    return zufalls_zeile

def main():
    link = pull_disscusion_link()
    chat_link = 'https://chat.openai.com/auth/login'
    
    open_browser(link)
    activity_loc = pyautogui.locateCenterOnScreen(r'Projekt\buttons\discussion_push_button\Latest_Activity_Button.png')
    pyautogui.click(activity_loc)
    week_activity_loc = pyautogui.locateCenterOnScreen(r'Projekt\buttons\discussion_push_button\Past_Week_Button.png')
    pyautogui.click(week_activity_loc)
    #auf die discussion clicken
    pyautogui.click(x=854, y=771)
    
    click_at_position(x=119, y=574)
    
    while pyautogui.locateCenterOnScreen(r'Projekt\buttons\discussion_push_button\Top_Button.png')==False:
        pyautogui.scroll('?')
        
    top_loc = pyautogui.locateCenterOnScreen(r'Projekt\buttons\discussion_push_button\Top_Button.png')
    pyautogui.moveTo(top_loc)
    
    pyautogui.hotkey(["ctrl","c"])
    open_browser(chat_link)
    
    #message_loc = pyautogui.locateCenterOnScreen(r'Message chat')
    #pyautogui.click(message_loc)
    pyautogui.hotkey(["ctrl","v"])
    clickOnCopy()
    #auf github einfügen und abschicken 
    
    
    
    
    
    