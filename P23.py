# Extract a given number of randomly selected elements from a list.
from random import randint
from P03 import Kth_element
from P04 import length
from LL import init_char_ll, Node, LinkedList

def random_select(LL, n):
    '''A function to extract a given number of randomly selected elements from a list
    and return a new Linked List.
    
    Parameters:
        LL (LinkedList): Linked list on which operation is to be performed.
        n (int): Number of nodes to be randomly selected.

    Returns:
        ll2 (LinkedList): New linked list with randomly selected elements of original list.
    '''

    ll2 = LinkedList(None)
    ll_length = length(LL)

    for i in range(n):
        # Generate random number and access the random node of 
        # original list and insert in the new list.
        ll2.insert(Kth_element(LL, randint(1, ll_length-1)))
    return ll2

if __name__ == "__main__":
    LL = init_char_ll()

    k = int(input("Enter N: "))
    
    LL2 = random_select(LL, k)
    
    print("Randomly generated", end=" ")
    ll = LinkedList(LL2.head)
    ll.print_ll()
