#PolymorphismEx4.py
#By using class name approach
class Circle:
    def draw(self):#Original method
        print("Drawing Circle")
class Rect(Circle):
    def draw(self): #Overridden method
        print("Drawing Rectangle")
class Square(Rect):
    def draw(self): #overrridden method
        print("Drawing Square")
        Circle.draw(self) ##This is called class name approach
#Main program
s=Square()
s.draw()