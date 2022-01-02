# python program to find factorial of a number using function
def factorial(n):
    if n<0:
        print("Please enter a positive number")
    elif n==0:
        print("The factorial of 0 is 1")
    else:
        fact=1
        for i in range(n,0,-1):
            fact*=i
        print(f"The factorial of {n} is {fact}")
n= int(input("Enter the number= "))
factorial(n)