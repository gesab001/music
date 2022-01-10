import json
import os
import subprocess


files = os.listdir()
#print(files)
for f in files:
  if f.endswith(".mp3"):
    #print(f)
    newName = f.replace(" ", "_")
    #print(newName)
    os.rename(f, newName)
files = os.listdir()
for f in files:
  if f.endswith(".mp3"):
    print(f)
f = open("musiclist.json", "r")

jsondata = json.loads(f.read())
f.close()
filename = input("filename: ")
songtitle = input("song title: ")
jsondata[filename] = songtitle

"""
for f in files:
  if f.endswith(".mp3") and "wonders-of-creation" in f:
    album = "wonders-of-creation_"
    split = f.split(album)
    songtitle = split[1][3:].split(".")[0].replace("-", " ").title()
    #print(songtitle)
    filename = f
    jsondata[filename] = songtitle

for f in files:
  if f.endswith(".mp3") and "love-of-god" in f:
    album = "love-of-god_"
    split = f.split(album)
    songtitle = split[1][3:].split(".")[0].replace("-", " ").title()
    #print(songtitle)
    filename = f
    jsondata[filename] = songtitle
"""    
#print(jsondata)    

sortedJsondata = dict(sorted(jsondata.items(), key=lambda item: item[1]))


for x in sortedJsondata:
  print(sortedJsondata[x])

with open("musiclist.json", "w") as outfile:
  
  json.dump(sortedJsondata, outfile, indent=4)

gitcommand = 'git add . && git commit -m  ' + '"added  ' + songtitle  + '" && git push --all'
subprocess.call(gitcommand, shell=True)