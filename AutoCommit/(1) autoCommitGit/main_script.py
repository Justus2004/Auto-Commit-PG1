# main_script.py
# from utils import initialize_driver, navigate_to_url, click_element
from utils import open_browser, perform_login, ask_chat_gpt, clickOnCopy
from idea_manager import IdeaManager
from clipboard_extractor import ClipboardExtractor

if __name__ == "__main__":
    # Benutzerdefinierter Dateipfad für IdeaManager
    custom_file_path = r"C:\Users\jpl\repository_AutoCommit\Auto-Commit-PG1\AutoCommit\(1) autoCommitGit\ideas.txt"
    
    url = 'https://chat.openai.com/auth/login'
    open_browser(url)

    # Erstelle eine Instanz von IdeaManager mit benutzerdefiniertem Dateipfad
    im = IdeaManager(file_path=custom_file_path)

    perform_login()
    ask_chat_gpt(im)
    clickOnCopy()
    ClipboardExtractor.extract_code_from_clipboard()


# open ai in python 