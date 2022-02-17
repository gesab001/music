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

f = open("musiclist2.json", "r")
musiclist2 = json.loads(f.read())
f.close()


f = open("musiclist.json", "r")
musiclist = json.loads(f.read())
f.close()

for x in musiclist:
  filename = x
  title = musiclist[x]
  firstLetter = title[0:1]
  print(firstLetter)
  musiclist2[firstLetter].append({"filename": filename, "title": title})

print(musiclist2)
with open("musiclist3.json", "w") as outfile:
  json.dump(musiclist2, outfile, indent=4, sort_keys=True)
  
