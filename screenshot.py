from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1"
driver = webdriver.Chrome()
driver.get(url)
email = "imranhosen133@gmail.com"
pwd = "Imran133"
elem_email = driver.find_element(By.ID,"user_email")
elem_email.send_keys(email)
time.sleep(3)
elem_pwd = driver.find_element(By.ID,"user_password")
elem_pwd.send_keys(pwd)
time.sleep(3)
#elem_login = driver.find_element(By.NAME,"commit")
#elem_login.click()
destination = "C:\\Users\\Achilies\\Desktop\\test.png"

try:
	driver.save_screenshot(destination)
	print("Screenshot saved to directory")
except:
	print("Error in saving Screenshot")

time.sleep(5)
driver.quit()