from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

arial_label = driver.find_element_by_xpath("//*[@id='gsri_ok0']")
if arial_label is not None:
	print("We find element")
else:
	print("We didn't find element")
time.sleep(5)
driver.quit()