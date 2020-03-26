#Basic Game Imports
import pygame
import random
import math
import time
import os
import math


clock = pygame.time.Clock()


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
#Game icon art made by FreePik
pygame.mixer.music.load("pong_song.wav")
pygame.mixer.music.play(-1)
#Pong hit sound effect
hit_sound = pygame.mixer.Sound("hit.wav")







# Left Paddle
left_paddleImg = pygame.image.load('rectangle.png')
# paddleImg art made by Alfredo Hernandez
left_paddleX = 10
left_paddleY = 280
left_paddleX_change = 0 
left_paddleY_change = 0 


def left_paddle(x, y):
	screen.blit(left_paddleImg, (x, y))


# Right Paddle
right_paddleImg = pygame.image.load('rectangle.png')
# again, paddleImg art made by Alfredo Hernandez
right_paddleX = 730
right_paddleY = 280
right_paddleX_change = 0 
right_paddleY_change = 0 

def right_paddle(x,y):
	screen.blit(right_paddleImg, (x,y))



#PONG DISPLAYED AT THE TOP
pong_font = pygame.font.Font('freesansbold.ttf', 64)
def disp_pong_text():
	pong_text = pong_font.render("PONG", True, (255,255,255))
	screen.blit(pong_text, (302, 50))





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
	
def ball_movement():
	global ball_direction
	global ballX
	global ballX_change
	if ball_direction == "Left":
		ballX_change = 4
		ballX += -ballX_change
	if ball_direction == "Right":
		ballX_change = 4
		ballX += ballX_change
	if ball_direction == "Still":
		ballX_change = 0
	#Make it work later.

def paddle_collision(left_paddleX, left_paddleY, ballX, ballY):
	distance = math.sqrt((math.pow(left_paddleX - ballX,2)) + (math.pow(left_paddleY - ballY,2)))
	if distance < 75:
		return True
	else:
		return False
def right_paddle_collision(left_paddleX, left_paddleY, ballX, ballY):
	distance = math.sqrt((math.pow(left_paddleX - ballX,2)) + (math.pow(left_paddleY - ballY,2)))
	if distance < 50:
		return True
	else:
		return False




def ball_reset():
	global ball_direction
	global ballX
	global ballY
	ball_direction = "Still"
	ballX = 400
	ballY = 300
	pygame.display.update()
	time.sleep(1)



#Code for if the paddle is up (above a certain number) or down,
# -- below a certain number

up = False
down = False

def left_paddle_up_or_down():
	global left_paddleY
	global up
	global down

def right_paddle_up_or_down():
	global right_paddleY
	global up
	global down



def ball_go_up():
	print "IN PROGRESS"

def ball_go_down():
	print "In PROGRESS"




running = True

while running:
	screen.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	keys = pygame.key.get_pressed()

	left_paddleY_change = 0
	right_paddleY_change = 0
	ballX_change = 0
	ballyX_change = 0

	if keys[pygame.K_w]:
		left_paddleY_change -= 5.5

	if keys[pygame.K_s]:
		left_paddleY_change += 5.5

	if keys[pygame.K_UP]:
		right_paddleY_change -= 5.5

	if keys[pygame.K_DOWN]:
		right_paddleY_change += 5.5
		
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
	left_paddleX += left_paddleX_change
	right_paddleX += right_paddleX_change

	#MAKE THE BALL X CHANGE BUT FIX IT LATER
	
	


	disp_pong_text()
	left_paddle(left_paddleX, left_paddleY)
	right_paddle(right_paddleX, right_paddleY)
	
	
	ball_movement()
	ball(ballX, ballY)
	if paddle_collision(left_paddleX, left_paddleY, ballX, ballY):
		ball_direction = "Right"
		print "Right"
		pygame.mixer.Sound.play(hit_sound)
	if right_paddle_collision(right_paddleX, right_paddleY, ballX, ballY):
		ball_direction = "Left"
		print "Left"
		pygame.mixer.Sound.play(hit_sound)
	print ("Left Paddle X %s. Left Paddle Y %s") % (left_paddleX, left_paddleY)
	print ("Right Paddle X %s, Right Paddle Y %s") % (right_paddleX, right_paddleY)
	print("Ball X %s, Ball Y %s") % (ballX, ballY)
	print("BallXchange %s") % (ballX_change)
	print("Ball Direction: %s") % (ball_direction) 


	if ballX > 780:
		ball_reset()
		left_paddle(left_paddleX, left_paddleY)
		right_paddle(right_paddleX, right_paddleY)
		left_paddleY = 280
		right_paddleY = 280
		pygame.display.update()
		time.sleep(0.5)
		ball_direction = "Right"
	if ballX < 0:
		ball_reset()
		left_paddle(left_paddleX, left_paddleY)
		right_paddle(right_paddleX, right_paddleY)
		left_paddleY = 280
		right_paddleY = 280
		pygame.display.update()
		time.sleep(0.5)
		ball_direction = "Left"




	#time.sleep(0.001)
	clock.tick(60)
	pygame.display.update()
