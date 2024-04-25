import time
from pynput import keyboard, mouse

if __name__ == "__main__":

    # Keyboard
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

    time.sleep(1)

    # Mouse
    mouse_controler = mouse.Controller()

    mouse_controler.position = (373, 105)
    time.sleep(0.5)
    mouse_controler.click(mouse.Button.left, 1)
    time.sleep(0.5)
    mouse_controler.position = (366, 143)
    time.sleep(0.5)
    mouse_controler.click(mouse.Button.left, 1)
    time.sleep(0.5)
    mouse_controler.position = (890, 64)
    time.sleep(0.5)
    mouse_controler.click(mouse.Button.left, 1)
    time.sleep(0.5)
    mouse_controler.position = (705, 91)
    time.sleep(0.5)
    mouse_controler.click(mouse.Button.left, 1)
    time.sleep(0.5)
    mouse_controler.position = (734, 222)
    time.sleep(0.5)
    mouse_controler.click(mouse.Button.left, 1)
    time.sleep(1)

    # Drawing
    mouse_controler.position = (800, 300)
    mouse_controler.press(mouse.Button.left)
    time.sleep(1)
    mouse_controler.move(50, 100)
    mouse_controler.release(mouse.Button.left)
    mouse_controler.press(mouse.Button.left)
    time.sleep(1)
    mouse_controler.move(0, 400)
    time.sleep(1)
    mouse_controler.move(200, 0)
    time.sleep(1)
    mouse_controler.release(mouse.Button.left)
