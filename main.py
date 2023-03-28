import sys
import pygame
import cars_project
import high_score_table as score_t
import db_utils


from settings import Settings

class Main():
    def __init__(self, user):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Cars Project")
        pygame.mouse.set_visible(True)

        self.user = user
        self.font = pygame.font.SysFont('Century Gothic', 32)
        self.records = self.font.render("HIGH SCORE TABLE", True, (255, 255, 255))

        self.greetings = self.font.render('Hello, ' + self.user, True, (255, 255, 255))

        self.new_game_label = self.font.render("New game", True, (255, 255, 255))
        self.new_game = pygame.Rect(870, 740, 200, 45)

    def run(self):
        while True:
            self._check_events()

    def show_main(self):
        greetings_rect = self.greetings.get_rect()
        greetings_rect.centerx = self.screen.get_rect().centerx
        greetings_rect.centery = 100
        self.screen.blit(self.greetings, greetings_rect)

        records_rect = self.records.get_rect()
        records_rect.centerx = self.screen.get_rect().centerx
        records_rect.centery = 340
        self.screen.blit(self.records, records_rect)

        pygame.draw.rect(self.screen, (0, 255, 0), self.new_game, 2)
        self.screen.blit(self.new_game_label, (880, 740))

        results = self.get_top_records()
        table = score_t.ResultsTable(self.screen, results, (760, 440))

        table.draw()

        pygame.display.flip()

    def get_top_records(self):
        user = db_utils.UserDB()
        return user.get_top_scores()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.new_game.collidepoint(pygame.mouse.get_pos()):
                    cars_project.main(self.user)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()


def main_window(user):
    ai = Main(user)
    ai.show_main()
    ai.run()

if __name__ == '__main__':
    main_window('kievBatyar')