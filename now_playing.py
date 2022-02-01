import spotipy
import spotipy.util as util
import creds

token = util.prompt_for_user_token(creds.username, creds.scope, creds.client_id, creds.client_secret, creds.redirect_uri)
spotify = spotipy.Spotify(auth=token)
current_track = spotify.current_user_playing_track()

try:
    print("Now Playing: " + \
    f"{current_track['item']['artists'][0]['name']}" + \
    " - " + \
    "'" + f"{current_track['item']['name']}" + "'" + \
    " | " + \
    " Album: " + \
    f"{current_track['item']['album']['name']}")
except TypeError:
    print("Now Playing: No song found... :(")
