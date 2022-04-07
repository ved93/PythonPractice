
# Remember that wonderful Python list we talked about eariler? It turns out that stack functionality is already built into it!

# The Python documentation shows how you can use built-in funtions to turn your Python list into a stack. pop() is a given function, and append() is equivalent to a push function.

# Of course, this functionality makes stack manipulation in Python all too easy. Let's make our own Stack class to see how a stack really works under the hood.

# https://geekflare.com/python-stack-implementation/
# https://www.section.io/engineering-education/stack-data-structure-python/
# https://www.programiz.com/dsa/stack

class Stack: 
    def __init__(self): 
        self.elements = [] 
    
    def push(self, data): 
        self.elements.append(data) 
        return data 
    
    def pop(self): 
        return self.elements.pop() 
        
    def peek(self): 
        return self.elements[-1] 
        
    def is_empty(self): 
        return len(self.elements) == 0

if __name__ == '__main__':
    stack = Stack()
    
    ## checking is_empty method -> true
    print(stack.is_empty())

    ## pushing the elements
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    ## again checking is_empty method -> false
    print(stack.is_empty())

    ## printing the topmost element of the stack -> 5
    print(stack.peek())

    ## popping the topmost element -> 5
    stack.pop()

    ## checking the topmost element using peek method -> 4
    print(stack.peek())

    ## popping all the elements
    stack.pop()
    stack.pop() 
    stack.pop() 
    stack.pop() 

    ## checking the is_empty method for the last time -> true
    print(stack.is_empty())



stack = []
 
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack')
print(stack)
 
# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)


# https://www.geeksforgeeks.org/stack-in-python/


"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""


"This is new Implementation of stack based on linkedlist. Read the comments at top"

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        if self.head:
            deleted_element = self.head
            temp = deleted_element.next
            self.head = temp
            return deleted_element
        else:
            return None

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete_first()



# Here's an alternative solution to delete_first() - https://gist.github.com/adarsh0806/02d8e1d54d510294e75dfbc0d9bd7059

# Benefits of this method:

# 1) this version has fewer lines of code with no loss of functionality 2) this version clears out the next field of the deleted element (good practice, even though it's not in the specification)



# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())
stack.push(e4)
print(stack.pop().value)