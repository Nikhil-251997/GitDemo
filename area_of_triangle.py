"""
When all the length of the triangle is known - a, b, c
Semi parameter(s) = (a+b+c)/2
Area = Square root of (s * (s-a) * (s-b) * (s-c))
"""
a = float(input("enter first side: "))
b = float(input("enter second side: "))
c = float(input("enter third side: "))
s = (a+b+c) / 2
area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
print("Area of triaangle with given sides", round(area, 2))

