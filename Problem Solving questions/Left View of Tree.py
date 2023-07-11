class Node:
    def __init__ (self,data):
        self.left= None
        self.right= None
        self.data= data
def add(root,a):
    if root == None:
        return Node(a)
    if root.data > a:
        root.left= add(root.left,a)
    else:
        root.right= add(root.right,a)
    return root
def leftview(root,lev):
    global maxlev
    if root==None:
        return
    else:
        if maxlev<lev:
            #print(maxlev,lev)
            print(root.data,end=" ")
            maxlev+=1
        leftview(root.left,lev+1)
        leftview(root.right,lev+1)

t=int(input())
for i in range(t):
    x=int(input())
    lst=list(map(int,input().split()))
    root= None
    for i in range(x):
        root= add(root,lst[i])
    maxlev=0
    lev=1
    leftview(root,lev)
    print()