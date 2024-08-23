import math
""" excercise for db control"""
test_x = [{"id": 1,"a":1,"b":1,"c":3},
          {"id": 2,"a":4,"b":5,"c":6},
          {"id": 3,"a":4,"b":5,"c":6},
          {"id": 4,"a":4,"b":5,"c":6},
          {"id": 5,"a":4,"b":5,"c":6},
          {"id": 6,"a":4,"b":5,"c":6},
          {"id": 7,"a":4,"b":5,"c":6},
          {"id": 8,"a":4,"b":5,"c":6},
          {"id": 9,"a":4,"b":5,"c":6},
          {"id": 10,"a":4,"b":5,"c":6},
          {"id": 11,"a":4,"b":5,"c":6},
          {"id": 12,"a":4,"b":5,"c":6},
          {"id": 13,"a":4,"b":5,"c":6},
          {"id": 14,"a":4,"b":5,"c":6},
          {"id": 15,"a":4,"b":5,"c":6},
          {"id": 16,"a":4,"b":5,"c":6},
          {"id": 17,"a":4,"b":5,"c":6},
          {"id": 18,"a":4,"b":5,"c":6},
          {"id": 19,"a":4,"b":5,"c":6},
          {"id": 20,"a":4,"b":5,"c":6},
          {"id": 21,"a":4,"b":5,"c":6},
          {"id": 22,"a":4,"b":5,"c":6},
          {"id": 23,"a":4,"b":5,"c":6},
          {"id": 24,"a":4,"b":5,"c":6},
          {"id": 25,"a":4,"b":5,"c":6},
          {"id": 26,"a":4,"b":5,"c":6},
          {"id": 27,"a":4,"b":5,"c":6},
          {"id": 28,"a":4,"b":5,"c":6},
          {"id": 29,"a":4,"b":5,"c":6},
          {"id": 30,"a":4,"b":5,"c":6},
          {"id": 31,"a":4,"b":5,"c":6},
          {"id": 32,"a":4,"b":5,"c":6},
          {"id": 33,"a":4,"b":5,"c":6},
          {"id": 34,"a":4,"b":5,"c":6},
          {"id": 35,"a":4,"b":5,"c":6},
          {"id": 36,"a":4,"b":5,"c":6},
          {"id": 37,"a":4,"b":5,"c":6},
          {"id": 38,"a":4,"b":5,"c":6},
          {"id": 39,"a":4,"b":5,"c":6},
          {"id": 40,"a":4,"b":5,"c":6},
          {"id": 41,"a":4,"b":5,"c":6},
          ]

class db_control:
    def __init__(self,db_s):
        self.db_ = db_s
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
            #print("bulduk bulduk bulduk")
            return result
       
    def id_query(self,id_):
#If the given id number is in the list, it returns the index number.
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
                
                #print(i[j])
                
        if result ==[]:
            return None
        
        else: 
            #print("bulduk bulduk bulduk")
            return result
     
        return None
        
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
            for i in range(((page_-1)*num_of_data_),(((page_)*num_of_data_))):
                bbf2= {}
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
        
class main_():
    
    def __init__(self):
        self.db_m = db_control(db_s=test_x)
        return None
    def test_(self):
        #print(self.db_m.val_query_(val_q=5))
        #buff ={}
        #buff["a"] = 1
        #print(buff)
        #print(self.db_m.key_val_query(**buff))
        #print(self.db_m.id_query(20))
        buff2 = {"id": 2,"a": 5,"b": 7,"c": 8}
        #print (buff2)
        self.db_m.rename_(2,**buff2)
        #self.db_m.add_({"id":5,"b":7,"c":8,'d':5})
        x = self.db_m.page_query(5)
        
        print(x())
        val_ = x()
        print(val_[0][1])
        self.db_m.val_delete(5)
        return None
x = main_()
x.test_()