import os
import time

from utils import open_browser, perform_login, ask_chat_gpt, clickOnCopy
from idea_manager import bearbeite_datei
from clipboard_extractor import extract_code_from_clipboard
from push_idea import Push

if __name__ == "__main__":
    idee = bearbeite_datei()
    url = 'https://chat.openai.com/auth/login'
    open_browser(url)

    # perform_login()
    time.sleep(5)
    ask_chat_gpt(idee)
    clickOnCopy()
    # Automatische Datenname funktioniert nicht
    extract_code_from_clipboard("Test.py")
    #Push.create_and_push_commit_file("Test.py","Test")


# open ai in python 