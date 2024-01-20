import sqlite3 as lite
from bd_crud_uteis import *

con = lite.connect('dados.db')  # Cria conexao

cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS invent(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, data DATE, '
            'valor DECIMAL, imagem TEXT)')


# Insere dados------------------------------------------------
def inserir_form():
    cabecalho('INSERE DADOS')
    desc = str(input('Descrição: '))
    local = str(input('Local: '))
    data = data_valida('Data: [DD/MM/AAAA] ')
    valor = leiafloat('Valor: R$')

    if confirma_sn('Confirma a inclusão? [S/N]'):
        dados = [desc, local, data, valor, 'c:imagens']
    else:
        return

    with con:
        query = 'INSERT INTO invent(nome, local, data, valor, imagem) VALUES(?,?,?,?,?)'
        cur.execute(query, dados)


# Ver os dados----------------------------------------------
def ver_form():
    with con:
        query = 'SELECT * FROM invent'
        cur.execute(query)

        filas = cur.fetchall()

        for i in filas:
            for c in range(0, 6):
                print(i[c], ' ', sep='|', end='')
            print()


# Atualizar----------------------------------------------------
def atualizar_form():
    cabecalho('ALTERA DADOS')
    reg = leiaint('Qual o num do registro? ')

    with con:
        query = 'SELECT * FROM invent WHERE id=?'
        cur.execute(query, [reg])
        fila = cur.fetchall()

    if len(fila) > 0:  # Encontrou o registro
        ident, desc, local, data, valor, imagem = fila[0]

        # Calcula quantidade de itens na tupla
        qtd_itens = itens_tupla(fila)

        # Imprime os itens
        descrição = ('Id.......: ', 'Descrição: ', 'Local....: ', 'Data.....: ', 'Valor....: ', 'Imagem...: ')
        for i in fila:
            for c in range(0, qtd_itens):
                print(f'{c} - {descrição[c]} {i[c]}')
            print()

        # LOOP PRA IR TROCANDO ATE NAO QUISER MAIS COM UM 0 PRA SAIR.
        item = 1
        while item > 0:
            while True:
                item = leiaint(f'Qual o item? Do 1 ao {qtd_itens - 1} para alterar, 0 para sair. ')
                if item in range(0, qtd_itens):
                    break

            match item:
                case 1:
                    desc = str(input('Descrição: '))
                case 2:
                    local = str(input('Local: '))
                case 3:
                    data = data_valida('Data: [DD/MM/AAAA] ')
                case 4:
                    valor = leiafloat('Valor: R$')
                case 5:
                    imagem = str(input('Imagem: '))

        # TESTA SE HOUVE ALTERAÇÃO, SE NÃO HOUVE NÃO ATUALIZA.
        dados = (ident, desc, local, data, valor, imagem)
        if dados != fila[0]:

            if confirma_sn('Confirma a alteração? [S/N]'):
                dados = [desc, local, data, valor, imagem, reg]
            else:
                return

            with con:
                query = 'UPDATE invent SET nome=?, local=?, data=?, valor=?, imagem=? WHERE id=?'
                cur.execute(query, dados)

    else:
        print('\033[31mERRO: Registro não encontrado.\033[m')


# Deletar----------------------------------------------------------------
def deletar_form():
    cabecalho('DELETA DADOS')
    reg = leiaint('Qual o num do registro? ')

    with con:
        query = 'SELECT * FROM invent WHERE id=?'
        cur.execute(query, [reg])
        fila = cur.fetchall()

    if len(fila) > 0:  # Encontrou o registro
        # Calcula quantidade de itens na tupla
        qtd_itens = itens_tupla(fila)

        # Imprime os itens
        descrição = ('Id.......: ', 'Descrição: ', 'Local....: ', 'Data.....: ', 'Valor....: ', 'Imagem...: ')
        print()
        for i in fila:
            for c in range(0, qtd_itens):
                print(f'{descrição[c]} {i[c]}')
            print()

        if confirma_sn('Confirma a exclusão? [S/N]'):
            with con:
                query = 'DELETE FROM invent WHERE id=?'
                cur.execute(query, [reg])
    else:
        print('\033[31mERRO: Registro não encontrado.\033[m')


# Ver os dados individual------------------------------------------------
def ver_individual():
    cabecalho('VER INDIVIDUAL')
    reg = leiaint('Qual o num do registro? ')

    with con:
        query = 'SELECT * FROM invent WHERE id=?'
        cur.execute(query, [reg])
        fila = cur.fetchall()

    if len(fila) > 0:  # Encontrou o registro
        # Calcula quantidade de itens na tupla
        qtd_itens = itens_tupla(fila)

        # Imprime os itens
        descrição = ('Id.......: ', 'Descrição: ', 'Local....: ', 'Data.....: ', 'Valor....: ', 'Imagem...: ')
        print()
        for i in fila:
            for c in range(0, qtd_itens):
                print(f'{descrição[c]} {i[c]}')
            print()
    else:
        print('\033[31mERRO: Registro não encontrado.\033[m')


# Sair do sistema----------------------------------------------------
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
