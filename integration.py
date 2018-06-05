import json
import urllib.request
from pprint import pprint
with open('prueba.json') as json_data:
    d = json.load(json_data)
# print(d['urls'])

for x in d['urls']:
	url = d['hostB']+x
	fp = urllib.request.urlopen(url)
	mybytes = fp.read()
	mystr = mybytes.decode("utf8")
	fp.close()
	tupla = x.partition("/") 
	f = open(x,'w')
	f.write(mystr)
	f.close()
	
# url = d['hostB']+d['urls'][0]
# url2 = "https://www.banamex.com/firmaygana/index.html"
# fp = urllib.request.urlopen(url2)
# mybytes = fp.read()
# mystr = mybytes.decode("utf8")
# fp.close()
# print(mystr)
# f = open('files/helloworld.js','w')
# f.write(mystr)
# f.close()