"""
When the length of the sides of triangle are known. i.e, a, b, c
semi perimeter (s) = (a + b + c) / 2
Area = square root of s * ( s - a ) * ( s - b ) * ( s - c )
Square root can be written as 1/2 or 0.5
"""

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))
s = ( a + b + c) / 2
area = ( s * ( s - a ) * ( s - b ) * ( s - c )) ** 0.5
print("The Area of the triangle is", area)

"""
To round off the value of output, We can use:
print("The Area of the triangle is", round(area, 2)) # Round offs to 2 after the decimal
"""