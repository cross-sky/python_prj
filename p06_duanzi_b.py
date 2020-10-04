from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

url = 'http://www.qiushibaike.com'

def get_html(url):
	r = requests.get(url, headers=headers)
	html = BeautifulSoup(r.text, 'lxml')
	return html

def get_jokes(contents):
	jokes = contents.find_all('div', {'class':'article'})
	#jokes = contents.find_all('div', attrs={''})
	for joke in jokes:
		content = joke.span.get_text()
		print(content)

html = get_html(url)
