from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://learn.letskodeit.com/p/practice")

elem_tag = driver.find_element_by_tag_name('h1')
print(elem_tag.text)
time.sleep(5)
driver.close()