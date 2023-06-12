import os
import logging
from datetime import datetime
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC
import undetected_chromedriver as uc
import pandas as pd

print('Please Wait...')

configure_logging(install_root_handler=True)
logging.disable(50)

# Declare start time
start_time = datetime.now()

# Start browser
executable_path = os.path.dirname(os.path.abspath(__file__)) + "\\chromedriver"
options = uc.ChromeOptions()
options.headless = True

driver = uc.Chrome(
    options=options,
    executable_path=executable_path,
    log_level=3,
    version_main=114,
)
driver.get('https://www.coingecko.com/')
try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "toTop"))
    )
    # Remove Ads
    driver.execute_script('''document.querySelectorAll("div[data-target='buy-sell-ads.coinRowBuy']").forEach(e => e.remove())''')

    pageSource = driver.page_source

    tables = []
    tables.append(pd.read_html(str(pageSource))[0])
    master_data = pd.concat(tables)
    master_data = master_data.loc[:, master_data.columns[1:-1]]
    master_data.to_csv('Selenium.csv', index=False)
    end_time = datetime.now()
    print('Execution duration: {}'.format(end_time - start_time))
finally:
    driver.quit()
