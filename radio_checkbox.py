from selenium.webdriver.support.ui import Select
from base import *
"""
benz_radio = driver.find_element(By.ID,"benzradio").click()
bmw_check = driver.find_element(By.ID,"bmwcheck").click()
time.sleep(3)
honda_check = driver.find_element(By.ID,"hondacheck").click()
time.sleep(3)
benz_check = driver.find_element(By.ID,"benzcheck").click()
time.sleep(3)
print("Is bmw radio button selected {}".format(honda_check.is_selected()))
radio_list = driver.find_elements(By.XPATH,"//input[contains(@type,'radio') and contains(@name,'cars')]")
print(len(radio_list))
"""
elem = driver.find_element(By.ID,"carselect")
sel =Select(elem)
sel.select_by_value("honda")
print("Honda selected")
time.sleep(5)
driver.quit()