class ListNode(object):
	def __init__(self, value):
		self.value = value
		self.next = None

def print_node(head):
	while head:
		print head.value
		head = head.next

def remove_node(head, target):
	if not head.next:
		return head

	fake_head = ListNode('fake_head')
	fake_head.next = head
	prev_node = fake_head
	while head:
		if head.value == target:
			prev_node.next = head.next
			head = head.next
		else:
			head = head.next
			prev_node = prev_node.next
	return fake_head.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print_node(remove_node(node1, 2))

import sys
print sys.version
