import sqlite3

class Admin:
    def __init__(self):
        self.database = sqlite3.connect('./sql/users.db')
        self.cursor = self.database.cursor()
        self.createLoginTable()

    def createLoginTable(self):
        return self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS login (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                name        VARCHAR(255),
                password    VARCHAR(255)
            )'''
        )

    def checkUser(self, user, password):
        result = self.cursor.execute('''SELECT * FROM login WHERE name = ? AND password = ?''', (user, password))
        return result


    def register(self, user, password):
        register = user , password

        self.cursor.execute('''INSERT INTO login(name, password) VALUES(?, ?)''', register)
        self.database.commit()
