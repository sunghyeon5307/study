class CircularQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.list = [None]*capacity
        self.front = 0
        self.rear = 0
    
def isEmpty(self):
    if self.front == self.rear:
        return True
    else:
        return False

def isFull(self):
    if self.rear == self.capacity:
        return True
    else:
        return False

def enqueue(self,item):
    if self.isFull:
        print("가득")
    else:
        self.rear += 1
def dequeue(self):

# enqueue (1)(2)(3)(4)(5), dequeue()()()