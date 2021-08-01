# Modified Run-length encoding of a list.
from LL import init_char_ll

def run_length_encoding(LL):
    temp = LL.head
    while temp:
        curr = temp.data
        cnt = 0
        while temp and curr == temp.data:
            cnt += 1
            temp = temp.next
        if cnt == 1:
            print(f'({curr})', end=" ")
        else:
            print(f'({cnt}-{curr})', end=" ")
    print()


if __name__ == "__main__":
    LL = init_char_ll()
    print(f'Modified Run-length encoding:', end=" ")
    run_length_encoding(LL)
