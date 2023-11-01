from program_internal_form import ProgramInternalForm
from symbol_table import SymbolTable


class Program:

    def __init__(self):
        self.identifier_table = SymbolTable(107)
        self.literal_table = SymbolTable(107)
        self.pif = ProgramInternalForm()
