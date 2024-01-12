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
            if n in range(1, qtd+1):
                break
            else:
                n = 0
                print('\033[31mERRO: Opção inválida\033[m')
    return n


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
