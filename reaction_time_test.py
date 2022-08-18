"""
Obnoxious mandatory docstring
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run(driver):
    """
    Solves the reaction time test as quickly as possible
    """

    # Start with the reaction time test
    test_location = driver.find_element(by="xpath", value="/html/body/div[1]/div/div[4]/div[1]")

    count = 0
    while True:
        if "view-go" in test_location.get_attribute('class').split():
            test_location.click()
            count += 1
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((test_location))
            ).click()
        if count >= 5:
            driver.find_element(by="xpath", value="/html/body/div[1]/div/div[4]/div[1]/div/div/div[3]/button[1]").click()
            return
