class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def second_largest(self, root):
		res = []
		self.helper(root, res)
		return [i for i in res if i][-2]

	def helper(self, root, res):
		if not root:
			return
		left = self.helper(root.left, res)
		res.append(left)
		res.append(root.val)
		right = self.helper(root.right, res)
		res.append(right)


root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

s = Solution()
print s.second_largest(root)
