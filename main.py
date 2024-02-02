import requests
from data_billboard import Top_100_title
from spotify import Spotify_data


user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
top_100 = Top_100_title(user_date)
top_100.retrieve_titles()
spot_data = Spotify_data()
get_songs = spot_data.get_song(song_names=top_100.titles, year=user_date.split("-")[0])
create_playlist = spot_data.create_playlist(user_date)
add_item_to_playlist = spot_data.add_item()