import pygame
from .menu import Menu

HEIGHT, WIDTH = 600, 1200
WHITE, BLACK = (210, 210, 210), (0, 0, 0, 0.8)

class Window():
    pygame.init()
    def __init__(self,
                 size: (int, int),
                 title: str,
                 bg: (int, int, int) = (210, 210, 210),
                 font: (str, int) = (None, 32)
                 ):
        self.size = size
        self.title = title
        self.screen = None
        self.bg = bg
        self.font = font
        self.components = []
        self.font = pygame.font.SysFont('Arial', 12)
        self.menu = None

        self.play = True

    def init(self):
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
        self.menu = Menu(("go_back.png", 'pause.png', 'play.png'))


    def refresh_screen(self):
        self.screen.fill(self.bg)
        for component in self.components:
            component.draw(self.screen)
        self.menu_draw()
        pygame.display.flip()

    def menu_draw(self):
        if self.speed > 0:
            progress_img = pygame.transform.rotate(self.menu.images[0], 180)
            speed = self.speed
            pos_img, pos_txt = ((WIDTH - 25) * 0.4, HEIGHT - 50), ((WIDTH - 25) * 0.43 , HEIGHT - 45)
        else:
            progress_img = self.menu.images[0]
            speed = - self.speed 
            pos_img, pos_txt = ((WIDTH - 25) * 0.6, HEIGHT - 50), ((WIDTH - 25) * 0.57, HEIGHT - 45)
        status = (self.menu.images[2] if self.play else self.menu.images[1])
        
        self.screen.blit(progress_img, pos_img)
        self.screen.blit(self.font.render('{}x'.format(speed), True, BLACK), pos_txt)
        self.screen.blit(status, ((WIDTH - 25) / 2, HEIGHT - 50))
            
    # def load_sprite(self, path: str, scale: (int, int) = None):
    #     sprite = pygame.image.load(os.path.join(diretorio_imagem, path)).convert_alpha()
    #     if scale:
    #         sprite = pygame.transform.scale(sprite, (25, 25))
    #     self.components.append(sprite)

    def append_component(self, component):
        self.components.append(component)

    def to_back(self):
        self.speed -= 1
        if not self.speed:
            self.speed = -1
        if self.frame > self.frames:
            self.speed = -1
            self.frame = self.frames

    def forward(self):
        self.speed += 1
        if not self.speed:
            self.speed = 1
        if self.frame < 0:
            self.speed = 1
            self.frame = 0

    def handle_play(self):
        self.play = not self.play

    def exit(self):
        pygame.quit()