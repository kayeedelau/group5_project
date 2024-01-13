import pygame
import sys
from settings import *
from level import Level
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
        pygame.display.set_caption('Dream Adventure 2.0')
        self.clock = pygame.time.Clock()
        self.is_dead = False
        self.level = Level()
        
        #level init here
        
        self.loading = False
        self.setting = False
        self.lobby = True
        self.rungame = False
        self.button_clicked = False
        
        #pause
        self.is_time_stopped = False
        
        #click sfx
        self.sfx = pygame.mixer.Sound('./audio/click.mp3')
        
        self.start_button = Button("./image/start.png", ((WIDTH-320)//2, 467), self.start_game)
        self.load_button = Button("./image/load.png", ((WIDTH-320)//2, 600), self.load_game)
        self.setting_button = Button("./image/setting.png", ((WIDTH-320)//2, 733), self.set_game)
        self.quit_button = Button("./image/quit.png", ((WIDTH-320)//2, 866), sys.exit)

    def save_game_data(self,ID):
        score = self.level.get_exp()
        health= self.level.get_health()
        energy= self.level.get_energy()
        pos   = self.level.get_pos().topleft
        speed = self.level.get_speed()
        
        file_name = f'{ID}.txt'
        with open(file_name, 'w')as file:
            file.write(f'score:{score}\n')
            file.write(f'health:{health}\n')
            file.write(f'energy:{energy}\n')
            file.write(f'pos:{pos}\n')
            file.write(f'speed:{speed}\n')

    def death_check(self):
        health = self.level.get_health()
        if health <=0:
            self.is_dead = True
            
    def start_game(self):
        print("Starting the game!")
        self.sfx.play()
        self.rungame  = True
        self.lobby= False
        self.button_clicked = True
        
    def load_game(self):
        print("Loading the game!")
        self.sfx.play()
        self.lobby= False
        self.loading=True
        self.button_clicked = True
        
    def set_game(self):
        print("Setting the game!")
        self.sfx.play()
        self.setting =True
        self.lobby = False
        self.button_clicked = True
        
    def run(self):
        
        while self.lobby:
            
            while self.loading and not self.button_clicked:
                self.screen.fill(BLACK)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                self.screen.blit(background, (0, 0))
                self.screen.blit(title_image, (288, -150))
                self.load_game_save(0)


            while self.setting and not self.button_clicked:
                self.screen.fill(BLACK)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                self.screen.blit(background, (0, 0))
                self.screen.blit(title_image, (288, -150))

            while self.lobby and not self.button_clicked:
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

        while self.rungame:
            self.screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()  # Update the display
            self.level.run()
            self.clock.tick(FPS)

    def load_game_save(self, ID):
        print("load_game")

if __name__ == '__main__':
    game = Game()
    game.run()

