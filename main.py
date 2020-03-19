import pygame
import random
import math
import time
import os


#Position the Game Window
windowX = 260
windowY = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (windowX, windowY)


pygame.init()
screen = pygame.display.set_mode((800, 600))

#Booting wait, without it the OS script will be a goofy poofy.
time.sleep(2)


pygame.display.set_caption("Pong")
icon = pygame.image.load('ping-pong.png')
pygame.display.set_icon(icon)
#Game icon art made by FreePic



# Left Paddle
left_paddleImg = pygame.image.load('rectangle.png')
# paddleImg art made by Alfredo Hernandez
left_paddleX = 10
left_paddleY = 450
left_paddleX_change = 0 
left_paddleY_change = 0 


def left_paddle(x, y):
	screen.blit(left_paddleImg, (x, y))


# Right Paddle
right_paddleImg = pygame.image.load('rectangle.png')
# again, paddleImg art made by Alfredo Hernandez
right_paddleX = 730
right_paddleY = 450
right_paddleX_change = 0 
right_paddleY_change = 0 

def right_paddle(x,y):
	screen.blit(right_paddleImg, (x,y))



#PONG DISPLAYED AT THE TOP
pong_font = pygame.font.Font('freesansbold.ttf', 64)
def disp_pong_text():
	pong_text = pong_font.render("PONG", True, (255,255,255))
	screen.blit(pong_text, (303, 50))





#ballImg made by Freepik
bigballImg = pygame.image.load('ball.png')
ballImg = pygame.transform.scale(bigballImg, (20,20))
ballX = 400
ballY = 300
ballX_change = 0
ballyX_change = 0
#ballX_vel = 0
#ballY_vel = 0
ball_direction = "Left"

def ball(x,y):
	screen.blit(ballImg, (x,y))
	




running = True

while running:
	screen.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	keys = pygame.key.get_pressed()

	left_paddleY_change = 0
	right_paddleY_change = 0

	if keys[pygame.K_w]:
		left_paddleY_change -= 1.5

	if keys[pygame.K_s]:
		left_paddleY_change += 1.5

	if keys[pygame.K_UP]:
		right_paddleY_change -= 1.5

	if keys[pygame.K_DOWN]:
		right_paddleY_change += 1.5
		
	#Boundaries
	if left_paddleY <= 0:
		left_paddleY = 0
	elif left_paddleY > 536:
		left_paddleY = 536
	if right_paddleY <= 0:
		right_paddleY = 0
	elif right_paddleY > 536:
		right_paddleY = 536

	left_paddleY += left_paddleY_change
	right_paddleY += right_paddleY_change
	
	

	disp_pong_text()
	left_paddle(left_paddleX, left_paddleY)
	right_paddle(right_paddleX, right_paddleY)
	ball(ballX, ballY)
	time.sleep(0.001)
	pygame.display.update()
