from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = "https://www.airbnb.com"
driver.get(url)
driver.maximize_window()

time.sleep(5)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL,'t')
sunny_link = driver.find_element(By.XPATH,"//*[@id='listing-10201545']/div/div/div[1]/div/div/div/div/div/a").get_attribute('href')
sunny = driver.find_element(By.XPATH,"//*[@id='listing-10201545']/div/div/div[1]/div/div/div/div/div/a/div/div/div/div/div")
print(sunny_link)
driver.get(sunny_link)
print(driver.title)

check_in = "10/10/2018"
check_out = "11/11/2018"
elem_check_in = driver.find_element(By.ID,"checkin")
elem_check_out = driver.find_element(By.ID,"checkout")
elem_book = driver.find_element(By.XPATH,"//*[@id='book_it_form']/div[2]/button/span/div")
elem_check_in.send_keys(check_in)
elem_check_out.send_keys(check_out)
elem_book.click()

#time.sleep(5)
####driver.quit()