from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
chrome_options = Options()
chrome_options.add_argument("--headless")
driver_path = "C:\Program Files\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service,
                          options=chrome_options)
driver.get('http://pythonscraping.com')
driver.implicitly_wait(1)
print(driver.get_cookies())