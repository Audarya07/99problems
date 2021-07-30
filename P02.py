# Find the last but one box of a list.
from LL import init_ll

def last_but_one(LL):
    curr = LL.head
    while curr.next.next:
        curr = curr.next
    while curr:
        print(curr.data, end=" ")
        curr = curr.next

if __name__ == "__main__":
    LL = init_ll()
    print(f'Last but one element:', end=" ")
    last_but_one(LL)
    print()
