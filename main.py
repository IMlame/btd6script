import time
from os.path import exists

import pyautogui
import pydirectinput
import win32api, win32con
from win32con import *
from ctypes import windll, Structure, c_long, byref

# seconds between each coordinate save
second_delay = 2.5


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return {"x": pt.x, "y": pt.y}


if not exists("positions.txt"):
    f = open("positions.txt", "w")
    # save monkey location
    print("move to hover over monkey")
    time.sleep(second_delay)
    pos = queryMousePosition()
    f.write(str(pos.get("x")) + " " + str(pos.get("y")) + " monkey position\n")
    click(pos.get("x"), pos.get("y"))

    time.sleep(2)
    # scroll in menu
    for i in range(20):
        win32api.mouse_event(MOUSEEVENTF_WHEEL, pos.get("x"), pos.get("y"), -100, 0)

    # click advanced challenge
    print("move to hover over the advanced challenge")
    time.sleep(second_delay)
    pos = queryMousePosition()
    f.write(str(pos.get("x")) + " " + str(pos.get("y")) + " advanced challenge position\n")
    click(pos.get("x"), pos.get("y"))

    # click new game
    print("move to hover over new game")
    time.sleep(second_delay)
    pos = queryMousePosition()
    f.write(str(pos.get("x")) + " " + str(pos.get("y")) + " new game position\n")
    click(pos.get("x"), pos.get("y"))

    # find spot for alchemist
    print("move mouse to alchemist spot (place at the end, barely touching track")
    # wait for game to load
    time.sleep(second_delay * 2)
    # select alchemist
    pydirectinput.keyDown('f')
    pydirectinput.keyUp('f')
    time.sleep(second_delay)
    pos = queryMousePosition()
    f.write(str(pos.get("x")) + " " + str(pos.get("y")) + " alch position\n")
    pydirectinput.keyDown('f')
    pydirectinput.keyUp('f')
    time.sleep(1)
    click(pos.get("x"), pos.get("y"))
    time.sleep(.5)
    click(pos.get("x"), pos.get("y"))
    for i in range(6):
        pydirectinput.keyDown('/')
        pydirectinput.keyUp('/')

    # druid
    print("move mouse to druid spot")
    time.sleep(second_delay)
    pydirectinput.keyDown('g')
    pydirectinput.keyUp('g')
    time.sleep(second_delay)
    pos = queryMousePosition()
    f.write(str(pos.get("x")) + " " + str(pos.get("y")) + " druid position\n")
    pydirectinput.keyDown('g')
    pydirectinput.keyUp('g')
    click(pos.get("x"), pos.get("y"))
    time.sleep(.5)
    click(pos.get("x"), pos.get("y"))
    for i in range(4):
        pydirectinput.keyDown('.')
        pydirectinput.keyUp('.')

    pydirectinput.keyDown(' ')
    pydirectinput.keyUp(' ')
    pydirectinput.keyDown(' ')
    pydirectinput.keyUp(' ')

    time.sleep(15)

    # click next
    print("move to hover over next button")
    time.sleep(second_delay)
    pos = queryMousePosition()
    f.write(str(pos.get("x")) + " " + str(pos.get("y")) + " next button position\n")
    click(pos.get("x"), pos.get("y"))

    # click home
    print("move to hover over home button")
    time.sleep(second_delay)
    pos = queryMousePosition()
    f.write(str(pos.get("x")) + " " + str(pos.get("y")) + " home button position\n")
    click(pos.get("x"), pos.get("y"))
    f.close()

# main script
xs = []
ys = []
f = open("positions.txt", "r")
lines = f.readlines()
for i, line in enumerate(lines):
    split = line.split()
    xs.append(int(split[0]))
    ys.append(int(split[1]))
    print(str(xs[i]) + " " + str(ys[i]))

time.sleep(4)
while True:
    # click monkey
    click(xs[0], ys[0])
    time.sleep(1)
    for i in range(20):
        win32api.mouse_event(MOUSEEVENTF_WHEEL, xs[0], ys[0], -100, 0)

    # click mission
    time.sleep(.5)
    click(xs[1], ys[1])

    # click new game
    time.sleep(.5)
    click(xs[2], ys[2])

    # wait for game to load
    time.sleep(second_delay * 2)

    # place alchemist
    pydirectinput.keyDown('f')
    pydirectinput.keyUp('f')
    time.sleep(.5)
    pyautogui.moveTo(xs[3], ys[3], .1)
    click(xs[3], ys[3])
    time.sleep(.5)
    click(xs[3], ys[3])
    # upgrade
    for i in range(6):
        pydirectinput.keyDown('/')
        pydirectinput.keyUp('/')

    # to counteract nudge mode
    time.sleep(.5)

    # place druid
    pydirectinput.keyDown('g')
    pydirectinput.keyUp('g')
    pyautogui.moveTo(xs[4], ys[4], .1)
    click(xs[4], ys[4])
    time.sleep(.2)
    click(xs[4], ys[4])
    # upgrade
    for i in range(4):
        pydirectinput.keyDown('.')
        pydirectinput.keyUp('.')

    # start round
    pydirectinput.keyDown(' ')
    pydirectinput.keyUp(' ')
    pydirectinput.keyDown(' ')
    pydirectinput.keyUp(' ')

    # wait for game to end
    time.sleep(15)

    click(xs[5], ys[5])
    time.sleep(1)

    click(xs[6], ys[6])
    time.sleep(2)