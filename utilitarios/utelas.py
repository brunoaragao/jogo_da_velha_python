import os


def limpar_tela():
    os.system('cls')


def imprimir_menu(menu):
    for index in menu:
        mensagem = menu[index]['mensagem']
        print(f'{index}. {mensagem}')


def escolher():
    return int(input('Digite o valor: '))
