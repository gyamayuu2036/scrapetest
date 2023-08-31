from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException
import time

def waitForLoad(driver):
    elem = driver.find_element(By.TAG_NAME,"html")
    count = 0
    while True:
        count += 1
        if count > 20:
            print('Timing out after 10 seconds and returning')
            return 
        time.sleep(.5)
        try:
            elem == driver.find_element(By.TAG_NAME, "html")
        except StaleElementReferenceException:
            return 

chrome_options = Options()
chrome_options.add_argument("--headless")
driver_path = "C:\Program Files\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('http://pythonscraping.com/pages/javascript/redirectDemo1.html')

waitForLoad(driver)
print(driver.page_source)
driver.close()