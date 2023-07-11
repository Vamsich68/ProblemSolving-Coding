
def subset(lst,x,index,ss):
    if index==x:
        return
    for i in range(index,x):
        ss.append(lst[i])
        print(*ss)
        subset(lst,x,i+1,ss)
        ss.pop()
    return
    
n=int(input())
for i in range(n):
    x=int(input())
    y=list(map(int,input().split()))[:x]
    z=sorted(y)
    #z=str.join(y)
    #print(z)
    index=0
    set=[]
    subset(z,x,0,set)
    print()
    
    
    