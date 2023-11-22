from utils.error import LexicalErr
from scanner import Scanner
from utils.fa_reader import FiniteAutomata


def main():

    fa_path = "definitions/Fa.in"

    fa = FiniteAutomata()
    fa.read_fa(fa_path)
    fa.display_console()
    print(fa.check("1234556"))

    # program_path = "programs/program_err.in"
    # st_path = "out/ST.out"
    # pif_path = "out/PIF.out"
    # file = open(program_path, 'r')
    # scanner = Scanner(file)
    #
    # try:
    #     program = scanner.scan()
    #     print("Lexically correct.")
    #
    #     with open(st_path, 'w') as file:
    #         file.write(str(program.identifier_table.table) + "\n")
    #         file.write(str(program.literal_table.table))
    #
    #     with open(pif_path, 'w') as file:
    #         file.write(str(program.pif))
    #
    # except LexicalErr as e:
    #     print(e)


if __name__ == '__main__':
    main()

