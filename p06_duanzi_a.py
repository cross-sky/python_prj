# https://www.jianshu.com/p/9c266216957b

from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
url = 'http://www.qiushibaike.com/8hr/page/{page}'


def get_html(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup


def get_jokes(contents):
    jokes = contents.select('.col1 > div')
    docs = ""
    for joke in jokes:
        if joke.select('.thumb'):
            continue
        jk = joke.select('.content > span')[0].get_text()
        docs += jk
        # print(jk)
        print("-----")
    return docs


def get_pages(number):
    with open('p06txt.txt', 'w', encoding='utf-8') as f:
        for p in range(1, number):
            print("page:", p)
            contents = get_html(url.format(page=p))
            doc = get_jokes(contents)
            f.write(doc)


contents = get_html(url.format(page=1))
get_jokes(contents)

# if __name__ == '__main__':
get_pages(3)
