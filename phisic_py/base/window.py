import pygame

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
        #self.font = pygame.font.SysFont(*font)
        self.font = font
        self.components = []

        self.play = True

    def start(self):
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)

    def refresh_screen(self):
        self.screen.fill(self.bg)
        for component in self.components:
            component.draw(self.screen)
        pygame.display.flip()

    def load_sprite(self, path: str, scale: (int, int) = None):
        sprite = pygame.image.load(os.path.join(diretorio_imagem, path)).convert_alpha()
        if scale:
            sprite = pygame.transform.scale(sprite, (45,50))
        self.components.append(sprite)

    def append_component(self, component):
        self.components.append(component)

    def to_back(self):
        self.speed -= 1
        if not self.speed:
            self.speed = -1

    def forward(self):
        self.speed += 1
        if not self.speed:
            self.speed = 1

    def handle_play(self):
        self.play = not self.play

    def exit(self):
        pygame.quit()


