#树的遍历
class Node ():
    def __init__(self,data,left=None,right=None):  #也是值在前面，指针在后面，默认为None
        self.data=data
        self.left=left
        self.right=right
class Tree():
    def __init__(self,base):
        self.base=base
    def bfs(self,node):
        queue=[]
        queue.append(node)
        while queue:
            temp=queue.pop(0)
            print(temp.data, end=' ')
            left=temp.left
            right=temp.right
            if left:
                queue.append(left)
            if right:
                queue.append(right)
    def fro(self,node):   #前序遍历==DFS
        if not node:
            return
        stack=[]
        stack.append(node)
        while stack:
            temp=stack.pop()
            print(temp.data, end=' ')
            right=temp.right
            left=temp.left
            if right:
                stack.append(right)
            if left:
                stack.append(left)
    def mid(self,node):  #左-根-右,左节点放在栈的最右边
        if not node:
            return
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            print(node.data,end=' ')
            node = node.right
    def beh(self,node):
        if not node:
            return
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left if node.left else node.right
            node = stack.pop()
            print(node.data,end=' ')
            if stack and stack[-1].left == node:
                node = stack[-1].right
            else:
                node = None
 
base = Node(1,Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))  # 树的根节点
tree = Tree(base)  # 树
 
print('BFS')
tree.bfs(tree.base)
print('\n')
 
print('前序遍历==DFS')
tree.fro(tree.base)
print('\n')
 
print('中序遍历')
tree.mid(tree.base)
print('\n')
 
print('后序遍历')
tree.beh(tree.base)
print('\n')