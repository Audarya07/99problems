# Find the K'th element of a list.

from LL import init_ll

def Kth_element(LL, k):
    curr = LL.head
    cnt = 1
    while curr:
        if cnt == k:
            return curr.data
        curr = curr.next
        cnt += 1

if __name__ == "__main__":
    LL = init_ll()
    k = int(input("Enter K: "))

    print(f'Kth element:', end=" ")
    node = Kth_element(LL, k)
    print(node)
