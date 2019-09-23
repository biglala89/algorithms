class Solution(object):
  def reverse(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    stack = []
    for i in input[0]:
      if i in ['a', 'e', 'i', 'o', 'u']:
        stack.append(i)
    new_string = ''
    for i in input[0]:
      if i in ['a', 'e', 'i', 'o', 'u']:
        new_string = new_string + stack.pop()
      else:
        new_string = new_string + i
    return new_string
  
a = ["qwertyuiop"]
s = Solution()
print s.reverse(a)
