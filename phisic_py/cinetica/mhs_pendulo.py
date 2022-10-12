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
        self.diameter = 20
        self.w = self.linear_frequency()
        self.SCALE = HEIGHT / L * 0.8

        self.movements = []
        self.position = 0

    def draw(self, win):
        x, y = self.movements[self.position]

        if self.position > 2:
            points = []
            for movement in self.movements[0: self.position]:
                points.append(self.transform(movement))

            pygame.draw.lines(win, BLACK, False, points, 2)

        pygame.draw.circle(win, BLACK, self.transform(self.movements[self.position]), self.diameter)
        pygame.draw.lines(win, BLACK, False, [(WIDTH / 2 , 0) , self.transform(self.movements[self.position])], 2)

    def transform(self, pos):
        x, y = pos
        return (x * self.SCALE + WIDTH / 2, y * self.SCALE)

    def linear_frequency(self):
        w = math.sqrt(self.g / self.L)
        return w

    def movement(self, interval):
        x = self.x
        time = interval
        while time < 20:
            x = self.w * self.A * math.cos(self.w * time)
            y = math.sqrt(math.pow(self.L, 2) - math.pow(x, 2))
            time += interval
            self.movements.append((x, y))
        return len(self.movements)

    def update_position(self, frame):
        if frame < len(self.movements) and frame >= 0:
            self.position = frame

class Game(Window):
    def __init__(self, size, txt, font):
        super().__init__(size, txt)

    def run(self):
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
        self.frames = obj.movement(self.velocity)
        self.append_component(obj)

        while self.start:
            clock.tick(40)

            self.refresh_screen()
            self.get_event()

            if self.play:
                self.frame += self.speed

            obj.update_position(self.frame)

        self.exit()

if __name__ == '__main__':
    game = Game((WIDTH, HEIGHT), "Movimento Harmônico Simples", ("comicsans", 16))
    game.run()
