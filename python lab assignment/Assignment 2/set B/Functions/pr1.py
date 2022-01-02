# Python program to return unique element of a list
def uniqueList(lst):
    return list(set(lst))
lst=[1,5,2,1,5,7,8,2,9,1]
lst= uniqueList(lst)
print(lst)
