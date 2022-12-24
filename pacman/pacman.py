import pygame

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
VELOCIDADE = 0.3
RAIO = 28
pygame.init()

tela = pygame.display.set_mode((640, 480), 0)
x = 320
y = 240
vel_x = VELOCIDADE
vel_y = VELOCIDADE
while True:
    x = x + vel_x
    y = y + vel_y

    if x + RAIO >= 640:
        vel_x = -VELOCIDADE
    if x - RAIO <= 0:
        vel_x = VELOCIDADE
    if y + RAIO > 480:
        vel_y = -VELOCIDADE
    if y - RAIO <= 0:
        vel_y = VELOCIDADE

    tela.fill(PRETO)
    pygame.draw.circle(tela, AMARELO, (x, y), RAIO, 0)
    pygame.display.update()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()