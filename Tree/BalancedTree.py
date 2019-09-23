class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def isBalanced(self, root):
    if not root:
      return True
    left = self.height(root.left)
    right = self.height(root.right)
    return abs(left - right) <= 1
    
    
  def height(self, root):
    if not root:
      return 0
    left = self.height(root.left)
    right = self.height(root.right)
    print root.val, 'diff: {}'.format(abs(left - right))
    if abs(left - right) > 1:
      return False
    return max(left, right) + 1


root = TreeNode(5)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.left = TreeNode(1)

root.right = TreeNode(7)
root.right.right = TreeNode(9)
root.right.right.left = TreeNode(8)
root.right.right.right = TreeNode(9)

s = Solution()
print s.isBalanced(root)



