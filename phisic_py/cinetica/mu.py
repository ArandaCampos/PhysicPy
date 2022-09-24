# -------------------------------------
#   Author: Renan Campos
#   Github: github.com/ArandaCampos
#
#   Movimento Uniforme (MU)
#--------------------------------------

import pygame
from base import Window, InputBox

HEIGHT, WIDTH = 600, 1200
WHITE, BLACK = (210, 210, 210), (0, 0, 0, 0.8)

class Objeto:
    def __init__ (self, x: float, y: float, pf: float, v: float):
        self.x = x
        self.y = y
        self.pf = pf
        self.v = v
        self.diameter = 20
        self.SCALEX = (WIDTH - 50 - self.diameter) / (pf - x)       # 10px == 1 metro
        self.SCALEY = (HEIGHT - 50 - self.diameter) / 4       # 10px == 1 metro

        self.movements = []
        self.position = 0

    def draw(self, win):
        x, y = self.movements[self.position]

        if len(self.movements) > 2:
            pygame.draw.line(win, BLACK, self.transform(self.movements[0]), self.transform(self.movements[self.position]), 2)

        pygame.draw.circle(win, BLACK, self.transform(self.movements[self.position]), self.diameter)

    def transform(self, pos: (float, float)):
        x, y = pos
        return (x * self.SCALEX + self.diameter + 15 , y * self.SCALEY - 1.1 * self.diameter + 25)

    def movement(self, interval):
        x = self.x
        time = interval
        while x < self.pf:
            v = self.v / 3.6
            x = self.x + v * time
            time += interval
            self.movements.append((x, self.y))

    def update_position(self, frame):
        if frame < len(self.movements) and frame >= 0:
            self.position = frame

class Game(Window):
    def __init__(self, size, txt, font):
        super().__init__(size, txt, font=font)

        self.velocity = 1/20
        self.speed = 1
        self.frame = 0

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

        self.start()

        boll = Objeto(x, 4, pf, v)
        boll.movement(self.velocity)
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

            if self.play:
                self.frame += self.speed
                boll.update_position(self.frame)

        pygame.quit()

if __name__ == '__main__':
    game = Game((WIDTH, HEIGHT), "Movimento Uniforme", ("comicsans", 16))
    game.run()
