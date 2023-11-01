import unittest
from io import StringIO

from utils.error import LexicalErr
from scanner import Scanner


class ScannerTestCase(unittest.TestCase):

    def setUp(self):
        self.io = StringIO()
        self.scanner = Scanner(self.io)

    def test_something(self):
        with self.assertRaises(LexicalErr):
            self.scanner._scan_string('"')
        self.write("fsd")
        with self.assertRaises(LexicalErr):
            self.scanner._scan_string('"')
        self.write('dfasdf"')
        self.scanner._scan_string('"')
        self.write("fsd  `")
        with self.assertRaises(LexicalErr):
            self.scanner._scan_string('"')
        self.write("fsd  +")
        with self.assertRaises(LexicalErr):
            self.scanner._scan_string('"')

        self.write("234")
        with self.assertRaises(LexicalErr):
            self.scanner._scan_integer('0')
        self.scanner._scan_integer('3')

        self.write("/")
        self.assertEqual(self.scanner._scan_operator("+"), "+")
        self.write("/")
        self.assertEqual(self.scanner._scan_operator("="), "=")
        self.write("=")
        self.assertEqual(self.scanner._scan_operator("<"), "<=")

        self.write("fjdf794^#_")
        self.scanner.scan()
        self.write("fjdf~794^#_")
        with self.assertRaises(LexicalErr):
            self.scanner.scan()
        self.write("2fjdf~794^#_")
        with self.assertRaises(LexicalErr):
            self.scanner.scan()

    def write(self, text):
        self.io.truncate(0)
        self.io.seek(0)
        self.io.write(text)
        self.io.seek(0)
        self.scanner = Scanner(self.io)
