class CustomDic(dict):
    def __setitem__(self, key, value):
        print(f'adding hook if we wanted to do something before using actual dictionary set item')
        t = type(key)
        if(key is not type(str)):
            #just a sample hook to restrict string keys only
            raise KeyError("Invalid key type")
        dict.__setitem__(self,key,value)
    def __getitem__(self,key):
        dict.__getitem__(self,key)
        
class CustomList(list):

    def __setitem__(self,index,value):
        if index == 0: raise IndexError
        if index > 0: index= index-1
        list.__setitem__(self, index, value)
    
    def __getitem__(self,index):
        if index == 0: raise IndexError
        if index > 0: index= index-1
        list.__getitem__(self,index)


c = CustomDic()
c['a']=5
c['b']=10
for k in c.keys():
    print(f'Key:{k} and Value:{c[k]}')
