# Array implementation of Queue 

class Queue:
    
    # below constructor initializes a new empty Queue
    def __init__(self):
        print("New Queue object is created just now")
        self.arr = []
        
    # below function should insert a new node at tail position
    def enqueue(self, value):
         self.arr.append(value)
         print(value, "enqueued successfully")
         
    
    # below function should remove the front node from linkedlist
    def dequeue(self):
        if len(self.arr) == 0:
            print("Queue is empty, nothing to delete")
            return
        
        
        print(self.arr[0], "deleted successfully")
        self.arr.pop(0)
        
    
    # below function just prints the Queue
    def printQueue(self):
        if len(self.arr) == 0:
            print("Queue is empty, nothing is there to print")
            return
        print(self.arr)

        
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
