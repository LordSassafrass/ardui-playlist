import spotipy
import logging
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth


# logging.basicConfig(filename='spotify.log', encoding='utf-8', level=logging.DEBUG)
file1 = open('spot_id.txt', 'r')
ID = file1.readline()
file1.close()
file1 = open('spot_secret.txt', 'r')
SECRET = file1.readline()
file1.close()
client_id = ID
client_secret = SECRET

creds = SpotifyClientCredentials(client_id=client_id,
                                 client_secret=client_secret)

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri='http://localhost:8888/callback'
    )
)
def intake(playlist, uri):
    uri_list = []
    if 'album' in uri:
        album_tracks = spotify.album_tracks(album_id='4NDXeXypRq8YdFCKqg4sAn')
        for i in album_tracks['items']:
            uri_list.append(i['uri'])

    elif 'track' in uri:
        uri_list.append(uri)

    results = spotify.playlist_add_items(playlist_id=playlist,
                                         items=uri_list)


    print(results)

intake('5oMiDLcZteHBe7ivCvply1', 'https://open.spotify.com/album/4NDXeXypRq8YdFCKqg4sAn?si=mUqVajpkSRGcYZGgbasvAg')