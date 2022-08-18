"""
Solves the chimp test to a specified sequence depth
"""


def run(driver, depth):
    """
    Runs the chimp test solver
    """
    driver.find_element(by="xpath", value="/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div[2]/button").click()
    
    
    order = ["" for _ in range(depth+1)]
    for _ in range(depth-3):
        game_grid = driver.find_element(by="xpath", value="/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div/div")
        for row in game_grid.find_elements(by="tag name", value="div"):
            for cell in row.find_elements(by="tag name", value="div"):
                if cell.get_attribute("data-cellnumber") is None or cell.get_attribute("data-cellnumber") == "":
                    pass
                else:
                    order[int(cell.get_attribute("data-cellnumber"))] = cell

        for position in order[1:]:
            if position != "":
                position.click()

        driver.find_element(by="xpath", value="/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div[3]/button").click()

    driver.find_element(by="xpath", value="/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div[3]/button[1]").click()

    return
