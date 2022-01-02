import json
import os

files = os.listdir()
#print(files)
jsondata = {}
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
    
#print(jsondata)    
sortedJsondata = dict(sorted(jsondata.items(), key=lambda item: item[1]))
artist = "For My People"

for x in sortedJsondata:
  print(sortedJsondata[x])
with open("musiclist.json", "w") as outfile:
  
  json.dump(sortedJsondata, outfile, indent=4)