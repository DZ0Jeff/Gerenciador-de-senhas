import sqlite3
from views.visual import lines

class Data:

    def __init__(self):
        self.connection = sqlite3.connect('./sql/data.db')
        self.cursor = self.connection.cursor()
        self.createTable()

    def createTable(self):
        return self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS senhas (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                account     VARCHAR(255),
                name        VARCHAR(255),
                password    VARCHAR(255)
            )'''
        )      

    def insert(self, inserter):
        insertInput = inserter['account'], inserter['name'], inserter['password']

        self.cursor.execute('''INSERT INTO senhas(account, name, password) VALUES(?,?,?)''', insertInput)
        self.connection.commit()

    def selectAll(self):
        query = self.cursor.execute("SELECT * FROM senhas")
        result = ''

        for item in query:
            result += f"""\n| Id: {item[0]} \n| Conta: {item[1]} \n| Conta: {item[2]} \n| senha: {item[3]} \n"""

        
        return result

    def update(self, target):
        innerInput = target['account'], target['name'], target['password'], target['id']
        sql = '''
            UPDATE senhas 
                SET account = ?,
                name = ?, 
                password = ? 
            WHERE id = ? 
        '''

        self.cursor.execute(sql, innerInput)
        self.connection.commit()

    def delete(self, id):
        id = (id, )
        self.cursor.execute(f"DELETE FROM senhas WHERE id = ?", id)
        self.connection.commit()

    def closeConnection(self):
        return self.connection.close()