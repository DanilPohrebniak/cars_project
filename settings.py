import pygame.image
import random


class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.background_image = pygame.image.load('images/main_surface.png')

        self.coords_for_bots = [265,425,585,765,935,1095,1255,1420]
        self.imgs_for_bots = ['images/cars/blue_car.png',
                              'images/cars/brown_car.png',
                              'images/cars/gold_car.png',
                              'images/cars/grey_car.png',
                              'images/cars/red_car.png']

        self.car_speed = 20
        self.bot_speed = random.randrange(5, 20)
        self.font = pygame.font.Font(None, 36)