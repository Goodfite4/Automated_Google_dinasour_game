import pyautogui
from time import sleep, time
import keyboard
from math import floor

def check_pixel_pos():
    while True:
        print(pyautogui.position())
        sleep(1)
def start():
    sleeper = 0.4
    # Use the func check_pixel_pos to check for x and y co-ords in front of the dinosaur
    x_left = 230
    x_right = 300
    sleep(2)    # so the user has time to tab over to start game

    pyautogui.press('up') # start game

    start_time = floor(time())
    while True:

        for i in reversed(range(x_left, x_right)):
            if pyautogui.pixelMatchesColor(i, 640, (172, 172, 172)):
                keyboard.press("up")
                break

            if pyautogui.pixelMatchesColor(i, 550, (172, 172, 172)):
                keyboard.press("down")
                sleep(sleeper)
                keyboard.release("down")
                break
        end_time = floor(time())

        time_passed = end_time - start_time

        if time_passed == 30:
            sleeper = 0.6
            x_right = 800
            x_left = 500


start()  # comment this out if checking for pixel position

# check_pixel_pos()  # uncomment to check for pixel position with your mouse