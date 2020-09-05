# Method for receiving user input
# Method for making the API endpoint request for artists ID
# Method for making the API endpoint request for recommendations
import requests
from config import token, user_id
import json

class CreateCustomPlaylist:

    def __init__(self):
        self.artist_count = int(input("How many artists do you wanna input? "))
        self.genre_count = int(input("How many genres do you wanna input?"))
        self.track_count = int(input("How many tracks do you wanna input? "))

    def make_api_artist_request(self):
        """Makes the request to search for the artist"""

        """Idea - For multiple artists -  We are going to ask Enter artists in this method and enter genre will be asked in different method
        and we will loop over how many artists that they wanna input - then we will give them a unique identifier ex. artist_1 - artist[i]
        Then we will have all the artists, then we will append them to a list and return it and the end of the function."""
        check_length = CreateCustomPlaylist.check_count(self.artist_count)
        if check_length:
            artists_list = []
            # List to loop over the number of artists
            for i in range(self.artist_count):
                artist_name = input("Enter an artist: ")
                artists_list.append(artist_name)
            
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
            print(final_artist_list)
            return final_artist_list
        
        print("Only can input up to 5 values")

    def make_api_track_request(self):
        """Makes request for the track"""
        check_length = CreateCustomPlaylist.check_count(self.track_count)
        if check_length:
            track_list = []
            # List to loop over the number of tracks
            for i in range(self.track_count):
                track_name = input("Enter track name: ")
                track_list.append(track_name)

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
            print(final_track_list)
            return final_track_list
        
        print("Only can input up to 5 values")

    def make_genre_request(self):
        """Makes a list of genres to pass into the recommend method"""
        check_length = CreateCustomPlaylist.check_count(self.genre_count)
        if check_length:
            genre_list = []
            for i in range(self.genre_count):
                genre_name = input("Enter a genre: ")
                genre_list.append(genre_name)
            
            genre_list = ','.join(genre_list)
            return genre_list

        print("Only can input up to 5 values")

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

    def check_count(count):
        if count > 5:
            return False
        elif count < 0:
            return False
        else:
            return True


if __name__ == "__main__":
    playlist = CreateCustomPlaylist()
    artist = playlist.make_api_artist_request()
    track = playlist.make_api_track_request()
    genre = playlist.make_genre_request()
    playlist_songs = playlist.make_recommend_api_request(artist, track, genre)
    playlist_id = playlist.create_playlist()
    playlist.add_items_to_playlist(playlist_id, playlist_songs)

    
     

