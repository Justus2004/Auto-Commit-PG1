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
        pyautogui.moveTo(1455, 640)
        print("channel found")
    else:
        print("channel not found")

def findName(name):
    name_lowercase = name.lower()  # Um sicherzustellen, dass der Name in Kleinbuchstaben ist
    while True:
        mate = pyautogui.locateCenterOnScreen(f'AutoCommit\\Projekt\\names\\{name_lowercase}.png')
        
        if mate is not None:
            pyautogui.moveTo(mate)
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
    time.sleep(2)
    getDots()
    time.sleep(2)
    getBell()
    
name = "Jonas"
discord_Main(name)