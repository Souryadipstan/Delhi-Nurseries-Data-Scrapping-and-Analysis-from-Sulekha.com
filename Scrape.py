from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

browser=webdriver.Chrome()
url='https://www.sulekha.com/plant-nurseries/delhi'
browser.get(url)
see_more=1
while see_more:
	try:
		see_more=browser.find_element_by_id('morebusinesslist')
		see_more.click()
	except:
		see_more=0
	time.sleep(2)
source=browser.page_source
soup=BeautifulSoup(source,features="xml")
lists=soup.find_all('li',{'class':'list-item view-r'})

fields = ['Name', 'Phone', 'Address']
out_file = open('data.csv','w')
csvwriter = csv.DictWriter(out_file, delimiter=',', fieldnames=fields)
details={}
ctr=0
for li in lists:
	ctr+=1
	try:
		name=li.get('data-name')
	except:
		name='Not Found'
	try:

		phone=li.get('data-bvn')
	except:
		phone='Not Found'
	try:

		address=li.find('address').text
	except:
		address='Not Found'
	details['Name']=name
	details['Phone']=phone
	details['Address']=address
	try:
		csvwriter.writerow(details)
		print(ctr)
		print(details)
	except:
		print(ctr)
		print('Error in writing')
