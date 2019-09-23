class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def totalval(self, root):
		if not root:
			return 0
		left = self.totalval(root.left)
		right = self.totalval(root.right)
		return root.val + left + right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

s = Solution()
print s.totalval(root)
