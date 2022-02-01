import spotipy
import spotipy.util as util
import creds

def now_playing():

    token = util.prompt_for_user_token(
            creds.username,
            creds.scope,
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

    try:
        while current_track['is_playing'] == True:
            print("Now Playing: " + \
            f"{current_track['item']['artists'][0]['name']}" + \
            " - " + \
            "'" + f"{current_track['item']['name']}" + "'" + \
            " | " + \
            " Album: " + \
            f"{current_track['item']['album']['name']}")
            break
        else:
            print("Song Paused")
    except TypeError:
        print("Now Playing: No song found... :(")

        # Artist Name
        #{current_track['item']['artists'][0]['name']}

        # Track Name
        #{current_track['item']['name']}

        # Album Name
        #{current_track['item']['album']['name']}

now_playing()
