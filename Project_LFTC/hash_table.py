
class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = [
            [] for _ in range(self.size)
        ]

    def hash(self, key):
        return (sum([ord(letter) for letter in key]) % self.size) + 1

    def get(self, key):
        position = self.hash(key)

        for e_key, e_value in self.table[position]:
            if key == e_value:
                return e_value
        return None

    def set(self, key, value):
        position = self.hash(key)
        pair = (key, value)
        position_list = self.table[position]

        if pair in position_list:
            position_list.remove(pair)
        position_list.append(pair)

    def search(self, key):
        position = self.hash(key)

        for e_key, _ in self.table[position]:
            if e_key == key:
                return True
        return False
