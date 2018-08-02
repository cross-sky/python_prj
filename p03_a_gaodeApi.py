from bs4 import BeautifulSoup
import requests
import csv
import time

url = "http://bj.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000"

page = 0
csv_file = open('brent.csv', 'w')
csv_write = csv.writer(csv_file, delimiter=',')
while True:
    page += 1
    print('fetch: ', url.format(page=page))

    response = requests.get(url.format(page=page))
    html = BeautifulSoup(response.text, 'lxml')
    house_list = html.select(".list > li")

    if not house_list:
        break

    if page >= 10:
        break

    for house in house_list:
        house_title = house.select('h2')[0].string
        house_url = 'http:%s' % house.select('a')[0]['href']
        house_info_list = house_title.split()

        if "公寓" in house_info_list[1] or "青年社区" in house_info_list[1]:
            house_location = house_info_list[0]
        else:
            house_location = house_info_list[1]

        house_money = house.select('.money')[0].select('b')[0].string

        csv_write.writerow([house_title, house_location, house_money, house_url])

    time.sleep(1)

csv_file.close()