class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = value
        print(f'Inserted: ({key}, {value}) at index {index}')

    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            print(f'Deleted: ({key}, {self.table[index]}) from index {index}')
            self.table[index] = None
        else:
            print(f'Key {key} not found for deletion.')

    def traverse(self):
        print("Hash Table Contents:")
        for index, value in enumerate(self.table):
            if value is not None:
                print(f'Index {index}: {value}')
            else:
                print(f'Index {index}: None')

if __name__ == "__main__":
    hash_table = HashTable(size=10)
    hash_table.insert(1, 'A')
    hash_table.insert(2, 'B')
    hash_table.insert(3, 'C')
    hash_table.traverse()
    hash_table.delete(2)
    hash_table.traverse()
