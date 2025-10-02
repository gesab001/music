import json
import os
from tinytag import TinyTag
import music_tag
import mutagen
from mutagen.wave import WAVE
import audioread

# Pass the filename into the
# Tinytag.get() method and store
# the result in audio variable



files = os.listdir()
  
def getMetadataItem(attribute, attribute_value, filename):
     result = "error"
     try:
       print(attribute +":" + attribute_value)
       result = attribute_value
     except:  
       result = "error"
     return result  
       
for file in files:
  if file.endswith("m4a") or file.endswith("mp3"):  
     print(file)
     audio = TinyTag.get(file)
     f = music_tag.load_file(file)
     print(audio)
     #voice = WAVE(file)
     duration = 0
     with audioread.audio_open(file) as audioread_file:
    # totalsec contains the length in float
        duration = audioread_file.duration
     print("DURATION: " + str(duration))   
     #print(f)
     #print(audio)
     # Use the attributes
     # and Display

     item = {}
     
     attribute = "title"
     response = getMetadataItem(attribute, audio.title, file)
     if response=="error":
       response = input("update " + attribute + " metadata for : " + file)
       #f[attribute] = update     
     item[attribute] = response 
     
     attribute = "album"
     response = getMetadataItem(attribute, audio.album, file)
     if response=="error":
       response = input("update "+ attribute+ " metadata for : " + file)
       f[attribute] = response    
     item[attribute] = response 
     
     attribute = "artist"
     response = getMetadataItem(attribute, audio.artist, file)
     if response=="error":
       response = input("update " + attribute + " metadata for : " + file)
       f[attribute] = response
     item[attribute] = response 
     
     attribute = "genre"
     response = getMetadataItem(attribute, audio.genre, file)
     if response=="error":
       response = input("update " + attribute + " metadata for : " + file)
       f[attribute] = response  
     item[attribute] = response 
     
     attribute = "source"
     response = file
     item[attribute] = response 
    
     attribute = "image"
     response = ""
     item[attribute] = response 
     
     attribute = "trackNumber"
     response = getMetadataItem(attribute, audio.track, file)
     if response=="error":
       response = input("update "+ attribute+ " metadata for : " + file)
       f[attribute] = int(response)   
     item[attribute] = response 
     
     attribute = "totalTrackCount"
     
     response = ""#getMetadataItem(attribute, audio.totalTracks, file)
     if response=="error":
       response = input("update "+ attribute+ " metadata for : " + file)
       f[attribute] = int(response)  
     item[attribute] = response 
       
     attribute = "year"
     response = getMetadataItem(attribute, audio.year, file)
     if response=="error":
       response = input("update "+ attribute+ " metadata for : " + file)
       f[attribute] = int(response)   
     item[attribute] = response 
  
     attribute = "duration"
     response = getMetadataItem(attribute, audio.duration, file)
     if response=="error":
       response = input("update "+ attribute+ " metadata for : " + file)
       #f.append_tag(attribute)
     item[attribute] = response 

     attribute = "site"
     response =  "https://github.com/gesab001/music/blob/main"    
     item[attribute] = response 

       #f[attribute] = int(update)   
     f.save()  
     musicfile = open("music.json", "r")
     musicjson = json.loads(musicfile.read())
     print(musicjson)
     musicfile.close()
     musicjson["music"].append(item)
     with open("music.json", "w") as outfile:
       json.dump(musicjson, outfile, indent=4)
     #print("TrackTotal: " + str(audio.track_total))
     """
     title = getTitle(filename)
     album = getAlbum(filename)
     artist = getArtist(filename)
     genre = getGenre(filename)
     source = filename
     image = ""
     trackNumber = getTrackNumber(filename)
     totalTrackCount = getTrackCount(filename)
     duration = getDuration(filename)
     pricelist = ["free", "paid"]
     print(pricelist)
     price = pricelist[input("select price: " )]
     site = "https://github.com/gesab001/music/raw/main"
	 """