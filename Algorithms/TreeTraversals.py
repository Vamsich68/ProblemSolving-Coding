# Given an array of unique elements, construct a Binary Search Tree and print the PreOrder, 
# InOrder and PostOrder Traversals of the tree.

# Input Format

# First line of input contains T - number of test cases. Its followed by 2T lines. 
# First line of each test case contains N - number of nodes in the BST. 
# The next line contains N unique integers - value of the nodes

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
def preOrder(root):
    if root is None:
        return 
    print(root.data,end=' ')
    preOrder(root.left)
    preOrder(root.right)
def inOrder(root):
    if root is None:
        return 
    inOrder(root.left)
    print(root.data,end=' ')
    inOrder(root.right)
def postOrder(root):
    if root is None:
        return 
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end=' ')
n=int(input())
for i in range(n):
    x=int(input())
    lst=list(map(int,input().split()))
    root= None
    for i in range(x):
        root= add(root,lst[i])
    preOrder(root)
    print()
    inOrder(root)
    print()
    postOrder(root)
    print()
    print()