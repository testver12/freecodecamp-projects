class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        if not isinstance(key, str):
            raise ValueError('Key must be a string')
        hash_sum = 0
        for char in key:
            hash_sum += ord(char)
        return hash_sum

    def add(self, key, value):
        hash_value = self.hash(key)
        if hash_value not in self.collection:
            self.collection[hash_value] = {}
        self.collection[hash_value][key] = value
        return self.collection[hash_value][key]

    def remove(self, key):
        hash_value = self.hash(key)
        if hash_value in self.collection and key in self.collection[hash_value]:
            del self.collection[hash_value][key]
            if not self.collection[hash_value]:
                del self.collection[hash_value]

    def lookup(self, key):
        hash_value = self.hash(key)
        if hash_value in self.collection and key in self.collection[hash_value]:
            return self.collection[hash_value][key]
        return None


# Example usage
q = HashTable()
q.add('dear', 102)
q.add('read', 101)

print('before', q.collection)

q.remove('dear')

print('after ', q.collection)
