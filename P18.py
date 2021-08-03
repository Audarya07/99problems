# Extract a slice from a list.
from LL import init_char_ll, Node, LinkedList

def splice(LL, s, e):
    '''A function to slice the linked list from given start and end index.
    
    Parameters:
        LL (LinkedList): Linked list on which operation is to be performed.
        s (int): Start index from which the linked list is to be spliced.
        e (int): End index till which the linked list is to be spliced.

    Returns:
        LinkedList: A reference of the head node of spliced linked list.
    '''

    head = LL.head
    if head == None:
        return None

    curr = head
    cnt = 0
    while curr:
        cnt += 1
        if cnt == s:
            head = curr
        if cnt == e:
            curr.next = None
            return head
        curr = curr.next
    return head

if __name__ == "__main__":
    LL = init_char_ll()

    s, e = map(int, input("Enter start and end index for the splice: ").split())
    LL.head = splice(LL, s, e)

    print("Sliced", end=" ")
    ll = LinkedList(LL.head)
    ll.print_ll()
