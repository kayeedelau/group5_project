#main.py
#Author: Kayee
#Establish: 23/11/06
import pygame, sys
from settings import *
class Game:
	def __init__(self):

		#general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		self.clock  = pygame.time.Clock()
		pygame.font.init()
		self.font = pygame.font.SysFont(None, 36)


	def run(self):
		game	= True
		loading = False
		setting = False
		lobby   = True
		run	 = False
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

					self.screen.fill(BLACK)
					#text = self.font.render('LOBBY', True, (0, 255, 255))
					#text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
					#self.screen.blit(text, text_rect)
					image_path = "./image/lobby_image.jpg"
					image = pygame.image.load(image_path)
					image = pygame.transform.scale(image,(1600,1200))
					

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
	def load_game_save(self,ID):
		return
	
	
if __name__ == '__main__':
	game = Game()
	game.run()
	
