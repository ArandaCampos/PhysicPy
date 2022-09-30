# -------------------------------------
#   Author: Renan Campos
#   Github: github.com/ArandaCampos
#
#   Movimento Uniforme (MU)
#--------------------------------------

import os
import pygame
from base import Window, Menu

HEIGHT, WIDTH = 600, 1200
WHITE, BLACK, GRAY = (210, 210, 210), (0, 0, 0, 0.8), (88, 88, 88)
ABS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
IMG_PATH = os.path.join(ABS_PATH, 'sprites')

class Objeto:
    def __init__ (self, x: float, y: float, pf: float, v: float):
        self.x = x
        self.y = y
        self.pf = pf
        self.v = v
        self.a = 0
        self.menu = Menu(('clock.png', 'pointer.png', 'speedometer.png', 'accelaration.png'))
        self.diameter = 15

        self.SCALEX = (WIDTH - 50 - self.diameter) / (pf - x)       # 10px == 1 metro
        self.SCALEY = (HEIGHT - 70 - self.diameter) / 4
        self.font = pygame.font.SysFont('Arial', 12)

        self.movements = []
        self.position = 0

    def draw(self, win):
        if self.position > 1:
            pygame.draw.line(win, GRAY, self.transform(self.movements[0]), self.transform(self.movements[self.position]), 2)

        pos = self.font.render('{:.1f} m'.format(self.movements[self.position][0]), True, BLACK)
        timer = self.font.render('{:.2f} s'.format(self.position/20), True, BLACK)
        vel = self.font.render('{:.2f} Km/h'.format(self.v), True, BLACK)
        a = self.font.render('{:.2f} m/s²'.format(self.a), True, BLACK)
        self.menu.draw(win, (pos, timer, vel, a))

        pygame.draw.circle(win, BLACK, self.transform(self.movements[self.position]), self.diameter)
        
    def transform(self, pos: (float, float)):
        x, y = pos
        return (x * self.SCALEX + 25 , y * self.SCALEY)

    def movement(self, interval):
        x = self.x
        time = 0
        while x < self.pf:
            v = self.v / 3.6
            x = self.x + v * time
            time += interval
            self.movements.append((x, self.y))
        return len(self.movements)

    def update_position(self, frame):
        if frame < len(self.movements) and frame >= 0:
            self.position = frame

    def set_sprite(self, name: str, scale: bool = False):
        img = pygame.image.load(os.path.join(IMG_PATH, name)).convert_alpha()
        if scale:
            return pygame.transform.scale(img, (25,25))
        return img

class Game(Window):
    def __init__(self, size, txt):
        super().__init__(size, txt)
        self.velocity = 1/20
        self.speed = 1
        self.frame = 0
        self.frames = 0

    def run(self):
        clock = pygame.time.Clock()
        run = True
        x = pf = v = None

        while x == None:
            try:
                x = float(input('Qual a posição inicial do objeto? (metros) '))
            except ValueError:
                print("Valor incompatível!")

        while pf == None or x >= pf:
            try:
                pf = float(input('Qual a posição final do objeto? (metros) '))
            except ValueError:
                print("Valor incompatível!")

        while v == None or v <= 0:
            try:
                v = float(input('Qual a velocidade do objeto? (km/h) '))
            except ValueError:
                print("Valor incompatível!")

        self.init()

        boll = Objeto(x, 4, pf, v)
        self.frames = boll.movement(self.velocity)
        self.append_component(boll)

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
                elif event.type == pygame.MOUSEBUTTONUP:
                    print(pygame.mouse.get_pos())
                    if self.menu.images[1].get_rect(center=((WIDTH - 12) / 2, HEIGHT - 38)).collidepoint(pygame.mouse.get_pos()) or self.menu.images[2].get_rect(center=((WIDTH - 25) / 2, HEIGHT - 50)).collidepoint(pygame.mouse.get_pos()):
                        self.handle_play()

            if self.play:
                self.frame += self.speed
                boll.update_position(self.frame)

        self.exit()

if __name__ == '__main__':
    game = Game((WIDTH, HEIGHT), "Movimento Uniforme")
    game.run()
