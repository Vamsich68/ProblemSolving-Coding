class Node:
    def __init__ (self,data):
        self.data=data
        self.left=None 
        self.right=None 
def add(root,a):
    if root == None:
        return Node(a)
    if root.data < a:
        root.right = add(root.right,a)
    else:
        root.left = add(root.left,a)
    return root
def vot(root,lst,level):
    if root == None:
        return 
    if level in lst:
        lst[level].append(root.data)
    else:
        lst[level]=[]
        lst[level].append(root.data)

    vot(root.left,lst,level-1)
    vot(root.right,lst,level+1)
    return lst
for i in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    root= None
    for i in range(a):
        root=add(root,l[i])
    lst={}
    res=vot(root,lst,0)
    for i in sorted(lst.keys()):
        res[i].sort()
        print(*res[i])
    print()
    
        