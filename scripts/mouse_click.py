import logging
import time
from pynput.mouse import Listener


logging.basicConfig(filename="mouse_loger.txt",
                    level=logging.DEBUG, format="%(message)s")


def mouse_loger():

    def on_move(x, y):
        logging.info(f"Mouse moved to ({x}), ({y})")


    def on_scrotll(x, y, dx, dy):
        logging.info(f"Mouse scroled at ({x}), ({y}); ({dx}), ({dy})")


    def on_click(x, y, button, pressed):
        """ Register movment on clic, to stop pres scroll """
        if pressed:
            logging.info(f"Mouse cliced at: ({x}), ({y}) with: ({button})")

        if button == button.middle:
            listener.stop()

    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scrotll) as listener:
        listener.join()
