import sys
import pygame
import random
import add_a_record


from settings import Settings
from car import Car
from bot import Bot

class CarsProject:
    def __init__(self, user):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Cars Project")
        pygame.mouse.set_visible(False)

        self.bgY = -self.screen.get_height()
        self.bgY2 = 0
        self.bg_speed = 20

        self.car = Car(self)
        self.bots = pygame.sprite.Group()

        self._create_bots()

        self.clock = pygame.time.Clock()
        self.create_bot = pygame.USEREVENT + 1
        self.update_score = pygame.USEREVENT + 2

        pygame.time.set_timer(self.create_bot, 800)

        self.user = user
        self.score = 0

    def run_game(self):
        while True:
            self._check_events()
            self.car.update()
            self._update_bots()
            self._update_screen()
            self._check_bots_bottom()
            self.clock.tick(120)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == self.create_bot:
                self._create_bots()
                self.score += 1

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.car.moving_right = True
        if event.key == pygame.K_LEFT:
            self.car.moving_left = True
        if event.key == pygame.K_UP:
            self.car.moving_up = True
        if event.key == pygame.K_DOWN:
            self.car.moving_down = True
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.car.moving_right = False
        if event.key == pygame.K_LEFT:
            self.car.moving_left = False
        if event.key == pygame.K_UP:
            self.car.moving_up = False
        if event.key == pygame.K_DOWN:
            self.car.moving_down = False

    def _create_bots(self):
        bot = Bot(self)
        self.bots.add(bot)

    def _check_bots_bottom(self):
        screen_rect = self.screen.get_rect()
        for bot in self.bots.sprites():
            if bot.rect.bottom >= screen_rect.bottom + 100:
                bot.kill()

    def _update_bots(self):
        self.bots.update()
        if pygame.sprite.spritecollideany(self.car, self.bots, collided=pygame.sprite.collide_mask):
            add_a_record.main_window(self.user, self.score)

    def _update_screen(self):
        self.redraw_screen()

        self.car.blitme()
        self.bots.draw(self.screen)

        pygame.display.flip()

    def redraw_screen(self):
        self.bgY += self.bg_speed
        self.bgY2 += self.bg_speed

        if self.bgY > self.screen.get_height():
            self.bgY = -self.screen.get_height()

        if self.bgY2 > self.screen.get_height():
            self.bgY2 = -self.screen.get_height()

        self.screen.blit(self.settings.background_image, (0, self.bgY))
        self.screen.blit(self.settings.background_image, (0, self.bgY2))

def main(user):
    ai = CarsProject(user)
    ai.run_game()

if __name__ == '__main__':
    main('kievBatyar')