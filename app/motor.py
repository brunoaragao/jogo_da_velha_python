from app import telas
from app.modelos import ItemMenu, Jogador
from app.partida import Partida
from app.telas import TelaSaida, TelaJogo, TelaManual, TelaMenu, TelaPlacar


class Motor:
    def __init__(self):
        self.__executando = False
        self.__partida = None
        self.__tela_exibida = None
        self.__telas = {
            telas.NOME_TELA_JOGO: TelaJogo(self),
            telas.NOME_TELA_MANUAL: TelaManual(self),
            telas.NOME_TELA_MENU: TelaMenu(self),
            telas.NOME_TELA_PLACAR: TelaPlacar(self),
            telas.NOME_TELA_SAIDA: TelaSaida(self)
        }
        self.__jogadores = [
            Jogador('Jogador', 'X'),
            Jogador('Máquina', 'O', ia=True)
        ]
        self.__comandos_globais = {
            'H': ItemMenu('MANUAL DO JOGO', telas.alterar_para_tela_manual),
            'M': ItemMenu('MENU PRINCIPAL', telas.alterar_para_tela_menu),
            'Q': ItemMenu('SAIR', telas.alterar_para_tela_saida)
        }

    @property
    def executando(self):
        return self.__executando

    @property
    def partida(self):
        return self.__partida

    @property
    def jogadores(self):
        return self.__jogadores

    @property
    def comandos_globais(self):
        return self.__comandos_globais

    def executar(self):
        if not self.executando:
            self.__executando = True

            self.__tela_exibida = self.__telas[telas.NOME_TELA_MENU]

            while self.executando:
                self.__tela_exibida.atualizar()

    def finalizar(self):
        self.__executando = False

    def alterar_tela(self, nome_tela):
        if nome_tela in self.__telas:
            self.__tela_exibida = self.__telas[nome_tela]

    def nova_partida(self):
        self.__partida = Partida()
