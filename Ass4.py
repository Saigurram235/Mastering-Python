class Box:
    def area(self):
        return self.width * self.height

    def __init__(self, width, height):
        self.width = width
        self.height = height


# Create an instance of Box.
x = Box(10, 2)
# Print area.
print(x.area())


''' Write a program to calculate distance so that it takes two Points (x1, y1) and (x2, y2) as arguments and displays the calculated distance, using Class. '''

#
# class Distence:
#
#     def __init__(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.y1 = y1.x
#         self.x2 = x2
#         self.y2 = y2
#
#     def length(self):
#         return (((self.x2 - self.x1)**2) + ((self.y2 - self.y1)**2))**(0.5)
#
#
# x = input().split(' ')
# x1 = int(x[0])
# y1 = int(x[1])
# y = input().split(' ')
# x2 = int(y[0])
# y2 = int(y[1])
# x = Distence(x1, y1, x2, y2)
# print(x.length())


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "x-value: " + str(self.x) + " y-value: " + str(self.y)

    def __add__(self, other):
        self.x = self.x+other.x
        self.y = self.y+other.y
        return self


p1 = Point(3,4)
p2 = Point(2,3)
print (p1+p2)