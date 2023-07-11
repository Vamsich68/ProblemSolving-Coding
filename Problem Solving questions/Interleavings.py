def interleaving(A,B,stra,ptr1,ptr2):
    if ptr1==len(A):
        while(ptr2<len(B)):
            stra=stra+B[ptr2]
            ptr2=ptr2+1
        lst.append(stra)
        return 
    if ptr2==len(B):
        while(ptr1<len(A)):
            stra=stra+A[ptr1]
            ptr1=ptr1+1
        lst.append(stra)
        return
    if A[ptr1]< B[ptr2]:
        interleaving(A,B,stra+A[ptr1],ptr1+1,ptr2)
        interleaving(A,B,stra+B[ptr2],ptr1,ptr2+1)
    if A[ptr1]> B[ptr2]:
        interleaving(A,B,stra+B[ptr2],ptr1,ptr2+1)
        interleaving(A,B,stra+A[ptr1],ptr1+1,ptr2)
        
n=int(input())
for i in range(n):
    print("Case #"+str(i+1)+":")
    A,B=map(str,input().split())
    ptr1=0
    ptr2=0
    lst=[]
    interleaving(A,B,"",ptr1,ptr2)
    for s in lst:
        print(s)