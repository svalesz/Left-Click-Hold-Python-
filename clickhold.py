import tkinter as tk
import pyautogui
import threading
import keyboard
import time

def start_holding():
    global holding
    holding = True
    threading.Thread(target=hold_click, daemon=True).start()

def hold_click():
    while holding:
        pyautogui.mouseDown()
        time.sleep(0.1)  

def stop_holding():
    global holding
    holding = False
    pyautogui.mouseUp()

def setup_hotkeys():
    keyboard.add_hotkey('g', start_holding) # A 'g' = start(ha átírod, akkor azzal indul)
    keyboard.add_hotkey('h', stop_holding) # A 'h' = stop(ha átírod, akkor azzal leáll)

root = tk.Tk()
root.title("Left Click Hold | SwalyKHY")
root.geometry("300x150")

tk.Button(root, text="Start (g)", command=start_holding, width=15, height=2).pack(pady=10)
tk.Button(root, text="Stop (h)", command=stop_holding, width=15, height=2).pack(pady=10)

setup_hotkeys()
root.mainloop()
