import sqlite3
from views.visual import lines, title, menuHeader
from controllers.inputController import inputs

def main():
    title("Lista de senhas")
    menuHeader()
    inputs()


if __name__ == "__main__":
    main()