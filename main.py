import credentials as cr
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import json

scope = "user-read-currently-playing"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=cr.SPOTIPY_CLIENT_ID,
    client_secret=cr.SPOTIPY_CLIENT_SECRET,
    redirect_uri=cr.SPOTIPY_REDIRECT_URI,
    scope=scope))

previous_track_id = None
file = None

try:
    file = open('songs.json', 'a')
    while True:

        current_track = sp.current_user_playing_track()

        if current_track is not None:
            current_track_id = current_track['item']['id']
            if current_track_id != previous_track_id:
                # Mi interessa salvare il nome dell'artista item -> artists -> 0 -> name
                # il nome della canzone item -> name
                json.dump(current_track, file)
                file.write(",")

            previous_track_id = current_track_id

        time.sleep(5)  # Intervallo di polling (5 secondi nel caso di questo esempio)
except KeyboardInterrupt:
    file.write("]\n}")
    file.close()