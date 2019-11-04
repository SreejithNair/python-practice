class CustomDic(dict):

    def __setitem__(self, key, value):
        print(f'adding hook if we wanted to do something before using actual dictionary set item')
        t = type(key)
        s = type(str)
        if(isinstance(key,str) == False):
            #just a sample hook to restrict string keys only
            raise KeyError("Invalid key type")
        dict.__setitem__(self,key,value)

    def __getitem__(self,key):
        dict.__getitem__(self,key)

c = CustomDic()
c['a']=70