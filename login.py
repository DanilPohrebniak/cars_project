import db_utils
import pygame
import cars_project
import main
import register


class LoginForm:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Cars Project")
        pygame.mouse.set_visible(True)

        self.font = pygame.font.SysFont('Century Gothic', 32)
        self.title = self.font.render("Login Form", True, (255, 255, 255))
        self.text = ""
        self.login_error = self.font.render(self.text , True, (255, 102, 102))
        self.username_label = self.font.render("Username:", True, (255, 255, 255))
        self.password_label = self.font.render("Password:", True, (255, 255, 255))
        self.send_button_label = self.font.render("Login", True, (255, 255, 255))
        self.register_label = self.font.render('Register', True, (255, 255, 255))
        self.username_input = pygame.Rect(275, 175, 240, 45)
        self.password_input = pygame.Rect(275, 275, 240, 45)
        self.username_input_active = False
        self.password_input_active = False
        self.send_button = pygame.Rect(325, 400, 140, 45)
        self.register_button = pygame.Rect(325, 460, 140, 45)
        self.username = ""
        self.password = ""
        self.user = db_utils.UserDB()
        self.is_active = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_active = False
            elif event.type == pygame.KEYDOWN:
                if self.username_input_active:
                    if event.key == pygame.K_BACKSPACE:
                        self.username = self.username[:-1]
                    else:
                        self.username += event.unicode
                elif self.password_input_active:
                    if event.key == pygame.K_BACKSPACE:
                        self.password = self.password[:-1]
                    else:
                        self.password += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.send_button.collidepoint(pygame.mouse.get_pos()):
                    self.check_login_data()
                elif self.register_button.collidepoint(pygame.mouse.get_pos()):
                    register.main()
                elif self.username_input.collidepoint(pygame.mouse.get_pos()):
                    self.username_input_active = True
                    self.password_input_active = False
                elif self.password_input.collidepoint(pygame.mouse.get_pos()):
                    self.username_input_active = False
                    self.password_input_active = True
                else:
                    self.username_input_active = False
                    self.password_input_active = False

    def draw(self):
        self.screen.fill((0, 0, 0))

        title_rect = self.title.get_rect(center=(self.width // 2, 50))
        self.screen.blit(self.title, title_rect)

        error_rect = self.title.get_rect(center=(220, 90))
        self.screen.blit(self.login_error, error_rect)

        username_label_rect = self.username_label.get_rect(center=(self.width // 2, 150))
        self.screen.blit(self.username_label, username_label_rect)

        password_label_rect = self.password_label.get_rect(center=(self.width // 2, 250))
        self.screen.blit(self.password_label, password_label_rect)

        pygame.draw.rect(self.screen, (121, 34, 204), self.username_input, 2)
        username_text = self.font.render(self.username, True, (255, 255, 255))
        username_text_rect = username_text.get_rect(
            midleft=(self.username_input.left + 10, self.username_input.centery))
        self.screen.blit(username_text, username_text_rect)

        pygame.draw.rect(self.screen, (121, 34, 204), self.password_input, 2)
        password_text = self.font.render("*" * len(self.password), True, (255, 255, 255))
        password_text_rect = password_text.get_rect(
            midleft=(self.password_input.left + 10, self.password_input.centery))
        self.screen.blit(password_text, password_text_rect)

        pygame.draw.rect(self.screen, (0, 255, 0), self.send_button, 2)
        self.screen.blit(self.send_button_label, (self.send_button.x + 28, self.send_button.y))

        pygame.draw.rect(self.screen, (0, 255, 0), self.register_button, 2)
        self.screen.blit(self.register_label, (self.register_button.x + 8, self.register_button.y))

        pygame.display.flip()

    def check_login_data(self):
        if self.user.check_user(self.username, self.password):
            main.main_window(self.username)
        else:
            self.text = "Login error, check the entered data"
            self.login_error = self.font.render(self.text, True, (255, 102, 102))
            error_rect = self.title.get_rect(center=(220, 90))
            self.screen.blit(self.login_error, error_rect)
            pygame.display.flip()

    def run(self):
        while self.is_active:
            self.draw()
            self.handle_events()

        pygame.quit()

if __name__ == '__main__':
    pygame.init()
    login_form = LoginForm(800, 600)
    login_form.run()