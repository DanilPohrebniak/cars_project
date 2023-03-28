import sys
import pygame
import cars_project
import high_score_table as score_t
import db_utils
import main


from settings import Settings

class Main():
    def __init__(self, user, score):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Cars Project")
        pygame.mouse.set_visible(True)

        self.user = user
        self.score = score
        self.font = pygame.font.SysFont('Century Gothic', 32)
        self.records = self.font.render("YOUR SCORE - " + str(self.score), True, (255, 255, 255))

        self.add_a_record_label = self.font.render("Add a record", True, (255, 255, 255))
        self.add_a_record = pygame.Rect(840, 440, 240, 45)

        self.new_game_label = self.font.render("New game", True, (255, 255, 255))
        self.new_game = pygame.Rect(840, 520, 240, 45)

    def run(self):
        while True:
            self._check_events()

    def show_main(self):
        records_rect = self.records.get_rect()
        records_rect.centerx = self.screen.get_rect().centerx
        records_rect.centery = 340
        self.screen.blit(self.records, records_rect)

        pygame.draw.rect(self.screen, (0, 255, 0), self.add_a_record, 2)
        self.screen.blit(self.add_a_record_label, (855, 440))

        pygame.draw.rect(self.screen, (0, 255, 0), self.new_game, 2)
        self.screen.blit(self.new_game_label, (870, 520))

        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.add_a_record.collidepoint(pygame.mouse.get_pos()):
                    self.add_record(self.score, self.user)
                    main.main_window(self.user)
                elif self.new_game.collidepoint(pygame.mouse.get_pos()):
                    cars_project.main(self.user)

    def add_record(self, score, user):
        record = db_utils.UserDB()
        record.add_record(score, user)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()


def main_window(user, score):
    ai = Main(user, score)
    ai.show_main()
    ai.run()

if __name__ == '__main__':
    main_window('kievBatyar', 100)