import os
import time

from utils import *
from idea_manager import *
from clipboard_extractor import *
from push_idea import *

if __name__ == "__main__":
    idee = idee_ziehen()
    url = 'https://chat.openai.com/auth/login'
    open_browser(url)

    # perform_login()
    time.sleep(5)
    ask_chat_gpt(idee)
    clickOnCopy()
    
    # Automatische Datenname funktioniert nicht
    extract_code_from_clipboard("Test.py")
    #create_and_push_commit_file("Test.py","Test")


# open ai in python 