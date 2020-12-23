from selenium import webdriver
import time

driver=webdriver.Chrome("/Users/Nikhil/Downloads/chromedriver")
driver.get('https://www.draftkings.com/account/sitelogin')
time.sleep(2)
login_box=driver.find_element_by_class_name("_3nxQRraP-yugQYGCGg8tJQ")
login_box.click()
time.sleep(1)
user_box=driver.find_element_by_name("username")
user_box.send_keys("anagy17@comcast.net")
pass_box=driver.find_element_by_name("password")
pass_box.send_keys("o31gTWXFBs")
sign_in=driver.find_element_by_xpath("//*[@id='react-mobile-home']/section/section[2]/div[3]/button")
sign_in.click()
time.sleep(10
           )
sportsbook_box=driver.find_element_by_xpath("//*[@id='dkjs-global-header']/div/header/div/div[2]/div[1]/nav/a[2]")
sportsbook_box.click()
time.sleep(2)
driver.get("https://sportsbook.draftkings.com/featured?category=live-in-game&subcategory=basketball")

























def isSimilar(h1,a1,h2,a2):
    if(h1==h2 and a1==a2):
        return True
    if(h1==h2):
        #need to manipulate a1 and a2 to show similarity
        return isSimilarHelper(h1,h2)
    if(a1==a2):
        #need to manipulate h1 and h2 to show similarity
        return isSimilarHelper(a1,a2)



def isSimilarHelper(x,y):
    #do somthing
    return True