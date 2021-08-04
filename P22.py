# Create a list containing all integers within a given range.
from LL import init_char_ll, Node, LinkedList

def generate_ll_from_range(l, u):
    '''A function to generate a linked list containing all integers within a given range
    provided lower bound < upper bound.
    
    Parameters:
        l (int): Lower bound of the range.
        u (int): Upper bound of the range.
    '''

    ll = LinkedList(None)
    for i in range(l, u+1):
        ll.insert(i)

    ll.print_ll()

if __name__ == "__main__":
    l, u = map(int, input("Enter lower and upper bound of range: ").split())
    generate_ll_from_range(l, u)