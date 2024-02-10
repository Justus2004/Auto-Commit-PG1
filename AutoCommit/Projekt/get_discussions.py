import random
from utils import *
import pyautogui
import time
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

def find_discussion(link):
    open_browser(link)
    time.sleep(3)
    activity_loc = pyautogui.locateCenterOnScreen('Projekt/buttons/discussion_push_button/Latest_Activity_Button.png')
    pyautogui.moveTo(activity_loc)
    pyautogui.click()
    
    week_activity_loc = pyautogui.locateCenterOnScreen('Projekt\buttons\discussion_push_button\Past_Week_Button.png')
    pyautogui.moveTo(week_activity_loc)
    pyautogui.click()
    
    #auf die discussion clicken
    pyautogui.click(x=854, y=771)
    
    
def copy_discussions():
    #zum kopierpunkt gehen
    pyautogui.moveTo(x=119, y=574)
    pyautogui.mouseDown()
    
    while pyautogui.locateCenterOnScreen('Projekt\buttons\discussion_push_button\Top_Button.png')==None:
        pyautogui.scroll(700)
        
    top_loc = pyautogui.locateCenterOnScreen('Projekt\buttons\discussion_push_button\Top_Button.png')
    pyautogui.moveTo(top_loc)
    pyautogui.mouseUp()
     
def get_discussion_main():
    #links
    link = pull_disscusion_link()
    chat_link = 'https://chat.openai.com/auth/login'
    #Git-Hub öffnen
    find_discussion(link)
    copy_discussions()
    #kopieren und in chatgpt einfügen
    pyautogui.hotkey(["ctrl","c"])
    open_browser(chat_link)
    pyautogui.hotkey(["ctrl","v"])
    clickOnCopy()
    find_discussion(link)
    while pyautogui.locateCenterOnScreen('Auto-Commit-PG1\AutoCommit\Projekt\buttons\discussion_push_button\Paste_Commend_Button.png') == None:
        pyautogui.scroll(700)
    
    paste_comment = pyautogui.locateCenterOnScreen('Auto-Commit-PG1\AutoCommit\Projekt\buttons\discussion_push_button\Paste_Commend_Button.png')
    pyautogui.click(paste_comment)
    
    send_comment = pyautogui.locateCenterOnScreen('Auto-Commit-PG1\AutoCommit\Projekt\buttons\discussion_push_button\Send_Comment_Button.png')
    pyautogui.click(send_comment)
    
    
    
    #auf github einfügen und abschicken

get_discussion_main()
    
    
    
    
    
    