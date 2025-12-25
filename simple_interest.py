"""
Simple Interest = ( P * R * T ) / 100
P = Principal amount
R = Rate of interest
T = time duration
"""

p = float(input("Enter the principal:"))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time duration: "))
si = (p * r * t) / 100
print("The Simple interest is ", si)
