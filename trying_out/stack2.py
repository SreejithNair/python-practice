class A():
      def __init__(self):
            pass

      def register_urc(self, text):
            print(text)

class B(A):
      def __init__(self):
            A.__init__(self)

class C():
      def __init__(self):
          pass
        
class Z(B, C):
      def __init__(self):
            B.__init__(self)
            C.__init__(self)

      def test(self):
          print("finished")

if __name__ == "__main__":
    z = Z()
    z.register_urc("Hello world")
    z.test()