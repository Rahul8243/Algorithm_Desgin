class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_sorted_lists(l1, l2):
    # Dummy node to simplify logic
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Attach the remaining part
    tail.next = l1 if l1 else l2

    return dummy.next

# Helper: Print linked list
def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Example lists
a = Node(1)
a.next = Node(3)
a.next.next = Node(5)

b = Node(2)
b.next = Node(4)
b.next.next = Node(6)

merged_head = merge_sorted_lists(a, b)
print_list(merged_head)