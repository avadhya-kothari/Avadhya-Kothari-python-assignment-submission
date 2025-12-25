"""
ci = A - P
Amount(A) = P * (1 + R/100) ** T
"""

p = float(input("Enter the principal: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time duration: "))
Amount1 = p * (1 + r/100) ** t
Amount2 = p * pow((1 + r/100), t)
print(Amount1, Amount2, sep=" and ")
ci = Amount1 - p
print("The compound interest is ", round(ci))