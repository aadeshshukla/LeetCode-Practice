#stack implementation usilng linked list
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class Stack:
#     def __init__(self):
#         self.top = None

#     def is_empty(self):
#         return self.top is None

#     def push(self, data):
#         new_node = Node(data)
#         new_node.next = self.top
#         self.top = new_node

#     def pop(self):
#         if self.is_empty():
#             raise IndexError("pop from empty stack")
#         popped_node = self.top
#         self.top = self.top.next
#         return popped_node.data

#     def peek(self):
#         if self.is_empty():
#             raise IndexError("peek from empty stack")
#         return self.top.data
#     def display(self):
#         current = self.top
#         elements = []
#         while current:
#             elements.append(current.data)
#             current = current.next
#         return elements
# # Example usage:
# if __name__ == "__main__":
#     stack = Stack()
#     stack.push(10)
#     stack.push(20)
#     stack.push(30)
#     print("Stack elements:", stack.display())  
#     print("Top element:", stack.peek())        
#     print("Popped element:", stack.pop())      
#     print("Stack elements after pop:", stack.display())  
#     print("Is stack empty?", stack.is_empty())  
#     stack.pop()
#     stack.pop()
#     print("Is stack empty after popping all elements?", stack.is_empty())  
# ----------------------------------------------------------------------------------
# queue implementation using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def is_empty(self):
        return self.front is None
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_node.data
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.front.data
    def display(self):
        current = self.front
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements
# Example usage:
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Queue elements:", queue.display())  
    print("Front element:", queue.peek())        
    print("Dequeued element:", queue.dequeue())      
    print("Queue elements after dequeue:", queue.display())  
    print("Is queue empty?", queue.is_empty())  
    queue.dequeue()
    queue.dequeue()
    print("Is queue empty after dequeuing all elements?", queue.is_empty())
    