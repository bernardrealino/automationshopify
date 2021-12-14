from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
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

    # driver.find_element_by_name("signup[email]").send_keys(df["email"][data_no])
    # driver.find_element_by_name("signup[password]").send_keys(df["password"][data_no])
    # driver.find_element_by_name("signup[shop_name]").send_keys(df["name"][data_no])
    x = 28
    driver.find_element_by_name("signup[email]").send_keys(f"john99{str(x)}@gmail.com")
    driver.find_element_by_name("signup[password]").send_keys("john123")
    driver.find_element_by_name("signup[shop_name]").send_keys(f"john99{str(x)}")
    driver.find_element_by_xpath('//*[@id="SignupForm_modal"]/div[6]/button').click()
    driver.implicitly_wait(10) # seconds
    driver.find_element_by_xpath('//*[@id="AppFrameMain"]/div/div/div/div[1]/div/footer/div/div[2]/button').click()

    country = driver.find_element_by_name('account_setup[country]')
    select_country = Select(country)
    fname = driver.find_element_by_name('account_setup[firstName]')
    lname = driver.find_element_by_name('account_setup[lastName]')
    city = driver.find_element_by_name('account_setup[city]')
    address = driver.find_element_by_name('account_setup[address1]')
    province = driver.find_element_by_name('province')
    select_province = Select(province)
    zip = driver.find_element_by_name('account_setup[zip]')
    phone = driver.find_element_by_name('account_setup[phone]')

    select_country.select_by_visible_text("Indonesia")
    fname.send_keys("hello")
    lname.send_keys("there")
    address.send_keys("this street")
    city.send_keys("luxemburg")
    select_province.select_by_visible_text("Lampung")
    zip.send_keys("35111")
    phone.send_keys("+62852271289")

    #proceed
    driver.find_element_by_xpath('//*[@id="AppFrameMain"]/div/div/div/div[2]/div/footer/div[1]/div[2]/button').click()
    driver.implicitly_wait(10) # seconds
    driver.get('https://apps.shopify.com/cooki-gdpr?surface_detail=cooki&surface_inter_position=1&surface_intra_position=15&surface_type=search')
    driver.implicitly_wait(10) # seconds
    #add app
    # driver.find_element_by_xpath('//*[@id="Main"]/section[1]/div/div/div/div[6]/form/input[2]')
    # driver.implicitly_wait(5) # seconds
    # driver.find_element_by_id('proceed_cta').click()

    # driver.find_elements_by_link_text("Apps").click
    # driver.find_element_by_xpath('//*[@id="AppFrameMain"]/div/div/div[1]/div/div[2]/div/a').click()
    # driver.implicitly_wait(10) # seconds
    # driver.find_element_by_name('q').send_keys("cooki" + Keys.ENTER)
    # driver.implicitly_wait(5) # seconds
    # driver.find_element_by_xpath('//*[@id="SearchResultsListings"]/div[15]/div/a').click()
    # driver.find_element_by_xpath('//*[@id="Main"]/section[1]/div/div/div/div[6]/form/input[2]').click()
    # driver.implicitly_wait(5) # seconds
    # driver.find_element_by_id('proceed_cta').click()


    # time.sleep(5)
    # driver.quit()
install(0)
# %%
