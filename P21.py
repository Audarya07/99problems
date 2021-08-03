# Insert an element at a given position into a list.
from LL import init_char_ll, Node, LinkedList

def insert_at_K(LL, k, value):
    '''A function to insert a node at a given index in the linked list.
    
    Parameters:
        LL (LinkedList): Linked list on which operation is to be performed.
        k (int): Index at which node is to be inserted.
        value (int): Value of the node to be inserted.

    Returns:
        LinkedList: A reference of the head node of linked list after insertion.
    '''

    new_node = Node(value)
    if k == 1:
        new_node.next = LL.head
        LL.head = new_node
    else:
        temp = LL.head
        for i in range(k-2):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
    return LL.head

if __name__ == "__main__":
    LL = init_char_ll()

    k = int(input("Enter position: "))
    value = input("Enter data to be inserted: ")
    
    print(f'Modified Linked List after inserting element:', end=" ")
    insert_at_K(LL, k, value)
    
    ll = LinkedList(LL.head)
    ll.print_ll()
