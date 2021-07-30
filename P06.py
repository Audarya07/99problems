# Find out whether a list is a palindrome.
from LL import init_ll

def is_palindrome(LL):
    curr = LL.head
    ispalin = True
    stack = []
    while curr:
        stack.append(curr.data)
        curr = curr.next
    
    while LL.head:
        node = stack.pop()
        if LL.head.data == node:
            ispalin = True
        else:
            ispalin = False
            break

        LL.head = LL.head.next
    return ispalin
        

if __name__ == "__main__":
    LL = init_ll()
    print(f'Linked list is palindrome:', end=" ")
    print(is_palindrome(LL))
