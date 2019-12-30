from views.visual import lines, title, menuHeader
from controllers.inputController import inputs
from controllers.loginController import login
from controllers.registerController import register


def main():
    log = False
    while not log:
        print(str('AUTENTICAÇÃO').center(40))
        logged = login()

        if(logged):
            log = True
        
        else:
            print("[ERRO] Usuario e/ou senha invalidos")
            print('Deseja registrar um usuario? (S/N)')
            option = str(input('> ')).lower()

            if option == "s":
                register()

    while True:
        title("Lista de senhas")
        menuHeader()
        inputs()


if __name__ == "__main__":
    main()