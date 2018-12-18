from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
#__________________________________________________
#to maximize browsing window
#______________________________________________________
driver.maximize_window()
#___________________________________________________
#print title of the page
#______________________________________________________
title = driver.title
print(title)
#___________________________________________________
#to get url of current page
#______________________________________________________
#current_url = driver.current_url
#print(current_url)
#_____________________________________________________
#to refresh
#______________________________________________________
#driver.refresh()
#____________________________________________________
#to go back one step back in browsing history
#______________________________________________________
#time.sleep(5)
#driver.back()
#_____________________________________________________
#to go one step forward in browsing history
#______________________________________________________
#time.sleep(5)
#driver.forward()
#______________________________________________________
#to get source of the current page
#______________________________________________________
#source = driver.page_source
#print(source)
#or to write in a file
#f = open("page_source.txt","w+",encoding='utf-8')
#f.write(source)
#______________________________________________________
time.sleep(5)
driver.quit()