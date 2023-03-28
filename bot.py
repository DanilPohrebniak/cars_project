import pygame
import random

from pygame.sprite import Sprite

class Bot(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.rndm_img = random.choice(self.settings.imgs_for_bots)
        self.image = pygame.transform.scale(pygame.image.load(self.rndm_img).convert_alpha(),(230, 150))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.settings.coords_for_bots)
        self.rect.y = -100

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.bot_speed
        self.rect.y = self.y

