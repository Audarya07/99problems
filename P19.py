# Rotate a list N places to the left.
from LL import init_ll, Node, LinkedList

def rotate_N_left(LL, n):
    '''A function to rotate the linked list N places to the left.
    
    Parameters:
        LL (LinkedList): Linked list on which rotation is to be performed.
        n (int): Places by which the linked list is to be left rotated.
    '''
    
    if not LL.head or n == 0:
        return None

    curr = LL.head
    cnt = 1

    while cnt < n and curr:
        curr = curr.next
        cnt += 1
    if not curr:
        return

    nth_node = curr
    while curr.next:
        curr = curr.next
    curr.next = LL.head
    LL.head = nth_node.next
    nth_node.next = None

if __name__ == "__main__":
    LL = init_ll()

    n = int(input("Enter value of N: "))
    rotate_N_left(LL, n)

    print(f'After rotation:', end=" ")
    ll = LinkedList(LL.head)
    ll.print_ll()