import json
import requests
import credentials
import time
import glob, random, vlc, sys
from tinytag import TinyTag


api_key = credentials.api_key
cities = ["Reston"]

# if have keyboard, can use command line:
# if len(sys.argv) <= 1:
#     print("Please specify a folder with mp3 files: ")
#     sys.exit(1)
# folder = sys.argv[1]

# for no keyboard with pi, use hardcode
songs = "/Users/user/Desktop/Projects/soothing_tones/songs"
# playlist = glob.glob(folder + "/*.mp3")
playlist = glob.glob(songs + "/*.mp3")
if len(playlist) == 0:
    print("No songs selected")
    sys.exit(1)
random.shuffle(playlist)