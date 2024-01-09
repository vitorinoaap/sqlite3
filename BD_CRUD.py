import sqlite3 as lite
from menu_bd_crud import *

con = lite.connect('dados.db')  #Cria conexao

cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS invent(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, data DATE, '
            'valor DECIMAL, imagem TEXT)')

def inserir_form(i):
    #Insere dados
    with con:
        cur = con.cursor()
        query = 'INSERT INTO invent(nome, local, data, valor, imagem) VALUES(?,?,?,?,?)'
        cur.execute(query, i)


def ver_form():
    #Ver os dados
    with con:
        cur = con.cursor()
        query = 'SELECT * FROM invent'
        cur.execute(query)

        filas = cur.fetchall()

        for i in filas:
            for c in range(0, 6):
                print(i[c], ' ', end='')
            print()


def atualizar_form(i):
    #Atualizar form
    with con:
        cur = con.cursor()
        query = 'UPDATE invent SET nome=?, local=?, data=?, valor=?, imagem=? WHERE id=?'
        cur.execute(query, i)


def deletar_form(i):
    #Deletar
    with con:
        cur = con.cursor()
        query = 'DELETE FROM invent WHERE id=?'
        cur.execute(query, i)


def ver_individual(i):
    #Ver os dados individual
    with con:
        cur = con.cursor()
        query = 'SELECT * FROM invent WHERE id=?'
        cur.execute(query, i)
        fila = cur.fetchall()
        print(fila)


# Abaixo, o controle do menu.  Poderia ter colocado em um arquivo a parte...
opções = ['Insere dados', 'Altera', 'Deleta', 'Ver individual', 'Ver todos', 'Sair']

while True:
    resposta = menu(opções)
    if resposta == 1:
        dados = ['mesa de pingpong', 'sala de jogos', '08/01/2024', 2198.00, 'c:imagens']
        inserir_form(dados)
    elif resposta == 2:
        cabecalho(opções[1])
        dados = ['fogo2', 'cozinha', '08/01/2024', 198.97, 'c:imagens', 9]
        atualizar_form(dados)
    elif resposta == 3:
        deletar_dados = '444444444444'
        deletar_form(deletar_dados)
    elif resposta == 4:
        ver_individual('2')
    elif resposta == 5:
        ver_form()
    elif resposta == 6:
        cabecalho('Finalizando...')
        break
    else:
        print('\033[31mERRO: Opção inválida\033[m')
