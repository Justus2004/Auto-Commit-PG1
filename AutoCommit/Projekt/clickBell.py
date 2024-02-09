import pyautogui
import time

def findName():
    while True:
        name = pyautogui.locateCenterOnScreen(r'Projekt\names\Marvin.png')
        
        if name is not None:
            pyautogui.moveTo(name)
            print("Name found!")
            break  
        else:
            pyautogui.scroll(700)
            time.sleep(1)  

def getDots():
    dots = pyautogui.locateCenterOnScreen(r'Projekt\buttons\dotsDiscord.png')
        
    pyautogui.moveTo(dots)
    pyautogui.click()


def getBell():
    bell = pyautogui.locateCenterOnScreen(r'Projekt\buttons\bellDiscord.png')
    
    pyautogui.moveTo(bell)
    pyautogui.click()
    

# if __name__ == "__main__":
    
#     time.sleep(3)
    
#     findName()
#     getDots()
#     getBell()