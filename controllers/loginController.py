from models.admin import Admin

def login():
    loginUsers = Admin()

    usuario = str(input('Usuario: '))
    senha = str(input('Senha: '))

    users = loginUsers.checkUser(usuario, senha)
    if users.fetchall():
        return True
    else:
        return False