""" Keaybord clicer func main file """
import time
import logging
from pynput.keyboard import Key, Controller, Listener


log_dir = ""

logging.basicConfig(filename=(log_dir + "key_loger.txt"),
                    level=logging.DEBUG, format="%(asctime)s: %(message)s")

keyboard = Controller()


def write_sentence(sentence: str):
    """ Allows write full sting sentence
    Args: sentence (str): whole sentenc to write
    """
    keyboard.type(sentence)
    time.sleep(1)


def pres_relise_key(key, delay=0.1):
    keyboard.press(key)
    time.sleep(delay)
    keyboard.release(key)


def on_press(key):
    logging.info(key)


def on_release(key):
    if key == Key.insert:
        return False


def keyboard_loger():
    """ save logs of typed char in file 'key_loger.txt' to exit type insert """
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


keyboard_loger()
