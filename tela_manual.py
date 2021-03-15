import utilitarios_de_tela as utils
import logica_jogo as jogo
import tela_manual
import tela_jogo
import tela_menu
import tela_despedida


def exibir():
    utils.limpar_tela()

    print('---- Manual do Jogo ----')
    print('Escolha um local para jogar com base nos números do teclado númerico')
    print('[7, 8, 9]')
    print('[4, 5, 6]')
    print('[1, 2, 3]')

    menu = {
        1: {'mensagem': 'Jogar', 'tela': tela_jogo},
        2: {'mensagem': 'Menu Principal', 'tela': tela_menu},
        3: {'mensagem': 'Sair', 'tela': tela_despedida}
    }

    utils.imprimir_menu(menu)
    escolha = utils.escolher()

    tela = menu[escolha]['tela'] if escolha in menu else tela_manual

    if tela is tela_jogo:
        jogo.novo_jogo()

    tela.exibir()
