"""
release notes:
n1 : An attempt was made to transform the system into a 
query-answer system by adding the DB control class and query functions.

n2 :"mid page" has been replaced with "new mid page".

n3:"worker det size" was deleted. It was added into db control.
"""
"""

main_start : giriş sayfası
    -> main_screen : ana ekranın ayarları
        -> senior_screen : verilerin  gösterildiği sayfa
            -> assistant_title() başlıkların (key lerin) yazdırıldığı fonksiyon
                ->  worker_cell : ilgili labelin yazdıırldığı fonksiyon.
            -> new_assistant_page verilerin (value lerin) yazdırıldığı fonksiyon
                ->  worker_cell
            -> new_assistant_page_info : sayfa bilgileri : kaç sayfa var, kaçıncı sayfadayız
                ->  worker_cell            
            -> mid_button_build : önceki sayfa - sonraki sayfa butonların olduğu fonksiyon
                ->  senior_screen : geçerli sayfa numarası bir değişken ile saklanıyor. Önceki ve ya sonraki butonuna basıldınca bu değer değiştirilir
                                   ve ana sayfa tekrar yüklenir.
                ->  assistant_button_build : önceki - sonraki butonları
                    ->  worker_page_button : buton ayarlarının tanımlandığı fonksiyon
        ->  senior_add_screen : veri ekleme sayfası
            ->  assistant_title : 
            ->  assistant_add_screen :
                ->  assistant_add_screen :
                    ->  worker_add_screen :
            ->  worker_add_button  :

"""
import os

import json
import math
import random
import re
import tkinter as tk
from tkinter import DISABLED, END, Menu, StringVar, ttk,Entry
from tkinter.ttk import Label

from screeninfo import get_monitors # type: ignore
for monitor in get_monitors():
    print(f"Width: {monitor.width}, Height: {monitor.height}")


class ProgX:
    def __init__(self, z):
        self.widgets_ = []

        self.db_ = db_control(z)
        self.page = 1
        
        self.new_val_ = {}
        self.get_val = []
        
        self.root = tk.Tk()
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
      
    def senior_screen(self):
        self.prev =[]
        self.widgets_ = []

        self.assistant_title()
        buff = self.db_.page_query(20)
        buff2 = buff(self.page)[1]
        self.new_assistant_page(buff2)
        self.new_assistant_page_info()
        #print(type(buff2))
        #print(buff(1)[1])
        self.mid_button_build()
        return None
        
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

    def new_assistant_page(self,kw_mp,roots_ = "show_list",heigh__ = None):
        if heigh__ == None:
            heigh__ = self.MH2
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
                                 total_row=len(kw_mp)+ 5,
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

    def new_assistant_page_info(self):
        bff = self.db_.page_query(20)
        bff2 = bff()[0]
        #print(bff2.values())
        #print(bff2)
        for i in bff2:
           # print(i)
          
            return None

        return None

    def mid_button_build(self):
    
        def _func_next(k):
      
            if (int(self.db_.len_db()))>= ((self.page+k)*20):     
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
            if (int(self.db_.len_db()))>= ((self.page+i+1)*20):                 
                self.assistant_button_build(23,((self.MW2/2)+((i+1)*100)),(">"*(i+1)),w_func=lambda i=i : _func_next(i+1))
                
        for j in range (3):
            if ((self.page-j-2)*20)>= 0:                            
                self.assistant_button_build(23,((self.MW2/2)-((j+1)*100)-100),("<"*(j+1)),w_func=lambda j=j : _func_prev(j+1))
                
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
        "width": (20 if self.MW2 <2000 else 30) + (len(_val)*20),
        "height": 40 if self.MH2 < 1200 else 50
        }
        #print (self.MH2)
        self.worker_page_button(_val,w_func,**_style)

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
                return None 

            _places=[]
            _right_menu = tk.Menu(_label,tearoff=0)
            _right_menu.add_command(label="ADD",command=_add_event)
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
                        None    
                        _curr("#C4D6A6")

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
            
            #self.json_X.append(kws_)
 

            #print("test")
            
        self.root_add.protocol("WM_DELETE_WINDOW", lambda: unauthorized_exit(self))
        
        #self.worker_add_screen(seq_row=1,total_row=5,seq_col=1,total_col=5,next_col=5,height_=add_s_mh)

        #name_entry.place(x=50, y=50)

        return None

    def assistant_add_screen(self,y_=1,t_y_=10,root_title ="add",heihgt___=None):
        add_value = {}  
        add_s_mh = int(self.MH2/4)
        buf_1 = int(self.db_.len_db())
        buf_2=self.db_.index_(buf_1-1)
        buf_3=int(buf_2['id'])+1
    
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
        
        self.new_assistant_page(_list,roots_="delete",heigh__=add_s_mh)
        self.worker_delete_button(self.root_delete,_id = bff_ )
        
         

        def unauthorized_exit(self):
 
            self.root_delete.destroy()

            for widget in self.root_x.winfo_children():
                widget.destroy()
            self.senior_screen()
            
            #self.json_X.append(kws_)
 

            #print("test")
            
        self.root_delete.protocol("WM_DELETE_WINDOW", lambda: unauthorized_exit(self))
        
        #self.worker_add_screen(seq_row=1,total_row=5,seq_col=1,total_col=5,next_col=5,height_=add_s_mh)

        #name_entry.place(x=50, y=50)

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
        self.db_ = db_s
        
    def len_db(self):
        return len(self.db_)
    
    def val_delete(self,id_d):
        t = self.id_query(id_d)
        t = self.db_[t]
        self.db_.remove(t)    

        return None
    
    def val_query_(self,val_q):
#Searches for values ​​in dicts. Returns the results it finds.
        result = []
        for i in self.db_:
            for j in i:
                try:
                    if i[j] == val_q:
                        #bff ={}
                        #bff[j] = i[j]    
                        #print(bff)
                        
                        result.append({j: i[j] for j in i})
                        #print (i) 
                        None
                    else :
                        #raise ValueError("hataaa")
                        None
                except ValueError:
                    #print("hata var")
                    None
                #print(i[j])
                
        if result ==[]:
            return None
        
        else: 
            return result
       
    def id_query(self,id_):
        result = None
        for i in self.db_:
            
            try:
                if i["id"] == id_:
                        #bff ={}
                        #bff[j] = i[j]    
                        #print(bff)
                    #print(self.db_.index(i))
                    result = (self.db_.index(i))
                        #print (i) 
                    None
                else :
                        #raise ValueError("hataaa")
                    None
            except ValueError:
                    #print("hata var")
                None
                                
        if result ==[]:
            return None
        
        else: 
            #print("bulduk bulduk bulduk")
            return result
     
    def key_val_query(self,**kws):
#key:values ​​search is performed
        result = []
        for i in self.db_:
            for j in i:
                try:
                    buff={}
                    buff[j] = i[j]
                    if buff == kws:
                        result.append({j: i[j] for j in i})                        
                    else:
                        None
                except ValueError:
                    #print("hata var")
                    None
                #print(i[j])
        if result ==[]:
            return None
        else: 
            #print("bulduk bulduk bulduk")
            return result
    
    def rename_(self,id_r,**kwr):
        bff = self.id_query(id_r)
        bff2 = self.val_check(kwr)
        
        if (bff != None) and bff2 :
            None
            self.db_[bff] = kwr
        else:
            print("yapçak birşey yok")
            return None
        return None
    
    def add_(self,val_new):
        new_ = self.val_check(val_new)
        if new_ != None:
            self.db_.append(val_new)
            #print(self.db_)
        None
 
    def val_check(self,val_control):
        try:
            if (len(val_control.keys()) != len(self.db_ [0].keys())) or (len(val_control.keys()) != len(self.db_ [0].keys())):
                raise ValueError("eksi veri")                    
        except AttributeError:
            print("Hatalı veri")
            return False
        except ValueError as e:
            return False
        else:
            return True
        #return val_control   
    
    def page_query(self,num_of_data_):
        result=[]
        data_len =len(self.db_)
        page_piece =   math.ceil(data_len  /num_of_data_)
        #print(page_piece)
        def page_(page_=1):
            bff ={}
            bff [page_] = page_piece
            result.append(bff)
            bbf2 =[]

            for i in range(((page_-1)*num_of_data_),(((page_)*num_of_data_))):
                #print(i)
                try:
                    self.db_[i]
                except AttributeError:
                    print("hata 1")
                    None
                except ValueError:
                    print("hata 2")
                    None
                except KeyError:
                    print("hata 3")
                except IndexError:
                    #print("hata 4")
                    None
                else:
                    #print(self.db_[i])
                    bbf2.append(self.db_[i])
                None
            result.append(bbf2)
            return result
        return page_

    def random_(self):
        j_buff=random.randint(1,len(self.db_))
    
        JOKER = self.db_[j_buff]
        
       
        
        
        return self.det_size(JOKER)

    def zero_index_(self):
        return self.db_[0]

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
x = r'fake_data.json'
with open(x, 'r') as file:
    data = json.load(file)
y = ProgX(data)
y.main_start()

