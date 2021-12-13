from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://shopify.com/")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id=\"Hero\"]/div/div[1]/div[2]/form/div/div/button"))
    )
finally:
    pass
element.click()

driver.find_element_by_name("signup[email]").send_keys("hello")
driver.find_element_by_name("signup[password]").send_keys("hello")
driver.find_element_by_name("signup[shop_name]").send_keys("hello")
time.sleep(5)
driver.quit()