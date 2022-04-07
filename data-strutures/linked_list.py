



# https://www.educative.io/edpresso/how-to-reverse-a-linked-list-in-python
# https://www.geeksforgeeks.org/python-program-for-reverse-a-linked-list/



#vbelwo based on grokking the codding



#prefered way
class Node(object):
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)    
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    def print_list(head):
        while head:
            print(head.value, head.next)
            head = head.next
        
    print_list(head)    




#### Another Way

"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        # This method will add a new Element to the end of our LinkedList.
        #  If the LinkedList already has a head, iterate through the next reference in every Element until you reach the end of the list. Set next for the end of the list to be the new_element. Alternatively, if there is no head already, you should just assign new_element to it and do nothing else.
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

#uncomment below code to test
# # Test cases
# # Set up some Elements
# e1 = Element(1)
# e2 = Element(2)
# e3 = Element(3)
# e4 = Element(4)

# # Start setting up a LinkedList
# ll = LinkedList(e1)
# ll.append(e2)
# ll.append(e3)

# # Test get_position
# # Should print 3
# print( ll.head.next.next.value)
# # Should also print( 3
# print( ll.get_position(3).value)

# # Test insert
# ll.insert(e4,3)
# # Should print( 4 now
# print( ll.get_position(3).value)

# # Test delete
# ll.delete(1)
# # Should print( 2 now
# print( ll.get_position(1).value)
# # Should print( 4 now
# print( ll.get_position(2).value)
# # Should print( 3 now
# print( ll.get_position(3).value)