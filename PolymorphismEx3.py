#PolymorphismEx3.py
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
        Rect.draw(self) ## This is called Class name approach
        Circle.draw(self) ##This is called class name approach
#Main program
s=Square()
s.draw()