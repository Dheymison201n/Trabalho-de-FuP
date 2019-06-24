import pygame, random
from pygame.locals import *

imagem_de_fundo = pygame.image.load('imagem.jpg')

def musica_jogatina():
    # Música de fundo do jogo durante a jogatina
    pygame.mixer.music.load('musica.wav')
    pygame.mixer.music.play()

# Nessa função a comida vai aparecer em algum lugar randômico sem está fora da linha, isto é, "10 por 10"
def comida_do_rato():
    x = random.randint(0, 590)
    y = random.randint(0, 590)

    return (x // 10 * 10, y // 10 * 10)


def comer_a_comida(colisao_cobra, colisao_comida):
    """nessa parte, quando a cabeça da cobra ficar na mesma posição da comida ela come,
    aumenta de tamanho e a comida aparce em outro lugar."""
    return colisao_cobra[0] == colisao_comida[0] and colisao_cobra[1] == colisao_comida[1]

volume = pygame.mixer.music.get_volume
print(volume)

cima = 0
direita = 1
baixo = 2
esquerda = 3

pygame.init()
tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Python em Python')

#chama a função que inicia a música do jogo
musica_jogatina()

cobra = [(200, 200), (210, 200), (220, 200)]

pele_da_cobra = pygame.Surface((10, 10))
pele_da_cobra.fill((255, 255, 0))
cabeca_da_cobra = pygame.Surface((10, 10))
cabeca_da_cobra.fill((0, 0, 255))

rato_pos = comida_do_rato()
rato = pygame.Surface((10, 10))
rato.fill((255, 0, 0))

direcao_da_cobra = esquerda

tempo = pygame.time.Clock()

fonte = pygame.font.Font('freesansbold.ttf', 18)

pontuacao = 0

cont = 10

level_v = 1

level = 0

game_over = False

tela.blit(imagem_de_fundo, (0, 0))

while not game_over:

    tempo.tick(cont)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


        if event.type == KEYDOWN:
            if event.key == K_UP and direcao_da_cobra != baixo:
                direcao_da_cobra = cima
            if event.key == K_DOWN and direcao_da_cobra != cima:
                direcao_da_cobra = baixo
            if event.key == K_LEFT and direcao_da_cobra != esquerda:
                direcao_da_cobra = esquerda
            if event.key == K_RIGHT and direcao_da_cobra != direita:
                direcao_da_cobra = direita

    if comer_a_comida(cobra[0], rato_pos):
        rato_pos = comida_do_rato()
        cobra.append((0, 0))
        pontuacao = pontuacao + 25
        level = level + 1

    if cobra[0][0] == 600 or cobra[0][1] == 600 or cobra[0][0] < 0 or cobra[0][1] < 0:
        game_over = True
        break


    for i in range(1, len(cobra) - 1):
        if cobra[0][0] == cobra[i][0] and cobra[0][1] == cobra[i][1]:
            game_over = True
            break

    if game_over:
        break

    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = (cobra[i - 1][0], cobra[i - 1][1])

    if direcao_da_cobra == cima:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if direcao_da_cobra == baixo:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if direcao_da_cobra == direita:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if direcao_da_cobra == esquerda:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])

    tela.fill((0, 0, 0))
    tela.blit(rato, rato_pos)

    for x in range(0, 600, 10):
        pygame.draw.line(tela, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10):
        pygame.draw.line(tela, (40, 40, 40), (0, y), (600, y))

    pontuacao_fonte = fonte.render('Pontuação: %s' % (pontuacao), True, (255, 255, 255))
    pontuacao_r = pontuacao_fonte.get_rect()
    pontuacao_r.topleft = (200 - 120, 10)
    tela.blit(pontuacao_fonte, pontuacao_r)

    pontuacao_fonte = fonte.render('level: %s' % (level_v), True, (255, 255, 255))
    pontuacao_r = pontuacao_fonte.get_rect()
    pontuacao_r.topleft = (500 - 120, 10)
    tela.blit(pontuacao_fonte, pontuacao_r)

    if level == 4:
        cont = cont + 5
        level = 0
        level_v = level_v + 1

    for pos in cobra:
        tela.blit(pele_da_cobra, pos)

    pygame.display.update()
