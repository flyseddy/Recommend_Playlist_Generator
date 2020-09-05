# Method for receiving user input
# Method for making the API endpoint request for artists ID
# Method for making the API endpoint request for recommendations
import requests
from config import token, user_id
import json

class CreateCustomPlaylist:

    def __init__(self):
        self.artist_1 = input("Enter a artist: ")
        self.artist_2 = input("Enter a second artist: ")
        self.genre = input("Enter a genre: ")
        self.track_1 = input("Enter a song: ")
        self.track_2 = input("Enter a second song: ")

    def make_api_artist_request(self):
        """Makes the request to search for the artist"""
        artists_list = [self.artist_1, self.artist_2]
        final_artist_list = []
        for name in artists_list:
            endpoint_artist_url = 'https://api.spotify.com/v1/search?'
            # Replaces the white space with (+) signs so it can pass through the api filter
            q = name.replace(' ', '+')
            query = f'{endpoint_artist_url}q={q}&type=artist&limit={1}'

            artist_response = requests.get(query,
                                            headers = {"Content-Type": "application/json",
                                                        "Authorization": "Bearer {}".format(token)})
            json_artist_response = artist_response.json()
            artist = json_artist_response['artists']['items'][0]['uri'].replace('spotify:artist:', '') 
            final_artist_list.append(artist)

        final_artist_list = ','.join(final_artist_list)
        return final_artist_list

    def make_api_track_request(self):
        """Makes request for the track"""
        track_list = [self.track_1, self.track_2]
        final_track_list = []
        for track in track_list:
            endpoint_track_url = 'https://api.spotify.com/v1/search?'
            q = track.replace(' ', '+')
            query = f"{endpoint_track_url}q={q}&type=track&market=US&limit={1}"
            track_response = requests.get(query,
                                                headers = {"Content-Type": "application/json",
                                                            "Authorization": "Bearer {}".format(token)})
            json_track_response = track_response.json()
            track_final = json_track_response['tracks']['items'][0]['uri'].replace('spotify:track:', '')
            final_track_list.append(track_final)
        
        final_track_list = ','.join(final_track_list)
        return final_track_list

    def make_genre_request(self):
        """Returns a single genre"""
        return self.genre

    def make_recommend_api_request(self, artist, track, genre):
        """Makes recommendation based on artists, genres, and tracks"""
        endpoint_rec_url = 'https://api.spotify.com/v1/recommendations?'
        query = f'{endpoint_rec_url}limit={20}&seed_artists={artist}&seed_genres={genre}&seed_tracks={track}'

        recommend_response = requests.get(query,
                                            headers = {"Content-Type": "application/json",
                                                        "Authorization": "Bearer {}".format(token)})
        json_rec_response = recommend_response.json()
        
        playlist = []
        for item in json_rec_response['tracks']:
            track = item['uri']
            playlist.append(track)
        
        return playlist

    def create_playlist(self):
        """Creates a playlist"""
        playlist_name = input("Title your playlist: ")
        endpoint_playlist_url = f'https://api.spotify.com/v1/users/{user_id}/playlists'

        request_body = json.dumps({
            "name": playlist_name,
            "description": "Custom Playlist - Powered by Spotify Web API",
            "public": False
        })
        response = requests.post(url = endpoint_playlist_url, data=request_body, headers={"Content-Type": "application/json",
                                                                                            "Authorization":"Bearer {}".format(token)})
        playlist_id = response.json()['id']
        return playlist_id

    def add_items_to_playlist(self, playlist_id, playlist_songs):
        """Adds songs to playlist"""
        endpoint_add_items_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks?'

        request_body = json.dumps({
            "uris": playlist_songs
        })
        response = requests.post(url = endpoint_add_items_url, data=request_body, headers = {"Content-Type": "application/json",
                                                                                                "Authorization": "Bearer {}".format(token)})
        if response.status_code == 201:
            print("Playlist Creation Successful")
        else:
            print("Something went wrong")

if __name__ == "__main__":
    playlist = CreateCustomPlaylist()
    artist = playlist.make_api_artist_request()
    track = playlist.make_api_track_request()
    genre = playlist.make_genre_request()
    playlist_songs = playlist.make_recommend_api_request(artist, track, genre)
    playlist_id = playlist.create_playlist()
    playlist.add_items_to_playlist(playlist_id, playlist_songs)

    
     

