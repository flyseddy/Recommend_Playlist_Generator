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
Enter an artist: arctic monkeys
Enter a genre: indie
Enter a track: star treatment
Title your playlist: My Custom Playlist
Playlist Creation Successful
```
## Config.py
```python
token = "YOUR_TOKEN_HERE"
user_id = "YOUR_USER_ID"
```
Note: To obtain OAuth token, you must go to https://developer.spotify.com/console/post-playlists/
and request the scopes playlist-modify-public and playlist-modify-private

Note: To obtain yor user_id go to your Spotify profile, click share, and copy our Spotify URI (only the last part of it - (ex. spotify:user{user_id}) - input the user_id part

## Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE)