# Linked list implementation of Queue 

# below class-node is used to create a new block of linked-list node each time
class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None 
        
class Queue:
    
    # below constructor initializes a new empty Queue
    def __init__(self):
        print("New Queue object is created just now")
        self.front = None 
        self.rear = None 
        # rear is same as tail 
        
    # below function should insert a new node at tail position
    def enqueue(self, value):
         newNode = Node(value)
         print(value, "enqueued successfully")
         if self.rear == None:
             self.front = self.rear = newNode 
             return
         
         self.rear.next = newNode 
         self.rear = newNode
         
    
    # below function should remove the front node from linkedlist
    def dequeue(self):
        if self.front == None:
            print("Queue is empty, nothing to delete")
            return
        
        frontNode = self.front 
        print(frontNode.val, "deleted successfully")
        self.front = self.front.next 
        del frontNode 
        
    
    # below function just prints the Queue
    def printQueue(self):
        if self.front == None:
            print("Queue is empty, nothing is there to print")
            return
        current = self.front 
        while current != None:
            print(current.val, end = " --> ")
            current = current.next 
        print() 

        
# new object initiated
Q1 = Queue()
Q2 = Queue() 

# empty
Q1.dequeue()
Q2.dequeue() 

# empty
Q1.printQueue()
Q2.printQueue()

# 10 times, inserted (50 to 60)
for i in range(50, 61):
    Q1.enqueue(i)
    
# should print from 50 to 60 in increasing order
Q1.printQueue()

# should insert values from 110 to 115
for i in range(110, 116):
    Q2.enqueue(i)
    
# should print values from 110 to 115
Q2.printQueue()

# deleting 50
Q1.dequeue()

# deleting 110
Q2.dequeue()

# should print from 51 to 60
Q1.printQueue()

# should print from 111 to 115
Q2.printQueue()

# should delete 51
Q1.dequeue()

# should delete 111
Q2.dequeue()

# should print values from 52 to 60
Q1.printQueue()

# should print values from 112 to 115
Q2.printQueue()
