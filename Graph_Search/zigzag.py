# BFS

class TreeNode(object):
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val

class Solution(object):
	def zigzagLevelOrder(self, root):
		if not root:
			return []
		frontier = [root]
		ans = []
		reverse = False
		while frontier:
			next_ = []
			curr = []
			for s in frontier:
				curr.append(s.val)
				if s.left:
					next_.append(s.left)
				if s.right:
					next_.append(s.right)
			ans.append(curr[::-1] if reverse else curr)
			frontier = next_
			reverse = not reverse
		return ans


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
res = s.zigzagLevelOrder(root)
print res
