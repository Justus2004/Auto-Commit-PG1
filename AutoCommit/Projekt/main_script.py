import os


from utils import open_browser, perform_login, ask_chat_gpt, clickOnCopy
from idea_manager import IdeaManager
from clipboard_extractor import ClipboardExtractor

if __name__ == "__main__":
    
    url = 'https://chat.openai.com/auth/login'
    open_browser(url)

    perform_login()
    ask_chat_gpt(IdeaManager.bearbeite_datei())
    clickOnCopy()
    ClipboardExtractor.extract_code_from_clipboard()


# open ai in python 