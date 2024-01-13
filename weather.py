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

random.shuffle(playlist)

# Weather predictions for cities kept in weather_dict
weather_dict = {}
code_set = {200, 201, 202, 210, 211, 212, 221, 230, 231, 232, 800, 802, 803, 804}

def forecast(city):
    """Takes in a city and returns json response of weather data"""
    print("In forecast")
    response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=" +
        api_key
    )
    return response.json()