import logging
import time
import json
from pynput.mouse import Listener, Controller, Button


logging.basicConfig(filename="mouse_loger.txt",
                    level=logging.DEBUG, format="%(message)s")

mouse = Controller()


def save_mouse_pattern_to_json(list_mouse_pattern=[], file_to_save="mouse_move.json"):
    """ Save movment of mouse in json file 
    Args:
        file_to_save (str, optional): name of file to save movment
        list_mouse_pattern (list, optional): list with dict in it to save. Defaults to [].
    """
    try:
        with open(file_to_save, "r", encoding="utf-8") as file_to_read:
            data = json.load(file_to_read)

    except (json.JSONDecodeError, FileNotFoundError):
        print(f"File dosn't have any data or file don't exist, will create one")
        data = []

    with open(file_to_save, "w", encoding="utf-8") as file_to_write:
        data.extend(list_mouse_pattern)
        json.dump(data, file_to_write)


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


def mouse_click_relise(key):
    """ Pres and relise key of mous
    Args:
        key (str): Button of mouse presed
    """
    match key:
        case "Button.left":
            mouse.click(Button.left)
        case "Button.right":
            mouse.click(Button.right)
        case "Button.middle":
            mouse.click(Button.middle)


def move_mouse_from_list(movment_mouse_list: list):
    """ Move and pres mouse from given list of dict
    Args:
        movment_mouse_list (list): List with movment save in dict
    """
    for move in movment_mouse_list:
        key_list = list(move.keys())

        if "mouse_move" in key_list:
            mouse.move(move["mouse_move"][0], move["mouse_move"][1])
        elif "mouse_click" in key_list:
            mouse_click_relise(move["mouse_click"])
        ...


if __name__ == "__main__":
    # mouse_loger()
    with open("mouse_move.json", "r", encoding="utf-8") as file:
        print("ewrything work")
        list_movment = json.load(file)
        move_mouse_from_list(list_movment)
    ...
