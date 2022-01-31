#### This is a simple Python script to display the current track you're listening to on Spotify by using [Spotipy](https://github.com/plamere/spotipy).

## Requirements:
#### Spotify account --you'll be creating a dev account
```
pip install spotipy
```
## Setup & Install:

```
https://developer.spotify.com/dashboard
Login
Click 'Create An App'
Create an 'App Name' and 'App Description'
Click 'Edit Settings'
Under Redirect URIs enter 'http://127.0.0.1:9999' then 'Add' and 'Save'
Replace 'client_id', 'client_secret', and 'username' values in creds.py with yours
```
## Running:
```
python now_playing.py
```
