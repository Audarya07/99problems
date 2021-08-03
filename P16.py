# Drop every N'th element from a list.
from LL import init_char_ll, Node, LinkedList

def drop_Nth_element(LL, n):
    '''A function to drop/skip every Nth node of linked list.
    
    Parameters:
        LL (LinkedList): Linked list on which operation is to be performed.
        n (int): Number whose multiples are used as indexes to be dropped from linked list.
    '''

    curr = LL.head
    prev = None
    cnt = 1
    while curr:
        if cnt % n == 0:
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next
        cnt += 1

if __name__ == "__main__":
    LL = init_char_ll()
    n = int(input("Enter value of N: "))

    print(f'Modified Linked List after dropping every Nth element:', end=" ")
    drop_Nth_element(LL, n)

    ll = LinkedList(LL.head)
    ll.print_ll()

