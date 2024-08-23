"""
release notes:
Data transactions transferred to mongodb
"""
"""
hierarchy
main_start : home page
    -> main_screen : settings of the main screen
        -> senior_screen : page where data is displayed
            -> assistant_title() function where titles (keys) are printed
                -> worker_cell : function where the relevant label is printed.
            -> new_assistant_page function where data (values) are printed
                -> worker_cell
            -> new_assistant_page_info : page information : how many pages are there, which page are we on
                -> worker_cell
            -> mid_button_build : function where previous page - next page buttons are
                -> senior_screen : current page number is stored with a variable. When the previous or next button is pressed, this value is changed
                                   and the main page is reloaded.
                -> assistant_button_build : previous - next buttons
                    -> worker_page_button   
                    
        -> worker_cell 
            -> senior_delete_screen
                -> assistant_title
                -> new_assistant_page
            -> senior_add_screen
                -> assistant_title
                -> assistant_add_screen
                    -> worker_add_screen
                        ->  worker_cell
                -> worker_add_button            
            -> senior_renaem_screen


I wanted to create 4 stages.
    Worker: Function that provides direct access to the relevant widget. 
            It is defined to display the relevant widgets once.    
    Assistant: Worker manager function. If there is more than one of the same widget, 
               this function transfers the data to the worker.    
    mid : (wildcard privilege) A function that provides access to more than one different function.
    senior : Admin function. Data coming from a function containing a different type of widget is collected here.   
"""
import os

import json
import math
import random
import re
import tkinter as tk
from tkinter import DISABLED, END, Menu, StringVar, ttk,Entry
from tkinter.ttk import Label
from bson import ObjectId
from pymongo import MongoClient

from screeninfo import get_monitors # type: ignore
for monitor in get_monitors():
    print(f"Width: {monitor.width}, Height: {monitor.height}")

class ProgX:
    def __init__(self, z):
        self.widgets_ = []

        self.db_ = db_control(z)
        self.page = 1
        
        self.re_val_={}
        self.new_val_ = {}
        self.get_val = []
        
        self.root = tk.Tk()
        self.m_h = int((monitor.height-200)/4)
        self.m_w = int((monitor.width - 200)/4)
        root_geometry = str(self.m_w) + 'x' + str(self.m_h)
        self.root.geometry(root_geometry)

        self.MH2 = int((monitor.height-200))
        self.MW2 = int((monitor.width - 200))
      
#first screen.In the future the file will be selected here
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
        button_width = int(self.m_w/3.1418) 
        button_height = int(self.m_h/3.1418)
        window_width = self.m_w
        window_height = self.m_h

        x_position = (window_width // 2) - (button_width // 2)
        y_position = (window_height // 2) - (button_height // 2)
        write_button.place(x=x_position, y=y_position, width=button_width, height=button_height)
        
        self.root.mainloop()
   
#Basis screen settings. 
    def main_screen(self):
        self.prev =[]
        self.seq_x = self.db_.random_()
        """

seq_x is a randomly generated data. The first digit is the total number of key: value, 
 the remaining numbers in the middle give the length (len()) of the values ​​in a randomly taken data. 
 The last digit gives the sum of these values. Since I did not change the label widths on the screen externally, 
 I took a random data at the beginning of the program and adjusted the label lengths according to the value lengths. 
 Thinking that the key could be longer, I chose the longest one by making a comparison.
        seq_x[0] gives me the total number of key values.
seq_x[1+ seq[0]] (last digit) gives the total number of parts the page will be divided into.
example: Let there be 5 key values. 1. value character length (len()) 11;
2. value (len()) = 22;
3. value (len()) = 33;
4. value (len()) = 44;
5. value (len()) = 55;
in this case seq_x = [5,11,22,33,44,55,165]. I will divide the page by 165. 
I will give a label length of 11 for the 1st value, 22 for the 2nd value...
When assigning length to any label, I assign it as seq_x[1 + (x.column)]
        """
        root_geometry = str(self.MW2) + 'x' + str(self.MH2)
        
        self.root_x = tk.Tk()
        self.root_x.geometry(root_geometry)
        self.root_x.resizable(False, False)
        self.root_x.title('jsonS')
        self.senior_screen()
        
        self.root_x.mainloop()
      
#<senior screen> Basis screen. Data is printed on this screen. I don't want the window to close and open when I refresh the screen. 
# That's why I defined the screen settings in a different function. Only data is printed in this function.
    def senior_screen(self):
        self.prev =[]
        self.widgets_ = []

        self.assistant_title()
        buff = self.db_.page_query(20)
        buff2 = buff(self.page)
        buff3 = buff2[1]
        self.total_page = (buff2[0])


        self.new_assistant_page(buff3)
        self.new_assistant_page_info()
        #print(type(buff2))
        #print(buff(1)[1])
        self.mid_button_build()
        return None
        
#global title. Keys in data are printed on this screen
    def assistant_title(self,y_=1,t_y_=25,root_title ="show_list",heihgt___=None):
        
        title_num= 0
        buff3 = None
        buff_2=self.seq_x[self.seq_x[0]+1]
        left_indent = 1
        i=0
        n = self.seq_x[i+1]
        for key_ in self.db_.zero_index_().keys():  
            buff3 = "t_"+ str(title_num)
            self.worker_cell(key_,y_,t_y_,n,buff_2,(self.seq_x[i+1]),root_=root_title,height_=heihgt___,col_=buff3) 
            
            n += self.seq_x[i+1]
            i+=1
            left_indent += 1
            title_num += 1
        return None

    def new_assistant_page(self,kw_mp,roots_ = "show_list",heigh__ = None,test= 0):
        if heigh__ == None:
            heigh__ = self.MH2
        #print(kw_mp)
        #print(kw_mp)
        self.old_ = []

        k = 0
        i=0
        c = 0
        buff_2=self.seq_x[self.seq_x[0]+1] # seq 
        n = self.seq_x[i+1]
        col_num_ = len(self.seq_x)- 2 #num of col
        
        for new_line in kw_mp:
            #print(len(kw_mp))
            #print(type(new_line))
            i = 0
            n= self.seq_x[i+1]
            for new_col in new_line.keys():

                bff3 = "c_" + str(c)+ "_" 
                #print(bff3)
                self.worker_cell(val=new_line[new_col],
                                 #seq_row=(k%20)+2,
                                 seq_row=k+2,
                                 #total_row=len(kw_mp)+ 5,
                                 total_row=25,
                                 seq_col=n,
                                 total_col=buff_2,
                                 next_col=self.seq_x[i+1],
                                 #root_=self.db_.index_(k),
                                 root_=roots_,
                                 col_=bff3,
                                 height_=heigh__)
                                                          
                n += (self.seq_x[i+1])
                i += 1
                c += 1
  
            k += 1
            
        return None

    def new_assistant_page_info(self,root_page="show_list"):
        curr_page = list(self.total_page.keys())[0]
        total_page = list(self.total_page.values())[0]
        buff_1 = str(curr_page) + "-" + str(total_page)
        # 2 + 1 +2
        buff_2 = ((self.MW2/2)-(len(buff_1)/2))
        self.worker_cell(buff_1,23,25,buff_2,self.MW2,200,root_=root_page)

    def mid_button_build(self):

        curr_page = list(self.total_page.keys())[0]
        total_page = list(self.total_page.values())[0]
        if(total_page)< (self.page):
            bff = self.page - total_page
            self.page = self.page - bff
            for widget in self.root_x.winfo_children():
                widget.destroy()
            self.senior_screen()            
            None

        def _func_next(k):
      
            if (total_page)>= (self.page):     
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
                print("hataa")
                return None
        
            for widget in self.root_x.winfo_children():
                widget.destroy()
            self.senior_screen()
       
            return None
        for i in range (3):
            if (total_page)>= (self.page+i+1):
            #if (int(self.db_.len_db()))>= ((self.page+i+1)*20):                 
                self.assistant_button_build(23,((self.MW2/2)+((i+1)*100)),(">"*(i+1)),w_func=lambda i=i : _func_next(i+1))
                
        for j in range (3):
            if ((self.page-j-2)*20)>= 0:                            
                self.assistant_button_build(23,((self.MW2/2)-((j+1)*100)-100),("<"*(j+1)),w_func=lambda j=j : _func_prev(j+1))
                
        return None

    def assistant_button_build(self,_col,_recess,_val,w_func):
        _style = {
        "x" :_recess,            
        #"x" :((self.MW2/2)+50),
        "y" : ((_col/25)*(self.MH2)),
        "width": (20 if self.MW2 <2000 else 30) + (len(_val)*20),
        "height": 40 if self.MH2 < 1200 else 50
        }
        #print (self.MH2)
        self.worker_page_button(_val,w_func,**_style)

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

    def worker_cell(self,val,seq_row,total_row,seq_col,total_col,next_col,root_,bg_ = "white",col_=None,height_=None):
        r_click = False
        total_ = self.seq_x[0]
        if height_ == None:
            height_= self.MH2
        
        if root_=="show_list":
             root__ = self.root_x
        elif root_ =="add":
            root__ = self.root_add
        elif root_ =="delete":

            root__ = self.root_delete
        elif root_ == "rename":
            root__ = self.root_rename
        else:
            root__ = self.root_x
        font_x = 15 if self.MW2 >= 2000 else 12
        _label = tk.Label(root__, text=val, font=("Helvetica", font_x),bg= bg_,name=col_,)
        BUFF1 = int((seq_row/total_row)*height_)
        BUFF2 = int((seq_col/total_col)*(self.MW2-200))

        _label.configure()
        buff=((next_col/total_col)*self.MW2)
        buff = ((buff)*0.8)
        self.MH2
        _label.place(x=BUFF2,y=BUFF1,width=buff,height=(30 if self.MW2 <2000 else 50))
        self.widgets_.append(_label)
        if root_=="show_list":
            #print(self.prev)
            def _delete_event():
                self.senior_delete_screen(self.prev)
                return None
            def _add_event():
                self.senior_add_screen()
                return None
            def _rename_event():
                self.senior_rename_screen(self.prev)
                return None 

            _places=[]
            _right_menu = tk.Menu(_label,tearoff=0)
            _right_menu.add_command(label="ADD",command=_add_event)
            if True:
                None
            _right_menu.add_command(label="RENAME",command=_rename_event)
            _right_menu.add_command(label="DELETE",command=_delete_event)
            
            def _curr(__bg):
    
                _current= []
                t_col_ = r'c_(\d+)_'            
                current_name = _label.winfo_name() 

                search_ = re.search(t_col_, current_name)
                res_ =search_.group(1)if search_ else None
                if res_ is not None:

                    res_ = int(res_)
                    for j in  range (total_):
                        _x,_y = divmod(res_,total_)
                                
                        current_col = (((_x)*total_)+j)
                        current_col = 'c_' + str(current_col) + '_'
                        _places.append(current_col)
                else:
                    None 
                for x_ in self.widgets_:

                    if x_.winfo_name() in _places:
                        _current.append(x_)

                    None
                for c_ in _current:
                    c_.configure(bg =__bg)
                    
                if self.prev == _current.copy():
                    return
                else:
                    self.prev = _current.copy()
                    #print(_current)
                    None       
                    
            def _lineout_out(event):
                    if r_click == True:
                        #print("motion çalışıyor")
                        None           
                    else:    
                        _curr("#C4D6A6")
                        None

            def _leave(event):
                if r_click == True:
                    None
                else:
                    _curr("white")
                    None
                    
            def _right_click(event):
                _right_menu.post(event.x_root, event.y_root)
    
            _label.bind("<Motion>",_lineout_out)
            _label.bind("<Leave>",_leave)   
            _label.bind("<Button-3>", _right_click)

    def senior_rename_screen(self,_current_r):
        add_s_mh = int(self.MH2/4)
        root_geometry = str(int(self.MW2)) + 'x' + str(add_s_mh)
        self.root_rename = tk.Tk()
        self.root_rename.geometry(root_geometry)
        self.root_rename.resizable(False, False)
        self.root_rename.title('RENAME') 
        self.assistant_title(root_title="rename",y_=1,t_y_=10,heihgt___=add_s_mh)
        self.assistant_rename_screen(old_val=_current_r,y__=3)
        self.worker_rename_button(self.root_rename)

        def unauthorized_exit(self):
            self.root_rename.destroy()
            for widget in self.root_x.winfo_children():
                widget.destroy()
            self.senior_screen()
            
        self.root_rename.protocol("WM_DELETE_WINDOW", lambda: unauthorized_exit(self))        
        
        return None

    def assistant_rename_screen(self,old_val,y__=1,t_y__=10,root_title_ ="rename",heihgt____=None):
        new_value = {}       
        add_r_mh = int(self.MH2/4)
        add_s_mh = int(self.MH2/4)
        #buf_1 = int(self.db_.len_db())
        # buf_1 = self.db_.last_()[0]['id']
        # #buf_2=self.db_.index_(buf_1-1)
        # buf_2 = self.db_.last_()[0]
        # #print(old_val)
        buff = {}
        _list = []
        j = 0
        for i in (self.db_.zero_index_().keys()):
            buff[i] = old_val[j].cget("text")
            j += 1
        _list.append(buff)
        #print(_list)
    
        buff_2=self.seq_x[self.seq_x[0]+1]
        left_indent = 1
        i=0
        k=0
        n = self.seq_x[i+1]
        (_list[0])
        
        for key_ in _list[0].keys():  
            if key_=='id':
                val_ = _list[0][key_]
                self.worker_rename_screen(seq_row=y__,total_row=t_y__,seq_col=n,total_col=buff_2,next_col=(self.seq_x[i+1]),col_=k,height_=add_s_mh,val__=val_,State_='readonly') 

            else:
                val___ = _list[0][key_]

                self.worker_rename_screen(seq_row=y__,total_row=t_y__,seq_col=n,total_col=buff_2,next_col=(self.seq_x[i+1]),col_=k,height_=add_s_mh,val__=val___) 

            n += self.seq_x[i+1]
            i+=1
            k+=1
            left_indent += 1
           
        return None
    
    def worker_rename_screen(self,seq_row,total_row,seq_col,total_col,next_col,col_=None,height_=None,val__='',State_='normal'):
        
        font_x = 15 if self.MW2 >= 2000 else 10        
  
        self.ren_= ttk.Entry(self.root_rename, background="red",font=("Helvetica", font_x),justify='center')
        BUFF1 = int((seq_row/total_row)*height_)
        BUFF2 = int((seq_col/total_col)*(self.MW2-200))
        
        buff=((next_col/total_col)*self.MW2)
        buff = ((buff)*0.8)
        
        self.ren_.place(x=BUFF2,y=BUFF1,width=buff,height=(50 if self.MW2 > 2000 else 30))         
           
        self.ren_.insert(0, val__)
        self. ren_.configure(state=State_)
        
        self.re_val_[col_] = self.ren_
             
        return None
    
    def worker_rename_button(self,root_r):
        add_s_mh = int(self.MH2/4)

        def click_button():
            buff_ = {}
            k=0
            
            for i in self.db_.zero_index_().keys():
                if i =='id':
                    buff_[i] = int(self.re_val_[k].get())
                else:
                    buff_[i] = self.re_val_[k].get()
                    
                k +=1
            bff_ = int((list(buff_.values()))[0])
            
            self.db_.rename_(id_r=bff_,**buff_)

            #print(test_)
            
            root_r.destroy()
            
            #self.json_X.append(kws_)
            for widget in self.root_x.winfo_children():
                widget.destroy()
            self.senior_screen()
    
            return None
            
        add_button = ttk.Button(
            root_r,
            text='RENAME',
            command=click_button
        )
        add_button_W = 200 if self.MW2 > 2000 else 160
        add_button_h = 100 if self.MH2 > 1000 else 50
        window_width = self.MW2
        window_height =add_s_mh
        x_position = (window_width // 2) - (add_button_W // 2)
        y_position =int( (window_height // 2) + (add_button_h // 5))
        add_button.place(x=x_position, y=y_position, width=add_button_W, height=add_button_h)
        
        return None

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
        def unauthorized_exit(self):
 
            self.root_add.destroy()

            for widget in self.root_x.winfo_children():
                widget.destroy()
            self.senior_screen()
            
        self.root_add.protocol("WM_DELETE_WINDOW", lambda: unauthorized_exit(self))
        
        return None

    def assistant_add_screen(self,y_=1,t_y_=10,root_title ="add",heihgt___=None):
        add_value = {}  
        add_s_mh = int(self.MH2/4)
        #buf_1 = int(self.db_.len_db())
        last_document_ = list(self.db_.collection_.find().sort('id', -1).limit(1))[0]
        buf_1 = int(last_document_['id'])
        
        #buf_2=self.db_.index_(buf_1-1)
        
        #buf_3=int(buf_2['id'])+1
        buf_3 = buf_1+1
        
        buff_2=self.seq_x[self.seq_x[0]+1]
        left_indent = 1
        i=0
        k=0
        n = self.seq_x[i+1]        
        
        for key_ in self.db_.zero_index_().keys():  
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
  
        self.ent_= ttk.Entry(self.root_add, background="red",font=("Helvetica", font_x),justify='center')
        BUFF1 = int((seq_row/total_row)*height_)
        BUFF2 = int((seq_col/total_col)*(self.MW2-200))
        
        buff=((next_col/total_col)*self.MW2)
        buff = ((buff)*0.8)
        
        self.ent_.place(x=BUFF2,y=BUFF1,width=buff,height=(50 if self.MW2 > 2000 else 30))         
           
        self.ent_.insert(0, val__)
        self. ent_.configure(state=State_)
        
        self.new_val_[col_] = self.ent_
        
        return None

    def worker_add_button(self,roots_,**kws_):
        add_s_mh = int(self.MH2/4)
        #new_last = (int(kws_['id'])-1)
        buff_ = {}
        def click_button():
            k=0
            for j in self.db_.zero_index_().keys():
                if j =='id':
                    buff_[j] = int(self.new_val_[k].get())
                else:
                    buff_[j] = self.new_val_[k].get()
                k +=1
            self.db_.add_(buff_)

            #print(self.json_X)
            
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
        add_button_W = 200 if self.MW2 > 2000 else 160
        add_button_h = 100 if self.MH2 > 1000 else 50
        window_width = self.MW2
        window_height =add_s_mh
        x_position = (window_width // 2) - (add_button_W // 2)
        y_position =int( (window_height // 2) + (add_button_h // 5))
        add_button.place(x=x_position, y=y_position, width=add_button_W, height=add_button_h)

        return None

    def senior_delete_screen(self,_current_val):
        add_s_mh = int(self.MH2/4)
        root_geometry = str(int(self.MW2)) + 'x' + str(add_s_mh)
        self.root_delete = tk.Tk()
        self.root_delete.geometry(root_geometry)
        self.root_delete.resizable(False, False)
        self.root_delete.title('DELETE') 
        self.assistant_title(root_title="delete",y_=1,t_y_=10,heihgt___=add_s_mh)
        buff = {}
        _list = []
        j = 0
        for i in (self.db_.zero_index_().keys()):
            buff[i] = _current_val[j].cget("text")
            j += 1
        _list.append(buff)
        #print(_current_val[0].cget("text"))
       
        bff_ = (int(_current_val[0].cget("text")))
        
        self.new_assistant_page(_list,roots_="delete",heigh__=self.MH2)
        self.worker_delete_button(self.root_delete,_id = bff_ )

        def unauthorized_exit(self):
 
            self.root_delete.destroy()

            for widget in self.root_x.winfo_children():
                widget.destroy()
            self.senior_screen()
            
        self.root_delete.protocol("WM_DELETE_WINDOW", lambda: unauthorized_exit(self))
        
        return None

    def worker_delete_button(self,root_d,_id):
        def click_delete():
            self.db_.val_delete(_id)
 
            self.root_delete.destroy()

            for widget in self.root_x.winfo_children():
                widget.destroy()
            self.senior_screen()
         
            return None
        add_d_mh = int(self.MH2/4)
        delete_button = ttk.Button(
            root_d,
            text='DELETE',
            command=click_delete
        )        
        delete_button_W = 200 if self.MW2 > 2000 else 160
        delete_button_h = 100 if self.MH2 > 1000 else 50
        window_width = self.MW2
        window_height =add_d_mh
        x_position = (window_width // 2) - (delete_button_W // 2)
        y_position =int( (window_height // 2) + (delete_button_h // 5))
        delete_button.place(x=x_position, y=y_position, width=delete_button_W, height=delete_button_h)
        return

class db_control:
    def __init__(self,db_s):
        self.db_check(db_s)
        return None
    
    def len_db(self):
        return  self.collection_.count_documents({})
    
    def val_delete(self,id_d):
        try:
            self.collection_.delete_one({"id": id_d})
        except:
            return False
        else:
            return True        
        # t_ = self.id_query(id_d)
        # if t_ != None:
        #     t = self.db_[t_]
        #     self.db_.remove(t)    
        #     x_ = r'fake_data.json'
        #     with open(x_, 'w') as file:
        #         json.dump(self.db_, file,indent=2)
 
    def rename_(self,id_r,**kwr):
        
        self.collection_.update_one(
            {"id": id_r}, 
            {"$set": kwr}  
            )        
        # bff = self.id_query(id_r)
        # bff2 = self.val_check(kwr)
        
        # if (bff != None) and bff2 :
            
        #     self.db_[bff] = kwr
        #     x_ = r'fake_data.json'
        #     with open(x_, 'w') as file:
        #         json.dump(self.db_, file,indent=2)
                
        # else:
        #     print("yapçak birşey yok")
            
        #     return None
        return None
    
    def add_(self,val_new):
        new_ = self.val_check(val_new)
        if new_ != None:
            self.collection_.insert_one(val_new)
            

        # x_ = r'fake_data.json'
        # with open(x_, 'w') as file:
        #     json.dump(self.db_, file,indent=2)
            #print(self.db_)
        None
 
    def val_check(self,val_control):

        try:
            if (len(val_control.keys()) != len(self.zero_index_().keys())) or (len(val_control.keys()) != len(self.zero_index_().keys())):
                raise ValueError("eksi veri")                    
        except AttributeError as e:
            print("Hatalı veri")
            print(e)
            return False
        except ValueError as e:
            return False
        else:
            return True
        #return val_control   
    
    def page_query(self,num_of_data_):
        result=[]
        data_len = self.len_db()
        page_piece =   math.ceil(data_len  /num_of_data_)
        #print(page_piece)
        def page_(page_=1):
            bff ={}
            bff [page_] = page_piece
            result.append(bff)
            bbf2 =[]
            result_ = self.collection_.find().skip((page_-1)*20).limit(20)
            #print(result_)
            #ress_ = self.custom_(result_)
            

            
            result.append(self.custom_(result_))
            return result
        return page_

    def random_(self):
        j_buff=random.randint(1,self.len_db())
        document = self.collection_.find_one({"id": j_buff})

        JOKER = self.custom_((document))
        
        return self.det_size(JOKER)

    def zero_index_(self):
        
        res_=  (self.custom_(self.collection_.find_one({"id": 1})))

        return(res_)

    def det_size(self,seq_q):
        def random_len(seq_x):    
            det =[]        
            for i in seq_x.keys():
                buff_1 = len(str(seq_x[i]))
                det.append(buff_1) 
            #print(det)
            return tuple(det)  
        def title_len(seq_x):    
            det =[]        
            for i in seq_x.keys():
                buff_1 = len(str(i))
                det.append(buff_1) 
            #print(det)
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

    def index_(self,x_):
        return self.db_[x_]
        
    def custom_(self,news_val):
        bff_ = []
        result_ = []
        if type(news_val) == dict:

            bff_ = {}
            for x_ in news_val.items():
                if x_[0] == "_id":
                    pass
                else:
                    bff_[x_[0]] = x_[1]
            return bff_
        else:       
            for i in news_val:
                
                bff = {}
                for j in i.items():
            
                    if j[0] =="_id":
                        pass
                    else:
                        bff[j[0]] = j[1]
                        pass
                bff_.append(bff)

        #print(bff_)
        return bff_

    def last_(self):
        
        try:
            highest_id_document_cursor = self.collection_.find().sort('id', -1).limit(1)
        except:
            print("hata")
                    
        return list(highest_id_document_cursor)

    def db_check(self,db_x):
        x = r'fake_data.json'
        with open(x, 'r') as file:
            data = json.load(file)
        client_ = db_x
        db_name = 'ProgX'
        collect_name = 'ProgX_collect'
        db_ = client_[db_name]
        self.collection_ = db_[collect_name]
        if collect_name not in db_.list_collection_names():
            self.collection_.insert_many(data)
        return None

final_prog = ProgX(MongoClient('localhost', 27017))
final_prog.main_start()