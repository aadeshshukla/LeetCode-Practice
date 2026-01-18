#stack implementation using list
# class Stack:
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         return len(self.items) == 0

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             raise IndexError("pop from empty stack")

#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             raise IndexError("peek from empty stack")

#     def size(self):
#         return len(self.items)

# s=Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# print(s.pop())
# print(s.peek())
# print(s.size())
# print(s.is_empty())
#_______________________________________________________________
#queue implementation using list
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("front from empty queue")

    def size(self):
        return len(self.items)
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.front())
print(q.size())
print(q.is_empty())
    
    