from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(0.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
	if pyautogui.pixel(728,134) [0] == 0:
		click(728,134)
	if pyautogui.pixel(880,134) [0] == 0:
		click(880,134)
	if pyautogui.pixel(1030,134) [0] == 0:
		click(1030,134)
	if pyautogui.pixel(1171,134) [0] == 0:
		click(1171,134)
