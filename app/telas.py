import os
import random
from app.modelos import ItemMenu

NOME_TELA_MENU = 'MENU'
NOME_TELA_JOGO = 'JOGO'
NOME_TELA_MANUAL = 'MANUAL'
NOME_TELA_PLACAR = 'PLACAR'
NOME_TELA_SAIDA = 'SAIDA'


def alterar_para_tela_jogo(motor):
    motor.alterar_tela(NOME_TELA_JOGO)


def alterar_para_tela_manual(motor):
    motor.alterar_tela(NOME_TELA_MANUAL)


def alterar_para_tela_menu(motor):
    motor.alterar_tela(NOME_TELA_MENU)


def alterar_para_tela_placar(motor):
    motor.alterar_tela(NOME_TELA_PLACAR)


def alterar_para_tela_saida(motor):
    motor.alterar_tela(NOME_TELA_SAIDA)


def limpar_tela():
    os.system('cls')


def imprimir_tabuleiro(motor):
    tabuleiro_str = str()

    for i, linha in enumerate(motor.partida.tabuleiro):
        if i > 0:
            tabuleiro_str += '\n―――――――――――\n'
        for j, jogada in enumerate(linha):
            if j > 0:
                tabuleiro_str += '|'
            if jogada != None:
                tabuleiro_str += f' {motor.jogadores[jogada].marcacao} '
            else:
                tabuleiro_str += '   '

    print(tabuleiro_str)


def novo_comando(mensagem=str()):
    if mensagem != str():
        mensagem = f'{mensagem} '
    return input(f'{mensagem}> ').upper()


class TelaMenu:
    def __init__(self, motor):
        self.__motor = motor

    def atualizar(self):
        limpar_tela()
        self.__exibir_menu()

    def __exibir_menu(self):
        menu = dict()

        itens_a_numerar = [
            ItemMenu('NOVO JOGO', alterar_para_tela_jogo),
            ItemMenu('MANUAL DO JOGO', alterar_para_tela_manual),
            ItemMenu('SAIR', alterar_para_tela_saida)]

        if self.__motor.partida and self.__motor.partida.em_andamento():
            continuar_partida = ItemMenu('CONTINUAR', alterar_para_tela_jogo)
            itens_a_numerar.insert(0, continuar_partida)

        menu_telas = dict((str(posicao + 1), item)
                          for posicao, item in enumerate(itens_a_numerar))

        menu.update(menu_telas)
        menu.update(self.__motor.comandos_globais)

        for chave, item in menu_telas.items():
            print(f'{chave}. {item.descricao}')

        comando = novo_comando()

        if comando in menu:
            menu[comando].funcao(self.__motor)
            if menu[comando].descricao == 'NOVO JOGO':
                self.__motor.nova_partida()


class TelaJogo:
    def __init__(self, motor):
        self.__motor = motor

    def atualizar(self):
        # apaga tudo que tem na tela
        limpar_tela()

        if self.__motor.partida.em_andamento():
            # imprime na tela, os jogadores e o tabuleiro
            self.__imprimir_jogadores()
            imprimir_tabuleiro(self.__motor)

            self.__realizar_jogada()
        else:
            self.__motor.alterar_tela(NOME_TELA_PLACAR)

    def __imprimir_jogadores(self):
        for index, jogador in enumerate(self.__motor.jogadores):
            vez = '[vez] ' if index == self.__motor.partida.jogador_da_vez else ''
            print(f'{vez}{jogador.nome}\'{jogador.marcacao}\'')

    def __realizar_jogada(self):
        jogadas_disponiveis = self.__motor.partida.jogadas_disponiveis()

        if not self.__motor.jogadores[self.__motor.partida.jogador_da_vez].ia:
            comando = novo_comando()

            if comando.isnumeric():
                jogada = int(comando)
                if jogada in jogadas_disponiveis:
                    self.__motor.partida.jogar(jogada)
            else:
                comandos_globais = self.__motor.comandos_globais
                if comando in comandos_globais:
                    comandos_globais[comando].funcao(self.__motor)
        else:
            index_aleatorio = random.randrange(0, len(jogadas_disponiveis))
            jogada_aleatoria = jogadas_disponiveis[index_aleatorio]
            self.__motor.partida.jogar(jogada_aleatoria)


class TelaPlacar:
    def __init__(self, motor):
        self.__motor = motor

    def atualizar(self):
        limpar_tela()

        self.__exibir_vencedor()
        imprimir_tabuleiro(self.__motor)

        comandos_globais = self.__motor.comandos_globais

        comando = novo_comando()

        if comando in comandos_globais:
            comandos_globais[comando].funcao(self.__motor)
        else:
            alterar_para_tela_menu(self.__motor)

    def __exibir_vencedor(self):
        if self.__motor.partida.terminou():
            print('Partida finalizada')

            if self.__motor.partida.ha_vencedor():
                vencedor = self.__motor.jogadores[
                    self.__motor.partida.vencedor()
                ]
                print(f'Vencedor: {vencedor.nome} [{vencedor.marcacao}]')
            else:
                print('Empate')
        else:
            print('Partida em andamento')


class TelaManual:
    def __init__(self, motor):
        self.__motor = motor

    def atualizar(self):
        limpar_tela()

        self.__imprimir_manual_jogadas()
        self.__imprimir_manual_comandos_globais()

        comando = novo_comando()

        comandos_globais = self.__motor.comandos_globais

        if comando in comandos_globais:
            comandos_globais[comando].funcao(self.__motor)
        else:
            alterar_para_tela_menu(self.__motor)

    def __imprimir_manual_jogadas(self):
        print(('-'*14) + '[JOGADAS]' + ('-'*15))
        print('Escolha sua jogada com base nos números do teclado númerico')
        print(' 7 | 8 | 9 ')
        print('―――――――――――')
        print(' 4 | 5 | 6 ')
        print('―――――――――――')
        print(' 1 | 2 | 3 ')

    def __imprimir_manual_comandos_globais(self):
        print(('-'*10) + '[COMANDOS_GLOBAIS]' + ('-'*10))
        print('H: Exibe a tela de manual do jogo')
        print('M: Exibe a tela de menu principal')
        print('Q: Fecha a aplicação')


class TelaSaida:
    def __init__(self, motor):
        self.__motor = motor

    def atualizar(self):
        limpar_tela()
        print('Obrigado por Jogar')
        print('Jogo da Velha em Python')
        print('Criado por Bruno Aragão')
        self.__motor.finalizar()
