from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://learn.letskodeit.com/p/practice")
elem_class = driver.find_elements(By.TAG_NAME,"td")
if elem_class is None:
	print("None")
else:
	print(len(elem_class))
time.sleep(5)
driver.quit()
