# -------------------------------------
#   Author: Renan Campos
#   Github: github.com/ArandaCampos
#--------------------------------------

import pygame
from base import Window

HEIGHT, WIDTH = 600, 1200
WHITE, BLACK = (210, 210, 210), (0, 0, 0, 0.8)

class Objeto:
    def __init__ (self, x: float, pf: float, v: float):
        self.x = x
        self.pf = pf
        self.v = v
        self.t = 0
        self.diametro = 20
        self.ESCALA = (WIDTH - 50) / (pf - x)       # 10px == 1 metro

        self.movimento = [(x * self.ESCALA + self.diametro , HEIGHT - 1.1 * self.diametro)]

    def draw(self, win):
        x, y = self.movimento[-1]

        if len(self.movimento) > 2:
            pygame.draw.lines(win, BLACK, False, self.movimento, 2)

        pygame.draw.circle(win, BLACK, (x, y), self.diametro)

    def deslocamento(self):
        v = self.v / 3.6
        px = self.x + v * self.t
        return px, v

    def update_position(self):
        self.t += 1/20
        x, v = self.deslocamento()
        pf, diametro = self.pf, self.diametro
        if x <= pf:
            print("%.2f | %.2f | %.2f" %(x, self.t, v))
            self.movimento.append((x * self.ESCALA + diametro , HEIGHT - 1.1 * diametro))

class Game(Window):
    def __init__(self, size, txt, font):
        super().__init__(size, txt, font=font)

    def play(self):
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

        boll = Objeto(x, pf, v)
        if boll:
            self.append_component(boll)

        while run:
            clock.tick(20)

            self.refresh_screen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            boll.update_position()

        pygame.quit()

if __name__ == '__main__':
    game = Game((WIDTH, HEIGHT), "Movimento Uniforme", ("comicsans", 16))
    game.play()
