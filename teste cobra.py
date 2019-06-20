import pygame, random
from pygame import *



def musica_jogatina():
    # Música de fundo do jogo durante a jogatina
    pygame.mixer.music.load('musica.wav')
    pygame.mixer.music.play()


pygame.init()
tela = pygame.display.set_mode((800,600))
pygame.display.set_caption('Python em Python')

#chama a função que inicia a música do jogo
musica_jogatina()

#valores das direções que a cobra vai andar
para_cima = 0
para_direita = 1
para_baixo = 2
para_esquerda = 3

#Corpo da cobra
cobra = [(200, 200), (210, 200), (220, 200)]
pele_da_cobra = pygame.Surface((10, 10))
pele_da_cobra.fill((255, 255, 0))
cabeca_da_cobra = pygame.Surface((10, 10))
cabeca_da_cobra.fill((0, 0, 255))

#Posição onde a fruta vai aparecer dentro do campo da cobra
def comida_do_rato():
    x = random.randint(0, 790)
    y = random.randint(0, 590)

    return (x//10 * 10, y//10 * 10)


rato_comer = comida_do_rato()
rato = pygame.Surface((10, 10))
rato.fill((20, 70, 30))

#direção inicial da cobra(A cabeça está do lado esquedo, logo o corpo cresce para o lado direito)
direção = para_esquerda

movimentação_da_cobra = pygame.time.Clock()



while True:
    movimentação_da_cobra.tick(12) #aqui é a velocidade que a cobra vai andar
    for event in pygame.event.get(): #Faz tem a opção de fechar o jogo
        if event.type == QUIT:
            pygame.quit()


    for k in range(len(cobra) -1, 0, -1): # Aqui faz o corpo andar junto com a cabeça
        cobra[k] = (cobra[k-1][0], cobra[k-1][1])

    if direção == para_cima:
       cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if direção == para_baixo:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if direção == para_direita:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if direção == para_esquerda:
        cobra[0] = [cobra[0][0] - 10, cobra[0][1]]

#Nessa parte a variável direção recebe a "direção"  que a cobra vai de acordo com a tecla clicada, no caso as setas
    if event.type == KEYDOWN:
        if event.key == K_UP:
            direção = para_cima
        if event.key == K_DOWN:
            direção = para_baixo
        if event.key == K_LEFT:
            direção = para_esquerda
        if event.key == K_RIGHT:
            direção = para_direita

    """for k in range(len(cobra) -1, 0, -1):
        cobra[k] = (cobra[k-1][0], cobra[k-1][1])"""




    tela.fill((0, 0, 0))
    tela.blit(rato, rato_comer)
    tela.blit(cabeca_da_cobra, cobra[0])
    for i in range(1, len(cobra)):
        tela.blit(pele_da_cobra, cobra[i])

    #for pos in cobra:
    #tela.blit(pele_da_cobra, pos)

    pygame.display.update()
