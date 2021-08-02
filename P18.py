# Extract a slice from a list.
from P17 import split_at_N
from LL import init_char_ll, Node, LinkedList

def splice(LL, s, e):
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

    s, e = map(int, input("Enter start and end of splice: ").split())
    LL.head = splice(LL, s, e)

    print("Sliced", end=" ")
    ll = LinkedList(LL.head)
    ll.print_ll()
