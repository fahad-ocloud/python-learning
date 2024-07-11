class Vector:

    def __init__(self,x,y):
        print("hello I am Contructor")
        self.x = x
        self.y= y

    def __add__(self,other):
        return Vector(self.x + other.x , self.y + other.y)
    def __del__(self):
        print("hello i'm destructore")

    def __repr__(self):
        return f' x:{self.x} y:{self.y}'
    
    def  __len__(self):
        return 21


v1 = Vector(1,4)
v2 = Vector(3,4)
v3 = v1 + v2
print(v3)
print(len(v3))