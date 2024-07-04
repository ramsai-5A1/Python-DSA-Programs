# Linked list implementation of Stack 
 
class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None 
 
 
class Stack:
    def __init__(self):
        print("New object for stack created successfully")
        self.top = None 
 
    # Insertion happens at Beginning 
    def push(self, value):
        print(value, "inserted in the stack successfully")
        newNode = Node(value)
        if self.top == None:
            # Only for first node this block is executed
            self.top = newNode
            return
 
        # Below line is responsible for inserting newNode at beginning
        newNode.next = self.top 
        self.top = newNode
 
 
    # Deletion happens at Beginning
    def pop(self):
        if self.top == None:
            print("Stack is empty, so we can't delete anything")
            return 
 
        print(self.top.val, "deleted from stack")
        # Storing secondNode address because this will be the future top node
        secondNode = self.top.next
 
        # Below line, we are removing the link between first and second node
        self.top.next = None
        del self.top
 
        # Below line we are moving our top pointer to secondNode
        self.top = secondNode
 
    def printStack(self):
        if self.top == None:
            print("Stack is empty, nothing to print")
            return 
 
        current = self.top 
        while current != None:
            print(current.val, end = " --> ")
            current = current.next 
        print()
 
 
# Object creation of stack
s1 = Stack()
 
# printing stack
s1.printStack()
 
# deleting from stack
s1.pop()
 
# inserting 5 values into stack
for i in range(10, 51, 10):
    s1.push(i)
 
# s1.push(10)
# s1.push(20)
# s1.push(30)
# s1.push(40)
# s1.push(50)
 
# printing those 5 values in stack
s1.printStack()
 
s1.pop()
 
s1.printStack()
 
s1.pop()
 
s1.printStack()
 
 
s2 = Stack()
for i in range(100, 106):
    s2.push(i)
 
s2.printStack()
