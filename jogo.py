from random import randint, choice
from time import sleep
from utilidades.mp3 import som
from engineJogo import textos


def evento1():
    print('\nVocê não achou nada, continue explorando...')
    som("audios/explorando.mp3")


def evento2():
    print('\nVocê encontrou o ítem ', end='')
    inventário.append(choice(drop))
    for pos in range(-1, 0):
        for chave in inventário[pos].keys():
            print(f'{chave},', end=' ')
            print('em sua exploração!')
    som("audios/loot.mp3")


def evento3():
    som("audios/encontro_monstro.mp3")
    while True:
        combate = str(
            input('\nVocê encontrou um monstro, deseja combatê-lo (S/N)? ').strip()[0])
        if combate in 'Ss':
            conflito()
            break
        elif combate in 'Nn':
            print('\nVocê decidiu poupá-lo!')
            som("audios/explorando.mp3")
            break
        else:
            print('\nOpção incorreta, tente novamente!')


def conflito():
    global hp
    hp_inimigo = randint(80, 120)
    print(f'\nHP do monstro: {hp_inimigo}')
    print(f'HP do jogador: {hp}')
    while True:
        decisão = str(input('\nAtacar [1] / Acessar o inventário [2]? ').strip()[0])
        if decisão != '1' and decisão != '2':
            print('\nOpção incorreta, tente novamente!')
        elif decisão == '1':
            dano = randint(10, 30)
            hp_inimigo -= dano
            som("audios/jogador.mp3")
            textos.RoundJogador(f'Dano: {dano} - HP do monstro: {hp_inimigo}')
            sleep(1)
            if hp_inimigo <= 0:
                print('Você derrotou o monstro!\n')
                print(f'Os itens', end=' ')
                for ítens in range(3):
                    inventário.append(choice(drop))
                for pos in range(-3, 0):
                    for chave in inventário[pos].keys():
                        print(f'{chave},', end=' ')
                print('foram recolhidos do monstro derrotado!')
                break
            dano_monstro = randint(5, 15)
            hp -= dano_monstro
            som("audios/monstro.mp3")
            textos.RoundMonstro(f'Dano: {dano_monstro} - HP do jogador: {hp}')
            sleep(1)
            if hp <= 0:
                print('\nVocê foi derrotado! GAME OVER!')
                som("audios/game_over.mp3")
                aventura()
        elif decisão == '2':
            som("audios/inventário_abrir.mp3")
            inv()


def inv():
    global hp
    while True:
        if inventário == []:
            print('\nO inventário está vazio!')
            som("audios/inventário_fechar.mp3")
            break
        textos.invInfo(inventário)
        usar_item = str(input('\nVocê deseja utilizar qual item do inventário (Escreva o nome do ítem ou deixe em branco para fechar) ').strip())
        if usar_item == '':
            som("audios/inventário_fechar.mp3")
            break
        for pos in range(len(inventário)):
            for chave, valor in inventário[pos].items():
                if usar_item == chave:
                    hp += valor
                    som("audios/consumir.mp3")
                    print(f'\nVocê utilizou o item {chave}, recuperando {valor} de vida. Agora você está com {hp} de vida!')
                    inventário.pop(pos)
                    inv()
                    return
            if pos == len(inventário)-1:
                print(f'\nO item "{usar_item}" não existe no inventário!')


def exploração():
    choice(eventos)() # Os parênteses '()' no final executam a função escolhida em 'choice', é similar a um chamamento de função padrão.
    while True:
        continuar = str(input('\nDeseja continuar (S/N)? ').strip()[0])
        if continuar in 'Ss':
            exploração()
        elif continuar in 'Nn':
            print('\n~~~ Adeus! ~~~')
            quit()
        else:
            print('\nPor favor, responda apenas com sim ou não. Tente novamente!')


def aventura():
    while True:
        global hp, inventário
        hp = 100
        inventário = list()
        aventura = str(input('\nDeseja iniciar uma nova aventura (S/N)? ').strip()[0])
        if aventura in 'Ss':
            exploração()
        elif aventura in 'Nn':
            print('\n~~~ Adeus! ~~~')
            quit()
        else:
            print('\nPor favor, responda apenas com sim ou não. Tente novamente!')


drop = [{'Pão': 25}, {'Maçã': 10}, {'Poção': 75}, {'Pera': 12}, {'Água': 5}]
eventos = [evento1, evento2, evento3]
aventura()
