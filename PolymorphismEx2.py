#PolymorphismEx2.py
#By using super()
class Circle:
    def draw(self):#Original method
        print("Drawing Circle")
class Rect(Circle):
    def draw(self): #Overridden method
        print("Drawing Rectangle")
        super().draw()
class Square(Rect):
    def draw(self): #overrridden method
        print("Drawing Square")
        super().draw()
#Main program
s=Square()
s.draw()