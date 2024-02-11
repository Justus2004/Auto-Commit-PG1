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
    if programming is not None:
        pyautogui.click(programming)
        print("channel found")
    else:
        print("channel not found")

def findName(name):
    pyautogui.moveTo(1455, 640)
    time.sleep(1)
    name_lowercase = name.lower()  # Um sicherzustellen, dass der Name in Kleinbuchstaben ist
    while True:
        mate = pyautogui.locateCenterOnScreen(f'AutoCommit\\Projekt\\names\\{name_lowercase}.png')
        
        if mate is not None:
            pyautogui.moveTo(mate)
            x, y = mate
            pyautogui.moveTo(x+955, y, duration = 1)
            pyautogui.moveTo(x+955, y-26, duration=1)
            pyautogui.click()
            # time.sleep(2)
            # pyautogui.moveTo(x+670, y)
            # pyautogui.click()
            # time.sleep(2)
            print("Name found!")
            break  
        else:
            pyautogui.scroll(700)
            time.sleep(1) 
 

def getDots():
    dots = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\dots_Discord.png')
    x, y = dots    
    pyautogui.moveTo(dots)
    pyautogui.click()
    time.sleep(2)
    pyautogui.click(x-270 ,y+5)


def getBell(name):
    while True: 
        field = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\twoEmojis.png')
        time.sleep(2)
        
        if field is not None:
            pyautogui.moveTo(field)
            
            x,y = field
            pyautogui.moveTo(x-105, y, duration=1)  
            pyautogui.click()
            break
        else:
            pyautogui.scroll(30)
            time.sleep(2)
            pyautogui.click(900, 5)
            findName(name)
            print("didn't work")
    
def discord_Main(name):
    open_discord()
    time.sleep(3)
    goToProgramingClass()
    findName(name)
    time.sleep(2)
    # getDots()
    # time.sleep(2)
    getBell(name)


name = "Pascal"
discord_Main(name)

# über threads, drei punkte, bell