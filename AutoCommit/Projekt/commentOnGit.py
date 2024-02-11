import random
import webbrowser
import pyautogui
import time


# switch to Chat
def switchToChat():
    chatIcon = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\chatIconWeb.png')
        
    if chatIcon is not None:
        pyautogui.moveTo(chatIcon)
        pyautogui.click()
        print("moved to ChatGPT!")
        
    else:
        print("move to ChatGPT unsuccesfull")

# switch to Git        
def switchToGit():
    GITIcon = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\GITIconWeb.png')
        
    if GITIcon is not None:
        pyautogui.moveTo(GITIcon)
        pyautogui.click()
        print("moved to GIT!")
        
    else:
        print("move to GIT unsuccesfull")

# -------------------------------------------------------------------------------------
# # functions for random website
def clickOnSortBy():
    sortBy = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\sortByGIT.png')
        
    if sortBy is not None:
        pyautogui.moveTo(sortBy)
        pyautogui.click()
        print("sortBy found!")  
    else:
        print("sortBy not found")
            
def clickOnPastWeek():
    # pastWeek = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\pastWeekGIT.png')
    pastWeek = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\pastDayGit.png')
        
    if pastWeek is not None:
        pyautogui.moveTo(pastWeek)
        pyautogui.click()
        print("pastWeek found!")  
    else:
        print("pastWeek not found")    

def load_urls_and_names(filename):
    urls_and_names = {}
    with open(filename, 'r') as file:
        for line in file:
            url, name = line.strip().split(',')
            urls_and_names[url.strip()] = name.strip()
    return urls_and_names

def get_random_url_and_name(urls_and_names):
    random_url = random.choice(list(urls_and_names.keys()))
    return random_url, urls_and_names[random_url]

def check_page_suitability():
    chatSymbol_0 = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\chatZeroGit.png')
    chatSymbol_1 = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\chatOneGit.png')
    
    if chatSymbol_0 is None and chatSymbol_1 is None:
        return False
    else:
        return True

# # # # acces random website
def access_random_website():
    filename = r'AutoCommit\Projekt\testUrl.txt' 
    # filename = r'AutoCommit\Projekt\urls.txt' 
    urls_and_names = load_urls_and_names(filename)
    
    while urls_and_names:
        random_url, name = get_random_url_and_name(urls_and_names)
        print("Accessing random website:", random_url)
        print("Name:", name)
        
        try:
            webbrowser.open(random_url)
            print("Website successfully opened in the default web browser.")
            
            #try to click the buttons to get to the discussions 
            time.sleep(5)  
            clickOnSortBy()
            time.sleep(2)
            clickOnPastWeek()
            
            # Decide whether the page is suitable or not
            if check_page_suitability():
                print("You can comment!")
                break  
            else:
                print("Two comments already exist")
                
                # close tab immediately
                pyautogui.hotkey('ctrl', 'w')
                
        except Exception as e:
            print("Error:", e)
        
        # Remove the failed link from the dictionary and try again
        del urls_and_names[random_url]
    
    if not urls_and_names:
        print("No more valid links available.")
        
    return name

# -----------------------------------------------------------------------------------------------

def clickChatSymbol():
    chatSymbol = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\chatGIT.png')
        
    if chatSymbol is not None:
        pyautogui.moveTo(chatSymbol)
        x, y = chatSymbol
        pyautogui.click(x + 50, y - 20)  
        print("chatSymbol found!")
    else:
        print("chatSymbol not found")
        
def clickOnDots():
    dots = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\discDotsGIT.png')    
        
    if dots is not None:
        pyautogui.moveTo(dots)
        pyautogui.click()
        
        print("discussion copied!")
    else:
        print("failed to copy discussion")
        
# # # # copy Discussion
def copyDiscussion():
    
    clickChatSymbol()
    time.sleep(1)
    
    clickOnDots()
    
    # locate references 
    time.sleep(1)  
    reference = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\referenceGIT.png')    
        
    if reference is not None:
        pyautogui.moveTo(reference)
        pyautogui.click()
        
        # in the text field
        time.sleep(2)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'c')
        
        #close field
        closeField = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\closeFieldGIT.png')
        
        if closeField is not None:
            pyautogui.moveTo(closeField)
            pyautogui.click()
            print("text field succesfully closed!")
        
        else:
            print("text field could not be closed")
        
        print("copy text worked!")
    else:
        print("copy text failed")


# #  get answer from Chat functions

# -----------------------------------------------------------------------------------------
# copy output
def copyOutput():
    copySymbol = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\copySymbolChat.png')
    
    if copySymbol is not None:
        pyautogui.moveTo(copySymbol)
        pyautogui.click()
        print("copied the comment!")
    else:
        print("couldn't copy the comment")
        
    
# # ask chat for feedback 
def ask_Chat_For_Comment():
    promtLine = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\promtLineChat.png')

    if promtLine is not None:
        # type the discussion in chat
        pyautogui.moveTo(promtLine)
        x, y = promtLine
        pyautogui.click(x-200, y)
        pyautogui.typewrite("Write a short and positive Feedback to the following description: ")
        pyautogui.hotkey('shift', 'enter')
        pyautogui.hotkey('shift', 'enter')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('enter')
        
        # copy the Output from Chat
        time.sleep(10)
        copyOutput()
        print("ask Chat succesfully!")
        
    else:
        print("can't ask Chat")

def ask_Chat_Main():
    # switch to ChatGPT tab
    switchToChat()
    ask_Chat_For_Comment()
 
# -------------------------------------------------------------------------------------
# click on quote reply
def clickOnQuoteReply():
    quote = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\quoteReplyGit.png')
    
    if quote is not None:
        pyautogui.moveTo(quote)
        pyautogui.click()
        print("click on Quote Reply succesfull!")
    else:
        print("click on Quote Reply unsuccesfull")   
        
# # # # write the comment
def write_Git_Comment_Main():
    
    switchToGit()
    clickOnDots()
    clickOnQuoteReply()
    
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'v')
    comment = pyautogui.locateCenterOnScreen(r'AutoCommit\Projekt\buttons\commentGit.png')  
    
    if comment is not None:
        pyautogui.moveTo(comment)
        pyautogui.click()
        print("comment Button worked!")
    else:
        print("comment Button didn't worked")

# -----------------------------------------------------------------------------------    
# close the two tabs
def closeTheTabs():
    pyautogui.hotkey('ctrl', 'w')
    switchToChat()
    # close ChatGPT Chat
    pyautogui.hotkey('ctrl', 'w')


def git_main():
    name = access_random_website()
    time.sleep(1)
    copyDiscussion()  
    time.sleep(1)
    ask_Chat_Main()
    time.sleep(1)
    write_Git_Comment_Main()
    time.sleep(1)
    closeTheTabs()
    return name  # Den extrahierten Namen zurückgeben


git_main()