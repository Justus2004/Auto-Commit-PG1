import pyautogui
import time

time.sleep(3)

# Funktion zum Scrollen bis zum Ende der Seite
def scroll_to_end():
    pyautogui.scroll(700)  # Scrolle nach unten

# Funktion zum Bewegen des Mauszeigers auf ein Bild
def move_to_image(image_name):
    image_location = pyautogui.locateCenterOnScreen(image_name)
    if image_location:
        pyautogui.moveTo(image_location)  # Hier wird der Mauszeiger zum Bild bewegt
        return True
    else:
        return False

def click_bell():
    dot_loc = pyautogui.locateCenterOnScreen(r'Projekt\buttons\dotsDiscord.png')
    bell_loc = pyautogui.locateCenterOnScreen(r'Projekt\buttons\bellDiscord.png')
    
    pyautogui.moveTo(dot_loc)
    pyautogui.click
    time.sleep(2)
    pyautogui.moveTo(bell_loc)
    pyautogui.click
    

# Endlos scrollen, bis das Bild gefunden wird
while True:
    if move_to_image(r'Projekt\names\Marvin.png'): 
        print("Image found")
        break  
    else:
        scroll_to_end() 

time.sleep(2)          
click_bell()
