class A:
    def __init__(self):
        print("parrent class A ")

    # def display1(self):
    #     print('hello display1  A')

    def display2(self):
        print('hello display2')

    def display3(self):
        print('hello display3')

class B: 
    def display1(self):
        print('hello display3 B')

class C(A,B):
#    pass
    # def display1(self):
    #     print('hello display3 C')
       
    def display5(self):
        print('hello display3')


obj2=C()      
obj2.display1()