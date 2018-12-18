from selenium import webdriver
import time
import re
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.facebook.com")
driver.implicitly_wait(5)
driver.find_element_by_xpath("//*[@id='email']").send_keys("mih133")
driver.find_element_by_xpath("//*[@id='pass']").send_keys("ImuOnu133")
driver.find_element_by_id("loginbutton").click()
driver.find_element_by_xpath("//*[@id='checkpointSubmitButton']").click()
driver.find_element_by_xpath("//*[@id='profile_pic_welcome_1155995189']").click()
driver.find_element_by_xpath("//a[@data-medley-id='pagelet_timeline_medley_friends']").click()


#### scrolling the page till it gets refreshed
flag=True
uls_beforeScroll =len(driver.find_elements_by_xpath("//div[@id='pagelet_timeline_app_collection_1155995189:2356318349:2']/ul"))
while(flag):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(4)
    uls_afterScroll = len(driver.find_elements_by_xpath("//div[contains(@id,'pagelet_timeline_app_collection_')]/ul"))
    if(uls_afterScroll == uls_beforeScroll):
        flag = False
    else:
        uls_beforeScroll = uls_afterScroll

names = driver.find_elements_by_xpath("//div[@class='fsl fwb fcb']")
print ("total no of friends   "+str(len(names)))
for name in names:
	print(name.find_element_by_tag_name("a").text)