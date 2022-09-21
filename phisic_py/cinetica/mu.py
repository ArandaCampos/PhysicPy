import pygame
from base import Window

HEIGHT, WIDTH = 600, 1200
WHITE = (210, 210, 210)
BLACK = (0, 0, 0, 0.8)

class Objeto:
    def __init__ (self, x, pf, v):
        self.x = x
        self.pf = pf
        self.v = v
        self.diametro = 20
        self.ESCALA = (WIDTH - 50) / (pf - x)       # 10px == 1 metro

        self.movimento = [(x * self.ESCALA + self.diametro , HEIGHT - 1.1 * self.diametro)]

    def draw(self, win):
        x, y = self.movimento[-1]

        if len(self.movimento) > 2:
            pygame.draw.lines(win, BLACK, False, self.movimento, 2)

        pygame.draw.circle(win, BLACK, (x, y), self.diametro)

    def deslocamento(self, t):
        v = self.v / 3.6
        px = self.x + v * t
        return px, v

    def update_position(self, t):
        x, v = self.deslocamento(t)
        pf, diametro = self.pf, self.diametro
        if x <= pf:
            print("%.2f | %.2f | %.2f" %(x, t, v))
            self.movimento.append((x * self.ESCALA + diametro , HEIGHT - 1.1 * diametro))

def main():
    run = True
    t = 0
    clock = pygame.time.Clock()

    try:
        x = float(input('Qual a posição inicial do objeto? (metros) '))
        pf = float(input('Qual a posição final do objeto? (metros) '))
        v = float(input('Qual a velocidade do objeto? (km/h) '))
    except:
        run = False

    WIN = Window((WIDTH, HEIGHT), "Movimento Uniforme", font=("comicsans", 16))
    WIN.start()

    boll = Objeto(x, pf, v)
    if boll:
        WIN.append_component(boll)

    while run:
        clock.tick(20)
        t += 1/20

        WIN.refresh_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        boll.update_position(t)

    pygame.quit()

if __name__ == '__main__':
    main()
