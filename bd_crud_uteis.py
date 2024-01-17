from datetime import datetime

def data_valida(msg=''):
    """
    Retorna uma data válida no formato dd/mm/aaaa.
    :param msg: opcional, mensagem a ser exibida no input
    :return: uma data
    """
    while True:
        try:
            dt = str(input(msg))
            datetime.strptime(dt, '%d/%m/%Y')

        except (ValueError, TypeError):
            print('Erro: Digite uma data válida.')

        except KeyboardInterrupt:
            print('  O usuário preferiu não informar os dados')
            dt = ''
            break
        else:
            break
    return dt


def linha(tam=42):
    """
    Desenha uma linha com o símbolo '-', 42 vezes.
    :param tam: quantidade de repetições
    :return: imprime a linha x vezes
    """
    return '-' * tam


def cabecalho(txt):
    """
    Imprime a msg repassada centralizada
    :param txt: msg a ser impressa
    :return:
    """
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaint(msg=''):
    """
    Lê um num inteiro e testa se ok
    :param msg: opcional, imprime msg repassada
    :return: o número inteiro
    """
    while True:
        try:
            n = int(input(msg))

        except (ValueError, TypeError):
            print('Erro: Digite um número inteiro válido.')

        except KeyboardInterrupt:
            print('  O usuário preferiu não informar os dados')
            n = 0
            break
        else:
            break
    return n


def leiafloat(msg=''):
    """
    Lê um num real e testa se ok
    :param msg: opcional, msg a ser exibida no input
    :return: o num real
    """
    while True:
        try:
            n = float(input(msg))

        except (ValueError, TypeError):
            print('Erro: Digite um número real válido.')

        except KeyboardInterrupt:
            print('  O usuário preferiu não informar os dados')
            n = 0
            break
        else:
            break
    return n


def confirma_sn(msg):
    """
    Retorna True se resposta = 'S'
    :param msg: Mensagem a ser exibida
    :return: Verdadeiro ou Falso
    """
    conf = ' '
    while conf not in 'SN':
        conf = str(input(msg)).upper().strip()
    return conf == 'S'


def menu(lista):
    """
    Imprime na tela as opções do menu
    :param lista: opções a serem escolhidas
    :return: o número inteiro da opção escolhida
    """
    cabecalho('MENU PRINCIPAL')
    # i = 1
    # for item in lista:
    #     print(f'{i} - {item}')
    #     i += 1

    for i, item in enumerate(lista, 1):
        print(f'{i} - {item}')

    print(linha())

    while True:
        opc = leiaint('Sua opção: ')
        if opc in range(1, len(lista) + 1):
            break
        else:
            print('\033[31mERRO: Opção inválida\033[m')

    return opc
