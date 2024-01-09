import sqlite3 as lite

con = lite.connect('dados.db')  #Cria conexao
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS invent(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, data DATE, '
            'valor DECIMAL, imagem TEXT)')
'''
import sqlite3 
import os.path 
connection = sqlite3.connect('config.db') 
c = connection.cursor() 
def create_table(): 
    c.execute('CREATE TABLE IF NOT EXISTS VideoCapture (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, value text)') 
    sql = 'SELECT * FROM VideoCapture WHERE name = ?' 
    search = 'NumCam' status = 0 
    for row in c.execute(sql, (search,)): 
        status = 1 
        else: 
        if status == 1: 
            print('Ja cadstrado') 
            else: 
            c.execute("INSERT INTO VideoCapture(name, value) VALUES('NumCam', 4)")
'''