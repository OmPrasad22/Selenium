from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def setDriver():
    driver_path = "D:\Desktop\Web Practice\Selenium\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    service = Service(driver_path)
    return service

def openSite(driver):
    url = "https://www.saucedemo.com/"
    driver.get(url)
    driver.maximize_window()
    time.sleep(1.5)
    
def loginSite(driver):
    driver.find_element(By.ID,'user-name').send_keys("standard_user")
    time.sleep(1.5)
    driver.find_element(By.ID,'password').send_keys("secret_sauce")
    time.sleep(1.5)
    driver.find_element(By.ID,'login-button').click()
    time.sleep(1.5)
    
def sortByPrice(driver):
    dropList = Select(driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/span/select'))
    time.sleep(1.5)
    dropList.select_by_visible_text('Price (high to low)')
    time.sleep(3)
    
def clickFirstProd(driver):
    driver.find_elements(By.CLASS_NAME,'inventory_item_name')[0].click()
    time.sleep(1.5)    

def addToCart1(driver):
    driver.find_element(By.CSS_SELECTOR,'#add-to-cart').click()
    time.sleep(1.5)
    
def checkOut(driver):
    driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[1]/div[3]/a').click()
    time.sleep(1.5)
    driver.find_element(By.ID,'checkout').click()
    time.sleep(1.5)
    driver.find_element(By.ID,'first-name').send_keys("Om")
    time.sleep(1.5)
    driver.find_element(By.ID,'last-name').send_keys("Prasad")
    time.sleep(1.5)
    driver.find_element(By.ID,'postal-code').send_keys("600096")
    time.sleep(1.5)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(1.5)
    driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/form/div[2]/input').click()
    time.sleep(1.5)
    driver.find_element(By.ID,'finish').click()
    time.sleep(1.5)
    driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")
    time.sleep(1.5)
    driver.find_element(By.ID,'back-to-products').click()
    time.sleep(1.5)
    
def logoutSite(driver):
    driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/button').click()
    time.sleep(1.5)
    driver.find_element(By.ID,'logout_sidebar_link').click()
    time.sleep(1)
    driver.execute_script("alert('Maqsad pura huwa');")
    time.sleep(3)
    driver.switch_to.alert.accept()
    time.sleep(1)




def main():
    driver = webdriver.Chrome(service=setDriver())
    openSite(driver)
    loginSite(driver)
    sortByPrice(driver)
    clickFirstProd(driver)
    addToCart1(driver)
    checkOut(driver)
    logoutSite(driver)
    


if __name__ == "__main__":
    main()