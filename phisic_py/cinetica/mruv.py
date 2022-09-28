#---------------------------------------------
#   Author: Renan Campos
#   Github: github.com/ArandaCampos
#   Movimento Retilínio Uniformemente Variado (MRUV)
#---------------------------------------------

import pygame
import math
from base import Window

WIDTH, HEIGHT = 1200, 600
WHITE, BLACK = (210, 210, 210), (0, 0, 0, .8)

class Objeto:
    g = -9.807 		       	# Aceleração da gravidade (m/s^2)

    def __init__(self, x, velocidade, aceleracao, pf):
        self.x = x													# Posição Vertical
        self.y = HEIGHT / 2											# Posição Horizontal 
        self.pf = pf
        self.v = velocidade
        self.a = aceleracao
        self.diameter = 20

        self.position = 0
        self.movements = []

        self.SCALE = (WIDTH - 50 - self.diameter) / (pf - x)

    def draw(self, win):
        if self.position > 2:
            pygame.draw.line(win, BLACK, self.transform(self.movements[0]), self.transform(self.movements[self.position]), 2)

        pygame.draw.circle(win, BLACK, self.transform(self.movements[self.position]), self.diameter)

    def transform(self, position):
        x, y = position
        x = x * self.SCALE + 25
        return (x, y)

    def velocity(self, time):
        a, v = self.a, self.v
        V = v * time + (math.pow(time, 2) * a) / 2
        return V

    def movement(self, interval):
        px, pf = self.x, self.pf
        time = 0
        while px < pf:
            v = self.velocity(time)
            px += v
            time += interval
            self.movements.append((px, self.y))

    def update_position(self, frame):
        if frame < len(self.movements) and frame >= 0:
            self.position = frame

class Game(Window):
    def __init__(self, size, title, font):
        super().__init__(size, title)

        self.velocity = 1/20
        self.speed = 1
        self.frame = 0

    def run(self):
        run = True
        clock = pygame.time.Clock()
        x = pf = velocidade = aceleracao = None

        while x == None:
            try:
                x = float(input('Qual posição inicial em metros? '))
            except ValueError:
                print("Valor incompatível")
        while pf == None or pf <= x:
            try:
                pf = float(input('Qual a posição final em metros '))
            except ValueError:
                print("Valor incompatível")
        while velocidade == None or velocidade <= 0:
            try:
                velocidade = float(input('Qual a velocidade inicial (m/s): '))
            except ValueError:
                print("Valor incompatível")
        while aceleracao == None:
            try:
                aceleracao = float(input('Qual a aceleracao, em m/s, do objeto? '))
            except ValueError:
                print("Valor incompatível")

        self.init()
        obj = Objeto(x, velocidade, aceleracao, pf)
        obj.movement(self.velocity)
        self.append_component(obj)

        while run:
            clock.tick(20)
            self.refresh_screen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.handle_play()
                    if event.key == pygame.K_LEFT:
                        self.to_back()
                    if event.key == pygame.K_RIGHT:
                        self.forward()

            if self.play:
                self.frame += self.speed
                obj.update_position(self.frame)

        self.exit()

if __name__ == "__main__":
    game = Game((WIDTH, HEIGHT), "Movimento Retilíneo Uniformemente Variado", ("comicsans", 16))
    game.run()