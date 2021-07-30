# Reverse a list.
from LL import init_ll

def reverse_ll(LL):
    curr = LL.head
    prev = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

if __name__ == "__main__":
    LL = init_ll()
    print(f'Length of linked list:', end=" ")
    node = reverse_ll(LL)
    print(node)