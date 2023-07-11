n=int(input())
for i in range(n):
    x=int(input())
    y=list(map(int,input().split()))
        
    for i in range(x-1):
        max=0
        for j in range(1,x-i,1):
            if y[j]>y[max]:
                max=j
        print(max,end=" ")
        y[max], y[x-1-i] = y[x-1-i], y[max]
    print()
    