import spotipy
from spotipy.oauth2 import SpotifyOAuth
from data_billboard import Top_100_title
import os

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID_value")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET_value")
REDIRECT_URL = os.environ.get("REDIRECT_URL_value")


class Spotify_data:
    def __init__(self) -> None:
        self.scope = "playlist-modify-private"
        self.sp = spotipy.Spotify(
                auth_manager=SpotifyOAuth(
                client_id=SPOTIPY_CLIENT_ID, 
                client_secret=SPOTIPY_CLIENT_SECRET, 
                redirect_uri=REDIRECT_URL, 
                scope=self.scope))
        self.current_user = self.sp.current_user()["id"]
        self.song_uris = []
        self.playlist = None

    def get_song(self, song_names, year):
        for song in song_names:
            self.result = self.sp.search(q=f"track:{song} year:{year}", type="track")
            try:
                self.uri = self.result["tracks"]["items"][0]["uri"]
                self.song_uris.append(self.uri)
                print(f"{song} added")
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")

    def create_playlist (self, data):
        self.playlist = self.sp.user_playlist_create(user=self.current_user, name=f"{data} Billboard 100", public=False)

    def add_item (self):
        self.sp.playlist_add_items(self.playlist["id"], items=self.song_uris)    
        
        

             

