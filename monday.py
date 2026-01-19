# stack implementation using a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
    def is_empty(self):
        return self.top is None
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.count += 1
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_node = self.top
        self.top = self.top.next
        self.count -= 1
        return popped_node.data
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data
    def size(self):
        return self.count
s=Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.peek())
print(s.size())
print(s.is_empty())
#_______________________________________________________________
# queue implementation using a linked list
class Queue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None
        self.count = 0
    def is_empty(self):
        return self.front_node is None
    def enqueue(self, item):
        new_node = Node(item)
        if self.rear_node:
            self.rear_node.next = new_node
        self.rear_node = new_node
        if not self.front_node:
            self.front_node = new_node
        self.count += 1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        dequeued_node = self.front_node
        self.front_node = self.front_node.next
        if not self.front_node:
            self.rear_node = None
        self.count -= 1
        return dequeued_node.data
    def front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.front_node.data
    def size(self):
        return self.count
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.front())
print(q.size())
print(q.is_empty())
