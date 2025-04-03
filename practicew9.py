from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time


def task1(driver):
    driver.get("https://artoftesting.com/samplesiteforselenium")
    driver.maximize_window()
    time.sleep(2)
    
def task2(driver):
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/main/article/div/div/div[1]/p[1]/a').click()
    time.sleep(2)
    
def task3(driver):
    driver.execute_script("window.scrollTo(0,500);")
    time.sleep(1)
    driver.find_element(By.ID,'fname').send_keys('Om Prasad')
    time.sleep(2)
    
def task4(driver):
    driver.find_element(By.ID,'idOfButton').click()
    time.sleep(2)
    
def task5(driver):
    action = ActionChains(driver)
    action.double_click(driver.find_element(By.ID,'dblClkBtn')).perform()
    time.sleep(2)
    driver.switch_to.alert.accept()
    time.sleep(2)


def main():
    driver = webdriver.Chrome(service=Service("D:\Desktop\Web Practice\Selenium\chromedriver-win64\chromedriver-win64\chromedriver.exe"))
    task1(driver)
    task2(driver)
    task3(driver)
    task4(driver)
    task5(driver)
    
    driver.execute_script("window.scrollTo(0,700);")
    
    # Radio button
    
    driver.find_element(By.ID,'male').click()
    time.sleep(2)
    
    # Check box
    
    driver.find_element(By.CLASS_NAME,'Automation').click()
    driver.find_element(By.CLASS_NAME,'Performance').click()
    time.sleep(2)
    
    # Reject alert box
    
    driver.find_element(By.CSS_SELECTOR,'#ConfirmBox > button').click()
    time.sleep(2)
    driver.switch_to.alert.dismiss()
    time.sleep(2)
    
    # drag & drop
    source = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/main/article/div/div/img')
    target = driver.find_element(By.ID,'targetDiv')
    action = ActionChains(driver)
    action.drag_and_drop(source, target).perform()
    time.sleep(2)
    
    
    
    
if __name__ == "__main__":
    main()