from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://monkeytype.com/")

def get_current_word():
    """
    When getting the words list. Sometimes the list in the website changes, and the list we have does not.
    To combat this, we get the first word possible which was not marked used.
    """
    global driver
    word = driver.find_element(By.CSS_SELECTOR,".word:not([data-processed='true'])")
    driver.execute_script("arguments[0].setAttribute('data-processed', 'true');", word)
    return word.text

def main():
    element = driver.find_element(By.ID, "wordsInput")
    
    try:
        while True:
            element.send_keys(get_current_word())
            element.send_keys(Keys.SPACE)              
    except:
        print("Typing stopped!")
        
    while driver.window_handles:
        pass
        
if __name__ == "__main__":
    main()