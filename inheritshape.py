import math

class Polygon:

    def __init__(self, ns, *sides):
        self.no_of_sides = ns
        self.sides = sides[:ns]


class Triangle(Polygon):

    def __init__(self, ns, *sides):
        Polygon.__init__(self, ns, *sides)

    def area(self):
        a, b, c = self.sides
        s = (a + b + c)/2
        area = math.sqrt(s * (s-a) * (s-b) * (s-c))
        return area


t1 = Triangle(8, 6, 15, 19, 2, 5, 8)
print('Area:', t1.area())
