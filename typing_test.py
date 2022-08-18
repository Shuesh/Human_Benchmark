"""
Mandatory docstring
"""

from selenium.webdriver import ActionChains


def run(driver):
    """
    Run the typing test solver
    """
    
    test_content = driver.find_element(by="xpath", value="/html/body/div[1]/div/div[4]/div[1]/div/div[2]/div")
    characters = test_content.find_elements(by="xpath", value="span")
    content_string = ""
    for character in characters:
        if character.text != '':
            content_string += character.text
        else:
            content_string += " "
    
    ActionChains(driver)\
        .send_keys(content_string)\
        .perform()

    driver.find_element(by="xpath", value="/html/body/div[1]/div/div[4]/div[1]/div/div[3]/button[1]").click()
    
    return
    