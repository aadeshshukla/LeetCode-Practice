class Linkedlist:
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

my_list1 = Linkedlist()
my_list1.append(10)
my_list1.append(20)
my_list1.append(30)
my_list1.display()
my_list2 = Linkedlist()
my_list2.append(40)
my_list2.append(50)
my_list2.append(60)
my_list2.display()

# Merging two linked lists
def merge_linkedlists(list1, list2):
    if not list1.head:
        return list2
    if not list2.head:
        return list1

    merged_list = Linkedlist()
    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.data <= current2.data:
            merged_list.append(current1.data)
            current1 = current1.next
        else:
            merged_list.append(current2.data)
            current2 = current2.next

    while current1:
        merged_list.append(current1.data)
        current1 = current1.next

    while current2:
        merged_list.append(current2.data)
        current2 = current2.next

    return merged_list
merged = merge_linkedlists(my_list1, my_list2)
merged.display()
