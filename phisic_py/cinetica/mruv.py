#---------------------------------------------
#   Author: Renan Campos
#   Github: github.com/ArandaCampos
#   Movimento Retilínio Uniformemente Variado (MRUV)
#---------------------------------------------

import pygame
import math
import os
from base import Window, Menu

WIDTH, HEIGHT = 1200, 600
WHITE, BLACK, GRAY = (210, 210, 210), (0, 0, 0, 0.8), (88, 88, 88)
ABS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
IMG_PATH = os.path.join(ABS_PATH, 'sprites')

class Objeto:
    g = -9.807 		       	# Aceleração da gravidade (m/s^2)

    def __init__(self, x, velocidade, aceleracao, pf):
        self.x = x									# Posição Vertical
        self.y = 4	              					# Posição Horizontal 
        self.pf = pf
        self.v = velocidade
        self.a = aceleracao
        self.diameter = 20

        self.position = 0
        self.menu = Menu(('clock.png', 'pointer.png', 'speedometer.png', 'accelaration.png'))
        self.font = pygame.font.SysFont('Arial', 12)

        self.movements = []
        self.velocities = []

        self.SCALE = (WIDTH - 50 - self.diameter) / (pf - x)

    def draw(self, win):
        if self.position > 2:
            pygame.draw.line(win, BLACK, self.transform(self.movements[0]), self.transform(self.movements[self.position]), 2)

        pygame.draw.circle(win, BLACK, self.transform(self.movements[self.position]), self.diameter)
        
        pos = self.font.render('{:.1f} m'.format(self.movements[self.position][0]), True, BLACK)
        timer = self.font.render('{:.2f} s'.format(self.position/20), True, BLACK)
        vel = self.font.render('{:.2f} Km/h'.format(self.velocities[self.position]), True, BLACK)
        a = self.font.render('{:.2f} m/s²'.format(self.a), True, BLACK)
        self.menu.draw(win, (pos, timer, vel, a))

    def transform(self, position):
        x, y = position
        x = x * self.SCALE + 25
        y = y * (HEIGHT - 70 - self.diameter) / 4
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
            self.velocities.append(v)
        return len(self.movements)

    def update_position(self, frame):
        if frame < len(self.movements) and frame >= 0:
            self.position = frame

class Game(Window):
    def __init__(self, size, title, font):
        super().__init__(size, title)

        self.velocity = 1/80
        self.speed = 2
        self.frame = 0
        self.frames = 0

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

if __name__ == "__main__":
    game = Game((WIDTH, HEIGHT), "Movimento Retilíneo Uniformemente Variado", ("comicsans", 16))
    game.run()