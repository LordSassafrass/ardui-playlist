import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials


client_id = os.environ['SPOTIPY_CLIENT_ID']
client_secret = os.environ['SPOTIPY_CLIENT_ID']

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

creds = SpotifyClientCredentials(client_id = client_id,
                                 client_secret = client_secret)


spotify = spotipy.Spotify(client_credentials_manager= creds)

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])