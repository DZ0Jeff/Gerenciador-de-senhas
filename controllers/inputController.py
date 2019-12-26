from views.visual import lines

def inputs():
    while True:
        print("Insira sua opção abaixo")
        choose = int(input("> "))
        
        if choose == 1:
            print("Você escolheu ver senhas salvas!")

        elif choose == 2:
            print("Você escolheu adicionar senha!")

        elif choose == 3:
            print("Você escolheu editar senha!")

        elif choose == 4:
            print("Você escolheu deletar senha!")

        elif choose == 5:
            print("Volte sempre!")
            break

        else:
            print("[ERROR] check your code!")

    lines()
