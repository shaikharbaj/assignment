# Python program to check perfect number
def isPerfect(n):
    lst=[]
    for i in range(1,n):
        if n%i==0:
            lst.append(i)
    if n==sum(lst):
        print(f"{n} is a perfect number")
    else:
        print(f"{n} is not a perfect number")
n= int(input("Enter the number= "))
isPerfect(n)
