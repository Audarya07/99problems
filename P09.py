# Pack consecutive duplicates of list elements into sublists.
from LL import init_char_ll

def pack_duplicates(LL):
    temp = LL.head
    while temp:
        curr = temp.data
        print("(", end=" ")
        while temp and curr == temp.data:
            print(curr, end=" ")
            temp = temp.next
        print(")", end=" ")
    print()


if __name__ == "__main__":
    LL = init_char_ll()
    print(f'Packed duplicates:', end=" ")
    pack_duplicates(LL)
