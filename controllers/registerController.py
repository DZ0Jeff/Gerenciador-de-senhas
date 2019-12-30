from models.admin import Admin

def register():
    sql = Admin()

    user = str(input('Usuario: '))
    senha = str(input('Senha do usuario: '))

    sql.register(user, senha)