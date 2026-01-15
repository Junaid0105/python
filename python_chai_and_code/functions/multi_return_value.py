import math
def circle_stats(radius):
    area = round((math.pi * radius ** 2),2)
    circumference = round((2 * math.pi * radius),2)

    return area, circumference

ar, cir = circle_stats(7)
print("Area of a Circle : ", ar, "\nCircumference of a circle : ", cir)
