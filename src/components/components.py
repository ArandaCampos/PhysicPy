import pygame

screen = pygame.display.set_mode((640, 480))
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
clock = pygame.time.Clock()

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
        self.font = pygame.font.Font(*font)
        self.components = []

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

    def exit(self):
        pygame.quit()

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = pygame.font.Font(None, 32).render(text, True, self.color)
        self.active = False

    def enable_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
        pygame.display.flip()



def main():
    clock = pygame.time.Clock()
    input_box1 = InputBox(100, 100, 140, 32)
    input_box2 = InputBox(100, 300, 140, 32)
    input_boxes = [input_box1, input_box2]
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes:
                box.enable_event(event)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        pygame.display.flip()
        clock.tick(30)


class Game(Window):
    def __init__(self, size, txt):
        super().__init__(size, txt)

    def play(self):
        self.start()

        run = 1

        input_box = InputBox(100, 100, 140, 32)
        self.append_component(input_box)

        while run:
            clock.tick(20)
            self.refresh_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = 0

        self.exit()

if __name__ == '__main__':
    #main()
    #pg.quit()

    x=Game((500,500), "teste2")
    x.play()
