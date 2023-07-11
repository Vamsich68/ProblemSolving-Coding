n=int(input())
for i in range(n):
    a = int(input())
    lst = list(map(int,input().split()))
    for j in range(1,len(lst)):
        k = j-1
        b = lst[j]
        while(k>=0 and lst[k]>b):
            lst[k+1] = lst[k]
            k=k-1
        print(k+1,end=' ')
        lst[k+1] = b
    print()
            