class Jogador:
    def __init__(self, nome, marcacao, ia=False):
        self.nome = nome
        self.marcacao = marcacao
        self.ia = ia


class ItemMenu:
    def __init__(self, descricao, funcao):
        self.descricao = descricao
        self.funcao = funcao
