from math import sqrt

def found_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(found_distance(2, 2, 5, 5))