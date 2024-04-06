""" Main script file """
from pynput.keyboard import Key, Listener, Controller
import time
import logging


# log_dir = ""

# logging.basicConfig(filename=(log_dir + "key_loger.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s")

# def on_press(Key):
#     logging.info(Key)

# with Listener(on_press=on_press) as listener:
#     listener.join()

keyboard = Controller()

def write_sentence(sentence):
    time.sleep(2)
    keyboard.type(sentence)

def pres_and_relise(key):
    keyboard.press(key)
    keyboard.release(key)


pres_and_relise(Key.cmd)
write_sentence("Youtube")
pres_and_relise(Key.space)