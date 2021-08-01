# Replicate the elements of a list a given number of times.
from LL import init_char_ll, Node, LinkedList

def replicate(LL, k):
    curr = LL.head
    while curr:
        for i in range(k-1):
            node = Node(curr.data)
            node.next = curr.next
            curr.next = node
            curr = node
        curr = curr.next

if __name__ == "__main__":
    LL = init_char_ll()
    k = int(input("Enter number of times to replicate:"))
    print(f'Replicate Linked List:', end=" ")
    replicate(LL, k)
    ll = LinkedList(LL.head)
    ll.print_ll()

