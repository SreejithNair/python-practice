  
        # Python class can be multiple inheritance (from more then one base class)
        # Or multi-level inheritance ( more than one indirect base classes)
        # The MRO method on Type will tell you how the hierarchy is been called or looked up
        # Python perform a depth-first searching approach this means
        # class D(C, B) inheritance style will first look-up at D, then C, and any base of C.
        # If C and B share same instance then the check will terminate. Now the search will be
        # performed on B and upto all bases on B and finally the object as the super class of all.
        # class D(C, B): call hierarchy [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
        # class D(B, C): # call hierarchy [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>]

        # So the order of placing base classes matters when perform a lookup for a method or attribute in the 
        # inheritance chain

class A(object):
    def print_me(self):
        print('I am from A')

class B(A):
    pass

class C(object):
    def print_me(self):
        print('I am from C')

# class D(C, B): # call hierarchy [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
    #pass

class D(B, C): # call hierarchy [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>]
    pass
if __name__ == "__main__":
    print(D.mro())
    d = D()
    d.print_me()