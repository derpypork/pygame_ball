#!/usr/bin/python

import pygame
from pygame import gfxdraw
import sys
import random

class ball(object):
	meteor = pygame.image.load("intro_ball.gif")
	def __init__(self):
		self.xpos = random.randint(1,width)
		self.ypos = random.randint(1,height)
		self.spdx = 10
		self.spdy = 10
		self.radius = 100
		self.meteor = pygame.transform.scale(self.meteor,(self.radius,self.radius))
	def redraw(self):
		screen.blit(self.meteor,(self.xpos,self.ypos))

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
pygame.init()
width = 800
height = 600
size = [width,height]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Balls")
clock = pygame.time.Clock()
balllist = []
randNum = random.randint(1,10)

for i in range(randNum):
	balllist.append(ball())
done = False

while done == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	for ball in balllist:
		ball.xpos = ball.xpos + ball.spdx
		ball.ypos = ball.ypos + ball.spdy
		if ball.xpos > width-100:
			ball.xpos = width-100
			ball.spdx = -ball.spdx
		if ball.xpos < 0:
			ball.xpos = 0
			ball.spdx = -ball.spdx
		if ball.ypos > height-100:
			ball.ypos = height-100
			ball.spdy = -ball.spdy
		if ball.ypos < 0:
			ball.ypos = 0
			ball.spdy = -ball.spdy
	screen.fill(white)
	for ball in balllist:
		ball.redraw()
	pygame.display.flip()
	clock.tick(20)