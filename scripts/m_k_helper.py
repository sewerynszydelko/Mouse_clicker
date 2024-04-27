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

    def click_at_position(self, cordinate_x, cordinate_y, preses=1, button=mouse.Button.left):
        self.mouse.position = (cordinate_x, cordinate_y)
        sleep(self.wait)
        self.mouse.click(button, preses)
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

    # Mouse

    controller.click_at_position(373, 105)
    controller.click_at_position(366, 143)
    controller.click_at_position(890, 64)
    controller.click_at_position(705, 91)
    controller.click_at_position(734, 222)

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
