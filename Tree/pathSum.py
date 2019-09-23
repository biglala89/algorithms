# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, target):
        if not root:
            return []
        res, path = [], []
        total = 0
        self.helper(root, path, total, target, res)
        return res
    
    def helper(self, root, path, total, target, res):
        total += root.val
        print 'total:', total
        path.append(root.val)
        print 'current path:', path
        if not root.left and not root.right:
            if total == target:
                res.append(path[:])
                print 'res:', res
                # path.pop()
            total -= root.val
            print 'total:', total
            path.pop()
            print 'current path:', path
            return
        if root.left:
            self.helper(root.left, path, total, target, res)
        if root.right:
            self.helper(root.right, path, total, target, res)
        path.pop()
        print path

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

s = Solution()
print s.pathSum(root, 22)
