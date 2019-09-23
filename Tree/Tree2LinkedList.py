# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        res = []
        self.helper(root, res)
        print res
        new_root = TreeNode(res[0])
        ans = [new_root.val]
        head = new_root
        i = 1
        while i < len(res):
            ans.append(None)
            # head.left = None
            head.right = TreeNode(res[i])
            ans.append(head.right.val)
            head = head.right
            i += 1
        return ans

        
    def helper(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.helper(root.left, res)
        self.helper(root.right, res)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

s = Solution()
print s.flatten(root)