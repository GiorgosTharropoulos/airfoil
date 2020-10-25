import math
import matplotlib.pyplot as plt


coordinates = open("naca0012.txt", "r")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"x: {self.x}, y: {self.y}"


class Element:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

    def length(self):
        return math.sqrt(
            (self.node1.x - self.node2.x) ** 2
            + (self.node1.y - self.node2.y) ** 2
        )

    def angle(self):
        dx = self.node2.x - self.node1.x
        dy = self.node2.y - self.node1.y
        return math.degrees(math.atan(dx / dy))

    def plot(self):
        plt.plot([self.node1.x, self.node2.x], [self.node1.y, self.node2.y])
        plt.show()


if __name__ == "__main__":
    points = [Point(0, 1), Point(0, 3)]

    p1 = Point(2, 6)
    p2 = Point(5, 7)
    elmnt1 = Element(p1, p2)

    print(elmnt1.length())
    print(elmnt1.angle())

    elmnt1.plot()
