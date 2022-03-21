import json

"""
alphabet = list("abcdefghijklmnopqrstuvwxyz".upper())

jsonData = {}
for x in alphabet:
  jsonData[x] = []
  
print(jsonData)

with open("musiclist2.json", "w") as outfile:
  json.dump(jsonData, outfile, indent=4, sort_keys=True)
  
"""

f = open("empty_alphabetical_list.json", "r")
musiclist2 = json.loads(f.read())
f.close()


f = open("musiclist.json", "r")
musiclist = json.loads(f.read())
f.close()

count = 0
for x in musiclist:
  filename = x
  print("filename: " + filename)
  count = count + 1
  title = musiclist[x]
  print("title: " + title)
  firstLetter = title[0:1]
  print(firstLetter)
  musiclist2["items"][firstLetter].append({"filename": filename, "title": title})

musiclist2["totalItems"] = count
print(musiclist2)

songIndex = 1
items = musiclist2["items"]
print(items)
for letter in items:
   songs = items[letter]
   if len(songs)>0:
     for x in range(0, len(songs)):
       print(songIndex)
       musiclist2["items"][letter][x]["songIndex"] = songIndex
       print(musiclist2["items"][letter][x])
       songIndex+=1
       
with open("musiclist2.json", "w") as outfile:
  json.dump(musiclist2, outfile, indent=4, sort_keys=True)
  
