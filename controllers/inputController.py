from views.visual import lines
from models.database import Data
from time import sleep

def inputs():
    
    sql = Data()

    print("Insira sua opção abaixo")
    choose = int(input("> "))
    
    if choose == 1:
        lines('-')
        result = sql.selectAll()

        if result == '':
            print('Vazio!, adicione as conta e senhas para salvar, para visualizar aqui')
        else :
            print(f"{result.center(40)}")

        lines('-')
        sleep(2)

    elif choose == 2:
        lines('-')

        inserter = {}
        inserter['name'] = str(input('Nome: '))
        inserter['password'] = str(input('senha: '))

        print('Inserindo...')
        sql.insert(inserter)

        lines('-')
        sleep(2)

    elif choose == 3:
        lines('-')

        inserter = {}
        inserter['id'] = str(input('Id: '))
        inserter['name'] = str(input('Nome: '))
        inserter['password'] = str(input('senha: '))
        sql.update(inserter)

        if sql.update(inserter):
            print("Dados atualizados com sucesso! :)")
        else:
            print('[ERRO] verifique os dados ou contate ajuda especialziada :(')

        lines('-')
        sleep(2)

    elif choose == 4:
        deleteId = int(input('Id da conta: '))
        
        if sql.delete(deleteId):
            print('Deletado com Sucesso :)')
        else:
            print('[ERRO] verifique os dados ou contate ajuda especialziada :(')
        
        sleep(2)

    elif choose == 5:
        print("Volte sempre!")
        sleep(1)
        quit()

    else:
        print("[ERROR] check your code!")
