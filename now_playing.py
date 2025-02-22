from datetime import datetime
import os
import sys
import spotipy
import spotipy.util as util
sys.path.insert(0, f'/Users/{os.getenv("USER")}/scripts/python')
import creds

def get_spotify_token(cred_file):
    """Retrieve the OAuth token for Spotify authentication."""
    return util.prompt_for_user_token(
        cred_file.username,
        'user-read-currently-playing',
        cred_file.client_id,
        cred_file.client_secret,
        cred_file.redirect_uri
    )

def get_current_track(spotify):
    """Fetch the current track from the Spotify API."""
    return spotify.current_user_playing_track()

def format_track_info(track):
    """Format the track information to display artist, track name, and album name."""
    artist_name = track['item']['artists'][0]['name']
    track_name = track['item']['name']
    album_name = track['item']['album']['name']
    return f"{artist_name} - '{track_name}' | Album: {album_name}"

def display_playing_info(track):
    """Display information when a song is currently playing."""
    track_info = format_track_info(track)
    print(f"Now Playing: {track_info}")

def display_paused_info(track):
    """Display information when the song is paused, including the timestamp."""
    timestamp = format_timestamp(track['timestamp'])
    track_info = format_track_info(track)
    print(f"Song Paused @ {timestamp}:")
    print(track_info)

def format_timestamp(timestamp):
    """Format the timestamp into HH:MM:SS format."""
    timestamp_str = str(timestamp)[:10]  # Remove milliseconds part
    return str(datetime.fromtimestamp(int(timestamp_str)))[11:19]

def now_playing(cred_file):
    """Check if a song is playing or paused and display relevant information."""
    token = get_spotify_token(cred_file)
    spotify = spotipy.Spotify(auth=token)
    current_track = get_current_track(spotify)
    if current_track is None:
        print("No song found... :(")
        return
    if current_track.get('is_playing', False):
        display_playing_info(current_track)
    else:
        display_paused_info(current_track)

def main(cred_file):
    now_playing(cred_file)

if __name__ == "__main__":
    main(creds)
