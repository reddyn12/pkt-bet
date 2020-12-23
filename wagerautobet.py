from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver=webdriver.Chrome("/Users/Nikhil/Downloads/chromedriver")
driver.get('https://wagerwizard.ag/')
time.sleep(2)
user_box=driver.find_element_by_id("txtAccessOfCode")
user_box.send_keys("Kz41")
time.sleep(2)
pass_box=driver.find_element_by_id("txtAccessOfPassword")
pass_box.send_keys("will"+Keys.RETURN)

#time.sleep(5)
#cont_box=driver.find_element_by_name("ctl00$cphWorkArea$cmbCancel")
#cont_box.click()
time.sleep(5)
livebet_box=driver.find_element_by_class_name("liveBetting ")
livebet_box.click()
