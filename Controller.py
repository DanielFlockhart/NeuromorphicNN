import pyautogui


def get_mouse_pos():
    return pyautogui.position()

def click(x,y):
    print(f"clicked at ({x},{y})")
    pyautogui.moveTo(x, y)
    pyautogui.click()

def press_key(key='space'):
    pyautogui.press(key)