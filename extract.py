import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from csv import writer

links_df = pd.read_csv('links.csv', header=None)
results_df = pd.DataFrame(columns=['title', 'link', 'contact_0', 'contact_1'])

#options = webdriver.ChromeOptions()
#options.add_argument('--headless')
#driver = webdriver.Chrome()

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)

for index, row in links_df.iterrows():
    contact_info = [[None, None]]
    driver.get(row[0])
    time.sleep(3)

    title = driver.find_element(By.ID, 'fsi-innertitle')
    title = title.get_attribute('innerText')

    if not title:
        title = 'not found'

    try:
        contact_info_1 = driver.find_element(By.XPATH, '//*[@id="fsi-title-info"]/span[1]/div/div[2]/a')
    except:
        contact_info_1 = None

    try:
        contact_info_2 = driver.find_element(By.XPATH, '//*[@id="fsi-title-info"]/span[2]/div/div[2]/a')
    except:
        contact_info_2 = None

    if contact_info_1:
        contact_info[0][0] = contact_info_1.get_property('text')
    else:
        contact_info[0][0] = ('not available')

    if contact_info_2:
        contact_info[0][1] = contact_info_2.get_property('text')
    else:
        contact_info[0][1] = ('not available')

    # add to results_df
    results_df.loc[len(results_df)] = {'title': title, 'link': row[0], 'contact_0': contact_info[0][0], 'contact_1': contact_info[0][1]}
    # add row to csv
    with open('results.csv', 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow([title, row[0], contact_info[0][0], contact_info[0][1]])
    
    print(f'adding {title} | {len(results_df)}/{len(links_df)} completed')

driver.quit()