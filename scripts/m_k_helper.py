from time import sleep
from pynput import keyboard, mouse


class Controller():
    """ Controler of mouse and keyboard"""
    wait = 0.5

    def __init__(self) -> None:
        self.mouse = mouse.Controller()
        self.keyboard = keyboard.Controller()

    def click_key(self, key_to_pres_relise):
        sleep(self.wait)
        self.keyboard.press(key_to_pres_relise)
        sleep(self.wait)
        self.keyboard.release(key_to_pres_relise)
        sleep(self.wait)

    def write_sentenc(self, sentence):
        sleep(self.wait)
        self.keyboard.type(sentence)

    def hold_and_press_key(self, key_to_hold, key_to_press):
        self.keyboard.press(key_to_hold)
        sleep(self.wait)
        self.keyboard.press(key_to_press)
        sleep(self.wait)
        self.keyboard.release(key_to_hold)
        self.keyboard.release(key_to_press)

if __name__ == "__main__":

    # Keyboard
    controller = Controller()

    controller.click_key(keyboard.Key.cmd_l)
    controller.write_sentenc("paint")
    controller.click_key(keyboard.Key.enter)
    controller.hold_and_press_key(keyboard.Key.cmd_l, keyboard.Key.up)


    # time.sleep(1)
    # controler.press(keyboard.Key.cmd_l)
    # controler.press(keyboard.Key.up)

    # with controler.pressed(keyboard.Key.cmd_l):
    #     controler.release(keyboard.Key.up)

    # time.sleep(1)

    # # Mouse
    # mouse_controler = mouse.Controller()

    # mouse_controler.position = (373, 105)
    # time.sleep(0.5)
    # mouse_controler.click(mouse.Button.left, 1)
    # time.sleep(0.5)
    # mouse_controler.position = (366, 143)
    # time.sleep(0.5)
    # mouse_controler.click(mouse.Button.left, 1)
    # time.sleep(0.5)
    # mouse_controler.position = (890, 64)
    # time.sleep(0.5)
    # mouse_controler.click(mouse.Button.left, 1)
    # time.sleep(0.5)
    # mouse_controler.position = (705, 91)
    # time.sleep(0.5)
    # mouse_controler.click(mouse.Button.left, 1)
    # time.sleep(0.5)
    # mouse_controler.position = (734, 222)
    # time.sleep(0.5)
    # mouse_controler.click(mouse.Button.left, 1)
    # time.sleep(1)

    # # Drawing
    # mouse_controler.position = (800, 300)
    # mouse_controler.press(mouse.Button.left)
    # time.sleep(1)
    # mouse_controler.move(50, 100)
    # mouse_controler.release(mouse.Button.left)
    # mouse_controler.press(mouse.Button.left)
    # time.sleep(1)
    # mouse_controler.move(0, 400)
    # time.sleep(1)
    # mouse_controler.move(200, 0)
    # time.sleep(1)
    # mouse_controler.release(mouse.Button.left)
