class A:
    def __init__(self):
        print("parrent class A ")
    def display1(self):
        print('hello display1 ')

    def display2(self):
        print('hello display2')

    def display3(self):
        print('hello display3')

class B(A):
    def __init__(self):
        super().__init__()
        print('child class B')
       
    def display4(self):
        print('hello display3')

class C(B):
    def __init__(self):
        super().__init__()
        print('child class')
       
    def display5(self):
        print('hello display3')

obj1 = B()
obj2=C()      
