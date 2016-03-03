import pygame
import time
from pygame.locals import *
from random import randrange
from timeit import default_timer
pygame.init()

pygame.display.set_caption("Count Game")

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

Width = 400
Height = 200

counter = 0
counter2 = 0
inBox = 0
speed = 1.0

screen = pygame.display.set_mode((Width,Height))
back = pygame.Surface((Width,Height))
background = back.convert()
background.fill(white)
screen.blit(background,(0,0))

positions = []
positionsLeave = []

stopIn = randrange(10, 20)
total = 0

#print stopIn

def enterHouse():
	global positions

	positions.append(Width)
	#print positions

def leaveHouse():
	global inBox
	global speed
	global positionsLeave

	positionsLeave.append(Width/2-25)

	inBox -= 1

	speed += 0.1

	#print speed
	#print positionsLeave

enterHouse()

#Main loop for game
while len(positions) > 0 or len(positionsLeave) > 0:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == KEYDOWN:
			if event.key == K_q:
				exit()

	counter += 1
	counter2 += 1

	if counter2 > randrange(120/int(speed),240/int(speed)) and inBox > 0 and len(positions) > 0:
		leaveHouse()
		counter2 = 0

	if counter > randrange(80/int(speed),160/int(speed)) and stopIn > total:
		enterHouse()
		counter = 0
		total += 1

	pygame.display.update()
	
	screen.blit(background,(0,0))

	for x in range(len(positions)):
		try:
			pygame.draw.rect(screen, blue, (positions[x],Height/2-25,50,50), 0)
			if positions[x] < Width/2-25:
				inBox += 1
				del positions[x]
		except:
			pass

	for x in range(len(positionsLeave)):
		try:
			pygame.draw.rect(screen, red, (positionsLeave[x],Height/2-25,50,50), 0)
			if positionsLeave[x] < -50:
				del positionsLeave[x]
		except:
			pass

	pygame.draw.rect(screen, pink, (Width/2-50,Height/2-50,100,100), 0)

	for x in range(len(positions)):
		positions[x] -= speed

	for x in range(len(positionsLeave)):
		positionsLeave[x] -= speed
	#print inBox

pygame.display.update()
time.sleep(2)

font = pygame.font.Font(None, 72)
text = font.render(str(inBox), 1, black)
textpos = text.get_rect()
textpos.centerx = Width/2
textpos.centery = Height/2
screen.blit(text, textpos)

pygame.display.update()

time.sleep(2)