# Method for receiving user input
# Method for making the API endpoint request for artists ID
# Method for making the API endpoint request for recommendations
import requests
from config import spotify_artist_token, spotify_rec_token

class CreateCustomPlaylist:

    def __init__(self):
        self.artist = input("Enter an artist: ")
        self.genre = input("Enter a genre: ")
        self.track = input("Enter a track: ")

    def make_api_artist_request(self):
        """Makes the request to search for the artist"""
        endpoint_artist_url = 'https://api.spotify.com/v1/search?'
        # Replaces the white space with (+) signs so it can pass through the api filter
        q = self.artist.replace(' ', '+')
        query = f'{endpoint_artist_url}q={q}&type=artist&limit={1}'

        artist_response = requests.get(query,
                                        headers = {"Content-Type": "application/json",
                                                    "Authorization": "Bearer {}".format(spotify_artist_token)})
        json_artist_response = artist_response.json()
        artist = json_artist_response['artists']['items'][0]['uri'].replace('spotify:artist:', '') 
        return artist

    def make_api_track_request(self):
        """Makes request for the track"""
        endpoint_track_url = 'https://api.spotify.com/v1/search?'
        q = self.track.replace(' ', '+')
        query = f"{endpoint_track_url}q={q}&type=track&market=US&limit={1}"
        track_response = requests.get(query,
                                            headers = {"Content-Type": "application/json",
                                                        "Authorization": "Bearer {}".format(spotify_artist_token)})
        json_track_response = track_response.json()
        track = json_track_response['tracks']['items'][0]['uri'].replace('spotify:track:', '')
        return track


    def make_recommend_api_request(self, artist, track):
        """Makes recommendation based on artists, genres, and tracks"""
        endpoint_rec_url = 'https://api.spotify.com/v1/recommendations?'
        query = f'{endpoint_rec_url}limit={10}&seed_artists={artist}&seed_genres={self.genre}&seed_tracks={track}'

        recommend_response = requests.get(query,
                                            headers = {"Content-Type": "application/json",
                                                        "Authorization": "Bearer {}".format(spotify_rec_token)})
        json_rec_response = recommend_response.json()
        for item in json_rec_response['tracks']:
            artist_name = item['album']['artists'][0]['name']
            artist_song = item['name']
            print(f"{artist_name} - {artist_song}")

    def create_playlist(self):
        pass

    def add_items_to_playlist(self):
        pass


if __name__ == "__main__":
    playlist = CreateCustomPlaylist()
    # playlist.make_api_artist_request()
    artist = playlist.make_api_artist_request()
    track = playlist.make_api_track_request()
    playlist.make_recommend_api_request(artist, track)
    
     

