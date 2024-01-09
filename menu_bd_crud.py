def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaint(msg):
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


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    i = 1
    for item in lista:
        print(f'{i} - {item}')
        i += 1
    print(linha())
    opc = leiaint('Sua opção: ')

    return opc
