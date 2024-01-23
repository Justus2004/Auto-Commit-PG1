import os
import time

from utils import open_browser, perform_login, ask_chat_gpt, clickOnCopy
from idea_manager import IdeaManager
from clipboard_extractor import ClipboardExtractor
from push_idea import Push

if __name__ == "__main__":
    idee = IdeaManager.bearbeite_datei()
    url = 'https://chat.openai.com/auth/login'
    open_browser(url)

    # perform_login()
    time.sleep(5)
    ask_chat_gpt(idee)
    clickOnCopy()
    ClipboardExtractor.extract_code_from_clipboard("Test.py")
    #Push.create_and_push_commit_file("Test.py","Test")


# open ai in python 