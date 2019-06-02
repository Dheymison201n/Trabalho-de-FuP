import pygame, random
from pygame import *

def cambiarra_do_rato():
    x = random.randint(0,590)
    y = random.randint(0, 590)

    return (x//10 * 10, y//10 * 10)

cima = 0
direita = 1
baixo = 2
esquerda = 3

pygame.init()
tela = pygame.display.set_mode((600,600))
pygame.display.set_caption('Python em Python')

cobra = [(200, 200), (210, 200), (220, 200)]
pele_da_cobra = pygame.Surface((10,10))
pele_da_cobra.fill((255,255,255))

pos_rato = cambiarra_do_rato()
rato = pygame.Surface((10,10))
rato.fill((255,0,0))

lado_do_bicho = esquerda

tempo = pygame.time.Clock()

while True:
    tempo.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                lado_do_bicho = cima
            if event.key == K_DOWN:
                lado_do_bicho = baixo
            if event.key == K_LEFT:
                lado_do_bicho = esquerda
            if event.key == K_RIGHT:
                lado_do_bicho = direita

    if lado_do_bicho == cima:
       cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if lado_do_bicho == baixo:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if lado_do_bicho == direita:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if lado_do_bicho == esquerda:
        cobra[0] = [cobra[0][0] - 10, cobra[0][1]]

    for k in range(len(cobra) -1, 0, -1):
        cobra[k] = (cobra[k-1][0], cobra[k-1][1])

    tela.fill((0,0,0))
    tela.blit(rato, pos_rato)
    for pos in cobra:
        tela.blit(pele_da_cobra, pos)


    pygame.display.update()
