class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, t):
        if not t:
            return ''
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        if not left and not right:
            return str(t.val)
        if not right:
            return str(t.val) + '(' + str(left) + ')'
        return str(t.val) + '(' + str(left) + ')' + '(' + str(right) + ')'

    def better_tree2str(self, t):
        if not t:
            return ''
        if not t.left and not t.right:
            return str(t.val)
        if not t.right:
            return str(t.val) + '(' + str(self.better_tree2str(t.left)) + ')'
        return str(t.val) + '(' + str(self.better_tree2str(t.left)) + ')' + '(' + str(self.better_tree2str(t.right)) + ')'

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

s = Solution()
# print s.tree2str(root)
# print
# print s.better_tree2str(root)

import time
times = 100000
start = time.time()
timer1, timer2 = 0, 0

for _ in range(times):
    start1 = time.time()
    s.tree2str(root)
    timer1 += time.time() - start1

    start2 = time.time()
    s.better_tree2str(root)
    timer2 += time.time() - start2

print 'Total Solution runtime: {}s'.format(str(timer1))
print 'Total Better Solution runtime: {}s'.format(str(timer2))
print 'Total Diff: {}s, runtime increased by {}%'.format(timer2-timer1, round((timer2-timer1)/timer1, 4)*100)




