from config import token
import requests

filename = 'genres.txt'

endpoint = 'https://api.spotify.com/v1/recommendations/available-genre-seeds'
response = requests.get(url=endpoint, headers={"Content-Type": "application/json",
                                                    "Authorization": "Bearer {}".format(token)})
genre_response = response.json()
with open(filename, 'w') as file_object:
    for item in genre_response['genres']:
        file_object.write(f"{item} \n")

