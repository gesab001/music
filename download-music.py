import json
import os
import subprocess

youtubeId = input("youtube url/id: ")
command = "youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 " + youtubeId
subprocess.call(command, shell=True)

