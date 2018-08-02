from bs4 import BeautifulSoup
import csv
import requests
import time


url = 'http://bj.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000'

file = open('a_rent.csv', 'w')
csv_file = csv.writer(file, delimiter=',')
page=0

while True:
	page += 1
	print("fetch: " + url.format(page=page))
	house_response = requests.get(url.format(page=page))
	html = BeautifulSoup(house_response.text, 'lxml')
	house_list = html.select('.list > li')

	if not house_list:
		break

	if page >= 5:
		break

	for house in house_list:
		house_title = house.select('h2')[0].string
		house_url = 'http: %s' % house.select('a')[0]['href']
		house_money = house.select('.money')[0].select('b')[0].string

		house_info_list = house_title.split()
		if "公寓" in house_info_list[1] or "青年社区" in house_info_list[1]:
			house_location = house_info_list[0]
		else:
			house_location = house_info_list[1]
		csv_file.writerow([house_title ,house_location, house_money, house_url])
	time.sleep(2)

csv_file.close()

