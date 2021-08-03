class Node:
    '''A basic node class for storing data.'''
    def __init__(self, data=None, next=None):
        '''Initialize data and reference to the next node in the linked list.'''
        self.data = data
        self.next = next

class LinkedList:
    '''Singly Linked List data structure class'''
    def __init__(self, head):
        '''Initialize the "head" attribute by setting
        it to "None", since the list is empty initially.
        '''
        self.head = head
    
    def insert(self, data):
        '''Insert a new node containing "data" to the end of the list.'''
        # Create a new node to store input data.
        new_node = Node(data)
        if self.head:
            # If list is not empty, traverse to end of list and place the new_node
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        else:
            # If the list is empty, assign the head to new_node, 
            # since it becomes the first in the list.
            self.head = new_node
    
    def print_ll(self):
        '''Display the linked list in proper format.'''
        linked_list = []
        curr = self.head
        while curr:
            linked_list.append(str(curr.data))
            curr = curr.next
        print("Linked List:"," -> ".join(linked_list))

def init_ll():
    '''Initialize a linked list containing integer data for testing purpose
    and display it.'''
    LL = LinkedList(None)
    LL.insert(1)
    LL.insert(1)
    LL.insert(2)
    LL.insert(3)
    LL.insert(3)
    LL.insert(4)
    LL.insert(3)
    LL.insert(3)
    LL.insert(2)
    LL.insert(1)
    LL.insert(1)

    LL.print_ll()

    return LL


def init_char_ll():
    '''Initialize a linked list containing character data for testing purpose
    and display it.'''
    LL = LinkedList(None)
    LL.insert("a")
    LL.insert("a")
    LL.insert("b")
    LL.insert("c")
    LL.insert("c")
    LL.insert("a")
    LL.insert("a")
    LL.insert("d")
    LL.insert("e")
    LL.insert("e")
    LL.insert("e")

    LL.print_ll()

    return LL
