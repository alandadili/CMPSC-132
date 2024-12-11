# Basic Python Programming Assignment_1
# Aland Adili

import math

# 1. WAP to take two different inputs from the user and swap it (Perform the task 1 using multiple assignment).

# input1 = input("Enter Input 1 ")  # input 1
# input2 = input("Enter Input 2 ")  # input 2

# input1, input2 = input2, input1  # swap using multiple assignment

# print("Input 1 Is Now", input1)
# print("Input 2 Is Now", input2)

# output

# Enter Input 1 12
# Enter Input 2 3
# Input 1 Is Now 3
# Input 2 Is Now 12

# 2. WAP to ask the user to enter the string. Display the first three characters of the string to upper case and rest
# in lower case.

# input = input("Enter a String pyth")
# upper = input[:3].upper()
# lower = input[3:].lower()
# final = upper + lower
# print(final)

# output

# Enter a String python
# PYThon

# 3. WAP to take the value of x, slope and y-intercept and calculate y-value using straight line equation.
# x = float(input("Enter x "))

# slope = float(input("Enter  slope "))
# y_intercept = float(input("Enter  y-intercept "))
# y=slope*x+y_intercept
# print("y is ",y)

# output

# Enter x 3
# Enter  slope 1.4
# Enter  y-intercept 2
# y is  6.199999999999999

# 4. WAP to take the decimal value from the user and convert it to binary, octal, and hexadecimal and vice-versa.
# enter = (int(input("Enter a Decimal ")))

# print("binary", bin(enter)[2:])
# print("octal", oct(enter)[2:])
# print("hexadecimal", hex(enter)[2:])

# output

# Enter a Decimal 12
# binary 1100
# octal 14
# hexadecimal c

# 5 Write a program to prompt the user for the coordinates (x, y) of points A and B. Calculate the Euclidean distance
# between these two points in a two-dimensional plane.

# enter_x_A=int(input("enter x value for A "))
# enter_y_A=int(input("enter y value for A "))
# =int(input("enter x value for B "))
# enter_y_B=int(input("enter y value for B "))
# calculate=math.sqrt((enter_x_B-enter_x_A)**2+(enter_y_B-enter_y_A)**2)
# print(calculate)

# output

# enter x value for A 2
# enter y value for A 4
# enter x value for B 6
# enter y value for B 8
# .656854249492381

# 6 WAP to ask the radius and height from the user and calculate volume of the cylinder.

# radius=float(input("enter radius "))
# height=float(input("enter height "))
# volume=3.14*radius**2*height
# print(volume)

# output

# enter radius 6
# enter height 4
# 452.16
