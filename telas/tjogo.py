class tjogo:
    def __init__(self, jogo, jogadores, utilitarios):
        self.jogo = jogo
        self.jogadores = jogadores
        self.utilitarios = utilitarios

    def exibir(self):
        self.utilitarios.limpar_tela()
        self.exibir_jogadores()
        self.exibir_tabuleiro()

    def exibir_tabuleiro(self):
        impressao = str()

        for i, linha in enumerate(self.jogo.tabuleiro):
            if i > 0:
                impressao += '\n―――――――――――\n'
            for j, jogada in enumerate(linha):
                if j > 0:
                    impressao += '|'
                if jogada != None:
                    impressao += f' {self.jogadores[jogada].marcacao} '
                else:
                    impressao += '   '

        print(impressao)

    def exibir_jogadores(self):
        for index, jogador in enumerate(self.jogadores):
            simbolo_vez = ''
            if index == self.jogo.jogador_da_vez:
                simbolo_vez = '> '
            print(f'{simbolo_vez}{jogador.nome}[{jogador.marcacao}]')


# def exibir():
#     utils.limpar_tela()

#     print('---- Tela de jogo ----')

#     exibir_tabuleiro()

#     if not jogo.terminou():
#         exibir_jogador_da_vez()

#         jogadas_disponiveis = jogo.jogadas_disponiveis()
#         jogador = jogo.jogador_da_vez()

#         if jogador['ia']:
#             index_aleatorio = random.randrange(0, len(jogadas_disponiveis))
#             jogada = jogadas_disponiveis[index_aleatorio]
#         else:
#             jogada = utils.escolher()

#         if jogada in jogadas_disponiveis:
#             jogo.jogar(jogada)

#         tela_jogo.exibir()
#     else:
#         print('Fim de jogo')

#         exibir_vencedor()

#         menu = {
#             1: {'mensagem': 'Novo Jogo', 'tela': tela_jogo},
#             2: {'mensagem': 'Menu Principal', 'tela': tela_menu},
#             3: {'mensagem': 'Manual do Jogo', 'tela': tela_manual},
#             4: {'mensagem': 'Sair', 'tela': tela_despedida}
#         }

#         utils.imprimir_menu(menu)
#         escolha = utils.escolher()

#         tela = menu[escolha]['tela'] if escolha in menu else tela_manual

#         if tela is tela_jogo:
#             jogo.novo_jogo()

#         tela.exibir()


# def exibir_tabuleiro():
#     tabuleiro = jogo.tabuleiro
#     for linha in range(2, -1, -1):
#         print(tabuleiro[linha])


# def exibir_jogador_da_vez():
#     jogador = jogo.jogador_da_vez()
#     print(f'Vez de {jogador["nome"]} {jogador["marcacao"]} ')


# def exibir_vencedor():
#     if jogo.ha_vencedor():
#         jogador = jogo.vencedor()
#         nome = jogador['nome']
#         marcacao = jogador['marcacao']
#         print(f'O vencedor foi {nome} [{marcacao}]')
#     else:
#         print('Não houve um vencedor')
