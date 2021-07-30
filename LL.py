class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        else:
            self.head = new_node
    
    def print_ll(self):
        linked_list = []
        curr = self.head
        while curr:
            linked_list.append(str(curr.data))
            curr = curr.next
        print("Linked List:"," -> ".join(linked_list))

def init_ll():
    LL = LinkedList()
    LL.insert(1)
    LL.insert(2)
    LL.insert(3)
    LL.insert(4)
    LL.insert(3)
    LL.insert(2)
    LL.insert(1)

    LL.print_ll()

    return LL
