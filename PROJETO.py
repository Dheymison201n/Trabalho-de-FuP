import pygame
import self as self
from pygame.locals import*

azul_jogador1 = (25, 25, 112)                         #azul da meia noite #191970 --- PEÇA NORMAL
azul_jogador1_dama = (72, 118, 255)                   #azul real 1 	#4876FF --- PEÇA QUE VIROU DAMA
vermelho_jogador2 = (205, 0, 0)                       #vermelho 2 #CD0000 --- PEÇA NORMAL
vermelho_jogador2_dama = (139, 0, 0)                  #Vermelho 4 (darkred) #8B0000 --- PEÇA QUE VIROU DAMA
branco = (255, 255, 255)
cor_de_chocolate = (255, 127, 36)                     #chocolate 1 #FF7F24 --- Cor de fundo do jogo onde vai ficar o tabuleiro




pygame.init()

largura_tela = 800
altura_tela = 600
resolucao = [largura_tela, altura_tela]
pos_x = 400
pos_y = 300

jogador1 = '1'
jogador2 = '2'

fundo = cor_de_chocolate

'''matriz_tabuleiro = [[0, 1, 0, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1],
                    [0, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [2, 0, 2, 0, 2, 0, 2, 0],
                    [0, 2, 0, 2, 0, 2, 0, 2],
                    [2, 0, 2, 0, 2, 0, 2, 0]]'''




tela = pygame.display.set_mode((largura_tela, altura_tela))
fundo_do_jogo = pygame.display.set_mode((resolucao))
pygame.display.set_caption(("Jogo De Damas"))

tamanho_tela_tabuleiro = 200



def jogo():
    abrir = True                                    # Se o abrir == False de vocês tiver dando erro coloca pygame.quit()
    while abrir:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                    abrir = False
            #print(events)

            fundo_do_jogo.fill(fundo)
        fundo_do_tabuleiro = pygame.draw.rect(tela, branco, [pos_x, pos_y, tamanho_tela_tabuleiro, tamanho_tela_tabuleiro])

        pygame.display.update()






def colocando_as_peças():                                   #Aqui o tabuleiro inicia com as peças colocadas de forma padrão antes do jogo começar
        matriz_tabuleiro = [[0, 1, 0, 1, 0, 1, 0, 1],
                            [1, 0, 1, 0, 1, 0, 1, 0],
                            [0, 1, 0, 1, 0, 1, 0, 1],
                            [0, 0, 0, 0, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [2, 0, 2, 0, 2, 0, 2, 0],
                            [0, 2, 0, 2, 0, 2, 0, 2],
                            [2, 0, 2, 0, 2, 0, 2, 0]]

        '''for pos_linha in range(len(matriz_tabuleiro)):
            for pos_coluna in range(len(matriz_tabuleiro[0])):
                if'''



colocando_as_peças()
jogo()
pygame.quit()