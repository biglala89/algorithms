# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        tree1 = []
        tree2 = []
        self.helper(p, tree1)
        self.helper(q, tree2)
        print tree1
        print tree2
        if len(tree1) != len(tree2):
            return False
        while tree1:
            if tree1.pop() != tree2.pop():
                return False
        return True
    
    def helper(self, root, res):
        if not root:
            res.append('null')
            return 
        res.append(root.val)
        self.helper(root.left, res)
        self.helper(root.right, res)
        

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)

s = Solution()
print s.isSameTree(root1, root2)
