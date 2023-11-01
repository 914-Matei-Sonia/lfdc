import unittest

from symbol_table import SymbolTable


class SymbolTableTestCase(unittest.TestCase):

    def setUp(self):
        self.table = SymbolTable(107)

    def test(self):
        self.assertEqual(len(self.table.table), 0)
        self.table.insert("2")
        self.assertEqual(len(self.table.table), 1)
        self.assertTrue(self.table.search("2"))
        self.assertFalse(self.table.search("d"))
        self.assertIsNone(self.table.get("2"))
        self.table.delete("2")
        self.assertEqual(len(self.table.table), 0)
