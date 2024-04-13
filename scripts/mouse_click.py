import logging
import time
import json
from pynput.mouse import Listener, Controller, Button


logging.basicConfig(filename="mouse_loger.txt",
                    level=logging.DEBUG, format="%(message)s")

mouse = Controller()


def mouse_loger():
    """ Save movment and presed button on mouse """

    def on_move(x, y):
        save_mouse_pattern_to_json([{"mouse_move": (x, y)}])
        logging.info(f"Mouse moved to ({x}), ({y})")

    def on_scrotll(x, y, dx, dy):
        save_mouse_pattern_to_json([{"mouse_scroll": (x, y, dx, dy)}])
        logging.info(f"Mouse scroled at ({x}), ({y}); ({dx}), ({dy})")

    def on_click(x, y, button, pressed):
        """ Register movment on clic, to stop pres scroll """
        if pressed:
            save_mouse_pattern_to_json([{"mouse_click": f'{button}'}])
            logging.info(f"Mouse cliced at: ({x}), ({y}) with: {button}")

        if button == button.middle:
            listener.stop()

    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scrotll) as listener:
        listener.join()

# TODO: func: read movment and make it hapend


def save_mouse_pattern_to_json(list_mouse_pattern=[]):

    try:
        with open("mouse_move.json", "r", encoding="utf-8") as file_to_read:
            data = json.load(file_to_read)

    except (json.JSONDecodeError, FileNotFoundError):
        print(f"File dosn't have any data or file don't exist, will create one")
        data = []

    with open("mouse_move.json", "w", encoding="utf-8") as file_to_write:
        data.extend(list_mouse_pattern)
        json.dump(data, file_to_write)


if __name__ == "__main__":
    # mouse_loger()
    ...