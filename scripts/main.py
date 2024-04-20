""" Main script file """
from pynput.keyboard import Key, Listener, Controller
from pynput.mouse import Listener
import json
import time
import logging
import mouse_click


def menu_print():
    "Print menu of choice to user"
    print("You can chose to:\
          \n1: Run mouse log movment(to top pres cicrcle or middle)\
          \n2: Run already saved move\
          \n3: Exit")


def loop_menu():
    "Its loop menu to chose betwi options"
    while True:
        print("Hello welcom in mouse loger")
        time.sleep(1)
        print("Here you can memorize and automate mouse movment")
        time.sleep(1.5)

        menu_print()
        user_input = input()

        match user_input:
            case "3":
                break
            case "1":
                mouse_click.mouse_loger()
            case "2":
                with open("mouse_move.json", "r", encoding="utf-8") as file:
                    print("ewrything work")
                    list_movment = json.load(file)
                mouse_click.move_mouse_from_list(list_movment)

if __name__ == "__main__":
    loop_menu()