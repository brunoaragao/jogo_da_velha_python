import random
import logica_jogo as jogo

tabuleiro = None
vez = None

jogadores = {
    1: {'nome': 'Jogador', 'marcacao': 'X', 'ia': False},
    2: {'nome': 'Máquina', 'marcacao': 'O', 'ia': True}
}


def novo_jogo(vez_inicial=None):
    jogo.vez = vez_inicial if vez_inicial != None else random.randrange(1, 3)
    jogo.tabuleiro = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]


def jogar(jogada):
    jogador = jogador_da_vez()

    linha = (jogada - 1) // 3
    coluna = (jogada - 1) % 3

    tabuleiro[linha][coluna] = jogador['marcacao']

    passar_vez()


def jogadas_disponiveis():
    disponiveis = []

    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == ' ':
                index = 3 * linha + (coluna + 1)
                disponiveis.append(index)

    return disponiveis


def jogador_da_vez():
    return jogadores[vez]


def vencedor():
    for jogador in jogadores.values():
        marcacao = jogador['marcacao']
        # jogadas horizontais
        for linha in tabuleiro:
            if linha.count(marcacao) == 3:
                return jogador
        # jogadas verticais
        for col in range(3):
            if all(linha[col] == marcacao for linha in tabuleiro):
                return jogador
        # jogadas diagonais
        if all(valor == marcacao for valor in [tabuleiro[0][0], tabuleiro[1][1], tabuleiro[2][2]]):
            return jogador
        if all(valor == marcacao for valor in [tabuleiro[0][2], tabuleiro[1][1], tabuleiro[2][0]]):
            return jogador


def passar_vez():
    jogo.vez = 2 if jogo.vez == 1 else 1


def terminou():
    return not ha_jogadas_disponiveis() or ha_vencedor()


def ha_jogadas_disponiveis():
    return any(jogadas_disponiveis())


def ha_vencedor():
    return vencedor() is not None
