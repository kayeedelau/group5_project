import pygame
from settings 	import *
from tile 		import Tile
from player 	import Player
from debug 		import debug
from support 	import *
from random 	import choice, randint
from weapon 	import Weapon
from ui 		import UI
from enemy 		import Enemy
from particles 	import AnimationPlayer
from magic 		import MagicPlayer
from upgrade 	import Upgrade

class Level:
	def __init__(self, file_name):

		# get the display surface
		self.display_surface= pygame.display.get_surface()
		self.game_paused 	= False

		# setting
		self.player_data = file_name
		
		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites= pygame.sprite.Group()
		
		#attack sprites
		self.current_attack 	= None
		self.attack_sprites 	= pygame.sprite.Group()
		self.attackable_sprites = pygame.sprite.Group()
		
		#sprite setup
		self.create_map()

		#user interface
		self.ui 	= UI()
		self.upgrade= Upgrade(self.player)
		
		#particles
		self.animation_player	= AnimationPlayer()
		self.magic_player 		= MagicPlayer(self.animation_player)

	def create_attack(self):
	
		self.current_attack = Weapon(self.player, [self.visible_sprites, self.attack_sprites])
	
	def create_magic(self, style, strength, cost):
		if style == 'heal':
			self.magic_player.heal(self.player, strength, cost, [self.visible_sprites])
		if style == 'teleport':
			self.magic_player.teleport(self.player, strength, cost, [self.visible_sprites])
		if style == 'flame':
			self.magic_player.flame(self.player, cost, [self.visible_sprites, self.attack_sprites])
	
	def destroy_attack(self):
		if self.current_attack:
			self.current_attack.kill()
		self.current_attack = None

	def create_map(self):
		

	def player_attack_logic(self):
		if self.attack_sprites:
			for attack_sprite in self.attack_sprites:
				collision_sprites =pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
				if collision_sprites:
					for target_sprite in collision_sprites:
						if target_sprite.sprite_type =='01'or target_sprite.sprite_type =='02':
							pos = target_sprite.rect.center
							offset = pygame.math.Vector2(0, 60)
							for leaf in range(randint(3, 6)):		
								self.animation_player.create_grass_particles(pos - offset, [self.visible_sprites])
							target_sprite.kill()
						else:
							target_sprite.get_damage(self.player, attack_sprite.sprite_type)
 
		
	def damage_player(self, amount, attack_type):
			if self.player.vulnerable:
				self.player.health -= amount
				self.player.vulnerable = False
				self.player.hurt_time = pygame.time.get_ticks()
				self.animation_player.create_particles(attack_type, self.player.rect.center, [self.visible_sprites])

	def trigger_death_particles(self, pos, particle_type):
			self.animation_player.create_particles(particle_type, pos, self.visible_sprites)
			
	def add_exp(self, amount):
		self.player.exp += amount
		
	def get_exp(self):
		return self.player.exp

	def get_health(self):
		return self.player.health

	def get_energy(self):
		return self.player.energy

	def get_pos(self):
		return self.player.rect

	def get_speed(self):
		return self.player.speed

	def toggle_menu(self):
		self.game_paused = not self.game_paused

	def run(self):
			self.visible_sprites.custom_draw(self.player)
			self.ui.display(self.player)
			if self.game_paused:
				self.upgrade.display()
			else:
				self.visible_sprites.update()
				self.visible_sprites.enemy_update(self.player)
				self.player_attack_logic()

class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		# general setup
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()
		
		#creating the floor
		floor_surf = pygame.image.load('./cool/03.png').convert()
		self.floor_surf = pygame.transform.scale(floor_surf, (1280*4, 800*4))
		self.floor_rect = self.floor_surf.get_rect(topleft = (0, 0))
		
	def enemy_update(self, player):
		enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') if sprite.sprite_type == 'enemy']
		for enemy in enemy_sprites:
			enemy.enemy_update(player)
			
	def custom_draw(self, player):

		# getting the offset
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height
		
		#drawing the floor
		floor_offset_pos = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_surf, floor_offset_pos)
		
		#for sprite in self.sprites()
		for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset 
			self.display_surface.blit(sprite.image, offset_pos)
			
