# Array or list based implementation of Stack 
 
class Stack:
    def __init__(self):
        print("New object for stack created successfully")
        self.arr = [] 
 
    # Insertion happens at Beginning 
    def push(self, value):
        print(value, "inserted in the stack successfully")
        self.arr.insert(0, value)
 
 
    # Deletion happens at Beginning
    def pop(self):
        if len(self.arr) == 0:
            print("Stack is empty, so we can't delete anything")
            return 
 
        print(self.arr[0], "deleted from stack")
        self.arr.pop(0)
 
 
    def printStack(self):
        if len(self.arr) == 0:
            print("Stack is empty, nothing to print")
            return 
 
        print(self.arr)
 
 
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
