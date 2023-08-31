from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")
driver_path = "C:\Program Files\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')

try:
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'loadedButton')))
finally:
    print(driver.find_element(By.ID,'content').text)
    driver.close()