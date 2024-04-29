from time import sleep
from pynput import keyboard, mouse


class Controller():
    """ Controler of mouse and keyboard"""
    wait = 0.5

    def __init__(self) -> None:
        self.mouse = mouse.Controller()
        self.keyboard = keyboard.Controller()

    def click_key(self, key_to_pres_relise):
        """ Pres and relise key of given key
        Args:
            key_to_pres_relise (Keyboard.Key.'name_key'): key from pynput keyborad.Key
        """
        sleep(self.wait)
        self.keyboard.press(key_to_pres_relise)
        sleep(self.wait)
        self.keyboard.release(key_to_pres_relise)
        sleep(self.wait)

    def click_at_position(self, cordinate_x, cordinate_y, preses=1, button=mouse.Button.left):
        """ Click at given position
        Args:
            cordinate_x (int): cordiante x of pixels
            cordinate_y (int): cordinate y of pixels
            preses (int, optional): number of presses. Defaults to 1.
            button (_type_, optional): button to use. Defaults to mouse.Button.left.
        """
        self.set_positon(cordinate_x, cordinate_y)
        sleep(self.wait)
        self.mouse.click(button, preses)
        sleep(self.wait)

    def set_positon(self, cordinate_x, cordinate_y):
        """Set posiotn of mouse
        Args:
            cordinate_x (int)
            cordinate_y (int)
        """
        self.mouse.position = (cordinate_x, cordinate_y)

    def pres_move_cursor(self, position_x, position_y, move_x, move_y, button=mouse.Button.left):
        """ Hold button and move it
        Args:
            position_x (int)
            position_y (int)
            move_x (int): amout of pixels to move
            move_y (int): amout of pixels to move
            button (int, optional): Defaults to mouse.Button.left.
        """
        self.set_positon(position_x, position_y)
        self.mouse.press(button)
        sleep(self.wait)
        self.mouse.move(move_x, move_y)
        sleep(self.wait)
        self.mouse.release(button)

    def write_sentenc(self, sentence):
        """ Writing full sentence
        Args:
            sentence (str): Sentenc to write
        """
        sleep(self.wait)
        self.keyboard.type(sentence)

    def hold_and_press_key(self, key_to_hold, key_to_press):
        """ Holding and presing 2 difrent key
        Args:
            key_to_hold (_type_): Key to hold
            key_to_press (_type_): Key to press
        """
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

    controller.pres_move_cursor(800, 300, 500, 100)
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
