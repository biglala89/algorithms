# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        if not root: return []
        res = []
        path = []
        self.helper(root, path, res)
        return res
        
    def helper(self, root, path, res):
        path.append(str(root.val))
        print 'current path:', path
        if not root.left and not root.right:
            res.append('->'.join(path))
            print 'last node:', path[-1]
            path.pop()
            return
        if root.left:
            self.helper(root.left, path, res)
        if root.right:            
            self.helper(root.right, path, res)
        print 'last node:', path[-1]
        path.pop()
        print path

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(8)

s = Solution()
print s.binaryTreePaths(root)
