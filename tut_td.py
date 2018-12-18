from selenium import webdriver
import csv
url = 'https://infobypokharelk.blogspot.com/'
driver = webdriver.Firefox()
driver.get(url)
#f = open("website_list.txt","w+")
row_count = len(driver.find_elements_by_xpath("//*[@id='post-body-6767393087210111064']/div[1]/table/tbody/tr"))
col_count = len(driver.find_elements_by_xpath("//*[@id='post-body-6767393087210111064']/div[1]/table/tbody/tr[1]/td"))
print("Number if Rows:",row_count)
print("Number of Columns",col_count)
first_part = "//*[@id='post-body-6767393087210111064']/div[1]/table/tbody/tr["
secound_part = "]/td["
third_part = "]"
all_data = []
for n in range(1,row_count+1):
	data = []
	for m in range(1,col_count+1):
		final_path = first_part + str(n) + secound_part + str(m) + third_part
		table_data = driver.find_elements_by_xpath(final_path)[0].text
		data.append(table_data)
	all_data.append(data)
with open('person.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(all_data)

csvFile.close()