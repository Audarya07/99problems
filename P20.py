# Remove the K'th element from a list.
from LL import init_char_ll, Node, LinkedList

def remove_Kth_element(LL, n):
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
        # curr = curr.next

if __name__ == "__main__":
    LL = init_char_ll()
    k = int(input("Enter value of K: "))
    print(f'Modified Linked List after removing Kth element:', end=" ")
    remove_Kth_element(LL, k)
    ll = LinkedList(LL.head)
    ll.print_ll()

