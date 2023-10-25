import hash_table


class SymbolTable:

    def __init__(self, size):
        self.table = hash_table.HashTable(size)

    def get_value_identifier(self, identifier):
        return self.table.get(identifier)

    def set_identifier(self, identifier, value):
        self.table.set(identifier, value)

    def search_identifier(self, identifier):
        return self.table.search(identifier)

      