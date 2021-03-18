class tplacar:
    def __init__(self, jogo, jogadores, utilitarios):
        self.jogo = jogo
        self.jogadores = jogadores
        self.utilitarios = utilitarios

    def exibir(self):
        self.utilitarios.limpar_tela()
        self.exibir_vencedor()
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

    def exibir_vencedor(self):
        if self.jogo.terminou():
            if self.jogo.ha_vencedor():
                vencedor = self.jogadores[self.jogo.vencedor()]
                print(f'- Vencedor: {vencedor.nome} [{vencedor.marcacao}]')
            else:
                print('- Empate')
        else:
            print('O jogo ainda não terminou')
