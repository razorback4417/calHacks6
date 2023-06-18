from dotenv import load_dotenv
import os
import base64
import json
from requests import post, get
import requests
from random import randrange
from transformer import transform

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')

    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': 'Basic ' + auth_base64,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data={'grant_type':'client_credentials'}
    result=post(url,headers=headers, data=data)
    json_result=json.loads(result.content)
    token = json_result['access_token']
    return token

def get_auth_header(token):
    return {'Authorization': 'Bearer ' + token}

def search_for_genre(token, genre_name):
    headers = get_auth_header(token)

    params = {
        'q' : {genre_name},
        'type': 'track',
        'limit': '20',
    }

    response = requests.get('https://api.spotify.com/v1/search', params=params, headers=headers)

    json_result = json.loads(response.text)
    if len(json_result) == 0:
        print('none exist')
        return None
    
    return json_result

def pick_a_song(token, album_id):
    url = f'https://api.spotify.com/v1/albums/{album_id}/tracks'
    headers = get_auth_header(token)
    response = requests.get(url, headers = headers)
    json_result = json.loads(response.content)
    return json_result

def play_song(token, song_id):
    response = requests.get(song_id)
    with open('song.mp3', 'wb') as f:
        f.write(response.content) #downloads new song to song.mp3 each time, replacing previous mp3 value


token = get_token()
result = search_for_genre(token, transform('sad')) #replace sad with Hume AI response
songs = []
for item in result['tracks']['items']:
    songs.append(item['preview_url'])

s = songs[randrange(len(songs))]
while(s is None):
    s = songs[randrange(len(songs))]

play_song(token, s)
