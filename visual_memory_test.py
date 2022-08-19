"""
Mandatory docstring
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run(driver, stop_score):
    
    # Click to start
    WebDriverWait(driver, stop_score+1).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[2]/button"))
    ).click()

    grid = WebDriverWait(driver, stop_score+1).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[2]/div"))
    )
    
    active = []
    for row in grid.find_elements(by="tag name", value="div"):
        for cell in row.find_elements(by="tag name", value="div"):
            
