from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://learn.letskodeit.com/p/practice")

text_elem = driver.find_element_by_link_text('Login')
if text_elem is not None:
	print("Found")
else:
	print("Not Found")
time.sleep(5)
driver.close()