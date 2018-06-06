import json
import urllib.request
import time
import os
from pprint import pprint
with open('prueba.json') as json_data:
    d = json.load(json_data)
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
def files(url,):
    t = x.split("/")
    
    #a_list = ["0","1","2"]

    i = 0;
    for folder in t:
        if i != 0
           cad = cad +"/"+ folder
           i++
        print (folder)        
            
    filename = t.pop()
    return v[,filename]
    
    
for x in d['urls']:
	url2 = d['hostB']+x
	fp = urllib.request.urlopen(url2)
	mybytes = fp.read()
	mystr = mybytes.decode("utf8")
	fp.close()
	t = files(x);	
	Cpath = "files/"+x
	createFolder(Cpath)
	ruta = ('files/'+x)
	# print(ruta)
	#f = open(ruta,'w+')
	#time.sleep(2)
	#f.write(mystr)
	#f.close()
	
	
# url = d['hostB']+d['urls'][0]
# url2 = "https://www.banamex.com/firmaygana/index.html"
# fp = urllib.request.urlopen(url2)
# mybytes = fp.read()
# mystr = mybytes.decode("utf8")
# fp.close()
# print(mystr)
# f = open('files/t1.html','w+')
# f.write(mystr)
# f.close()
