from utils.error import LexicalErr
from scanner import Scanner


def main():
    program_path = "programs/program_err.in"
    st_path = "out/ST.out"
    pif_path = "out/PIF.out"
    file = open(program_path, 'r')
    scanner = Scanner(file)

    try:
        program = scanner.scan()
        print("Lexically correct.")

        with open(st_path, 'w') as file:
            file.write(str(program.identifier_table.table) + "\n")
            file.write(str(program.literal_table.table))

        with open(pif_path, 'w') as file:
            file.write(str(program.pif))

    except LexicalErr as e:
        print(e)


if __name__ == '__main__':
    main()

