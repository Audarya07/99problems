# Remove the N'th element from a list.
from LL import init_char_ll, Node, LinkedList

def remove_Kth_element(LL, n):
    '''A function to remove the Nth node of linked list.
    
    Parameters:
        LL (LinkedList): Linked list on which deletion is to be performed.
        n (int): Index of node to be removed from linked list.
    '''

    curr = LL.head
    prev = None
    cnt = 1
    while curr:
        if cnt == n:
            rem_node = curr
            prev.next = curr.next
            curr = curr.next

            del rem_node
        else:
            prev = curr
            curr = curr.next
        cnt += 1

if __name__ == "__main__":
    LL = init_char_ll()
    k = int(input("Enter value of K: "))

    print(f'Modified Linked List after removing Kth element:', end=" ")
    remove_Kth_element(LL, k)
    
    ll = LinkedList(LL.head)
    ll.print_ll()

