#### This is a simple Python script to display the current track you're listening to on Spotify using [Spotipy](https://github.com/plamere/spotipy).

## Requirements:
#### Spotify account --you'll be creating a dev account
```
pip3 install spotipy
```
## Setup & Install:

```
https://developer.spotify.com/dashboard
Login
Click 'Create An App'
Create an 'App Name' and 'App Description'
Click 'Edit Settings'
Under Redirect URIs enter 'http://127.0.0.1:9999' then 'Add' and 'Save'
Back on the Dashboard Overview page, click Show Client Secret and make note of 'Client ID' and 'Client Secret'
Replace 'client_id', 'client_secret', and 'username' (your Spotify username) values in creds.py with yours
```
## Running:
#### On your first run your web browser will open to accept the token. The token lasts ~24 hrs.
```
python now_playing.py
```
![screenshot](/image/screenshot.png)
