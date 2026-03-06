#PolymorphismEx.py
class Circle:
    def draw(self):
        print("Drawing Circle")
    def draw(self):
        print("Drawing Rectangle")
#Main program
c=Circle()
c.draw()
#This will call the latest one only.....