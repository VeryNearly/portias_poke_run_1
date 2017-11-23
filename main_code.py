import pygame
import random 
import time
from pygame.locals import *
#import pokemon database

pygame.init()

game_end = False
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Pokemon Insert Funny Name Here: ___")
clock = pygame.time.Clock()

#some colors we might need (feel free to add/delete here):
space_violet = (81,0,130)
vivid_plum = (143,5,149)
periwinkle = (204,204,255)
green = ()
white = (0,0,0)

class Trainer:
    def __init__(self, filename):
        self.image = pygame.image.load(filename).convert_alpha() #loads in full sprite sheet as .image() 
        #PRO TIP: "convert_alpha()" is really only necessary if the file isn't saved with a transparent background
	self.dead = False
	
        self.default = 
        self.walk_r = []
        self.walk_l = []
        self.walk_up = []
        self.walk_d = []
        
    def idle(self,x,y,frame): #default idle faces left
        gameDisplay.blit(self.image,(x,y),self.default)
        
    def walk_r():
        pass
    
class Pokemon:
    def __init__(self, filename, cols, rows):
	#we're playing by pokemon red/blue rules but
	#I am pulling images from pokemon platnium/black and white
        self.image = pygame.image.load(filename).convert_alpha()
	self.health = 100
	self.dead = False
	
        self.default = (0,0,64,64)
	seflf.intro_animate = []
        self.attack = []

    def feel_pain(x):
	health = health-x
    
    def special_attack():
	#play music
	#change background
	#doo doo doot doo doo dooooo~

#HERE IS THE SKIN AND BONES FIGHT FUNCTION
def fight():
    frame = 0
    frame_max = 7
    pass
    
#HERE IS THE MAIN GAME LOOP BELOW
#THIS IS THE "ABOVEWORLD"/BIRD EYE VIEW
def game_loop():
    
    pygame.mixer.music.load("MUSICFILENAME.mp3")
    pygame.mixer.music.play(-1)	#-1 makes the music play forever. may run into problems with this later when switching music??? idk.
    pygame.mixer.music.set_volume(0.2) #adjust volume accordingly. I'm just using 0.2 right now. Max is 10
    
    #MIGHT HAVE START UP SCREEN HERE
    
    x_change = 0 #if x_change is a negative number, trainer is moving left. if positive, trainer is moving right
    y_change = 0 #if is neg trainer is moving down. if pos, trainer is going up
    
    old_x = -1 #this variable stores the old x_change value, which keeps track of what direction the trainer WAS moving, so his idle sprite faces the right way when he stops
    x = display_width #800
    y = display_height #600
    frame = 0 #this variable helps me keep track of frames so I can blit through the right sequence of sprites
    
    trainer_ = Trainer("filename.png") #initializes Trainer object named trainer_
    
    trainer_.idle(x/2,y/2,frame) #trainer is in the middle of the screen when game boots up
    
    while game_end == False:
        for event in pygame.event.get():
	    
	    #fight check goes here
	    #fight(trainer_,pokemon_?)
	    
            if (event.type == pygame.QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE): #<--condition allows the x button or the esc key to close game
                pygame.quit()
                quit()
            if (event.type == pygame.KEYDOWN):
                if event.key == pygame.K_LEFT:
                    x_change = -10 #the values for left and right travel and be adjusted accordingly
                if event.key == pygame.K_RIGHT:
                    x_change = 10
            if (event.type == pygame.KEYUP):
                if x_change != 0:
                    old_x = x_change
                x_change = 0
        
        #updates x location
	x += x_change
	
	#"refill" game background HERE
	gameDisplay.fill(white)
	
	if (x_change>0):
	    trainer_.walk_r(x,y,frame) #walks RIGHT
	    
	elif (x_change<0):
	    trainer_.walk_l #walks LEFT
	    
	elif (x_change == 0) and (old_x<0):
	    ziont_.idle(x,y,frame)
        
        elif (x_change == 0) and (old_x>0):
	    ziont_.idle(x,y,frame) #idle, faces RIGHT
	  
	#now that animation frame is blitted in, flip frame count to next frame    
	frame = frame + 1
	
	#this loop will reset the framerate if at end of animation
	#trainer's most complex aboveworld animation shouldn't be more than 3 frames
	if frame == 3: 
		frame = 0	    

	pygame.display.update()       
	clock.tick(6) #currently running at 6fps to make the animation look nice, but not too choppy	


game_loop()
pygame.quit()
quit()