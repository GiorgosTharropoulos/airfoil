import math

coordinates = open("naca0012.txt", "r")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def x_angle(self, other):
        pass

    def __repr__(self) -> str:
        return f"x: {self.x}, y: {self.y}"


class Element:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.length = node1.distance(node2)


if __name__ == "__main__":
    points = [Point(0, 1), Point(0, 3)]
