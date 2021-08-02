# Split a list into two parts; the length of the first part is given.
from LL import init_char_ll, Node, LinkedList

def split_at_N(LL, n):
    if LL.head == None:
        return None
    curr = LL.head
    temp = None
    cnt = 0
    while curr:
        cnt += 1
        if cnt == n:
            temp = curr.next
            curr.next = None
            return temp
        curr = curr.next
    return  None

if __name__ == "__main__":
    LL = init_char_ll()
    LL1 = LinkedList(None)

    n = int(input("Enter value of N: "))
    LL1.head = split_at_N(LL, n)

    print(f'Split 1:', end=" ")
    ll = LinkedList(LL.head)
    ll.print_ll()

    print(f'Split 2:', end=" ")
    ll1 = LinkedList(LL1.head)
    ll1.print_ll()
