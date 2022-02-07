import spotipy
import spotipy.util as util
import creds
from datetime import datetime

token = util.prompt_for_user_token(
        creds.username,
        'user-read-currently-playing',
        creds.client_id,
        creds.client_secret,
        creds.redirect_uri
)

"""
Build OAuth token for your Spotify app

Parameters:
    username = 'username'
    scope = 'user-read-currently-playing'
    client_id='aaaaaaaaaaaaaaaa1234567890123456'
    client_secret='aaaaaaaaaaaaaaaa1234567890123456'
    redirect_uri='http://127.0.0.1:9999'
"""

spotify = spotipy.Spotify(auth=token)
current_track = spotify.current_user_playing_track()
 
def now_playing():
    try:
        while current_track['is_playing'] == True:
            playing()
            break
        else:
            paused()
    except TypeError:
        print("Now Playing: No song found... :(")

def playing():
    print(f"Now Playing: " + \
    f"{current_track['item']['artists'][0]['name']}" + \
    " - " + \
    "'" + f"{current_track['item']['name']}" + "'" + \
    " | " + \
    " Album: " + \
    f"{current_track['item']['album']['name']}")

def paused():
    a=str(current_track['timestamp'])
    a=a[0:10]
    a=str(datetime.fromtimestamp(int(a)))
    a=a[11:19]

    print(f"Song Paused @ " + a + ":")
    print(f"{current_track['item']['artists'][0]['name']}" + \
    " - " + \
    "'" + f"{current_track['item']['name']}" + "'" + \
    " | " + \
    " Album: " + \
    f"{current_track['item']['album']['name']}")

    """
    Parameters:
        a = '1644100566336'
        a = '1644100566'
        a = '2022-02-05 17:36:06'
        a = '17:36:06'
    """

now_playing()
