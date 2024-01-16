from datetime import datetime


def data_valida(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False


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


def leiaint(msg, qtd):
    """
    Lê um num inteiro e testa se ok
    :param msg: imprime msg repassada
    :param qtd: quantidade de opções a ser validada
    :return: o número inteiro referente a opção desejada
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
            if n in range(1, qtd + 1):
                break
            else:
                n = 0
                print('\033[31mERRO: Opção inválida\033[m')
    return n


def leiafloat(msg):
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
    i = 1
    for item in lista:
        print(f'{i} - {item}')
        i += 1
    print(linha())
    opc = leiaint('Sua opção: ', len(lista))
    return opc
