import random
import utilitarios_de_tela as utils
import logica_jogo as jogo
import tela_jogo
import tela_menu
import tela_manual
import tela_despedida


def exibir():
    utils.limpar_tela()

    print('---- Tela de jogo ----')

    exibir_tabuleiro()

    if not jogo.terminou():
        exibir_jogador_da_vez()

        jogadas_disponiveis = jogo.jogadas_disponiveis()
        jogador = jogo.jogador_da_vez()

        if jogador['ia']:
            index_aleatorio = random.randrange(0, len(jogadas_disponiveis))
            jogada = jogadas_disponiveis[index_aleatorio]
        else:
            jogada = utils.escolher()

        if jogada in jogadas_disponiveis:
            jogo.jogar(jogada)

        tela_jogo.exibir()
    else:
        print('Fim de jogo')

        exibir_vencedor()

        menu = {
            1: {'mensagem': 'Novo Jogo', 'tela': tela_jogo},
            2: {'mensagem': 'Menu Principal', 'tela': tela_menu},
            3: {'mensagem': 'Manual do Jogo', 'tela': tela_manual},
            4: {'mensagem': 'Sair', 'tela': tela_despedida}
        }

        utils.imprimir_menu(menu)
        escolha = utils.escolher()

        tela = menu[escolha]['tela'] if escolha in menu else tela_manual

        if tela is tela_jogo:
            jogo.novo_jogo()

        tela.exibir()


def exibir_tabuleiro():
    tabuleiro = jogo.tabuleiro
    for linha in range(2, -1, -1):
        print(tabuleiro[linha])


def exibir_jogador_da_vez():
    jogador = jogo.jogador_da_vez()
    print(f'Vez de {jogador["nome"]} {jogador["marcacao"]} ')


def exibir_vencedor():
    if jogo.ha_vencedor():
        jogador = jogo.vencedor()
        nome = jogador['nome']
        marcacao = jogador['marcacao']
        print(f'O vencedor foi {nome} [{marcacao}]')
    else:
        print('Não houve um vencedor')
