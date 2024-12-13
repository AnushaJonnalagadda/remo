from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
try:
    driver.get("https://www.python.org")
    ele=driver.find_element(By.CLASS_NAME,'introduction')
    print("Text from selected element:",ele.text)
    download_link=driver.find_element(By.LINK_TEXT,'Downloads')
    download_link.click()
    time.sleep(5)
finally:
    driver.quit()