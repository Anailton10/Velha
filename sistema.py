branco = " "


class JgVelha:
    def __init__(self):
        self.__velha = [
            [branco, branco, branco],
            [branco, branco, branco],
            [branco, branco, branco]
        ]

    @property
    def velha(self):
        return self.__velha

    def printarLayout(self):
        print(' 0    1    2')
        for i in range(3):
            print('  │ '.join(self.velha[i]))
            if i < 2:
                print('-' * 12)

    def movimentoJogada(self, linha, coluna):
        self.velha[linha][coluna] = "X"
        self.__cpu()

    def __cpu(self):
        from random import randrange
        from time import sleep
        self.printarLayout()
        sleep(2)
        linha = randrange(0, 3)
        coluna = randrange(0, 3)
        while self.velha[linha][coluna] != branco:
            linha = randrange(0, 3)
            coluna = randrange(0, 3)
        self.velha[linha][coluna] = "O"

    def verificaMovimento(self, linha, coluna):
        if self.velha[linha][coluna] != branco:
            return True
        else:
            return False

    def verificaGanhador(self):
        for linha in range(3):
            if self.velha[linha][0] == self.velha[linha][1] and self.velha[linha][1] == self.velha[linha][2] and self.velha[linha][0] != branco:
                return self.velha[linha][0]

        for coluna in range(3):
            if self.velha[0][coluna] == self.velha[1][coluna] and self.velha[1][coluna] == self.velha[2][coluna] and self.velha[0][coluna] != branco:
                return self.velha[0][coluna]

        if self.velha[0][0] != branco and self.velha[0][0] == self.velha[1][1] and self.velha[1][1] == self.velha[2][2]:
            return self.velha[0][0]

        if self.velha[0][2] != branco and self.velha[0][2] == self.velha[1][1] and self.velha[1][1] == self.velha[2][0]:
            return self.velha[0][2]

        for linha in range(3):
            for coluna in range(3):
                if self.velha[linha][coluna] == branco:
                    return False

        return "EMPATE..."


