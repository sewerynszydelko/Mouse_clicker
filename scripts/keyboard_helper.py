from pynput import keyboard

if __name__ == "__main__":
    controler = keyboard.Controller()

    controler.press(keyboard.Key.cmd)
    controler.release(keyboard.Key.cmd)

    controler.type("paint")

    controler.press()