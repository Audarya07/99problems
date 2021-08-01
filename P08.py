# Eliminate consecutive duplicates of list elements.
from LL import init_char_ll

def remove_duplicates(LL):
    temp = LL.head
    print("(", end=" ")
    while temp:
        curr = temp.data
        print(curr, end=" ")
        while temp and curr == temp.data:
            temp = temp.next
    print(")", end=" ")
    print()


if __name__ == "__main__":
    LL = init_char_ll()
    print(f'Remove duplicates:', end=" ")
    remove_duplicates(LL)
