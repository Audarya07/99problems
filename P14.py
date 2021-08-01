# Duplicate the elements of a list.
from LL import init_char_ll, Node, LinkedList

def duplicate(LL):
    curr = LL.head
    while curr:
        node = Node(curr.data)
        node.next = curr.next
        curr.next = node
        curr = node
        curr = curr.next

if __name__ == "__main__":
    LL = init_char_ll()
    print(f'Duplicate Linked List:', end=" ")
    duplicate(LL)
    ll = LinkedList(LL.head)
    ll.print_ll()
