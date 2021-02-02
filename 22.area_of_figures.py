import math
figure_type = str(input())
area = 0
if figure_type == "square":
    a = float(input())
    area = a * a 
elif figure_type == "rectangle":
    a = float(input())
    b = float(input()) 
    area = a * b
elif figure_type == "circle":
    r = float(input())
    area = math.pi * r**2
elif figure_type == "triangle":
    a = float(input())
    ha = float(input())
    area = a * ha / 2
print(f'{area:.3f}')
