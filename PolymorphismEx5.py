#PolymorphismEx5.py
#Whatever the Inheritance written first will came into the picture only.
#By using class name approach
class Circle:
    def draw(self):#Original method
        print("Drawing Circle")
class Rect:
    def draw(self): #Original method
        print("Drawing Rectangle")
class Square(Circle,Rect):
    def draw(self): #Overridden method
        print("Drawing Square")
        super().draw()
       ## super().draw()==>>It is not possible to call draw() of rect class
        Rect.draw(self) #Possible with class name approach
#Main program
s=Square()
s.draw()