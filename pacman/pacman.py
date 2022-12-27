import pygame

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
VELOCIDADE = 0.3

RAIO = 28
pygame.init()

tela = pygame.display.set_mode((800, 600), 0)


class Pacman:
    def __init__(self):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.vel_x = 0.3
        self.vel_y = 0.1
        self.tamanho = 800 // 30
        self.raio = self.tamanho // 2

    def calcular_regras(self):
        self.coluna = self.coluna + self.vel_x
        self.linha = self.linha + self.vel_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)

        if self.centro_x + self.raio >= 800:
            self.vel_x = -VELOCIDADE
        if self.centro_x - self.raio <= 0:
            self.vel_x = VELOCIDADE
        if self.centro_y + self.raio > 600:
            self.vel_y = -VELOCIDADE
        if self.centro_y - self.raio <= 0:
            self.vel_y = VELOCIDADE
    def pintar(self, tela):
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)
        canto_boca = (self.centro_x, self. centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)

if __name__ == "__main__":
    x = 320
    y = 240
    vel_x = VELOCIDADE
    vel_y = VELOCIDADE
    pacman = Pacman()

    while True:

        tela.fill(PRETO)
        pacman.calcular_regras()


        pacman.pintar(tela)
        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                print(e.key)
            if e.type == pygame.QUIT:
                exit()
