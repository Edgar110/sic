import json
import git,os,shutil
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
    temp = ""
    i = 0;    
    for folder in t:
        if folder.find(".") == -1:
           temp = temp +"/"+ folder
           i = i + 1   
    filename = t.pop()
    v = []
    v.append([filename,temp])
    return v
    
    
for x in d['urls']:
	url2 = d['hostB']+x
	fp = urllib.request.urlopen(url2)
	mybytes = fp.read()
	mystr = mybytes.decode("utf8")
	fp.close()
	rutas = files(x);
	print(rutas[0][1])
	createFolder("files"+rutas[0][1])
	#createFolder("files/test")
	# print(ruta)
	f = open("files"+rutas[0][1]+"/"+rutas[0][0],'w+')
	#time.sleep(2)
	f.write(mystr)
	f.close()

        
def repositorio():
    git_url = "http://dev.difactor.in/Home_SIT/home_citibanamex.git"
    repo_dir = "git"
    from git import Repo
    Repo.clone_from(git_url, repo_dir)   

repositorio();	
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
