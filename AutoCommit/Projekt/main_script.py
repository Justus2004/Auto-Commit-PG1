import os
import time

from utils import *
from idea_manager import *
from clipboard_extractor import *
from push_idea import *
from clickBell import *
from commentOnGit import *
from askChat import *
from newDiscussion import*

if __name__ == "__main__":
    #idee
    idee = idee_ziehen()[:-2]
    name = idee + ".py"
    print(idee)
    
    # open Chat
    chatgpt_url = 'https://chat.openai.com/auth/login'
    GitHub_url = 'https://github.com/Justus2004/codespaces-jupyter/discussions'
    open_browser(chatgpt_url)

    # ask chat
    time.sleep(5)
    ask_chat_gpt(idee)
    clickOnCopy()

    # push file
    extract_code_from_clipboard(name)
    time.sleep(2)
    create_and_push_commit_file(name, "new Programm")
    open_browser(GitHub_url)
    
    # write new discussion
    time.sleep(2)
    new_discussion_main(idee)

    # comment on git and add bell on discord
    time.sleep(2)
    name = git_main()  # Name von git_main erhalten
    discord_Main(name)  # Name an discord_Main übergeben
