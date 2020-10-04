from bs4 import BeautifulSoup
import argparse
import requests

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--url', type=str, help='novel url')
	args = parser.parse_args()
	return vars(args)


def get_html(url):
	#args = get_args()
	#url = args['url']
	html_response = requests.get(url)
	html = BeautifulSoup(html_response.text, 'lxml')
	return html


html = get_html("http://www.biqukan.com/24_24209/")
