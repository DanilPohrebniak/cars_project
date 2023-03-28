import pygame

class ResultsTable:
    def __init__(self, screen, results, position=(0, 0)):
        self.screen = screen
        self.results = results
        self.position = position
        self.font = pygame.font.SysFont('Century Gothic', 32)
        self.surface = pygame.Surface((400, 250))
        self.surface.fill((100, 15, 105))
        self.render_table()

    def render_table(self):
        for i, (name, score) in enumerate(self.results):
            name_text = self.font.render(name, True, (0, 0, 0))
            score_text = self.font.render(str(score), True, (0, 0, 0))
            self.surface.blit(name_text, (50, i*50))
            self.surface.blit(score_text, (250, i*50))

    def draw(self):
        self.screen.blit(self.surface, self.position)