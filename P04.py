# Find the number of elements of a list.
from LL import init_ll

def length(LL):
    curr = LL.head
    cnt = 0
    while curr:
        curr = curr.next
        cnt += 1
    return cnt

if __name__ == "__main__":
    LL = init_ll()
    print(f'Length of linked list:', end=" ")
    node = length(LL)
    print(node)
