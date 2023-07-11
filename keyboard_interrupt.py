import keyboard

sp1 = None
paused = False


def initializeSpotify(sp=None):
    global sp1
    sp1 = sp


def on_key_press(event):
    global sp1, paused
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt') and keyboard.is_pressed('right'):
        print("CTRL + Alt + Freccia destra premuti contemporaneamente.")
        sp1.next_track()
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt') and keyboard.is_pressed('space'):
        if paused:
            sp1.start_playback()
        else:
            sp1.pause_playback()
        paused = not paused
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt') and keyboard.is_pressed('p'):
        print("Added to favorites")
        file = open('songs.txt', 'a+')
        file.write("LIKED ")




keyboard.on_press(on_key_press)
