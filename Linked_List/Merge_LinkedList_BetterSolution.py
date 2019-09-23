# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from ListNode import *

class Solution(object):
  def merge(self, one, two):
    NewNode = ListNode('new')
    prev_node = NewNode
    while one and two:
      if one.val <= two.val:
        prev_node.next = one
        prev_node = prev_node.next
        print 'previous node: (-) ', prev_node.val
        one = one.next
        if one:
          print 'p1 node: ', one.val
      else:
        prev_node.next = two
        prev_node = prev_node.next
        print 'previous node: (--)', prev_node.val
        two = two.next
        if two:
          print 'p2 node: ', two.val
    while one and one is not None:
      prev_node.next = one
      print "{}'s next is {}".format(prev_node.val, one.val)
      prev_node = prev_node.next
      one = one.next
    while two and one is not None:
      prev_node.next = two
      prev_node = prev_node.next
      two = two.next
    return NewNode.next

  def print_node(self, head):
    alist = []
    while head:
      alist.append(head.val)
      head = head.next
    print alist

one1 = ListNode(0)
one2 = ListNode(5)
one3 = ListNode(5)
one4 = ListNode(5)
one5 = ListNode(8)
one6 = ListNode(10)

two1 = ListNode(2)
two2 = ListNode(3)
two3 = ListNode(4)
two4 = ListNode(4)
two5 = ListNode(5)
two6 = ListNode(7)

one1.next = one2
one2.next = one3
one3.next = one4
one4.next = one5
one5.next = one6

two1.next = two2
two2.next = two3
two3.next = two4
two4.next = two5
two5.next = two6

s = Solution()
res = s.merge(one1, two1)
s.print_node(res)