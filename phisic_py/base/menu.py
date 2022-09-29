import pygame
import os

ABS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
IMG_PATH = os.path.join(ABS_PATH, 'sprites')
HEIGHT, WIDTH = 600, 1200
WHITE, BLACK = (210, 210, 210), (0, 0, 0, 0.8)

class Menu:
    def __init__(self, imgs):
        self.imgs = imgs
        self.images = []
        self.font = pygame.font.SysFont('Arial', 12)
        self.set_images()
            
    def set_images(self):
        for img in self.imgs:
            self.images.append(pygame.image.load(os.path.join(IMG_PATH, img)).convert_alpha())
        
    def add_image(self, name: str):
        self.images.append(pygame.image.load(os.path.join(IMG_PATH, name)).convert_alpha())
        
    def draw(self, win, texts):
        for index, text in enumerate(texts):
            win.blit(self.images[index], (WIDTH - 150, 20 + 50 * index))
            win.blit(text, (WIDTH - 100, 25 + 50 * index))
            
            