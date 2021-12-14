from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

options = Options()
options.headless = True
PATH = "C:\Program Files (x86)\chromedriver.exe"
# driver = webdriver.Chrome(PATH, options=options)


#=========================FILE
df = pd.read_excel('data_input.xlsx')
# print(df["name"][0])
print(df["name"][0]) 


#========================FUNCTIONS
def cells(x,y):
    return df["Unnamed: "+str(x-1)][y-2]
#%%
def install(data_no):
    driver = webdriver.Chrome(PATH)
    driver.get("https://shopify.com/")
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="Hero"]/div/div[1]/div[2]/form/div/div/button'))
        )
    finally:
        pass
    element.click()

    driver.find_element_by_name("signup[email]").send_keys(df["email"][data_no])
    driver.find_element_by_name("signup[password]").send_keys(df["password"][data_no])
    driver.find_element_by_name("signup[shop_name]").send_keys(df["name"][data_no])
    x = 35
    # driver.find_element_by_name("signup[email]").send_keys(f"john99{str(x)}@gmail.com")
    # driver.find_element_by_name("signup[password]").send_keys("john123")
    # driver.find_element_by_name("signup[shop_name]").send_keys(f"john99{str(x)}")
    driver.find_element_by_xpath('//*[@id="SignupForm_modal"]/div[6]/button').click()
    driver.implicitly_wait(10) # seconds
    try:
        driver.find_element_by_id('MessageId_b8be')
        driver.find_element_by_xpath('//*[@id="MessageId_b8be"]/span[2]/a').click()
        # driver.find_element_by_id('account_email').send_keys(f'john99{str(x)}@gmail.com')
        driver.find_element_by_id('account_email').send_keys(df["email"][data_no])
        time.sleep(3)
        #gives time for email verification
        driver.find_element_by_id('account_email').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element_by_id('account_password').send_keys(f'john123' + Keys.ENTER)
    except:
        pass
    
    driver.implicitly_wait(5) # seconds

    try:
        print('skip')
        driver.find_element_by_xpath('//*[@id="AppFrameMain"]/div/div/div/div[1]/div/footer/div/div[2]/button').click()

    except:
        pass
    
    try:
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

        print("enter form")
        select_country.select_by_visible_text(df["country"][data_no])
        fname.send_keys(df["fname"][data_no])
        lname.send_keys(df["lname"][data_no])
        address.send_keys(df["address"][data_no])
        city.send_keys(df["city"][data_no])
        select_province.select_by_visible_text(df["province"][data_no])
        zip.send_keys(df["zip"][data_no])
        phone.send_keys(df["phone"][data_no])
    except:
        pass

    try:
        print('#proceed')
        driver.find_element_by_xpath('//*[@id="AppFrameMain"]/div/div/div/div[2]/div/footer/div[1]/div[2]/button').click()
    except:
        pass

    driver.implicitly_wait(10) # seconds
    driver.get('https://apps.shopify.com/cooki-gdpr?surface_detail=cooki&surface_inter_position=1&surface_intra_position=15&surface_type=search')
    driver.implicitly_wait(10) # seconds
    print('add app')
    driver.find_element_by_xpath('//*[@id="Main"]/section[1]/div/div/div/div[6]/form/input[1]').send_keys(Keys.ENTER)
    try:
        driver.find_element_by_id('account_email').send_keys(df["email"][data_no])
        time.sleep(3)
        #gives time for email verification
        driver.find_element_by_id('account_email').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element_by_id('account_password').send_keys(df["password"][data_no])
        time.sleep(3)
        driver.find_element_by_id('account_password').send_keys(Keys.ENTER)
    except:
        pass

    print("click emails")
    driver.find_element_by_xpath('//*[@id="body-content"]/div[2]/div/div/div/div/div[2]/div/div[2]/a[1]').click()
    print('Install app')
    driver.find_element_by_id('proceed_cta').click()
    print("data no {} Success".format(data_no))
    driver.quit()
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

def delete(data_no):
    pass
    driver = webdriver.Chrome(PATH)
    #goto shopify.com
    driver.get("https://shopify.com/")
    #wait
    driver.implicitly_wait(5)
    #login
    driver.find_element_by_xpath('//*[@id="ShopifyMainNav"]/ul[2]/li/a').click()
    #enter username, delay
    driver.implicitly_wait(5)
    driver.find_element_by_id('account_email').send_keys(df["email"][data_no])
    #gives time for email verification
    time.sleep(5)
    driver.find_element_by_id('account_email').send_keys(Keys.ENTER)
    time.sleep(5)
    #enter password, delay
    driver.find_element_by_id('account_password').send_keys(df["password"][data_no])
    time.sleep(5)
    driver.find_element_by_id('account_password').send_keys(Keys.ENTER)
    #go to apps
    # driver.get(f'https://{df["name"][data_no]}.myshopify.com/admin/apps')
    driver.implicitly_wait(15)
    driver.find_element_by_xpath('//*[@id="AppFrameNav"]/nav/div[2]/ul[1]/li[8]').click()
    #select ...
    driver.find_element_by_xpath('//*[@id="gid://shopify/App/5428615"]/div[4]/div/button').click()
    #delete
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="Polarispopover12"]/div/div/div/ul/li[3]/button').click()
    #select deleting reason
    reason = driver.find_element_by_xpath('//*[@id="PolarisSelect2"]')
    select_reason = Select(reason)
    select_reason.select_by_visible_text("Other")
    #delete button
    driver.find_element_by_xpath('//*[@id="PolarisPortalsContainer"]/div[10]/div[1]/div/div/div/div/div[3]/div/div/div[2]/div/div[2]/button').click()
    time.sleep(5)
    driver.quit()
    print("App Deleted")




# for i in range(len(df.index)):
#     install(i)
# install(0)
delete(0)
# print(len(df.index))

# %%
