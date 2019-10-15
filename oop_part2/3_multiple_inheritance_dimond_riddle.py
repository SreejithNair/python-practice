#draw the inheritance diagram in a paper
#class F(E,D,C)-> MRO= [<class '__main__.F'>, <class '__main__.E'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
#class F(D,C,E)-> MRO= [<class '__main__.F'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.E'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

class A(object):
    pass
class B(A):
    pass
class C(A):
    pass
class D(B):
    pass
class E(B):
    pass
# class F(E,D,C):
#     pass
class F(D,C,E):
    pass
if __name__ == "__main__":
    print(F.mro()) 