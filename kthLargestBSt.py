class Solution:
    def dfs(self,root):
        if not root: return
        self.dfs(root.right)
        if self.k==0: return
        self.k-=1
        if self.k==0: self.res=root.val
        self.dfs(root.left)
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k=k
        self.dfs(root)
        return self.res