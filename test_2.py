from bson import ObjectId
from pymongo import DESCENDING, MongoClient

#client = MongoClient('localhost', 27017)

class MongoDbConversion:
    def __init__(self,dbs_):
        client = dbs_
        db_ = client['admin']
        self.collection_ = db_['_new_collect']
        self.count = self.collection_.count_documents({})

  
    def get_(self):
        documents = self.collection_.find()

        # for doc in documents:
        #     print((doc))    
        document = self.collection_.find_one({"id": 2})
        #print(type(document))
 
        
        new_ = self.custom_(document)
        print(new_)
        #print(type(new_))
        #print(new_)
        
    def add_(self,new_val):
        self.collection_.insert_one(new_val)

        None
        
    def delete_by_id_(self,id_):
        try:
            self.collection_.delete_one({"id": id_})
        except:
            return False
        else:
            return True
        
    def renames_(self,id_r,**kwr):
        self.collection_.update_one(
            {"id": id_r}, 
            {"$set": kwr}  
            )
        return None
        
    def custom_(self,news_val):
        bff_ = []
        result_ = []
        if type(news_val) == dict:
            print("hata")
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

    def search_id(self,search_id):
        try:
            document = self.collection_.find_one({"id":search_id })
            None
        except:
            print("hata lo lo lo")
            return None
        else:
            try:
                bff = self.custom_(document)
            except:
                return None
            else:
                return bff

    def get_20(self,seq_):
        result_ = self.collection_.find().skip(seq_*20).limit(20)
        ress_ = self.custom_(result_)
        return ress_

    def last_(self):
        
        try:
            highest_id_document_cursor = self.collection_.find().sort('id', -1).limit(1)
        except:
            print("hata")
                    
        return list(highest_id_document_cursor)

c_ = MongoDbConversion(MongoClient('localhost', 27017))
abc_ = {
        'id': 1001, 
        'first_name': 'yusuf', 
        'last_name': 'test', 
        'email': 'test@salon.com', 
        'gender': 'male', 
        'ip_address': '192.64.174.141'
        }
#c_.get_()
c_.last_()
#res = c_.get_20(2)

#c_.write_(abc_)

