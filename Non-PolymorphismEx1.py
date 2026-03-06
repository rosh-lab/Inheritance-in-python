#Non-PolymorphismEx.py(Inheritance program)
class Circle:
    def draw1(self):
        print("Drawing Circle:")
class Rect(Circle):
    def draw2(self):
        print("Drawing Rectangle:")
#Main program
r=Rect()
r.draw1()
r.draw2()