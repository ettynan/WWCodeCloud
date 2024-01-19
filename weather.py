import requests
import credentials
import time
import glob
import vlc
from tinytag import TinyTag

# API key and cities
api_key = credentials.api_key
cities = ["Reston"]

# Songs and playlist
songs_folder = "./songs"
playlist = glob.glob(f"{songs_folder}/*.mp3")

# Check if songs are available
if not playlist:
    print("No songs selected")
    exit(1)

# Weather predictions for cities kept in weather_dict
weather_dict = {}
code_set = {200, 201, 202, 210, 211, 212, 221, 230, 231, 232, 800, 802, 803, 804}

def forecast(city):
    """Takes in a city and returns JSON response of weather data"""
    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}"
    )
    return response.json()

def is_thunderstorm(weather_dict):
    """Determine if thunderstorms are expected, return boolean value for music"""
    return any('weather' in v and any('id' in k and k['id'] in code_set for k\
        in v['weather']) for v in weather_dict.values())

def play_music(song):
    """Play the given song using VLC"""
    vlc_instance = vlc.Instance()
    tag = TinyTag.get(song)
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(song)
    player.set_media(media)
    player.play()
    print(tag.duration)
    time.sleep(tag.duration)

def check_weather(weather_dict, cities):
    """Check weather periodically for specified cities and play music if storming"""
    while True:
        # Get forecast for each city
        for city in cities:
            weather_dict[city] = forecast(city)

        # Play music if thunderstorm expected
        if is_thunderstorm(weather_dict):
            for song in playlist:
                play_music(song)
        else:
            time.sleep(10)

check_weather(weather_dict, cities)
