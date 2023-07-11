import keyboard

sp1 = None


def initializeSpotify(sp=None):
    global sp1
    sp1 = sp


def on_key_press(event):
    global sp1
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt') and keyboard.is_pressed('right'):
        print("CTRL + Alt + Freccia destra premuti contemporaneamente.")
        sp1.next_track()


keyboard.on_press(on_key_press)
