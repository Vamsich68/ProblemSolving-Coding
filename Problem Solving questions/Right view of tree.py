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
def rightview(root,lev,maxlev):
    if root==None:
        return
    else:
        if maxlev[0]<lev:

            print(root.data,end=" ")
            maxlev[0]=lev
        rightview(root.right,lev+1,maxlev)
        rightview(root.left,lev+1,maxlev)

t=int(input())
for i in range(t):
    x=int(input())
    lst=list(map(int,input().split()))
    root= None
    for i in range(x):
        root= add(root,lst[i])
    maxlev=[0]
    lev=1
    rightview(root,lev,maxlev)
    print()