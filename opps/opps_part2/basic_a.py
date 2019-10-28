
class CustomList(object):
    def __init__(self,max_size):
        self.max_size=max_size
        self.__inner_list=[]
    
    def push(self,item):
        if len(self.__inner_list) <= self.max_size:
            self.__inner_list.append(item)
        else:
            self.__inner_list.pop(0)
            self.__inner_list.append(item)
    
    def pop(self):
        return self.__inner_list

if __name__ == "__main__":
    c = CustomList(2)
    c1 = CustomList(1)
    c.push('Sree')
    c.push('Jith')
    c.push('Nair')
    c.push('Nair')
    c1.push('Sree')
    c1.push('Jith')
    c1.push('Nair')
    c1.push('Nair')
    print(c.pop())
    print(c1.pop())






