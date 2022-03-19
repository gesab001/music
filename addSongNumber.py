import json

f = open("musiclist2.json", "r")

jsonObj = json.loads(f.read())
f.close()
songIndex = 1
items = jsonObj["items"]
print(items)
for letter in items:
   songs = items[letter]
   if len(songs)>0:
     for x in range(0, len(songs)):
       print(songIndex)
       jsonObj["items"][letter][x]["songIndex"] = songIndex
       print(jsonObj["items"][letter][x])
       songIndex+=1
       
with open("musiclist2.json", "w") as outfile:
    json.dump(jsonObj, outfile, sort_keys=True, indent=4)       

