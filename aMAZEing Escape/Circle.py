print("What is the type of measurement?   ", "\n", "\t", "Press 1 for Radius", "\n", "\t", "Press 2 for Diameter", "\n", "\t","Press 3 for Circumference")

class Circle:
    def __init__(self, radius):
        self.radius = Radius

    def Circle_area(self):
        return radius ** 2 * 3.14159

    measurement = int(input("Select the given measurement type:  "))
    if measurement == 1:
        #measurement = int(input("Enter the value: "))

        print(f"The area of the circle is:  (circle.Circle_area)')

    elif measurement == 2:
        #measurement = int(input("Enter the value: "))
        print("The area of the circle is:" + " ", +  circle.Circle_area / 2)

    else:
        print("Select a valid option")


radius = int(input("Enter the value: "))
circle = Circle(radius)
circle.Circle_area()

