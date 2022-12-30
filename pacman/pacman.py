import pygame

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
VELOCIDADE = 0.1

RAIO = 30
pygame.init()

tela = pygame.display.set_mode((800, 600), 0)


class Pacman:
    def __init__(self):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.vel_x = 0
        self.vel_y = 0
        self.tamanho = 800 // 30
        self.raio = self.tamanho // 2

    def calcular_regras(self):
        self.coluna = self.coluna + self.vel_x
        self.linha = self.linha + self.vel_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)

        if self.centro_x + self.raio >= 800 or self.centro_x - self.raio <= 0:
            self.vel_x = 0
        if self.centro_y + self.raio > 600 or self.centro_y - self.raio <= 0:
            self.vel_y = 0

    def pintar(self, tela):
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)
        canto_boca = (self.centro_x, self. centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)

    def processar_eventos(self, eventos):

        for e in eventos:
            if e.type == pygame.QUIT:
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    if self.centro_x + self.raio >= 800:
                        self.vel_x = 0
                    else:
                        self.vel_x = VELOCIDADE
                elif e.key == pygame.K_LEFT:
                    if self.centro_x - self.raio <= 0:
                        self.vel_x = 0
                    else:
                        self.vel_x = -VELOCIDADE
                elif e.key == pygame.K_UP:
                    if self.centro_y - self.raio <= 0:
                        self.vel_y = 0
                    else:
                        self.vel_y = -VELOCIDADE
                elif e.key == pygame.K_DOWN:
                    if self.centro_y + self.raio > 600:
                        self.vel_y = 0
                    else:
                        self.vel_y = VELOCIDADE


if __name__ == "__main__":
    pacman = Pacman()

    while True:

        tela.fill(PRETO)
        pacman.calcular_regras()

        pacman.pintar(tela)
        pygame.display.update()

        eventos = pygame.event.get()
        pacman.processar_eventos(eventos)
