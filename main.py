from new import *

v = JgVelha()
ganhador = v.verificaGanhador()
while not ganhador:
    v.printarLayout()
    try:
        linha = int(input('Digite valor da linha:'))
        if linha > 2:
            linha = int(input('Digite valor da linha:'))
    except:
        print('Jogada Inválida!!')
        linha = int(input('Digite valor da linha:'))
    try:
        coluna = int(input('Digite a Coluna:'))
        if linha > 2:
            coluna = int(input('Digite a Coluna:'))
    except:
        print('Jogada Inválida!!')
        coluna = int(input('Digite a Coluna:'))
    if v.movimentoJogada(linha, coluna):
        v.verificaMovimento(linha, coluna)
    ganhador = v.verificaGanhador()



