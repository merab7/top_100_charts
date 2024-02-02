import requests
from bs4 import  BeautifulSoup



class Top_100_title:
    def __init__(self, user_input) -> None:
        self.titles = []
        self.user_input = user_input
        self.billboard_url = f"https://www.billboard.com/charts/hot-100/{self.user_input}/"

    def retrieve_titles(self):
        self.response = requests.get(self.billboard_url)
        self.markup = self.response.text
        self.soup = BeautifulSoup(self.markup, "html.parser")
        self.song_name_spans = self.soup.select("li ul li h3")
        self.titles = [song.getText().strip() for song in self.song_name_spans]

