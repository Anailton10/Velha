from random import randrange
branco = " "
jgd1 = ['X']
jgd2 = ['O']


def layout():
    velha = [
        [branco, branco, branco],
        [branco, branco, branco],
        [branco, branco, branco]
    ]
    return velha


def mostralayout(velha):
    print('  0        1         2\n')
    for i in range(3):
        print('      │  '.join(velha[i]))
        print(i)
        if i < 2:
            print('-' * 25)

def getInput(msg):
    try:
        n = int(input(msg))
        if n > 2:
            return getInput(msg)
    except:
        print('Jogada Inválida..')
        return n

def fazMovimento(linha, coluna, velha, jogador):
    velha[linha][coluna] = jgd1[jogador]


def verificaMovimento(linha, coluna, velha):
    if velha[linha][coluna] == branco:
        return True
    else:
        return False


def verificaGanhador(velha):
    pass


def cpujoga(velha, cpu):
    linha = randrange(0, 3)
    coluna = randrange(0, 3)
    while velha[linha][coluna] != branco:
        linha = randrange(0, 3)
        coluna = randrange(0, 3)
        velha[linha][coluna] = jgd2[cpu]





