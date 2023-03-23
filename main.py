from sistema import *
jogador = 0
cpu = 1
velha = layout()
mostralayout(velha)
ganhador = verificaGanhador(velha)
while not ganhador:
    linha = getInput('Digite a linha: ')
    coluna = getInput('Digite a coluna: ')
    cpujoga(velha, cpu)
    if fazMovimento(velha, linha, coluna, jogador):
        verificaMovimento(linha, coluna, velha)
    else:
        print('Posição ja foi ocupada.')
    ganhador = verificaGanhador(velha)