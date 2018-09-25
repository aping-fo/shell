'''
节点
'''


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(left: Node, right: Node) -> Node:
    head = Node(0)
    current = head
    sum = 0

    while left or right:
        print("adding:", left.val, right.val)
        sum //= 10
        if left:
            sum += left.val
            left = left.next
        if right:
            sum += right.val
            right = right.next

        current.next = Node(sum % 10)
        current = current.next

    if sum // 10 == 1:
        current.next = Node(1)

    return head.next


number1 = Node(2)
number1.next = Node(4)
number1.next.next = Node(3)
number2 = Node(5)
number2.next = Node(6)
number2.next.next = Node(4)
result = add_two_numbers(number1, number2)
print(result.val)
