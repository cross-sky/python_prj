#! python3
#https://www.jb51.net/article/135671.htm
#https://blog.csdn.net/Jo_Andy/article/details/89714777
import argparse, requests
import logging
import sys, os
import re
from contextlib import closing

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(message)s')

logging.debug(sys.getdefaultencoding())


# Get ts file

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/71.0.2924.87 Safari/537.36'
           #,'connection': 'close'
           }

#test url  https://media.finger66.com/posts/84222300000/MTU1NjEwNDU0ODI2Nw==.mp4.m3u8

def check_path(_path):
    if os.path.isdir(_path) or os.path.isabs(_path):
        # path is null
        if not os.listdir(_path):
            return _path
        else:
            print('There are files exists')
            return _path
    else:
        os.makedirs(_path)
        return _path

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, help='m3u8 url')
    args = parser.parse_args()
    logging.debug('args: %s' % (vars(args)))
    return vars(args)


def get_html(_url, _path):
    all_url = _url.split('/')
    url_pre = '/'.join(all_url[:3]) + '/'
    url_next = all_url[-1]
    logging.debug('all: %s\n, pre: %s.\n next: %s' % (all_url, url_pre, url_next))

    os.chdir(_path)
    logging.debug('Os path: %s' % (_path))

    m3u8_txt = requests.get(_url, headers=headers)
    with open(url_next, 'wb') as m3u8_content:
        m3u8_content.write(m3u8_txt.content)

    movies_url = []
    _urls = open(url_next, 'r')
    pat = '/(.*?).ts'
    urls = re.compile(pat).findall(_urls.read())
    _urls.close()
    for url in urls:
        movies_url.append(url_pre + url + '.ts')

    logging.debug(movies_url)
    os.remove(url_next)
    return movies_url

def download_movies(movie_url, _path, trys = 0):
    if trys >= 3:
        logging.debug('fail to download.')
        return
    n = 0

    err_get = []

    for _url in movie_url:
        movie_name = _url.split('/')[-1]
        n = n + 1

        logging.debug('Downloading %d of %d.' % (n, len(movie_url)))

        try:
            with closing(requests.get(_url, headers=headers, stream=True)) as response:
                with open(movie_name, 'wb') as file:
                    for data in response.iter_content(chunk_size=1024):
                        file.write(data)
        except:
            err_get.append(_url)
            continue

    if err_get:
        logging.debug('There are %d file fail to download.' % (len(err_get)))
        download_movies(err_get, _path, trys + 1)
    else:
        logging.debug('Success downloading.')



"""
https://media.finger66.com/qUEtVIse0lNoxlZQL3sEWFQVA2U=/Fk6kp-BaUmoVrSxoIyFm1PHGTAZd/000003.ts
https://www.leavesongs.com/PYTHON/resume-download-from-break-point-tool-by-python.html
"""

if __name__ == '__main__':
    arg = get_args()
    test_url = 'https://media.finger66.com/posts/84222300000/MTU1NjEwNDU0ODI2Nw==.mp4.m3u8'
    test_path = 'test_data\\aa'
    test_path = check_path(test_path)
    movie_urls = get_html(test_url, test_path)
    download_movies(movie_urls, test_path)
