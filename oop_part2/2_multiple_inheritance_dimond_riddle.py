# In a multiple-level inheritance / diamond problem
# D inherit from B and C, where B inherit from A and C inherit from A
# This is an ambiguity since B and C share same base class.
# In such case From D, it will travel upto B and then find A is been refereed in both B and C. so it will cut off
# the walk at B and then start from C and then walk up to A

#Class D(B,C) the MRO on D will give [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
#Class D(C, B) the MRO on D will give [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
class A(object):
    pass
class B(A):
    pass
class C(A):
    pass
class D(C,B):
    pass
# class D(B,C):
#     pass

if __name__ == "__main__":
    print(D.mro()) 