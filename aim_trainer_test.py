"""
Perfect the aim trainer test
"""

from selenium import webdriver

def run(driver):
    # Start the test
    target = driver.find_element(by="xpath", value="/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div[2]/div/div/div[2]")

    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(target, 0, 0)
    action.click()
    action.perform()
    
    
    
    # driver.find_element(by="xpath", value="/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div[2]/div/div/div[1]").click()
    
    for _ in range(30):
        target = driver.find_element(by="xpath", value="/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div/div/div/div[2]")

        action.move_to_element_with_offset(target, 0, 0)
        action.click()
        action.perform()
        
    driver.find_element(by="xpath", value="/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div/div[3]/button[1]").click()
    
    return
