from selenium import webdriver
import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("/Users/Nikhil/Downloads/chromedriver")
driver.get('https://ibet.ag')

user_box=driver.find_element_by_id("username")
user_box.send_keys("BOSSMAN200")
pass_box=driver.find_element_by_id("password")
pass_box.send_keys("1234")
login=driver.find_element_by_id("login-account")
login.click()
time.sleep(2)

livebet_box=driver.find_element_by_link_text("EZ Live Betting")
livebet_box.click()

time.sleep(2)
countrydropdown=driver.find_elements_by_class_name("sports-list")
country=Select(driver.find_elements_by_id("child"));
country.selectByVisibleText("CIENFUEGOS_PINARDELRÍO");

#teambet=driver.find_element_by_id("CIENFUEGOS_PINARDELRÍO")
#teambet.click()
