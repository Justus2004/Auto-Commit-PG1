import os
import time

from utils import *
from idea_manager import *
from clipboard_extractor import *
from push_idea import *

if __name__ == "__main__":
    idee = idee_ziehen()[:-2]
    name = idee + ".py"

    print(idee)
    
    chatgpt_url = 'https://chat.openai.com/auth/login'
    GitHub_url ='https://github.com/Justus2004/codespaces-jupyter/discussions'
    open_browser(chatgpt_url)

    # perform_login()
    time.sleep(5)
    ask_chat_gpt(idee)
    clickOnCopy()
    
    # extract and push
    extract_code_from_clipboard(name)
    time.sleep(2)
    create_and_push_commit_file(name,"new Programm")
    open_browser(GitHub_url)

# 1. Clicks in Prozent (mit Anzahl der Pixel, pyautogui hat ein Befehl für das anzeigen der Anzahl)
# 2. Chat, nach Benutzung löschen
# 3. Nach Copied wechsel zu GITHUB
# 4. Diskussion über Selenium, xPath
# 5. Programm soll nach 7 Tagen gelöscht werden 