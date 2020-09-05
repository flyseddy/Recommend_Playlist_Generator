# Recommend_Playlist_Generator
Creates a recommended playlist for you based upon your favorite artist, genre, and song.
## Installation (required libraries)

```bash
pip install -r requirements.txt
```

## Run

```python
python3 custom_playlist.py
```
## Examples
```python
Enter an artist: ll cool j
Enter a second artist: lauryn hill
Enter a genre: hip-hop
Enter a song: around the way girl
Enter a second song: doo wop
Title your playlist: Hip-Hop
Playlist Creation Successful
```
## Config.py
```python
token = "YOUR_TOKEN_HERE"
user_id = "YOUR_USER_ID"
```
Note: To obtain OAuth token, you must go to https://developer.spotify.com/console/post-playlists/
and request the scopes playlist-modify-public and playlist-modify-private

Note: To obtain your user_id, go to your Spotify profile, click share, and copy your Spotify URI (only the last part of it - (ex. spotify:user{user_id})

## Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
