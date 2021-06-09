import collections


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, base):
        self.base = base

    def levelOrder(self, root):
        if not root:return
        res=[]
        queue=collections.deque([root])
        while queue:
            tmp=collections.deque()
            for _ in range(len(queue)):
                node=queue.popleft()
                if len(res)%2: tmp.appendleft(node.val)
                else:tmp.append(node.val)
                if node.left:queue.append(node.left)
                if node.right:queue.append(node.right)
            res.append(list(tmp))
        return res




base = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))  # 树的根节点
tree = Tree(base)
result = tree.levelOrder(tree.base)
print(result)
res=''
for i in result:
    for j in i:
        res=res+str(j)+' '
print(res)


