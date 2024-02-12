import pyautogui
import time

def open_discord():
    # discord_icon_open = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\discordIcon.png')  
    # discord_icon_close = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\discord_icon_close.png') 
    
    # if discord_icon_open is not None:
    #     pyautogui.click(discord_icon_open)
    #     print("was able to open discord_open")
    # else:
    #     print("was unabel to open discord_open")
    
    # time.sleep(1)
    
    # if discord_icon_close is not None:
    #     pyautogui.click(discord_icon_close)
    #     print("was able to open discord_close")
    # else:
    #     print("was unabel to open discord_close")   
    
    pyautogui.click(536, 1044)  
          
def goToProgramingClass():
    # programming = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\programming.png')  
    # if programming is not None:
    #     pyautogui.click(programming)
    #     print("channel found")
    # else:
    #     print("channel not found")
    
    pyautogui.moveTo(48, 234)
    pyautogui.click()

def findRightChannel():
    pyautogui.moveTo(422, 390)
    time.sleep(2)
    pyautogui.scroll(-500)
    
    weeklyCoding = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\weeklyCodingDiscord.png')
    
    if weeklyCoding is not None:
        pyautogui.moveTo(weeklyCoding)
        pyautogui.click()
    else:
        print("didn't work")

def findName(name):
    pyautogui.moveTo(1455, 640)
    time.sleep(1)
    name_lowercase = name.lower()  # Um sicherzustellen, dass der Name in Kleinbuchstaben ist
    while True:
        mate = pyautogui.locateCenterOnScreen(f'AutoCommit\\Projekt\\names\\{name_lowercase}.png')
        
        if mate is not None:
            pyautogui.moveTo(mate)
            
            # get to threads
            x, y = mate
            pyautogui.moveTo(x+955, y, duration = 1)
            pyautogui.moveTo(x+955, y-20, duration=1)
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
 

# def getDots():
#     dots = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\dots_Discord.png')
#     x, y = dots    
#     pyautogui.moveTo(dots)
#     pyautogui.click()
#     time.sleep(2)
#     pyautogui.click(x-240 ,y+5)
    
#     # move to dots
#     time.sleep(2)
#     pyautogui.moveTo()
#     pyautogui.click()


# def getThread(name):

#     field = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\twoEmojis.png')
#     time.sleep(2)
    
#     if field is not None:
#         pyautogui.moveTo(field)
#         x,y = field
#         pyautogui.moveTo(x-105, y, duration=1)  
#         pyautogui.click()
#     else:
#         print("didn't work")
        
def getReaction():
    reaction = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\reactionDiscordText.png')
    
    if reaction is not None:
        pyautogui.moveTo(reaction)
        # click on Dots
        x, y = reaction
        pyautogui.moveTo(x-60, y-50)
        pyautogui.click()
        # # click on bell
        # pyautogui.moveTo(x-250, y+10)
        # pyautogui.click()
    else:
        print("didn't work")
    
def discord_Main(name):
    open_discord()
    time.sleep(3)
    goToProgramingClass()
    time.sleep(1)
    findRightChannel()
    time.sleep(1)
    findName(name)
    # time.sleep(2)
    # getDots()
    # time.sleep(2)
    # getThread(name)
    time.sleep(2)
    getReaction()


name = "Jonas"
discord_Main(name)

# über threads, drei punkte, bell