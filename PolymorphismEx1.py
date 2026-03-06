#PolymorphismEx1.py
#Here methods are same but methods body are different
class Circle:
    def draw(self):#Original method
        print("Drawing Circle")
class Rect(Circle):
    def draw(self): #Overridden method
        print("Drawing Rectangle")
        super().draw() #Preeceeded with super()
#Main program
r=Rect()
r.draw()