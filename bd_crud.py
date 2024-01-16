import sqlite3 as lite
from bd_crud_uteis import *

con = lite.connect('dados.db')  #Cria conexao

cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS invent(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, data DATE, '
            'valor DECIMAL, imagem TEXT)')


# Insere dados
def inserir_form():
    cabecalho('INSERE DADOS')
    desc = str(input('Descrição: '))
    local = str(input('Local: '))
    data = str(input('Data: [DD/MM/AAAA] '))
    print(data_valida(data))
    valor = leiafloat('Valor: R$')

    if confirma_sn('Confirma a inclusão? [S/N]'):
        dados = [desc, local, data, valor, 'c:imagens']
    else:
        return

    with con:
        cur = con.cursor()
        query = 'INSERT INTO invent(nome, local, data, valor, imagem) VALUES(?,?,?,?,?)'
        cur.execute(query, dados)


#Ver os dados
def ver_form():
    with con:
        cur = con.cursor()
        query = 'SELECT * FROM invent'
        cur.execute(query)

        filas = cur.fetchall()

        for i in filas:
            for c in range(0, 6):
                # print(i[c], ' ', end='')
                print(i[c], ' ', sep='|', end='')
            print()


#Atualizar
def atualizar_form():
    dados = ['fogo2', 'cozinha', '08/01/2024', 198.97, 'c:imagens', 9]
    with con:
        cur = con.cursor()
        query = 'UPDATE invent SET nome=?, local=?, data=?, valor=?, imagem=? WHERE id=?'
        cur.execute(query, dados)


#Deletar
def deletar_form():
    i = '5'
    with con:
        cur = con.cursor()
        query = 'DELETE FROM invent WHERE id=?'
        cur.execute(query, i)


#Ver os dados individual
def ver_individual():
    i = '8'
    with con:
        cur = con.cursor()
        query = 'SELECT * FROM invent WHERE id=?'
        cur.execute(query, i)
        fila = cur.fetchall()
        print(fila)


def sair():
    cabecalho('Finalizando...')
    quit()


def main():
    # Abaixo, o controle do menu.
    opções = ('Insere dados', 'Altera', 'Deleta', 'Ver individual', 'Ver todos', 'Sair')
    funções = {1: inserir_form, 2: atualizar_form, 3: deletar_form, 4: ver_individual, 5: ver_form, 6: sair}

    while True:
        resposta = menu(opções)
        funções[resposta]()


if __name__ == '__main__':
    main()
