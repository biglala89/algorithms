class TreeNode(object):
	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None


def lca(root, p, q):
	if not root:
		return 
	if root.val == p or root.val == q:
		return root
	left = lca(root.left, p, q)
	right = lca(root.right, p, q)
	if left and right:
		return root
	if not left:
		return right
	if not right:
		return left


root = TreeNode(0)
root.left = TreeNode(1)
root.left.left = TreeNode(2)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(5)

print lca(root, 4, 5).val
