class Node:
    def __init__(self, val, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')

a.left = b
a.right =c 
b.left = e
c.right = f

# iterative implementation
def dfs(node):
    stack = [node]
    while stack:
        res = stack.pop()
        print(res, end=' ')
        if res.right :
            stack.append(res.right)
        if res.left :
            stack.append(res.left)
      
      
dfs(a)
    
# recursive preorder traversal
def dfs_recursive(node):
    if not node:
        return None
    print(node, end=' ')
    dfs_recursive(node.left)
    dfs_recursive(node.right)

dfs_recursive(a)