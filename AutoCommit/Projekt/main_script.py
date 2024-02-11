import os
import time

from utils import *
from idea_manager import *
from clipboard_extractor import *
from push_idea import *
from clickBell import *
from commentOnGit import *
from askChat import *

if __name__ == "__main__":
    idee = idee_ziehen()[:-2]
    name = idee + ".py"
    print(idee)

    chatgpt_url = 'https://chat.openai.com/auth/login'
    GitHub_url = 'https://github.com/Justus2004/codespaces-jupyter/discussions'
    open_browser(chatgpt_url)

    time.sleep(5)
    ask_chat_gpt(idee)
    clickOnCopy()

    extract_code_from_clipboard(name)
    time.sleep(2)
    create_and_push_commit_file(name, "new Programm")
    open_browser(GitHub_url)

    name = git_main()  # Name von git_main erhalten
    discord_Main(name)  # Name an discord_Main übergeben

    

# 1. Clicks in Prozent (mit Anzahl der Pixel, pyautogui hat ein Befehl für das anzeigen der Anzahl)
# 2. Chat, nach Benutzung löschen
# 3. Nach Copied wechsel zu GITHUB
# 4. Diskussion über Selenium, xPath
# 5. Programm soll nach 7 Tagen gelöscht werden 