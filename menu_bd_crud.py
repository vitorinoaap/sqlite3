def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaint(msg, qtd):
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
    cabecalho('MENU PRINCIPAL')
    i = 1
    for item in lista:
        print(f'{i} - {item}')
        i += 1
    print(linha())
    opc = leiaint('Sua opção: ', len(lista))

    return opc
