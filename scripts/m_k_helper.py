import time
from pynput import keyboard, mouse

if __name__ == "__main__":

    controler = keyboard.Controller()

    controler.press(keyboard.Key.cmd_l)
    controler.release(keyboard.Key.cmd_l)
    time.sleep(1)
    controler.type("paint")
    time.sleep(1)
    controler.press(keyboard.Key.enter)
    controler.release(keyboard.Key.enter)
    time.sleep(1)
    controler.press(keyboard.Key.cmd_l)
    controler.press(keyboard.Key.up)

    with controler.pressed(keyboard.Key.cmd_l):
        controler.release(keyboard.Key.up)

    # controler.release(keyboard.Key.up)
    # controler.press(keyboard.Key.cmd_l)
    # controler.press(keyboard.Key.page_up)
    # time.sleep(0.5)
    # controler.release(keyboard.Key.page_up)
    # controler.release(keyboard.Key.cmd_l)
