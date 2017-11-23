import pygame
from pygame.locals import *
import time

pygame.init()

game_end = False

display_width = 640
display_height = 480

pygame.display.set_caption("Staryu Fight")
gameDisplay = pygame.display.set_mode((display_width,display_height))

clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)

class Pokemon:
	def __init__(self, filename, cols, rows):
		self.sheet = pygame.image.load(filename).convert_alpha()		
		self.cols = cols
		self.rows = rows
		self.totalCellCount = cols * rows
		
		self.rect = self.sheet.get_rect()
		w = self.cellWidth = int(self.rect.width / cols)
		h = self.cellHeight = int(self.rect.height / rows)	
		
		self.cells = list([(index % cols * w, int(index / cols) * h, w, h) for index in range(self.totalCellCount)])
		
	def animate(self, gameDisplay, cellIndex, x, y):
		gameDisplay.blit(self.sheet,(x, y), self.cells[cellIndex])

	def idle(self, gameDisplay, x, y):
		gameDisplay.blit(self.sheet,(x, y),(0,0,self.cellWidth,self.cellHeight))
		
	def special(self, gameDisplay, cellIndex, x, y, bg):	
		frame = 0
		while frame < 6:
			gameDisplay.blit(bg, (0, 0))
			gameDisplay.blit(self.sheet,(x, y), self.cells[cellIndex])
			frame = frame+1
		#print("end loop")
	
def game_loop():

	pygame.mixer.music.load("shooting_stars.mp3")
	stars_bg = pygame.image.load("sp8_bit.png")
	
	frame = 0 #for animation	
	action = "idle"
	staryu_ = Pokemon("staryu_animated.png",4,5) #columns then rows
	
	while game_end == False:
		if action == "idle":
			staryu_.idle(gameDisplay, display_width/2, display_height/2)
		
		if action == "move":
			staryu_.animate(gameDisplay,frame % staryu_.totalCellCount, display_width/2, display_height/2)	
			
		if action == "special":
			staryu_.special(gameDisplay,frame % staryu_.totalCellCount, display_width/2, display_height/2, stars_bg)
					
		frame += 1
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if (event.type == pygame.KEYDOWN):
				if event.key == pygame.K_LEFT:
					print("Idle mode activated")
					action = "idle"
				if event.key == pygame.K_RIGHT:
					print("Animation move activated")
					action = "move"
				if event.key == pygame.K_UP: #special move
					print("kyup")
					pygame.mixer.music.play(1)	
					action = "special"
				if event.key == pygame.K_DOWN:
					print("kdown")
					gameDisplay.fill(black)
		
		pygame.display.update()
		clock.tick(6)
		if action == "special":
			gameDisplay.blit(stars_bg, (0, 0))
		else:
			gameDisplay.fill(white)		

game_loop()
pygame.quit()
quit()