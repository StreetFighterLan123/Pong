#Basic Game Imports
import pygame
import random
import math
import time
import os
import math
import sys

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
ballY_change = 0
ball_direction = "Left"

def ball(x,y):
	screen.blit(ballImg, (x,y))
	
def ball_movement():
	global ball_direction
	global ballX
	global ballX_change
	global ballY
	global ballY_change
	if ball_direction == "Left":
		ballX_change = 4
		ballX += -ballX_change
	if ball_direction == "Right":
		ballX_change = 4
		ballX += ballX_change
	if ball_direction == "Still":
		ballX_change = 0
	ballY += ballY_change


def check_ball_hits_wall():
	global ballY_change
	if ballY > 580:
		ballY_change = -ballY_change
	if ballY < 20:
		ballY_change = -ballY_change





def left_paddle_collision(left_paddleX, left_paddleY, ballX, ballY):
	distance = math.sqrt((math.pow(left_paddleX - ballX,2)) + (math.pow(left_paddleY - ballY,2)))
	if distance < 75:
		return True
	else:
		return False

def right_paddle_collision(left_paddleX, left_paddleY, ballX, ballY):
	global ballY_change
	distance = math.sqrt((math.pow(left_paddleX - ballX,2)) + (math.pow(left_paddleY - ballY,2)))
	if distance < 50:
		return True
	else:
		return False
		


def ball_reset():
	global ball_direction
	global ballX
	global ballY
	global ballY_change
	ball_direction = "Still"
	ballX = 400
	ballY = 300
	ballY_change = 3
	pygame.display.update()
	time.sleep(1)



#Score Variables
left_score = 0
right_score = 0

left_score_font = pygame.font.Font('freesansbold.ttf', 32)
right_score_font = pygame.font.Font('freesansbold.ttf', 32)


def print_left():
	global left_score
	left_score_text = left_score_font.render(str(left_score), True, (255,255,255))
	screen.blit(left_score_text, (180, 60))
def print_right():
	global right_score
	right_score_text = right_score_font.render(str(right_score), True, (255,255,255))
	screen.blit(right_score_text, (600, 60))


win_font = pong_font = pygame.font.Font('freesansbold.ttf', 64)
def win():
	global win_font
	global right_score
	global left_score
	if right_score >= 10:
		win_text = win_font.render("Right Player Wins!", True, (255,255,255))
		screen.blit(win_text, (120,310))
	if left_score >= 10:
		win_text = win_font.render("Left Player Wins!", True, (255,255,255))
		screen.blit(win_text, (120,310))
	

running = True
ballY_change = 3
while running:
	screen.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	keys = pygame.key.get_pressed()

	left_paddleY_change = 0
	right_paddleY_change = 0
	ballX_change = 0
	#ballY_change = 0

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

	
	if left_paddle_collision(left_paddleX, left_paddleY, ballX, ballY):
		ball_direction = "Right"
		which = "Left"
		print "Right"
		pygame.mixer.Sound.play(hit_sound)
		ballY_change = random.randint(-9,9)
		ballY_change = -ballY_change

		
	if right_paddle_collision(right_paddleX, right_paddleY, ballX, ballY):
		ball_direction = "Left"
		which = "Right"
		print "Left"
		pygame.mixer.Sound.play(hit_sound)
		ballY_change = random.randint(-9,9)
		ballY_change = -ballY_change
	

	
	
	
	#Prints the positions to the terminal, I used this for troubleshooting.
	print ("Left Paddle X %s. Left Paddle Y %s") % (left_paddleX, left_paddleY)
	print ("Right Paddle X %s, Right Paddle Y %s") % (right_paddleX, right_paddleY)
	print("Ball X %s, Ball Y %s") % (ballX, ballY)
	print("BallXchange %s") % (ballX_change)
	print("Ball Direction: %s") % (ball_direction) 
	


	check_ball_hits_wall()
	ball_movement()
	ball(ballX, ballY)


	#Scored!
	if ballX > 780:
		ball_reset()
		left_paddle(left_paddleX, left_paddleY)
		right_paddle(right_paddleX, right_paddleY)
		left_paddleY = 280
		right_paddleY = 280
		left_score += 1 
		print_left()
		pygame.display.update()
		time.sleep(0.5)
		ball_direction = "Right"
	if ballX < 0:
		ball_reset()
		left_paddle(left_paddleX, left_paddleY)
		right_paddle(right_paddleX, right_paddleY)
		left_paddleY = 280
		right_paddleY = 280
		right_score += 1
		print_right()
		pygame.display.update()
		time.sleep(0.5)
		ball_direction = "Left"


	if left_score >= 10 or right_score >= 10:
		win()
		ballX = 10000000
		right_paddleX = 1000000
		left_paddleX = 100000
		pygame.display.update()
		time.sleep(2)
		running = False
		sys.exit()



	#Printing the Score
	print_left()
	print_right()


	clock.tick(60)
	pygame.display.update()
