from pynput import mouse


if __name__ == "__main__":
    def mouse_helper():
        """ Print info about place of mouse by pres, if want exit pres midles mouse button"""
        def on_click(x, y, button, pressed):
            if button == button.middle:
                listner.stop()
            print(f"x = {x} y = {y}")

        with mouse.Listener(on_click=on_click) as listner:
            listner.join()
