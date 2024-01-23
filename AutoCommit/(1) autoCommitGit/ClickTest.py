import pyautogui

print(pyautogui.position()) 



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# url = 'https://chat.openai.com/auth/login'

# def initialize_driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     return driver

# def navigate_to_url(driver, url):
#     driver.get(url)

# if __name__ == "__main__":
#     driver = initialize_driver()
#     navigate_to_url(driver, url)

#     # Example: Typing into a login form
#     username_input = driver.find_element(By.ID, 'username')  # Replace 'username' with the actual ID or other locator of the username input field
#     username_input.send_keys('your_username')

#     password_input = driver.find_element(By.ID, 'password')  # Replace 'password' with the actual ID or other locator of the password input field
#     password_input.send_keys('your_password', Keys.ENTER)

#     # Example: Hovering over an element
#     some_element = driver.find_element(By.XPATH, '//xpath/to/some/element')
#     ActionChains(driver).move_to_element(some_element).perform()

#     # Example: Waiting for an element to be visible
#     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'some_element_id')))

#     # Other actions you want to perform...

#     # Close the browser window
#     driver.quit()