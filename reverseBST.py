
class Node(object):                #定义树的结点
    def __init__(self, data=-1, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild
class Binsearchtree(object):
    def __init__(self, data):
        self.root = Node(data)
    def inverttree(self, treenode):      #真正的翻转只有这8行代码
        if treenode == None:
            return None
        temp = treenode.lchild
        treenode.lchild = treenode.rchild
        treenode.rchild = temp
        self.inverttree(treenode.lchild)
        self.inverttree(treenode.rchild)
