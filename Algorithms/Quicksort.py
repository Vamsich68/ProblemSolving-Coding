def Quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst)//2]
    small =[]
    greater=[]
    equal=[]
    for x in lst:
        if x == pivot:
            equal.append(x)
        if x<pivot:
            small.append(x)
        if x>pivot:
            greater.append(x)
    return Quicksort(small)+equal+Quicksort(greater)
lst = [1,3,4,2,7,5,8,9,8]
sortedList=Quicksort(lst)
print(sortedList)
