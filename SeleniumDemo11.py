import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager("").install()))
driver.get("https://magento.softwaretestingboard.com/customer/account/login")

driver.find_element(By.XPATH, "//*[@id='email' and @type='email']").send_keys("admin12@gmail.com")
driver.find_element(By.XPATH, "//input[@id='pass' or @title='password']").send_keys("admin12!@")
driver.find_element(By.XPATH, "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]").click()
driver.find_element(By.CSS_SELECTOR, 'a:contains("My Orders")').click()



time.sleep(5)
