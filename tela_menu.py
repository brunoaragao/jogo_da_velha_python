import utilitarios_de_tela as utils
import logica_jogo as jogo
import tela_menu
import tela_jogo
import tela_manual
import tela_despedida


def exibir():
    utils.limpar_tela()

    print('---- Menu Principal ----')

    menu = {
        1: {'mensagem': 'Jogar', 'tela': tela_jogo},
        2: {'mensagem': 'Manual do Jogo', 'tela': tela_manual},
        3: {'mensagem': 'Sair', 'tela': tela_despedida}
    }

    utils.imprimir_menu(menu)
    escolha = utils.escolher()

    tela = menu[escolha]['tela'] if escolha in menu else tela_menu

    if tela == tela_jogo:
        jogo.novo_jogo()

    tela.exibir()
