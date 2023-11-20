import keyboard
from spotipy import SpotifyException


class HotkeyListener():
    pause: bool = False
    sp = None

    def __init__(self, sp):
        if sp is None:
            raise RuntimeError("You have to pass a Spotify Client!")
        self.sp = sp

    def on_key_press(self, event):
        try:
            """
            if keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt') and keyboard.is_pressed('right'):
                print("CTRL + Alt + Freccia destra premuti contemporaneamente.")
                self.sp.next_track()
            if keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt') and keyboard.is_pressed('space'):
                if self.pause:
                    self.sp.start_playback()
                else:
                    self.sp.pause_playback()
                self.pause = not self.pause
            """
            if keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt') and keyboard.is_pressed('p'):
                print("Added to favorites")
                with open('songs.txt', 'rb+') as file:
                    file.seek(-2, 2)
                    file.write(' LIKED\n'.encode())
        except SpotifyException:
            print("You don't have PREMIUM!")

    def listen(self):
        keyboard.on_press(self.on_key_press)
