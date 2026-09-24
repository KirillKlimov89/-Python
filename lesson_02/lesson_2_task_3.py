import math


def square(side):
    area = side * side
    if side != int(side):
        return math.ceil(area)
    return area


side = 5.5
result = square(side)
print(f"Площадь квадрата со стороной {side}: {result}")