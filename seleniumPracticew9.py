from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

def main():
    driver = webdriver.Chrome(service=Service("D:/Desktop\Web Practice/Selenium/chromedriver-win64/chromedriver-win64/chromedriver.exe"))
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    time.sleep(2)
    
    # hover select
    driver.execute_script('window.scrollTo(0,1000);')
    time.sleep(2)
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.ID,'mousehover')).perform()
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/div[4]/div/fieldset/div/div/a[2]').click()
    time.sleep(2)
    main = driver.current_window_handle
    driver.switch_to.frame(driver.find_element(By.ID,'courses-iframe'))
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/div/header/div[3]/div/div/div[2]/nav/div[2]/ul/li[2]/a').click()
    time.sleep(2)
    driver.switch_to.default_content()
    time.sleep(2)
    select = Select(driver.find_element(By.ID,'dropdown-class-example'))
    select.select_by_visible_text('Option2')
    time.sleep(2)
    # s = driver.find_elements(By.ID,'autocomplete').send_keys('India')
    # s[0].click()
    # time.sleep(5)
    driver.switch_to.new_window('tab')
    time.sleep(2)
    driver.get('http://www.google.com')
    time.sleep(2)
    
    
    
if __name__ == "__main__":
    main()