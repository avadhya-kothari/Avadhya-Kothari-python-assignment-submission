"""
Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
Expected Output:
The program should output a greeting like:

"""

name1 = input("Enter your first name: ")
name2 = input("Enter your last name: ")
full_name = name1 + " " + name2
print("Hello,", full_name + "! Welcome to python program.")