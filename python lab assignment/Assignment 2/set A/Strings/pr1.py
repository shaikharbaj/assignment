# Python program to check if a string is pallindrome or symmetric
def isPallindrime(s):
    if s==s[::-1]:
        print("The entered string is pallindrome")
    else:
        print("The entered string is pallindrome")
def isSymmetric(s):
    mid=int(len(s)/2)
    if len(s)%2==0:
        s1=s[:mid]
        s2=s[mid:]
    else:
        s1=s[:mid]
        s2=s[mid+1:]
    if s1==s2:
        print("The givem string is symmetric")
    else:
        print("The givem string is not symmetric")
s= input("Enter the string= ")
isPallindrime(s)
isSymmetric(s)

