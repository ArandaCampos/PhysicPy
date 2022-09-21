import pygame
from window import Window
from inputs import InputBox

clock = pygame.time.Clock()

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

    x=Game((500,500), "teste2")
    x.play()
