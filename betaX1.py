import json
import random

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Label

from screeninfo import get_monitors
for monitor in get_monitors():
    print(f"Width: {monitor.width}, Height: {monitor.height}")
class ProgX:
    def __init__(self, z):
        self.z = z
        
    def start_x(self):
        root = tk.Tk()
        m_h = int((monitor.height-200)/4)
        m_w = int((monitor.width - 200)/4)
        root_geometry = str(m_w) + 'x' + str(m_h)
#The first window that opens will be 1/4 of the screen resolution. It looks good to my eyes...
        root.geometry(root_geometry)
        root.resizable(False, False)
        root.title('jsonSSS')
        def click_button():
            root.destroy()
            self.screen_x(self.z)
        
            
        write_button = ttk.Button(
            root,
            text='Write Table',
            command=click_button
        )
        button_width = 200
        button_height = 100
        window_width = m_w
        window_height = m_h

        x_position = (window_width // 2) - (button_width // 2)
        y_position = (window_height // 2) - (button_height // 2)
#I centered the button in the middle of the screen
        write_button.place(x=x_position, y=y_position, width=button_width, height=button_height)
        

        
        root.mainloop()

    def screen_x(self,json_X):
        j_buff=random.randint(1,len(json_X))
        #j_buff = 448
        print(j_buff)
        JOKER = json_X[j_buff]
           
        #print(seq_x)
        m_h = int((monitor.height-200))
        m_w = int((monitor.width - 200))
#For reference when creating a cell on the screen,
# I save the length of the values ​​of a "dict" that I took randomly into an array. 
# In order not to run the "len()" function continuously in the program, 
# I saved the length of the data in the first element of the array. 
# The values ​​in the random data I took may be smaller than the values ​​in the other dict. 
# That's why I enlarged the very small data a little bit.
        def det_size(seq_q):
            k = 0    
            det =[]
            det.append(len(JOKER))
            for i in seq_q.keys():
                buff_1 = len(str(JOKER[i]))
                det.append(buff_1) 
                k += len(str(JOKER[i]))
            for i in range(1,len(det)):
                if (det[i]/k) <= (1/(det[0]*2)):
                    det[i] = det[i]*2
                    k = k + (det[i]*0.3)
                if(det[i]/k) >= (2/(det[0])):
                    det[i] = det[i]*0.7
                    k = k + det[i]*0.1
            
            z = 0
            det.append(k)
            print(k)
            
            return tuple(det)
                           
        seq_x = det_size(JOKER)
        
        # def title_x(val,seq_row,total_row,seq_col,total_col):
        #     label = tk.Label(root_x, text=val, font=("Helvetica", 15),bg="red")
        #     int((seq_row/total_row)*m_h)
        #     int((seq_col/total_col)*m_w)
            
        #     label.place(x=int((seq_col/total_col)*m_w),y=int((seq_row/total_row)*m_h),width=200,height=50)
        def title_y(val,seq_row,total_row,seq_col,total_col,next_col):
            font_x = 15 if m_w >= 2000 else 10
            label = tk.Label(root_x, text=val, font=("Helvetica", font_x),bg="red")
            BUFF1 = int((seq_row/total_row)*m_h)
            BUFF2 = int((seq_col/total_col)*(m_w-200))
            #bbff=(((len(str(val)))/total_col)*m_w)
            bbff=((next_col/total_col)*m_w)
            #print(len(str(val)))
            bbff = ((bbff)*0.8)
         
            label.place(x=BUFF2,y=BUFF1,width=bbff,height=50)
       
#In summary, I divide the incoming row-column number by the total 
# row-column number and call it with the window resolution of the screen 
# (leaving a small margin left and right) so that if it comes in 6 columns or 10 columns, 
# the system will automatically share it on the screen.
       
        root_geometry = str(m_w) + 'x' + str(m_h)
#The window size will be slightly smaller than the screen resolution.
        root_x = tk.Tk()
        root_x.geometry(root_geometry)
        root_x.resizable(False, False)
        root_x.title('jsonS')
        #top_indent = 1
        left_indent = 1
        
        i=0
        buff_2=seq_x[seq_x[0]+1]
        n = seq_x[i+1]
#title
        for t in json_X[0].keys():  
            #title_x(t,top_indent,20,left_indent,10)
            title_y(t,1,25,n,buff_2,(seq_x[i+1])) 
            
            n += seq_x[i+1]
            i+=1
            left_indent += 1
# area
        for k in range (20):
            i = 0
            n= seq_x[i+1]
             
            for t in json_X[0].keys():  
                buff = seq_x[0]
                  
                #title_y(json_X[k][t],k+2,25,n,buff_2)  
                title_y(json_X[k][t],k+2,25,n,buff_2,seq_x[i+1])           
                #title_x(json_X[0][t],4,20,1 + i,7) 
                #title_y(json_X[0][t],8,20,n, buff_2)
                #print(JOKER)
                #print(j_buff)
                #print(seq_x[buff])
                n += (seq_x[i+1])
                i += 1
                #print(json_X[0][t])
                #print(json_X[k][t])
            
            
        root_x.mainloop()
x = r'fake_data.json'
with open(x, 'r') as file:
    data = json.load(file)
y = ProgX(data)
y.start_x()
