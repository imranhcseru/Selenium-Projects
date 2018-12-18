from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
#url for 10th parliament member list
url = 'http://www.parliament.gov.bd/index.php/en/mps/members-of-parliament/current-mp-s/list-of-10th-parliament-members-english'
driver = webdriver.Chrome()
driver.get(url)
#xpath for counting row number in table
row_count = len(driver.find_elements(By.XPATH,"//*[@id='main']/div[3]/div/table/tbody/tr"))
#xpath for counting colummn number in table
col_count = len(driver.find_elements(By.XPATH,"//*[@id='main']/div[3]/div/table/tbody/tr[1]/td"))
print("Number if Rows:",row_count)
print("Number of Columns",col_count)
#creating splitted variable in three part to create a final xpath
first_part = "//*[@id='main']/div[3]/div/table/tbody/tr["
secound_part = "]/td["
third_part = "]/div"
#initializing list all_data[] to store data
all_data = []
#opening a csv fine 
for n in range(1,row_count+1):
	data = []
	for m in range(1,4):
			#as in 4th <td> conatains photograph of MPs we will skip this data
			#creating final xpath for each <td>
		final_path = first_part + str(n) + secound_part + str(m) + third_part
			#fetchinng data per <td>
		value = driver.find_elements_by_xpath(final_path)
		if len(value)<1:
			continue
		table_data = value[0].text
		#appending data to a list initialized as data[]
		data.append(table_data)
	#finally appending data[] list in all_data[]
	all_data.append(data)
	#opening a csv fine 
with open('mplistbd10p.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    #writing all_data to csv file
    writer.writerows(all_data)
csvFile.close()
time.sleep(10)
driver.quit()