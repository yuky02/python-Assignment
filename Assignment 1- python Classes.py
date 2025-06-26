'''
 Task 1: Perform Basic Mathematical Operations
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
'''
a = input("Enter the first Number: ")
b= input("Enter the second  Number: ")
a=float(a)
b=float(b)
print("Addtion :" ,a+b)
print("Substraction :" ,a-b)
print("Multiplication :" ,a*b)
print("Division :" ,a/b)

'''
#Task 2: Create a Personalized Greeting
#Problem Statement: Write a Python program that:
#1.  Takes a user's first name and last name as input.
#2.  Concatenates the first name and last name into a full name.
#3.  Prints a personalized greeting message using the full name.
'''
a = input("Enter the first name : ")
b = input("Enter the last name :  ")
print("Hello,"+a+b+"! Welcome to this World.")
