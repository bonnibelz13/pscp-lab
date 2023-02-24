import pygame
pygame.init()
screen = pygame.display.set_mode((1024, 780))
pygame.display.set_caption('Space Invaders')

icon = pygame.image.load('5724-duck.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('bg_purple.png')


while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			quit()
	screen.blit(bg, (0, 0))
	pygame.display.update()
class Player(pygame.sprite.Sprite):
	def __init__(self,pos,constraint,speed):
		super().__init__()
		self.image = pygame.image.load('../graphics/player.png').convert_alpha()
		self.rect = self.image.get_rect(midbottom = pos)
		self.speed = speed
		self.max_x_constraint = constraint
		self.ready = True
		self.laser_time = 0
		self.laser_cooldown = 600

		self.lasers = pygame.sprite.Group()

		self.laser_sound = pygame.mixer.Sound('../audio/laser.wav')
		self.laser_sound.set_volume(0.5)

	def get_input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			self.rect.x += self.speed
		elif keys[pygame.K_LEFT]:
			self.rect.x -= self.speed