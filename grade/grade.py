# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import  re

import pprint
file_path = 'grade_url.txt'

#html_file = open(file_path, 'r', encoding='utf-8').read()

with open(file_path, 'r', encoding='utf-8') as f:
    html_file = f.read()

soup = BeautifulSoup(html_file,  'lxml')

all_name = soup.find_all(string=re.compile('else if'))

print(len(all_name))
#for name in soup.find_all(string=re.compile("else if")):
#    print(name)

#print(soup.prettify)

#ss = "('.*'==姓名)('.*'==身份证号)('.*'==证书编号)".decode("utf8")
#print(all_name[0])

regex = re.compile(r"'(.*)'==姓名 && '(.*)'==身份证号 && '(.*)'==证书编号")

print(type(all_name))
match = regex.findall(all_name[0])
#print(match)
#result = match.groups()

#print(result)

#with open('result_url.txt', 'w', encoding='utf-8') as f:
#    f.write(str(match))
name, id, num = match[1]

with open('data\\grade_urls.py', 'w', encoding='utf-8') as f:
    f.write('names = ' + pprint.pformat(match) + '\n')

print(name, id, num)
