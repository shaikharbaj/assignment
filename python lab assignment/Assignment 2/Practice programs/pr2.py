# Python program to check if a substring is present in a given string
str1= input("Enter the string= ")
substr= input("Enter the substring= ")
if str1.find(substr)!=-1:
    print("The substring is present in the string")
else:
    print("The substring is not present in the string")
