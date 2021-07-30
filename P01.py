# Find the last box of a list.
from LL import init_ll

def last_element(LL):
    curr = LL.head
    while curr.next:
        curr = curr.next
    print(f'Last element: {curr.data}')


if __name__ == "__main__":
    LL = init_ll()
    last_element(LL)
