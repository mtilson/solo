from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.example.com/')
header_text = driver.find_element(by=By.XPATH, value='//h1').text

print("Answer is: {0}".format(header_text ))
print("Should be: Example Domain")

driver.quit()
