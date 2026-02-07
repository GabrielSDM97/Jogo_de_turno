from utilidades.cores import cor

def RoundJogador(txt):
    print('\n' + (int(len(txt)/2)-6) * '~', cor('Round do Jogador', 2), (int(len(txt)/2)-7) * '~')
    print(f'  {txt}')
    print((len(txt)+4)*'~', '\n')


def RoundMonstro(txt):
    print((int(len(txt)/2)-7) * '~', cor('Round do Monstro', 1), (int(len(txt)/2)-7) * '~')
    print(f'  {txt}')
    print((len(txt)+4)*'~')


def invInfo(lista):
    print(f'\n------ {cor('Inventário', 3)} ------')
    print(f'{' ':3}{'Item':<10}{'Nutrição'}')
    for pos in range(len(lista)):
        for chave, valor in lista[pos].items():
            print(f'{' ':3}{chave:<10}{valor}')
    print('------------------------')
