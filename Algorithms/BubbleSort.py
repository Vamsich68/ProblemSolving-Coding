n=int(input())
for i in range(n):
    x=int(input())
    y=list(map(int,input().split()))
    c=0
    for k in range(x):
        for j in range(x-1-k):
            if y[j]>y[j+1]:
                t=y[j]
                y[j]=y[j+1]
                y[j+1]=t
                c+=1
    print(c)
    