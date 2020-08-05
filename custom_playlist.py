# Method for receiving user input
# Method for making the API endpoint request for artists ID
# Method for making the API endpoint request for recommendations
import requests
from config import spotify_artist_token

class CreateCustomPlaylist:

    def __init__(self):
        self.artist = input("Enter an artist: ")
        self.genre = input("Enter a genre: ")
        self.track = input("Enter a track: ")

    def make_api_artist_request(self):
        endpoint_artist_url = 'https://api.spotify.com/v1/search?'
        q = self.artist.replace(' ', '+')
        query = f'{endpoint_artist_url}q={q}&type=artist&limit={1}'

        artist_response = requests.get(query,
                                        headers = {"Content-Type": "application/json",
                                                    "Authorization": "Bearer {}".format(spotify_artist_token)})
        json_artist_response = artist_response.json()
        return json_artist_response['artists']['items'][0]['uri'].replace('spotify:artist:', '')                                            

    def make_recommend_api_request(self):
        pass

    def create_playlist(self):
        pass

    def add_items_to_playlist(self):
        pass

if __name__ == "__main__":
    playlist = CreateCustomPlaylist()
    print(playlist.make_api_artist_request()) 

