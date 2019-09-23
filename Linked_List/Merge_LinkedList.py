class ListNode(object):
	def __init__(self, value):
		self.value = value
		self.next = None

def print_node(head):
	while head:
		print head.value
		head = head.next

def merge_linkedlist(head1, head2):
	if not head1.next or not head2.next:
		return head1, head2
	fake_head = ListNode('fake_head')
	prev_node = fake_head
	while head1 and head2:
		if head1.value >= head2.value:
			prev_node.next = head1
			prev_node = prev_node.next
			head1 = head1.next

		else:
			prev_node.next = head2
			prev_node = prev_node.next
			head2 = head2.next
	while head1:
		prev_node.next = head1
		head1 = head1.next
	while head2:
		prev_node.next = head2
		head2 = head2.next
	return fake_head.next

node1 = ListNode(10)
node2 = ListNode(8)
node3 = ListNode(5)

node4 = ListNode(7)
node5 = ListNode(6)
node6 = ListNode(2)

node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6

print_node(merge_linkedlist(node1, node4))



