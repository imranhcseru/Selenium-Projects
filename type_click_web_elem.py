from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = "https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1"
driver.get(url)
driver.implicitly_wait(3)

email = "imranhosen133@gmail.com"
pwd = "Imran133"
find_email = driver.find_element(By.ID,"user_email")
find_pwd = driver.find_element(By.ID,"user_password")
find_login = driver.find_element(By.XPATH,"//*[@id='new_user']/div[3]/input")
find_email.send_keys(email)
find_pwd.send_keys(pwd)
find_login.click()

"""
time.sleep(3)
find_email.clear()
time.sleep(3)
find_pwd.clear()
"""

time.sleep(5)
driver.quit()