import pygame
from numpy import random


class Bird(pygame.sprite.Sprite):
    def __init__(self, y, x=150):
        super().__init__()
        self.image = pygame.image.load(r"images\bird.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 50))
        self.rect = self.image.get_rect(center=(x, y))
        self.hiz = 0

    def zipla(self):
        self.hiz = -8

    def update(self):
        self.hiz += 0.5
        self.rect.y += self.hiz

class Pipes(pygame.sprite.Sprite):
    def __init__(self, x, renk=(0, 102, 0)):
        super().__init__()
        self.boy = random.randint(100, 400)
        self.image = pygame.image.load(r"images\pipe.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, self.boy))
        self.rect = self.image.get_rect(midbottom=(x, 650))
        self.hiz = 3

    def update(self):
        self.rect.x -= self.hiz
        if self.rect.right < 0:
            self.kill()

class TopPipes(pygame.sprite.Sprite):
    def __init__(self, x,alfa, renk=(0, 102, 0)):
            super().__init__()
            self.boy = 500
            self.image = pygame.image.load(r"images\pipe.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (100, self.boy))
            self.rect = self.image.get_rect(midbottom=(x, alfa))
            self.hiz = 3

    def update(self):
        self.rect.x -= self.hiz
        if self.rect.right < 0:
            self.kill()

class Point(pygame.sprite.Sprite):
    def __init__(self, x,beta):
            super().__init__()
            self.image = pygame.image.load(r"images\coin.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.rect = self.image.get_rect(midbottom=(x, beta))
            self.hiz = 3

    def update(self):
        self.rect.x -= self.hiz
        if self.rect.right < 0:
            self.kill()