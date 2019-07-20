from time import sleep
from random import randint
import sys

# ######### Marcação dos pontos dos jogadores ###########
ponts_jogador = 0
ponts_computador = 0

# ######## Loop do jogo ##########
while True:
    jogador = ''
    primeira_jogada = ''
    # posições aonde serem jogadas
    p1, p2, p3, p4, p5, p6, p7, p8, p9 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    # posições livres para ser jogadas
    lv = 'livre'
    pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9 = lv, lv, lv, lv, lv, lv, lv, lv, lv
    jogada = 0
    computador = 0
    jogada_aleatoria = 0
    turnos = 1
    vencedor = ''

    # ####### EX: De como jogar e mostrando em números inteiros para te guiar aonde jogar!!! #######
    tabuleiro = '''
                    >>>>>>>>>>>> COMO JOGAR <<<<<<<<<<<<
Quando for sua vez, digite o número que corresponde aposição aonde você quer jogar.
OBS: DIGITAR O NÚMERO E APERTA ENTER PARA CONFIRMAR.

                                |       |      
                              1 |   2   |  3  
                                |       |     
                            ------------------
                                |       |     
                              4 |   5   |  6  
                                |       |     
                            ------------------
                                |       |     
                              7 |   8   |  9  
                                |       |     
    '''
    print(f'\033[33m{tabuleiro}\033[m')

    # ######### Escolher entre 'X' ou 'O' para ser o marcador ############
    while jogador != 'O' and jogador != 'X':
        print('OPÇÕES: ( \033[31mX\033[m | O)')
        jogador = str(input('Escolha suas opções: ')).upper()
        # # Se o jogador digitar diferente que X ou O, irá da Inválido. Até digitar corretor a representação das opções.
        if jogador != '0' and jogador != 'X':
            print('\nESCOLHA INVÁLIDA!')

    # # Se o jogador escolher 'X' o computador ficará com 'O', se jogador escolher uma opção automáticamente o computador ficará com a outra opção.
    if jogador == 'X':
        computador = 'O'
        print('\nENTÃO ESCOLHO (O)')
    elif jogador == 'O':
        computador = 'X'
        print('\nENTÃO ESCOLHO (X)')

    # ####### Decisão de quem começa jogando primeiro o jogador ou o computador. O jogador que decide isso ##########

    try:
        print('''\n
Quem joga primeiro? 
[ 1 ] EU
[ 2 ] COMPUTADOR''')
        primeira_jogada = int(
            input('Digite (1) ou (2), para começar você ou o computador: '))
        if primeira_jogada == 1:
            print('\nEntão você começa.')
        elif primeira_jogada == 2:
            print('\nEntão computador começa.')
    except ValueError:
        print('\nESCOLHA INVÁLIDA!')
        break

    # # Atualização do tabuleiro conforme as jogadas vão saindo dos jogadores
    def tabuleiro_atualizado():
        global p1, p2, p3, p4, p5, p6, p7, p8, p9
        tab_velho = f'''
                     |       |   
                  {p1}  |   {p2}   |  {p3}
                     |       |
                -------------------
                     |       |   
                  {p4}  |   {p5}   |  {p6}
                     |       |
                -------------------
                     |       |   
                  {p7}  |   {p8}   |  {p9}
                     |       |
        '''
        print(f'\033[1;35m{tab_velho}\033[m')

    # # Definir as jogadas do jogador (1), as opções dele jogar pelo tabuleiro
    def jogada_jogador():
        global jogada

    # # Loop que rodará até enquanto for verdadeiro, com tratamento de execesões caso tenha erros.
        while True:
            try:
                print('Digite sua jogada, você tem de (1 a 9) posições.')
                jogada = int(input('ESCOLHA SUA POSIÇÃO: '))
                break
            except ValueError:
                print('\nValor digitado inválido. Digite um número inteiro de 1 a 9!\n')

    # # Definir a rota de jogadas, Para que não haja jogadas na mesma posição do jogador (1).
    def rota_jogador():
        global jogada
        global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

        # # Mensagem que a posição escolhida já foi escolhida pelo computador ou pelo jogador mesmo.
        msg = '\nESPAÇO ESTÁ OCUPADO\n'

        # ######## JOGADOR (1) #########
        jogada_jogador()

        # # loop para mostrar que as jogadas escolhidas pelo jogador está ocupada e ele escolher outra posição
        while jogada not in range(1, (9 + 1)):
            jogada_jogador()
            if jogada not in range(1, (9 + 1)):
                print('\n\033[31mINVÁLIDO\033[m\n')

        # # Posições ocupadas que pode acontecer conforme a partida vai acontecendo.
        while jogada == 1 and pos1 == 'ocupada' or \
            jogada == 2 and pos2 == 'ocupada' or \
            jogada == 3 and pos3 == 'ocupada' or \
            jogada == 4 and pos4 == 'ocupada' or \
            jogada == 5 and pos5 == 'ocupada' or \
            jogada == 6 and pos6 == 'ocupada' or \
            jogada == 7 and pos7 == 'ocupada' or \
            jogada == 8 and pos8 == 'ocupada' or \
                jogada == 9 and pos9 == 'ocupada':
            print(msg)
            rota_jogador()

    # # Atualização das jogadas do jogador (1) no tabuleiro
    def jogador_atualizado():
        global jogada
        global p1, p2, p3, p4, p5, p6, p7, p8, p9
        global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

        # # Estrutura de decisões do jogador (1) nas posições que podem esta ocupadas e ficam impossiveis de jogar nelas.
        if jogada == 1:
            p1 = jogador
            pos1 = 'ocupada'
        elif jogada == 2:
            p2 = jogador
            pos2 = 'ocupada'
        elif jogada == 3:
            p3 = jogador
            pos3 = 'ocupada'
        elif jogada == 4:
            p4 = jogador
            pos4 = 'ocupada'
        elif jogada == 5:
            p5 = jogador
            pos5 = 'ocupada'
        elif jogada == 6:
            p6 = jogador
            pos6 = 'ocupada'
        elif jogada == 7:
            p7 = jogador
            pos7 = 'ocupada'
        elif jogada == 8:
            p8 = jogador
            pos8 = 'ocupada'
        elif jogada == 9:
            p9 = jogador
            pos9 = 'ocupada'

    # # Jogadas atualizadas do computador (2) no tabuleiro.
    def computador_atualizado():
        global jogada, jogada_aleatoria, computador
        global p1, p2, p3, p4, p5, p6, p7, p8, p9
        global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

        # # Um sleep para simular que o computador está pensando em sua próxima jogada
        print('Computador: Pensando em sua jogada...')
        print(' ' * 1, '\033[1;35mX\033[m')
        sleep(1)
        print(' ' * 2, '\033[1;95mO\033[m')
        sleep(1)
        print(' ' * 3, '\033[1;35mX\033[m')
        sleep(1)
        # # Fazendo jogada aleatoria do computador indicando com randint para o computador que ele tem que escolher de 1 a 9 para pode jogar.
        jogada_aleatoria = randint(1, 9)

        # # Aqui será mostrado para o computador aonde o jogador (1) jogou e estará ocupada ou mesmo o computador indicando que ele já jogou ali naquela posição.
        while jogada_aleatoria == 1 and pos1 == 'ocupada' or \
            jogada_aleatoria == 2 and pos2 == 'ocupada' or \
            jogada_aleatoria == 3 and pos3 == 'ocupada' or \
            jogada_aleatoria == 4 and pos4 == 'ocupada' or \
            jogada_aleatoria == 5 and pos5 == 'ocupada' or \
            jogada_aleatoria == 6 and pos6 == 'ocupada' or \
            jogada_aleatoria == 7 and pos7 == 'ocupada' or \
            jogada_aleatoria == 8 and pos8 == 'ocupada' or \
                jogada_aleatoria == 9 and pos9 == 'ocupada':
            jogada_aleatoria = randint(1, 9)

        # # O Computador mostrará para o jogador (1) aonde ele jogou, facilitando para que o jogador não jogue na mesma posição.
        print(f'\nComputador: Joguei na posição: {jogada_aleatoria}!')

        # # Estrutura de decisões do computador (2) nas posições que podem esta ocupadas e ficam impossiveis de jogar nelas.
        if jogada_aleatoria == 1:
            p1 = computador
            pos1 = 'ocupada'
        elif jogada_aleatoria == 2:
            p2 = computador
            pos2 = 'ocupada'
        elif jogada_aleatoria == 3:
            p3 = computador
            pos3 = 'ocupada'
        elif jogada_aleatoria == 4:
            p4 = computador
            pos4 = 'ocupada'
        elif jogada_aleatoria == 5:
            p5 = computador
            pos5 = 'ocupada'
        elif jogada_aleatoria == 6:
            p6 = computador
            pos6 = 'ocupada'
        elif jogada_aleatoria == 7:
            p7 = computador
            pos7 = 'ocupada'
        elif jogada_aleatoria == 8:
            p8 = computador
            pos8 = 'ocupada'
        elif jogada_aleatoria == 9:
            p9 = computador
            pos9 = 'ocupada'

    # # Placar do jogo, será definido um checador de placar para mostra quem esta ganhando ou perdendo
    def checar_placar():
        global jogador, computador, turnos, vencedor, ponts_jogador, ponts_computador
        global p1, p2, p3, p4, p5, p6, p7, p8, p9

        # # Estruta para saber se o jogador (1) ganhou
        if p1 == jogador and p2 == jogador and p3 == jogador or \
           p1 == jogador and p4 == jogador and p7 == jogador or \
           p1 == jogador and p5 == jogador and p9 == jogador or \
           p2 == jogador and p5 == jogador and p8 == jogador or \
           p3 == jogador and p5 == jogador and p7 == jogador or \
           p3 == jogador and p6 == jogador and p9 == jogador or \
           p4 == jogador and p5 == jogador and p6 == jogador or \
           p7 == jogador and p8 == jogador and p9 == jogador:
            print('\n\033[33m🎉 VOCÊ GANHOU!\033[m 🎉')
            ponts_jogador += 1
            vencedor = 1  # Eu (JOGADOR)
            turnos = 10

        # # Estrutura para saber se o computador (2) ganhou.
        if p1 == computador and p2 == computador and p3 == computador or \
           p1 == computador and p4 == computador and p7 == computador or \
           p1 == computador and p5 == computador and p9 == computador or \
           p2 == computador and p5 == computador and p8 == computador or \
           p3 == computador and p5 == computador and p7 == computador or \
           p3 == computador and p6 == computador and p9 == computador or \
           p4 == computador and p5 == computador and p6 == computador or \
           p7 == computador and p8 == computador and p9 == computador:
            print('\n\033[33m🎉 COMPUTADOR GANHOU!\033[m 🎉')
            ponts_computador += 1
            vencedor = 2  # Computador (PC)
            turnos = 10

    # # Definindo um atualizador da partida, cada partida ele será atualizado em tudo.
    def partida_atualizar():
        global jogada
        global turnos
        global vencedor

        if primeira_jogada == 1:
            rota_jogador()
            jogador_atualizado()
            tabuleiro_atualizado()
            checar_placar()

            if turnos == 5:
                print('\033[1;90mNÓS EMPATAMOS!\033[m\n')
                turnos = 10
                vencedor = 'EMPATE'

            if vencedor == '':
                computador_atualizado()
                tabuleiro_atualizado()
                checar_placar()

        elif primeira_jogada == 2:
            computador_atualizado()
            tabuleiro_atualizado()
            checar_placar()

            if turnos == 5:
                print('\033[1;90mNÓS EMPATAMOS!\033[m\n')
                turnos = 10
                vencedor = 'EMPATE'
            if vencedor == '':
                rota_jogador()
                jogador_atualizado()
                tabuleiro_atualizado()
                checar_placar()

        jogada = 0
        turnos += 1

    while turnos <= 5:
        partida_atualizar()

    print('\033[1;33m--------------------- PLACAR ------------------\033[m')
    print(f'\033[1;34mVocê: {ponts_jogador}\033[m  |  \033[1;32mComputador: {ponts_computador}\033[m'.center(70))
    print('\033[1;33m-----------------------------------------------\033[m')

    reiniciar = str(input('\nQuer jogar de novo? (Y/N)')).lower()
    if reiniciar in ('y', 'Y'):
        print('\n \033[1;33m>>>>>>>>>>>>>>>> JOGAR <<<<<<<<<<<<<<<<<\033[m')
        continue
    elif reiniciar in ('n', 'N'):
        print('---------- FIM DE PROGRAMA ------------')
        break
    else:
        sys.exit(0)
