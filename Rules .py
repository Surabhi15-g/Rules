#  Constants in UPPER_CASE
PI = 3.14159
MAX_USERS = 100

#  Class in PascalCase
class Circle:
    #  Constructor method with snake_case parameters
    def __init__(self, radius):
        self.radius = radius  #  Instance variable in snake_case

    #  Method in snake_case
    def calculate_area(self):
        return PI * self.radius ** 2

#  Variable name is meaningful and uses snake_case
user_radius = 5

#  Create an object using a meaningful name
my_circle = Circle(user_radius)

#  Use descriptive function name and print result
area = my_circle.calculate_area()
print("Area of the circle:", area)
