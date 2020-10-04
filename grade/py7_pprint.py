import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)

fileobj = open('data\\myCats.py', 'w')
fileobj.write('cats = ' + pprint.pformat(cats) +'\n')
fileobj.close()
