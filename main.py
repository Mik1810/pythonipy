import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
from datetime import datetime
from keyboard_interrupt import HotkeyListener
import json

credentials_path = "credentials.json"
scope = "user-read-currently-playing user-modify-playback-state"


def get_credentials():
    with open(credentials_path, "r") as keys:
        data = json.load(keys)
    return data['client-id'], data['secret-id'], data['redirect-url']


def store_song(sp):

    previous_track_id = None
    try:
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
                    with open('songs.txt', 'a') as file:
                        file.write(data_ora_formattata + " " +
                                   current_track['item']['name'] + " - " + current_track['item']['artists'][0]['name'])
                        file.write("\n")
                    print(data_ora_formattata, " ",
                          current_track['item']['name'] + " - " + current_track['item']['artists'][0]['name'])

                previous_track_id = current_track_id

            time.sleep(5)  # Polling interval
    except KeyboardInterrupt:
        print("Esecuzione interrotta")
        with open('songs.txt', 'a') as file:
            file.write("\n")
    finally:
        file.close()


if __name__ == "__main__":
    selected = int(input("1. Use credentials.json\n2. Pass it manually\n"))
    if selected == 1:
        client, secret, redirect = get_credentials()

        # Initialize spotify client
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=client,
            client_secret=secret,
            redirect_uri=redirect,
            scope=scope))

        # Initialize spotify for hotkeys listener
        listener = HotkeyListener(sp)
        listener.listen()

        # Store songs data
        store_song(sp)

    elif selected == 2:
        # TODO: implement manually storing credentials
        pass
    else:
        raise ValueError("Choose 1 or 2!")
