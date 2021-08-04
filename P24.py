# Lotto: Draw N different random numbers from the set 1..M.
from random import randint
from LL import init_char_ll, Node, LinkedList

def lottoSelect(count, limit) :
    '''A function to draw N different random numbers from the set 1..limit.
    
    Parameters:
        count (int): Number of random elements to be generated.
        limit (int): Upper bound of the range [1...limit]
    '''

    ll = LinkedList(None)

    for i in range(count) :
        ll.insert(randint(1, limit))

    ll.print_ll()

if __name__ == '__main__' :
    print("The list after selecting 6 random elements in range [1, 49] : ", end=" ")
    ll = lottoSelect(6, 49)
