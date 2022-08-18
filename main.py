"""
Obnoxious mandatory docstring
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import reaction_time_test
import chimp_test
import aim_trainer_test
import typing_test
import verbal_memory_test
import number_memory_test
import visual_memory_test

def main():
    driver = webdriver.Chrome(executable_path=r'C:\Program Files\Chromedriver\chromedriver.exe')

    # Load the website and start it on the reaction time test
    driver.get("https://humanbenchmark.com/tests/visual-memory")
    
    # # Reaction Test
    # reaction_time_test.run(driver)
        
    # # Chimp Test
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div[2]/div[2]/div/table[1]/tbody/tr[4]/td[2]/div/a[1]"))
    # ).click()
    # chimp_test.run(driver, 40)

    # # Aim Trainer
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div[2]/div[2]/div/table[1]/tbody/tr[5]/td[2]/div/a[1]"))
    # ).click()
    
    # Aim Trainer
    # driver.find_element(by='xpath', value="/html/body/div[1]/div/div[4]/div/div/div[2]/div[2]/div/table[1]/tbody/tr[5]/td[2]/div/a[1]").click()
    # aim_trainer_test.run(driver)
    
    # Typing
    # driver.find_element(by='xpath', value="/html/body/div[1]/div/div[4]/div/div/div[2]/div[2]/div/table[1]/tbody/tr[6]/td[2]/div/a[1]").click()
    # typing_test.run(driver)
    
    # Verbal Memory
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div[2]/div[2]/div/table[1]/tbody/tr[7]/td[2]/div/a[1]"))
    # ).click()
    # verbal_memory_test.run(driver, 1000)
    
    # Number Memory
    # driver.find_element(by='xpath', value="/html/body/div[1]/div/div[4]/div/div/div[2]/div[2]/div/table[1]/tbody/tr[8]/td[2]/div/a[1]").click()
    # number_memory_test.run(driver, 3)
    
    # Visual Memory
    driver.find_element(by='xpath', value="/html/body/div[1]/div/div[4]/div/div/div[2]/div[2]/div/table[1]/tbody/tr[9]/td[2]/div/a[1]").click()
    visual_memory_test.run(driver)

    while True:
        pass

    # Close the driver
    driver.quit()


if __name__ == '__main__':
    main()