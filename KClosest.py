class Solution(object):
  def kClosest(self, array, target, k):
    """
    input: int[] array, int target, int k
    return: int[]
    """
    # write your solution here
    # if target > max(array) or target < min(array):
    # 	return None
    new_list = []
    left, right = 0, len(array) - 1
    while left < right - 1:
      mid = (left + right) / 2
      if array[mid] <= target:
        left = mid
      else:
        right = mid

    print array[left], array[right]###

    while k > 0 and right < len(array):
      if abs(array[left] - target) <= abs(array[right] - target):
        new_list.append(array[left])
        left -= 1
      else:
        new_list.append(array[right])
        right += 1
      k -= 1
    for j in range(k):
      new_list.append(array[left-j])
    return new_list

s = Solution()
a = [[1,4,4,6,9,9,12,15],0,5]
print (s.kClosest(a[0], a[1], a[2]))
