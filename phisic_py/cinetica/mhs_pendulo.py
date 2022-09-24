#---------------------------------------
#   Author: Renan Campos
#   Github: github.com/ArandaCampos
#   Movimento Harmônica Simples (MHS)
#----------------------------------------
import math
import pygame
from base import Window

WIDTH, HEIGHT = 1200, 600
WHITE = (210, 210, 210)
BLACK = (0, 0, 0, .8)

class Objeto:
    g = 9.807 		       	                # Aceleração da gravidade (m/s^2)

    def __init__(self, angulo, m, L):
        self.angulo = angulo
        self.A = L * math.sin(math.radians(angulo))
        self.x = 0
        self.y = 0
        self.m = m
        self.L = L
        self.t = 0
        self.diametro = 20
        self.movimento = []
        self.w = self.frequencia_angular()
        self.ESCALA = HEIGHT / L * 0.8

    def draw(self, win):
        updated_points = []
        for point in self.movimento:
            x, y = point
            updated_points.append((x, y))

        if len(self.movimento) > 2:
            pygame.draw.lines(win, BLACK, False, updated_points, 2)

        pygame.draw.circle(win, BLACK, (self.x, self.y), self.diametro)
        pygame.draw.lines(win, BLACK, False, [(WIDTH / 2 , 0) , (self.x, self.y)], 2)

    def transformacaoLinear(self):
        self.x = self.x * self.ESCALA + WIDTH /2
        self.y = self.y * self.ESCALA

    def frequencia_angular(self):
        w = math.sqrt(self.g / self.L)
        return w

    def deslocamento(self):
        self.x = self.w * self.A * math.cos(self.w*self.t)
        self.y = math.sqrt(math.pow(self.L, 2) - math.pow(self.x, 2))

    def update_position(self):
        self.t += 1/20
        self.deslocamento()
        self.transformacaoLinear()
        self.movimento.append((self.x, self.y))

class Game(Window):
    def __init__(self, size, txt, font):
        super().__init__(size, txt)

    def play(self):
        clock = pygame.time.Clock()
        run = True
        theta = m = L = 0

        while theta <= 0 or theta > 10:
            try:
                theta = float(input('Qual o angulo inicial em graus? (menor que 10) '))
            except ValueError:
                print("Valor incompatível!")
        while m <= 0:
            try:
                m = float(input('Qual a massa do objeto? '))
            except ValueError:
                print("Valor incompatível!")
        while L <= 0:
            try:
                L = float(input('Qual o comprimento da linha? (em m) '))
            except ValueError:
                print("Valor incompatível!")

        self.init()

        obj = Objeto(theta, m, L)
        self.append_component(obj)

        while run:
            clock.tick(20)
            self.refresh_screen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            obj.update_position()

        self.exit()

if __name__ == '__main__':
    game = Game((WIDTH, HEIGHT), "Movimento Harmônico Simples", ("comicsans", 16))
    game.play()
