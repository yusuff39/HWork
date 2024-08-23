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
#Data is being added to json x but there are errors.
import json
import random
import tkinter as tk
from tkinter import DISABLED, END, Menu, StringVar, ttk,Entry
from tkinter.ttk import Label

from screeninfo import get_monitors # type: ignore
for monitor in get_monitors():
    print(f"Width: {monitor.width}, Height: {monitor.height}")


class ProgX:
    def __init__(self, z):
        self.page = 0
        self.root = tk.Tk()
        self.json_X = z
        self.test__ = {}
        self.get_val = []
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
                  
                self.worker_cell(self.json_X[k][t],(k%20)+2,25,n,buff_2,self.seq_x[i+1],self.json_X[k])           
    
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
        
    def assistant_title(self,y_=1,t_y_=25,root_title ="show_list",heihgt___=None):
        
        buff_2=self.seq_x[self.seq_x[0]+1]
        left_indent = 1
        i=0
        n = self.seq_x[i+1]
        for key_ in self.json_X[0].keys():  
            self.worker_cell(key_,y_,t_y_,n,buff_2,(self.seq_x[i+1]),root_=root_title,height_=heihgt___) 
            
            n += self.seq_x[i+1]
            i+=1
            left_indent += 1

    
        return None

    def assistant_page_info(self,start__,stop__,root_page="show_list"):
        buff_1 = str(start__) + "-" + str(stop__)
        # 2 + 1 +2
        buff_2 = ((self.MW2/2)-(len(buff_1)/2))
  
        self.worker_cell(buff_1,23,25,buff_2,self.MW2,200,root_=root_page)
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
        def random_len(seq_x):    
            det =[]        
            for i in seq_x.keys():
                buff_1 = len(str(seq_x[i]))
                det.append(buff_1) 
            print(det)
            return tuple(det)  
        def title_len(seq_x):    
            det =[]        
            for i in seq_x.keys():
                buff_1 = len(str(i))
                det.append(buff_1) 
            print(det)
            return tuple(det)          

        
        x = random_len(seq_q)
        y = title_len(seq_q)
        def len_versus(a,b):
            det =[]
            k=0
            det.append(len(a))
            for i in range (len(a)):
                if a[i] >= b[i]:
                    k += a[i]
                    det.append(a[i])
                else:
                    k += b[i]
                    det.append(b[i])
            det.append(k)
            
            return det
        z = len_versus(x,y)
        return tuple(z) 
     
    def worker_cell(self,val,seq_row,total_row,seq_col,total_col,next_col,root_,col_=None,height_=None):

        if height_ == None:
            height_= self.MH2
        
        if root_=="show_list":
             root__ = self.root_x
        elif root_ =="add":
            root__ = self.root_add
        else:
            root__ = self.root_x
        font_x = 15 if self.MW2 >= 2000 else 10
        label = tk.Label(root__, text=val, font=("Helvetica", font_x),bg="white")
        BUFF1 = int((seq_row/total_row)*height_)
        BUFF2 = int((seq_col/total_col)*(self.MW2-200))
            
        buff=((next_col/total_col)*self.MW2)
        buff = ((buff)*0.8)
         
        label.place(x=BUFF2,y=BUFF1,width=buff,height=50)
        m = Menu(self.root_x,tearoff=0)
        def _delete_event():
            
            return None
        def _add_event():
            print(col_)
            self.senior_add_screen()

            """
            heigh_ = (self.MH2)/4
            wid_=(self.MW2)
            root_y_geometry = str(int(wid_)) + 'x' + str(int(heigh_))
            root_y = tk.Tk()
            root_y.resizable(False, False)
            root_y.title('Add Screen')
            root_y.geometry(root_y_geometry)
            """
            
           
            return None
        def _rename_evet():
            return None 
        m.add_command(label="add",command=_add_event)
        if (col_ != None):       
            
            m.add_command(label="rename")
            m.add_command(label="delete",command=_delete_event)

        def _menu_event(event): 
            try: 
                m.tk_popup(event.x_root, event.y_root) 
            finally: 
                m.grab_release() 
        label.bind("<Button-3>", _menu_event)

    def senior_add_screen(self):
        add_s_mh = int(self.MH2/4)
        root_geometry = str(int(self.MW2)) + 'x' + str(add_s_mh)
        self.root_add = tk.Tk()
        self.root_add.geometry(root_geometry)
        self.root_add.resizable(False, False)
        self.root_add.title('ADD') 
        self.assistant_title(root_title="add",y_=1,t_y_=10,heihgt___=add_s_mh)
         
        self.assistant_add_screen(y_=3)
        self.worker_add_button(self.root_add)
        #self.worker_add_screen(seq_row=1,total_row=5,seq_col=1,total_col=5,next_col=5,height_=add_s_mh)

        #name_entry.place(x=50, y=50)

        return None

    def assistant_add_screen(self,y_=1,t_y_=10,root_title ="add",heihgt___=None):
        add_value = {}  
        add_s_mh = int(self.MH2/4)
        buf_1 = len(self.json_X)
        buf_2=self.json_X[buf_1-1]
        print(buf_2)
        buf_3=int(buf_2['id'])+1
    
        buff_2=self.seq_x[self.seq_x[0]+1]
        left_indent = 1
        i=0
        k=0
        n = self.seq_x[i+1]
        
        
        for key_ in self.json_X[0].keys():  
            if key_=='id':
                self.worker_add_screen(seq_row=y_,total_row=t_y_,seq_col=n,total_col=buff_2,next_col=(self.seq_x[i+1]),col_=k,height_=add_s_mh,val__=buf_3,State_='readonly') 

            else:
                 self.worker_add_screen(seq_row=y_,total_row=t_y_,seq_col=n,total_col=buff_2,next_col=(self.seq_x[i+1]),col_=k,height_=add_s_mh,val__=key_) 

            n += self.seq_x[i+1]
            i+=1
            k+=1
            left_indent += 1
        
        return None
         
    def worker_add_screen(self,seq_row,total_row,seq_col,total_col,next_col,col_=None,height_=None,val__='',State_='normal'):
        
        font_x = 15 if self.MW2 >= 2000 else 10        
        self.ent_= ttk.Entry(self.root_add, font=("Helvetica", font_x),justify='center')
        BUFF1 = int((seq_row/total_row)*height_)
        BUFF2 = int((seq_col/total_col)*(self.MW2-200))
        
        buff=((next_col/total_col)*self.MW2)
        buff = ((buff)*0.8)
        
        self.ent_.place(x=BUFF2,y=BUFF1,width=buff,height=50)

        def change_val(event):
            None
           
        self.ent_.insert(0, val__)
        self. ent_.configure(state=State_)
        
        self.ent_.bind("FocusIn",change_val)
        self.test__[col_] = self.ent_

        
        
        return None

    def worker_page_button(self,_text,_func,**_place):
        
        _style = ttk.Style()
        _style.configure('my.TButton', font=('Helvetica', 20,'bold'))
        write_button = ttk.Button(
            self.root_x,
            text=_text,
            style='my.TButton',
            command=_func
            
        )
        
        write_button.place (_place )  

    def worker_add_button(self,roots_,**kws_):
        add_s_mh = int(self.MH2/4)
        #new_last = (int(kws_['id'])-1)
        buff_ = {}
        def click_button():
            
            b1=  len(self.json_X)
            b2 = self.json_X[b1-1]
            print(b2)
            b3=int(b2['id'])
            print(b3)
            
            k=0
            for j in self.json_X[0].keys():
                buff_[j] = self.test__[k].get()
                k +=1
            self.json_X.append(buff_)
            print(self.json_X)

            
            self.senior_screen()
            #print(test_)
            
            roots_.destroy()
            
            #self.json_X.append(kws_)
            for widget in self.root_x.winfo_children():
                widget.destroy()
            self.senior_screen()
            #print(self.json_X)
                

        
        add_button = ttk.Button(
            roots_,
            text='add',
            command=click_button
        )
        add_button_W = 200
        add_button_h = 100
        window_width = self.MW2
        window_height =add_s_mh
        x_position = (window_width // 2) - (add_button_W // 2)
        y_position =int( (window_height // 2) + (add_button_h // 5))
        add_button.place(x=x_position, y=y_position, width=add_button_W, height=add_button_h)

        return None

class db_control:
    def __init__(self,k):
        self._db = k
   
x = r'fake_data.json'
with open(x, 'r') as file:
    data = json.load(file)
y = ProgX(data)
y.main_start()
new_db = db_control(k=data)

