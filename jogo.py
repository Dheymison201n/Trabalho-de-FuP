import pygame, random
from pygame import *

imagem_de_fundo = pygame.image.load('Background_do_jogo_800x600.jpg')


def musica_jogatina():
    # Música de fundo do jogo durante a jogatina
    pygame.mixer.music.load('musica.wav')
    pygame.mixer.music.play()


def comer_a_comida(colisao_cobra, colisao_comida):
    """nessa parte, quando a cabeça da cobra ficar na mesma posição da comida ela come,
    aumenta de tamanho e a comida aparce em outro lugar."""
    return colisao_cobra[0] == colisao_comida[0] and colisao_cobra[1] == colisao_comida[1]


pygame.init()

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Python em Python')



pontuacao = 0
contador = 0

# chama a função que inicia a música do jogo
musica_jogatina()

# valores das direções que a cobra vai andar
para_cima = 0
para_direita = 1
para_baixo = 2
para_esquerda = 3

# Corpo da cobra
cobra = [(200, 200), (210, 200), (220, 200)]
pele_da_cobra = pygame.Surface((10, 10))
pele_da_cobra.fill((255, 255, 0))
cabeca_da_cobra = pygame.Surface((10, 10))
cabeca_da_cobra.fill((0, 0, 255))


# Nessa função a comida vai aparecer em algum lugar randômico sem está fora da linha, isto é, "10 por 10"
def comida_do_rato():
    x = random.randint(0, 790)
    y = random.randint(0, 590)

    return (x // 10 * 10, y // 10 * 10)


# criando a comida
rato_comer = comida_do_rato()
rato = pygame.Surface((10, 10))
rato.fill((255, 70, 30))

# direção inicial da cobra(A cabeça está do lado esquedo, logo o corpo cresce para o lado direito)
direção = para_esquerda

movimentação_da_cobra = pygame.time.Clock()
inicio_do_jogo = True
while inicio_do_jogo:


    if pontuacao >= 0:
        movimentação_da_cobra.tick(12)  # aqui é a velocidade que a cobra vai andar




    for event in pygame.event.get():  # Faz tem a opção de fechar o jogo
        if event.type == QUIT:
            pygame.quit()

    tela.blit(imagem_de_fundo, (0, 0))

    # Nessa parte a cobra come a maçã e em seguida cresce
    if comer_a_comida(cobra[0], rato_comer):
        rato_comer = comida_do_rato()
        pontuacao = pontuacao + 25
        cobra.append((0, 0))
        contador = contador + 1




    # Aqui faz o corpo andar junto com a cabeça
    for k in range(len(cobra) - 1, 0, -1):
        cobra[k] = (cobra[k - 1][0], cobra[k - 1][1])

    if direção == para_cima:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if direção == para_baixo:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if direção == para_direita:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if direção == para_esquerda:
        cobra[0] = [cobra[0][0] - 10, cobra[0][1]]

    # Nessa parte a variável direção recebe a "direção"  que a cobra vai de acordo com a tecla clicada, no caso as setas
    if event.type == KEYDOWN:
        if event.key == K_UP:
            if direção != para_baixo:
                direção = para_cima
        if event.key == K_DOWN:
            if direção != para_cima:
                direção = para_baixo
        if event.key == K_LEFT:
            if direção != para_direita:
                direção = para_esquerda
        if event.key == K_RIGHT:
            if direção != para_esquerda:
                direção = para_direita

    """for k in range(len(cobra) -1, 0, -1):
        cobra[k] = (cobra[k-1][0], cobra[k-1][1])"""

    """Nessa parte essa estrutura de decisão vai fazer com que a cobra morra se tentar sair da 
        tela de jogo"""

    if cobra[0][0] == 800 or cobra[0][1] == 600 or cobra[0][0] < 0 or cobra[0][1] < 0:
        inicio_do_jogo = False
        break

    # tela.fill((255, 255, 255))
    tela.blit(rato, rato_comer)
    tela.blit(cabeca_da_cobra, cobra[0])
    for i in range(1, len(cobra)):
        tela.blit(pele_da_cobra, cobra[i])

    # for pos in cobra:
    # tela.blit(pele_da_cobra, pos)
    pygame.font

    # Nessa parte faz aparecer a pontuação do jogador
    pygame.font.init()
    font = pygame.font.get_default_font()  # Fonte padrão
    mostrar_pont = pygame.font.SysFont(font, 40)  # tamanho 40
    texto_pontuacao = mostrar_pont.render('Pontuação: %s' % (pontuacao), True, (255, 200, 70))
    tela.blit(texto_pontuacao, (550, 10))

    pygame.display.update()

pygame.quit()

"""for k in range(len(cobra) -1, 0, -1):
       cobra[k] = (cobra[k-1][0], cobra[k-1][1])"""