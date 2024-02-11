import pyautogui
import time

def open_discord():
    discord_icon_open = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\discord_icon_open.png')  
    discord_icon_close = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\discord_icon_close.png') 
    
    if discord_icon_open is not None:
        pyautogui.click(discord_icon_open)
        print("was able to open discord_open")
    else:
        print("was unabel to open discord_open")
    
    time.sleep(1)
    
    if discord_icon_close is not None:
        pyautogui.click(discord_icon_close)
        print("was able to open discord_close")
    else:
        print("was unabel to open discord_close")   
        
def goToProgramingClass():
    programming = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\programming.png')  
    if programming:
        pyautogui.click(programming)
        print("channel found")
    else:
        print("channel not found")

def findName(name):
    while True:
        name = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\names\Marvin.png')
        
        if name is not None:
            pyautogui.moveTo(name)
            print("Name found!")
            break  
        else:
            pyautogui.scroll(700)
            time.sleep(1)  

def getDots():
    dots = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\dotsDiscord.png')
        
    pyautogui.moveTo(dots)
    pyautogui.click()


def getBell():
    bell = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\bellDiscord.png')
    
    pyautogui.moveTo(bell)
    pyautogui.click()
    
def discord_Main(name):
    open_discord()
    time.sleep(3)
    goToProgramingClass()
    findName(name)
    getDots()
    getBell()
    
name = "Jonas"
discord_Main(name)