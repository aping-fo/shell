class Node:
    def __init__(self, x):
        self.val = x
        self.next = Node
        self.pre = None


def delete_node(node):
    if node is None:
        raise ValueError
    if node.next is None:
        node.pre.next = None

    node.pre.next = node.next
    node.next.pre = node.pre


head = Node(1)
curr = head
tem = head;
for i in range(2, 6):
    curr.next = Node(i)
    curr.pre = head
    curr = curr.next
    head = curr

node3 = tem.next.next
# after delete_node => 1 -> 2 -> 4
delete_node(node3)
