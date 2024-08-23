"""
    main start(first screen) =>  **main_screen
        main_screen => **senior_screen
            senior_screen =>  **assistant_title,**mid_page,**mid_button_build
                assistant_title => **worker_cell
                mid_page => **worker_cell,**assistant_page_info
                    assistant_page_info => **worker_cell
                mid_button_build => **assistant_button_build
                    assistant_button_build => **worker_page_button
"""
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
        self.page = 0
        self.root = tk.Tk()
        self.json_X = z
        self.m_h = int((monitor.height-200)/4)
        self.m_w = int((monitor.width - 200)/4)
        root_geometry = str(self.m_w) + 'x' + str(self.m_h)
        self.root.geometry(root_geometry)
        
        self.MH2 = int((monitor.height-200))
        self.MW2 = int((monitor.width - 200))
        
    def main_start(self):        
        self.root.resizable(False, False)
        self.root.title('jsonSSS')
        def click_button():
            self.root.destroy()
            self.main_screen()
        
        write_button = ttk.Button(
            self.root,
            text='Write Table',
            command=click_button
        )
        button_width = 200
        button_height = 100
        window_width = self.m_w
        window_height = self.m_h

        x_position = (window_width // 2) - (button_width // 2)
        y_position = (window_height // 2) - (button_height // 2)
        write_button.place(x=x_position, y=y_position, width=button_width, height=button_height)
        
        self.root.mainloop()
    
    def main_screen(self):
        
        j_buff=random.randint(1,len(self.json_X))
    
        JOKER = self.json_X[j_buff]
        
        self.seq_x = self.worker_det_size(JOKER)

        root_geometry = str(self.MW2) + 'x' + str(self.MH2)

        self.root_x = tk.Tk()
        self.root_x.geometry(root_geometry)
        self.root_x.resizable(False, False)
        self.root_x.title('jsonS')
        self.senior_screen()
        
        self.root_x.mainloop()
      
    def senior_screen(self):
        self.assistant_title()
        self.mid_page(self.page*20,(((self.page)+1)*20)) 
        self.mid_button_build()
        return None
  
    def mid_page(self,start_,stop_):
        
        i=0
        buff_2=self.seq_x[self.seq_x[0]+1]
        n = self.seq_x[i+1]
# area
        for k in range (start_,stop_):
            i = 0
            n= self.seq_x[i+1]
             
            for t in self.json_X[0].keys():  
                buff = self.seq_x[0]
                  
                self.worker_cell(self.json_X[k][t],(k%20)+2,25,n,buff_2,self.seq_x[i+1])           
    
                n += (self.seq_x[i+1])
                i += 1
     
        self.assistant_page_info(start_,stop_)
        return None

    def mid_button_build(self):
    
        def _func_next(k):
      
            if (len(self.json_X))>= ((self.page+k+1)*20):     
                self.page += k
            else:
                return None
        
            for widget in self.root_x.winfo_children():
                widget.destroy()
            self.senior_screen()

        def _func_prev(k):
            if (0)<= ((self.page-k)*20):     
                self.page -= k
            else:
                return None
        
            for widget in self.root_x.winfo_children():
                widget.destroy()
            self.senior_screen()
       
            return None
        for i in range (3):
            if (len(self.json_X))>= ((self.page+i+2)*20):                 
                self.assistant_button_build(23,((self.MW2/2)+((i+1)*100)),(">"*(i+1)),w_func=lambda i=i : _func_next(i+1))
        for j in range (3):
            if ((self.page-j-1)*20)>= 0:                            
                self.assistant_button_build(23,((self.MW2/2)-((j+1)*100)-100),("<"*(j+1)),w_func=lambda j=j : _func_prev(j+1))
  
        return None
        
    def assistant_title(self):
        buff_2=self.seq_x[self.seq_x[0]+1]
        left_indent = 1
        i=0
        n = self.seq_x[i+1]
        for t in self.json_X[0].keys():  
            self.worker_cell(t,1,25,n,buff_2,(self.seq_x[i+1])) 
            
            n += self.seq_x[i+1]
            i+=1
            left_indent += 1

    
        return None

    def assistant_page_info(self,start__,stop__):
        buff_1 = str(start__) + "-" + str(stop__)
        # 2 + 1 +2
        buff_2 = ((self.MW2/2)-(len(buff_1)/2))
  
        self.worker_cell(buff_1,23,25,buff_2,self.MW2,200)
        return None

    def assistant_button_build(self,_col,_recess,_val,w_func):
        _style = {
        "x" :_recess,            
        #"x" :((self.MW2/2)+50),
        "y" : ((_col/25)*(self.MH2)),
        "width": 32 + (len(_val)*20),
        "height": 50
        }
        self.worker_page_button(_val,w_func,**_style)
  
    def worker_det_size(self,seq_q):
        k = 0    
        det =[]
        det.append(len(seq_q))
        for i in seq_q.keys():
            buff_1 = len(str(seq_q[i]))
            det.append(buff_1) 
            #print(buff_1)
            k += len(str(seq_q[i]))
        for i in range(1,len(det)):
            if (det[i]/k) <= (1/(det[0]*2)):
                det[i] = int(det[i]*2)
                k = k + int(det[i]*0.3)
            if(det[i]/k) >= (2/(det[0])):
                det[i] = int(det[i]*0.8)
                k = k + int(det[i]*0.1)
            
        z = 0
        det.append(int(k))
        print(det)
        return tuple(det)   
     
    def worker_cell(self,val,seq_row,total_row,seq_col,total_col,next_col):
        font_x = 15 if self.MW2 >= 2000 else 10
        label = tk.Label(self.root_x, text=val, font=("Helvetica", font_x),bg="white")
        BUFF1 = int((seq_row/total_row)*self.MH2)
        
        BUFF2 = int((seq_col/total_col)*(self.MW2-200))
            
        buff=((next_col/total_col)*self.MW2)
        buff = ((buff)*0.8)
         
        label.place(x=BUFF2,y=BUFF1,width=buff,height=50)

    def worker_page_button(self,_text,_func,**_place):
        
        _style = ttk.Style()
        _style.configure('my.TButton', font=('Helvetica', 20,'bold'))
        write_button = ttk.Button(
            self.root_x,
            text=_text,
            style='my.TButton',
            command=_func
            
        )
        
        write_button.place (_place)  
  
x = r'fake_data.json'
with open(x, 'r') as file:
    data = json.load(file)
y = ProgX(data)
y.main_start()

