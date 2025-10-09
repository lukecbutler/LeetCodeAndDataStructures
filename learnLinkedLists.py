class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val # The data stored in the node
        self.next = next # The pointer to the next node

class LinkedList:
    def __init__(self):
        # The constructor sets the initial head to None for a new list.
        self.head = None

    def add_node_back(self, value_to_add: int):
        new_node = ListNode(value_to_add) # Create the new node
        # If the Linked Lit is empty, then make the new node as head
        if self.head is None:
            self.head = new_node
            return
        # Else, traverse to the last node using self.head as the start.
        current = self.head
        while current.next is not None:
            current = current.next
        # Link the last node to the new node.
        current.next = new_node

    def add_node_front(self, value_to_add: int):
        new_node = ListNode(value_to_add) # Create the new node
        new_node.next = self.head # Link the new node to the old list
        self.head = new_node

    #traverse and print the linked list
    def traverse_list(self):
        current = self.head # Assign the head to a variable
        while current is not None: # Continue until end of list
            print(current.val) # Print the value of the current node
            current = current.next

    # return the middle node of the linked List
    # input: List = [1,2,3,4,5]
    # output: [3,4,5]
    def find_middle(self):
        #first, return the head[√]
        '''
        return self.head
        '''
        #second, return the last node[√]
        '''
        current = self.head
        while current is not None: # continue until the end of list
            if current.next is None:
                return current.val
            current = current.next
        '''
        #third, return the middle node[]
        #move slow 1, move fast 2
        fast = self.head
        slow = self.head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next


        return slow.val

        
        


        








#1. Create a singly LinkedList object:
ll = LinkedList()

ll.add_node_back(1)
ll.add_node_back(2)
ll.add_node_back(3)
ll.add_node_back(4)
#ll.add_node_back(5)


#3. Call the traverse method on the object(print entire list)
print(ll.traverse_list)