from ..logica.ljogo import exibir
# import telas.tjogo
# import telas.tmanual
# import telas.tdespedida
# import telas.tmenu


def exibir():
    utelas.limpar_tela()

    # menu = {
    #     1: {'mensagem': 'Jogar', 'tela': tjogo},
    #     2: {'mensagem': 'Manual do Jogo', 'tela': tmanual},
    #     3: {'mensagem': 'Sair', 'tela': tdespedida}
    # }

    print('---- Menu Principal ----')
    utelas.imprimir_menu(menu)
    escolha = utelas.escolher()

    # tela = menu[escolha]['tela'] if escolha in menu else tmenu

    # if tela == tjogo:
    #     ljogo.novo_jogo()

    # tela.exibir()
