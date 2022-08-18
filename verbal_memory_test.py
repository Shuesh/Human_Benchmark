"""
Mandatory docstring
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run(driver, stop_score):
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[4]/button"))
    ).click()
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[3]/button[1]"))
    )
    seen_button = driver.find_element(by="xpath", value="/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[3]/button[1]")
    new_button = driver.find_element(by="xpath", value="/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[3]/button[2]")
    
    seen_words = []
    count = 0
    while count < stop_score:
        word = driver.find_element(by="xpath", value="/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[2]/div")
        if word.text in seen_words:
            seen_button.click()
        else:
            seen_words.append(word.text)
            new_button.click()
        count += 1
    
    for _ in range(3):
        if word.text in seen_words:
            new_button.click()
        else:
            seen_button.click()
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div/div[3]/button[1]"))
    ).click()
    