from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
#%%
import pandas as pd
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#=========================FILE
df = pd.read_excel('data_input.xlsx')
# print(df["name"][0])
print(df["name"][0]) 


#========================FUNCTIONS
def cells(x,y):
    return df["Unnamed: "+str(x-1)][y-2]
#%%
def install(data_no):
    driver.get("https://shopify.com/")
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"Hero\"]/div/div[1]/div[2]/form/div/div/button"))
        )
    finally:
        pass
    element.click()

    driver.find_element_by_name("signup[email]").send_keys(df["email"][data_no])
    driver.find_element_by_name("signup[password]").send_keys(df["password"][data_no])
    driver.find_element_by_name("signup[shop_name]").send_keys(df["name"][data_no])
    driver.find_element_by_xpath('//*[@id="SignupForm_modal"]/div[6]/button').click()
    
    # time.sleep(5)
    # driver.quit()
install(0)