import credentials as cr
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
from datetime import datetime
from keyboard_interrupt import initializeSpotify

scope = "user-read-currently-playing user-modify-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=cr.SPOTIPY_CLIENT_ID,
    client_secret=cr.SPOTIPY_CLIENT_SECRET,
    redirect_uri=cr.SPOTIPY_REDIRECT_URI,
    scope=scope))

previous_track_id = None
file = None

# Initialize spotify for hotkeys listener
initializeSpotify(sp)

try:

    file = open('songs.txt', 'a', encoding='utf-8')
    while True:

        current_track = sp.current_user_playing_track()

        if current_track is not None:
            current_track_id = current_track['item']['id']
            if current_track_id != previous_track_id:
                # Mi interessa salvare il nome dell'artista item -> artists -> 0 -> name
                # il nome della canzone item -> name
                data_ora_corrente = datetime.now()
                # Formatta la data e l'orario corrente tra parentesi quadre
                data_ora_formattata = "[" + data_ora_corrente.strftime("%Y-%m-%d %H:%M:%S") + "]"
                file.write(data_ora_formattata+ " "+
                           current_track['item']['name'] + " - " + current_track['item']['artists'][0]['name'])
                file.write("\n")
                print(data_ora_formattata, " ",
                        current_track['item']['name'] + " - " + current_track['item']['artists'][0]['name'])

            previous_track_id = current_track_id

        time.sleep(5)  # Intervallo di polling (5 secondi nel caso di questo esempio)
except KeyboardInterrupt:
    print("Esecuzione interrotta")
    file.write("\n")
finally:
    file.close()
