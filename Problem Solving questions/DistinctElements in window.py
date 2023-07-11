# Given an array of integers and a window size K, find the number of distinct elements in every window of size K of the given array.

# Input Format

# First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - size of the array and K - size of the window. The second line contains N integers - elements of the array.

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    lst=list(map(int,input().split()))
    d={}
    res=[]
    for i in range(k):
        if lst[i] in d:
            d[lst[i]]+=1 
        else:
            d[lst[i]]=1 
    res.append(len(d))
    for j in range(0,n-k):
        if d[lst[j]]>1:
            d[lst[j]]-=1 
        else:
            d.pop(lst[j])
        if lst[k+j] in d:
            d[lst[k+j]]+=1 
        else:
            d[lst[k+j]]=1 
        res.append(len(d))
    print(*res)
            
    