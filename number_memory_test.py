"""
Mandatory docstring
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run(driver, stop_score):
    
    # Click to start
    WebDriverWait(driver, stop_score+1).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[3]/button"))
    ).click()
    
    count = 0
    while count < stop_score:
        # Get the number
        number = WebDriverWait(driver, stop_score+1).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[1]"))
        ).text
        
        # type number to /html/body/div[1]/div/div[4]/div[1]/div/div/div/form/div[2]/input
        input_element = WebDriverWait(driver, stop_score+1).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div/div/form/div[2]/input"))
        )
        input_element.send_keys(number)
        
        # click submit: /html/body/div[1]/div/div[4]/div[1]/div/div/div/form/div[3]/button
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div/div/form/div[3]/button").click()
        
        # click next: /html/body/div[1]/div/div[4]/div[1]/div/div/div/div[2]/button
        number = WebDriverWait(driver, stop_score+1).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[2]/button"))
        ).click()
        
        count += 1
    

    
    # type number to /html/body/div[1]/div/div[4]/div[1]/div/div/div/form/div[2]/input
    input_element = WebDriverWait(driver, stop_score*2).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div/div/form/div[2]/input"))
    )
    input_element.send_keys("1")
    
    # click submit: /html/body/div[1]/div/div[4]/div[1]/div/div/div/form/div[3]/button
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div/div/form/div[3]/button").click()
    
    # click to save score
    WebDriverWait(driver, stop_score+1).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[2]/div/button[1]"))
    ).click()
    

