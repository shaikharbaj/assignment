# python program to sum all the numbers in a list
def sumList(lst):
    sum=0
    for i in lst:
        sum+=i
    print("The sum of the numbers in list= ",sum)
lst=[1,5,7,3]
sumList(lst)