import time, pyautogui  # type: ignore
import PySimpleGUI as sg  # type: ignore
import multiprocessing  # type: ignore
from collections import defaultdict, deque, Counter
from itertools import (
    chain,
    combinations,
    combinations_with_replacement,
    compress,
    count,
    cycle,
)
from collections.abc import Callable, Iterable, AsyncIterable, Iterator


def KeepUI():

    sg.theme("Dark")
    layout = [
        [
            sg.Text(
                "Keep-Me-Up is now running.\nYou can keep it minised, and it will continue running.\nClose it to disable it."
            )
        ]
    ]
    window = sg.Window("Keep-Me-Up", layout)

    p2 = multiprocessing.Process(target=dontsleep)
    p2.start()

    while True:
        try:
            event, values = window.read()
            if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
                if p2.is_alive():
                    p2.terminate()
                break
        except:
            time.sleep(45)


def dontsleep():
    while True:
        try:
            pyautogui.press("volumedown")
            time.sleep(1)
            pyautogui.press("volumeup")
            time.sleep(45)
        except:
            time.sleep(45)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=KeepUI)
    p1.start()
