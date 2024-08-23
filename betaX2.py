import json

import random

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Label

from screeninfo import get_monitors
for monitor in get_monitors():
    print(f"Width: {monitor.width}, Height: {monitor.height}")
root = tk.Tk()
class HW2:
    def __init__(self):
        self.m_h = int((monitor.height-200)/4)
        self.m_w = int((monitor.width - 200)/4)
        root_geometry = str(self.m_w) + 'x' + str(self.m_h)
        root.geometry(root_geometry)
        root.resizable(False, False)
        root.title('jsonSSS')
        self.button(self.m_h,self.m_w)
    def button(self,MH,MW):
        def click_button():
            root.destroy()
        write_button = ttk.Button(
        root,
        text='Write Table',
        command=click_button
        )
        button_width = 200
        button_height = 100
        window_width = MW
        window_height = MH
        x_position = (window_width // 2) - (button_width // 2)
        y_position = (window_height // 2) - (button_height // 2)
        write_button.place(x=x_position, y=y_position, width=button_width, height=button_height)
        

        
        print("test")
hw1 = HW2()
root.mainloop()

     
    
    