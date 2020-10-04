# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


import  re

file_path = 'url.txt'

html_file = open(file_path, 'r', encoding='utf-8').read()

soup = BeautifulSoup(html_file,  'lxml')

all_name = soup.find_all(string=re.compile('else if'))

print(len(all_name))
#for name in soup.find_all(string=re.compile("else if")):
#    print(name)

#print(soup.prettify)

#ss = "('.*'==姓名)('.*'==身份证号)('.*'==证书编号)".decode("utf8")
#print(all_name[0])

p = re.compile(r"('.*'==姓名)('.*'==身份证号)('.*'==证书编号)")

print(type(all_name))
match = p.search(all_name[0])
result = p.search(all_name).groups()

print(result)
