import unittest

from utils.enums import Token
from structures.program_internal_form import ProgramInternalForm


class PIFTestCase(unittest.TestCase):

    def setUp(self):
        self.table = ProgramInternalForm()

    def test_something(self):
        self.assertEqual(len(self.table.tokens), 0)
        self.table.insert("'", Token.LITERAL)
        self.assertEqual(len(self.table.tokens), 1)

        # with self.assertRaises(KeyError):


