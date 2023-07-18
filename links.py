import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

#https://engage.englandnetball.co.uk/EnglandNetball

#DRIVER_PATH = '/path/to/chromedriver'
driver = webdriver.Chrome()
driver.get('https://engage.englandnetball.co.uk/EnglandNetball')

# after page loads click on button with text 'Find a Club'
driver.find_element(By.ID, "btnFindClub").click()

count = 0
rows = 0

while(True):
    time.sleep(5)

    # get all elements with class 'fsi-panel-row-title'
    elements = driver.find_elements(By.CLASS_NAME, "fsi-panel-row-title")
    rows += len(elements)

    # print all elements
    for idx, elem in enumerate(elements):
        #print(re.sub("[^0-9]", "", element.get_attribute('onclick')))
        elements[idx] = re.sub("[^0-9]", "", elem.get_attribute('onclick'))

    # append to a csv
    with open('links.csv', 'a') as f:
        for item in elements:
            f.write("%s\n" % item)

    driver.find_element(By.CLASS_NAME, "fsi-grid-panel-next-x").click()

    time.sleep(5)
    count += 1
    print('pages competed: ', count)
    print('rows scraped: ', rows)