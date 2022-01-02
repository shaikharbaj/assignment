# Python program ot check if number is in a given range or not
def isInrange(n,l,u):
    if n in range(l,u):
        print(f"{n} is in given range")
    else:
        print(f"{n} is not in given range")

lower= int(input("Enter the lower range= "))
upper= int(input("Enter the upper range= "))
num=int(input("Enter the number= "))
isInrange(num,lower,upper)
