import pygame
import sys
from settings import *

class Button:
    def __init__(self, image_path, position, callback):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=position)
        self.callback = callback

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.start_button = Button("./image/start.png", ((WIDTH-320)//2, 467), self.start_game)
        self.load_button = Button("./image/load.png", ((WIDTH-320)//2, 600), self.load_game)
        self.setting_button = Button("./image/setting.png", ((WIDTH-320)//2, 733), self.set_game)
        self.quit_button = Button("./image/quit.png", ((WIDTH-320)//2, 866), sys.exit)

    def start_game(self):
        print("Starting the game!")
        self.run  = True
        self.lobby= False
        
    def load_game(self):
        print("Loading the game!")
        
    def set_game(self):
        print("Setting the game!")
		
    def run(self):
        game = True
        loading = False
        setting = False
        lobby = True
        run = False
        while game:
            print("Game")
            while loading:
                self.screen.fill(BLACK)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

            while setting:
                self.screen.fill(BLACK)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

            while lobby:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if self.start_button.is_clicked(mouse_pos):
                            self.start_button.callback()
                        if self.quit_button.is_clicked(mouse_pos):
                            self.quit_button.callback()
                        if self.load_button.is_clicked(mouse_pos):
                            self.load_button.callback()
                        if self.setting_button.is_clicked(mouse_pos):
                            self.setting_button.callback()

                self.screen.fill(BLACK)

                background_path = "./image/lobby_image.jpg"
                title_path = "./image/title.png"

                background = pygame.image.load(background_path)
                title_image = pygame.image.load(title_path)

                background = pygame.transform.scale(background, (1600, 1200))

                background.set_alpha(128)
                title_image.set_alpha(200)
                self.screen.blit(background, (0, 0))
                self.screen.blit(title_image, (288, -150))

                # Draw buttons
                self.start_button.draw(self.screen)
                self.quit_button.draw(self.screen)
                self.load_button.draw(self.screen)
                self.setting_button.draw(self.screen)

                pygame.display.update()  # Update the display
                self.clock.tick(FPS)

            while run:
                self.screen.fill(BLACK)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                pygame.display.update()  # Update the display
                self.clock.tick(FPS)

    def load_game_save(self, ID):
        return

if __name__ == '__main__':
    game = Game()
    game.run()

