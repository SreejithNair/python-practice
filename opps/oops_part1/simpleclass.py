#Simple class definition

class Shape:
    
    def __init__(self):
        pass
    def __str__(self):
        return  f'Shape class instance with height {self.height} and width {self.width}'
    def set_coordinates(self,height,width):
        self.height=height
        self.width=width

ins = Shape()
ins.set_coordinates(10,20)

