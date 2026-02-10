# dictionary data structure implementation in python
class Dictionary:
    def __init__(self):
        self.dict = {}

    def add(self, key, value):
        self.dict[key] = value

    def remove(self, key):
        if key in self.dict:
            del self.dict[key]

    def get(self, key):
        return self.dict.get(key, None)

    def contains(self, key):
        return key in self.dict

    def size(self):
        return len(self.dict)

    def clear(self):
        self.dict.clear()
# Example usage
if __name__ == "__main__":
    my_dict = Dictionary()
    my_dict.add("name", "Alice")
    my_dict.add("age", 30)
    print(my_dict.get("name"))  # Output: Alice
    print(my_dict.contains("age"))  # Output: True
    print(my_dict.size())  # Output: 2
    my_dict.remove("name")
    print(my_dict.get("name"))  # Output: None
    my_dict.clear()
    print(my_dict.size())  # Output: 0

# hash table implementation in python
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    return
            self.table[index].append((key, value))

    def remove(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    return

    def get(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def contains(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return True
        return False

    def size(self):
        count = 0
        for bucket in self.table:
            if bucket is not None:
                count += len(bucket)
        return count

    def clear(self):
        self.table = [None] * self.size

# Example usage
if __name__ == "__main__":
    my_hash_table = HashTable()
    my_hash_table.add("name", "Alice")
    my_hash_table.add("age", 30)
    print(my_hash_table.get("name"))  # Output: Alice
    print(my_hash_table.contains("age"))  # Output: True
    print(my_hash_table.size())  # Output: 2
    my_hash_table.remove("name")
    print(my_hash_table.get("name"))  # Output: None
    my_hash_table.clear()
    print(my_hash_table.size())  # Output: 0
    