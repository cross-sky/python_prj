#https://github.com/learrn/lianjia/tree/master/python
import csv
import random
import re
import time

from bs4 import BeautifulSoup
import requests
import sys

from .items import LianjiaItem

user_agent = [
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36',
	'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
]

headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, sdch',
	'Accept-Language': 'zh-CN,zh;q=0.8',
	'User-Agent': user_agent[random.randint(0, 5)]
}

first_line = True

def get_latitude(url):
	time.sleep(1)
	content = get_html(url)



url = 'https://sh.lianjia.com/zufang/'
def get_html(url):
	contents = requests.get(url, headers=headers)
	contents.encoding = 'utf-8'
	content = BeautifulSoup(contents.text, 'lxml')
	return content

def parse(content):
	area_list = content.find('div', {'class':'option-list'}).find_all('a')[1: -1]
	#area_list = content.select('.dl-lst')[0].select('.option-list > a')[1: -1]
	for area in area_list:
		url = 'https://sh.lianjia.com/{}'.format(area['href'])
		detail_url(url)

def detail_url(url):
	for i in range(1, 2):
		page = url + '/pg{i}'.format(i=i)
		time.sleep(1)
		contents = get_html(page)
		houselists = content.find_all('div', {'class':'info-panel'})
		for house in houselists:
			item = LianjiaItem()
			item['title'] = house.select('h2 > a')[0]['title']
			#item['title'] = house.find('h2').find('a')['title']

			item['community'] = house.find('a', {'class':'laisuzhou'}).find('span').string
			#item['community'] = house.select('.laisuzhou > span')[0].string

			item['model'] = house.select('.zone > span')[0].string
			item['area'] = house.find('span', {'class':'meters'}).string

			other_con = house.select('.con')[0].get_text().split('/')
			item['time'] = other_con[2]
			item['house_type'] = other_con[1]

			item['price'] = house.select('.price > span')[0].string

			item['link'] = house.select('h2 > a')[0]['href']



content = get_html(url)
