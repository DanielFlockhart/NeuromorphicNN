import pyautogui,string

pyautogui.FAILSAFE = False
def get_mouse_pos():
    return pyautogui.position()

def click(x,y):
    print(f"clicked at ({x},{y})")
    pyautogui.moveTo(x, y)
    pyautogui.click()

def press_key(key):
    pyautogui.press(string.ascii_lowercase[key])