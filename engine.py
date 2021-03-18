import random
from logica.ljogo import ljogo
from telas.tjogo import tjogo
from telas.tplacar import tplacar
from modelos.mjogador import mjogador
from utilitarios import utelas as utilitarios


class engine:
    def __init__(self):
        self.jogo = ljogo()
        self.jogadores = [
            mjogador('Jogador', 'X', ia=True),
            mjogador('Máquina', 'O', ia=True)
        ]
        self.tela = tjogo(self.jogo, self.jogadores, utilitarios)

    def reiniciar_jogo():
        self.jogo = ljogo()

    def rodar(self):
        while not self.jogo.terminou():
            self.tela.exibir()
            self.jogo.jogar(self.nova_jogada())

        placar = tplacar(self.jogo, self.jogadores, utilitarios)
        placar.exibir()

    def nova_jogada(self):
        jogadas_disponiveis = self.jogo.jogadas_disponiveis()

        if self.jogadores[self.jogo.jogador_da_vez].ia:
            index_aleatorio = random.randrange(0, len(jogadas_disponiveis))
            return jogadas_disponiveis[index_aleatorio]

        else:
            return utilitarios.escolher()
