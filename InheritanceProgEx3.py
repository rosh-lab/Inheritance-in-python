#Program for demonstrating the need of inheritance
#InheritanceProgEx3.py
#Adding Data members and getting the output...
class C1:
    def getA(self):
        self.a=10
class C2:
    def getB(self):
        self.b=20
class C3(C1,C2):
    def operation(self):
        self.c=self.a+self.b
        print("Sum ({},{})---->{}".format(self.a,self.b,self.c))

#Main program
o3=C3()
o3.getA()
o3.getB()
o3.operation()