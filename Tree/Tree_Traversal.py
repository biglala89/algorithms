class TreeNode(object):
	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None

class Tree(object):
	def pre_order_traversal(self, root):
		res = []
		self.pre_order_helper(root, res)
		return res

	def pre_order_helper(self, root, res):
		if not root:
			return
		res.append(root.val)
		self.pre_order_helper(root.left, res)
		self.pre_order_helper(root.right, res)

	def in_order_traversal(self, root):
		res = []
		self.in_order_helper(root, res)
		return res

	def in_order_helper(self, root, res):
		if not root:
			return
		self.in_order_helper(root.left, res)
		res.append(root.val)
		self.in_order_helper(root.right, res)

	def Height(self, root):
		if not root:
			return 0
		left = self.Height(root.left)
		right = self.Height(root.right)
		return 1 + max(left, right)
	


# Initialization
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

# print root.left.val
# print root.right.val


# Traversal
t = Tree()
print t.pre_order_traversal(root)
print t.in_order_traversal(root)
print t.Height(root)

