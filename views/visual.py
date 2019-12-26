def lines(lines=40):
    print("~" * lines)


def title(msg):
    lines()
    print(str(msg).center(40))
    lines()


def menuHeader():
    options = ["Ver senhas salvas", "adicionar senha", "editar senha", "deletar senha","sair"]

    for indice, option in enumerate(options):
        print(f"{indice + 1} -  {option}")
    lines()
