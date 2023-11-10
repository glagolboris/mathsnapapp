import sqlite3


class Db:
    def __init__(self):
        self.con = sqlite3.connect('history.db')
        self.cursorObj = self.con.cursor()
        self.cursorObj.execute(
            'CREATE TABLE IF NOT EXISTS history(equation TEXT, solution TEXT)')
        self.con.commit()

    def add_to_db(self, eq, sol):
        self.cursorObj.execute('INSERT INTO history VALUES(?, ?)', (eq, sol))
        self.con.commit()

    def getEquationList(self):
        result = self.cursorObj.execute('SELECT equation FROM history').fetchall()
        return result

    def clearAll(self):
        self.cursorObj.execute('DELETE FROM history')
        self.con.commit()

    def getSolution(self, eq):
        result = self.cursorObj.execute('SELECT solution FROM history WHERE equation = ?', (eq,)).fetchall()
        return result[0][0]


db = Db()
print(db.getEquationList())
