import sqlite3

class Data:

    def __init__(self):
        self.connection = sqlite3.connect('./sql/data.db')
        self.cursor = self.connection.cursor()
        self.createTable()

    def createTable(self):
        return self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS senhas (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                name        VARCHAR(255),
                password    VARCHAR(255)
            )'''
        )

    def insert(self, inserter):
        insertInput = inserter['name'], inserter['password']

        self.cursor.execute('''INSERT INTO senhas(name, password) VALUES(?,?)''', insertInput)
        self.connection.commit()
        self.closeConnection()

    def selectAll(self):
        query = self.cursor.execute("SELECT * FROM senhas")
        result = ''

        for item in query:
            result += f"\nId: {item[0]} - Conta: {item[1]} - senha: {item[2]}"

        self.closeConnection()
        return result

    def update(self, target):
        innerInput = target['name'], target['password'], target['id']
        sql = '''
            UPDATE senhas 
                SET name = ?, 
                password = ? 
            WHERE id = ? 
        '''

        self.cursor.execute(sql, innerInput)
        self.connection.commit()
        self.closeConnection()

    def delete(self, id):
        id = (id, )
        self.cursor.execute(f"DELETE FROM senhas WHERE id = ?", id)
        self.connection.commit()
        self.closeConnection()

    def closeConnection(self):
        return self.connection.close()