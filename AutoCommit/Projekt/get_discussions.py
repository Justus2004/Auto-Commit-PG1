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
    activity_loc = pyautogui.locateCenterOnScreen(r'sort by activiy')
    pyautogui.click(activity_loc)
    week_activity_loc = pyautogui.locateCenterOnScreen(r'sort by week')
    pyautogui.click(week_activity_loc)
    if pyautogui.locateCenterOnScreen(r' ')==False:
        
    else:
        discussion_loc = pyautogui.locateCenterOnScreen(r'Last Week')
        pyautogui.click(discussion_loc)
    
    click_at_position(x=119, y=574)
    
    if pyautogui.locateCenterOnScreen(r'top bild')==False:
        pyautogui.scroll('?')
    else:
        top_loc = pyautogui.locateCenterOnScreen(r'top bild')
        pyautogui.moveTo(top_loc)
    
    pyautogui.hotkey(["ctrl","c"])
    open_browser(chat_link)
    message_loc = pyautogui.locateCenterOnScreen(r'Message chat')
    pyautogui.click(message_loc)
    pyautogui.hotkey(["ctrl","v"])
    clickOnCopy()
    #auf github einfügen und abschicken 
    
    
    
    
    
    