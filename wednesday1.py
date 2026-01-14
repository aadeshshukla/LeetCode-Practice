class Linkdlist:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    def update(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                return
            current = current.next
    def insert_after(self, prev_data, new_data):
        current = self.head
        while current:
            if current.data == prev_data:
                new_node = self.Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next        
    def delete(self, key):
        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if not current:
            return
        if prev:
            prev.next = current.next
        else:
            self.head = current.next    
    def search(self,key):
        current=self.head
        while current:
            if current.data==key:
                return True
            current=current.next
        return False
ll = Linkdlist()
ll.append("Apple")
ll.append("Banana")
ll.append("Grapes")
ll.display()
ll.update("Banana", "Blueberry")
ll.display()
ll.delete("Apple")
ll.display()
ll.insert_after("Blueberry", "Orange")
ll.display()
print(ll.search("Grapes"))

