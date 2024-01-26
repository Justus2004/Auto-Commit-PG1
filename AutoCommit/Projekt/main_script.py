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
    
    url = 'https://chat.openai.com/auth/login'
    open_browser(url)

    # perform_login()
    time.sleep(5)
    ask_chat_gpt(idee)
    clickOnCopy()
    
    # extract and push
    extract_code_from_clipboard(name)
    time.sleep(2)
    create_and_push_commit_file(name,"new Programm")
