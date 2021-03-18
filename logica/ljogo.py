import random


class ljogo:
    # construtor de um jogo
    def __init__(self):
        # define um tabuleiro sem jogadas
        self.tabuleiro = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        # define dois jogadores
        self.jogadores = list(range(2))
        # define o jogador inicial aleatoriamente
        self.jogador_da_vez = random.randint(0, 1)

    # realiza uma jogada
    def jogar(self, jogada):
        # se a jogada esta disponivel
        if jogada in self.jogadas_disponiveis():
            # calcula a linha e coluna com base na jogada
            linha = 2 - ((jogada - 1) // 3)
            coluna = (jogada - 1) % 3

            # se a posicao no tabuleiro estiver disponivel
            # e se o jogo ainda não terminou
            if self.tabuleiro[linha][coluna] == None and not self.terminou():
                # realiza a jogada
                self.tabuleiro[linha][coluna] = self.jogador_da_vez
                # passa a vez
                self.passar_vez()

    # lista as jogadas disponiveis
    def jogadas_disponiveis(self):
        # instancia uma lista vazia de jogadas
        disponiveis = list()

        # busca as jogadas no tabuleiro
        for i, marcacoes in enumerate(self.tabuleiro):
            for j, marcacao in enumerate(marcacoes):
                # se a jogada ainda nao foi feita
                if marcacao == None:
                    # calcula a jogada com base na linha e coluna
                    jogada = j + 3 * (2 - i) + 1
                    # insere a joga na lista de jogadas disponiveis
                    disponiveis.append(jogada)

        # retorna as jogadas ordenadas de forma crescente
        return sorted(disponiveis)

    # consulta o vencedor do jogo
    def vencedor(self):
        # # busca entre os jogadores
        for jogador in self.jogadores:
            # se ha qualquer linha onde todas as jogadas pertencem ao jogador
            if any(all(jogada == jogador for jogada in linha) for linha in self.tabuleiro):
                return jogador  # retorna o jogador como vencedor

            # se ha qualquer coluna onde todas as jogadas pertencem ao jogador
            if any(all(linha[j] == jogador for linha in self.tabuleiro) for j in range(3)):
                return jogador  # retorna o jogador como vencedor

            # se ha qualquer diagonal onde todas as jogadas pertencem ao jogador
            if any(all(marcacao == jogador for marcacao in marcacoes) for marcacoes in
                   [[self.tabuleiro[0][0], self.tabuleiro[1][1], self.tabuleiro[2][2]],
                    [self.tabuleiro[0][2], self.tabuleiro[1][1], self.tabuleiro[2][0]]]):
                return jogador  # retorna o jogador como vencedor

    # passa a vez ao outro jogador
    def passar_vez(self):
        # se o jogador da vez for o jogador 0 o proximo jogador sera o jogador 1
        # se nao o proximo jogador sera o jogador 0
        self.jogador_da_vez = 1 if self.jogador_da_vez == 0 else 0

    # valida se o jogo ja terminou
    def terminou(self):
        # retorna sim(True) se nao houver jogadas disponiveis
        # ou se ha um jogador vencedor
        return not self.ha_jogadas_disponiveis() or self.ha_vencedor()

    # valida se ha jogadas disponiveis
    def ha_jogadas_disponiveis(self):
        # retorna sim(True) se houver qualquer jogada disponivel
        return any(self.jogadas_disponiveis())

    # valida se ha um vencedor
    def ha_vencedor(self):
        # retorna sim(True) se hover um jogador vencedor
        return self.vencedor() is not None
