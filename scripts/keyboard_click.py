""" Keaybord clicer func main file """
import time
import logging
import json
from pynput.keyboard import Key, Controller, Listener


log_dir = ""

logging.basicConfig(filename=(log_dir + "key_loger.txt"),
                    level=logging.DEBUG, format="%(message)s")

keyboard = Controller()


def save_keyboard_move_to_json(list_keyboard_pattern=[], file_to_save="keyboard_move.json"):
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
        data.extend(list_keyboard_pattern)
        json.dump(data, file_to_write)


def keyboard_loger():
    """ Sace keybord presed keys , to stop press insert"""
    def on_press(key):
        logging.info(key)
        save_keyboard_move_to_json([{"pressed_key": f'{key}'}])

    def on_release(key):
        if key == Key.insert:
            listener.stop()

    """ save logs of typed char in file 'key_loger.txt' to exit type insert """
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


def write_sentence(sentence: str):
    """ Allows write full sting sentence
    Args: sentence (str): whole sentenc to write
    """
    keyboard.type(sentence)
    time.sleep(1)


def pres_relise_key(key, delay=0.1):
    """ Pres and realise a given key on keyboard and adjast delay betwin
    Args:
        key (str): specific key to pres
        delay (float, optional): delay betwin pres and realuse Defaults to 0.1.
    """
    keyboard.press(key)
    time.sleep(delay)
    keyboard.release(key)


def keyboard_auto_pres(list_presed_keys):
    for key in list_presed_keys:
        key_list = list(key.keys())

        if "pressed_key" in key_list:
            pres_relise_key(key["pressed_key"])
        elif "Key" in key_list["pressed_key"]:
            print("found it")
        else:
            print("not work")
    ...


if __name__ == "__main__":

    with open("keyboard_move.json", "r",encoding="utf-8") as file:
        list_presed_keys = json.load(file)
        keyboard_auto_pres(list_presed_keys)
    #keyboard_loger()
