from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

driver = webdriver.Chrome()

def type_current_word(input_element):
    global driver

    # When getting the word list, the website sometimes changes it,
    # so the list we have may become outdated.
    # To prevent this, we get the first word that has not been marked as used.
    word = driver.execute_script(
    """
        word = document.querySelector(".word:not([used])");
        word.setAttribute("used", "");
        return word.textContent;
    """)
    input_element.send_keys(word + Keys.SPACE)

def main():
    driver.get("https://monkeytype.com/")
    input_element = driver.find_element(By.ID, "wordsInput")

    try:
        while True:
            type_current_word(input_element)
            
    except:
        pass

    os._exit(0) # Aggressive exit to bypass destructors and keep the website open.

if __name__ == "__main__":
    main()