class Point:
    def __init__(self, x: int, y:int):
        x = x
        y = y

    def set_x(self, new_x: int):
        x = new_x

    def set_y(self, new_y: int):
        y = new_y

    def __str__(self):
        return f'The point has coordinates ({x},{y})'


p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)
