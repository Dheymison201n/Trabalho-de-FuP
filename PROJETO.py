from typing import Tuple

import pygame
from pygame.locals import*

azul_jogador1=(25, 25, 112)                         #azul da meia noite #191970 --- PEÇA NORMAL
azul_jogador1_dama=(72, 118, 255)                   #azul real 1 	#4876FF --- PEÇA QUE VIROU DAMA
vermelho_jogador2=(205, 0, 0)                       #vermelho 2 #CD0000 --- PEÇA NORMAL
vermelho_jogador2_dama=(139, 0, 0)                  #Vermelho 4 (darkred) #8B0000 --- PEÇA QUE VIROU DAMA

cor_de_chocolate=(255, 127, 36)  #chocolate 1 #FF7F24 --- Cor de fundo do jogo onde vai ficar o tabuleiro
fundo = cor_de_chocolate

pygame.init()






largura_tela = 800
altura_tela = 600
resolucao=[largura_tela, altura_tela]

tela = pygame.display.set_mode((resolucao))
fundo_do_jogo = pygame.display.set_mode((resolucao))
pygame.display.set_caption(("Jogo De Damas"))



#pygame.display.update()

abrir = True


while abrir:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            abrir = False
        print(events)

fundo_do_jogo.fill(cor_de_chocolate)

