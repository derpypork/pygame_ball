import sys, pygame
import random as rand

class ball(object):
    image = pygame.image.load("intro_ball.gif")
    def __init__(self):
        self.xpos = rand.randint(75,width - 75)
        self.ypos = rand.randint(75,height - 75)
        self.spdx = rand.randint(5, 25)
        self.spdy = rand.randint(5, 25)
        self.length = rand.randint(25, 75)
        self.angle = 0
        self.isAlive = True
        self.image = pygame.transform.scale(self.image,(self.length,self.length))

    def redraw(self, screen):
        self.image = pygame.transform.scale(self.image,(self.length,self.length))
        self.angle += 3.0
        self.rotimage = pygame.transform.rotate(self.image, self.angle)
        rotrect = self.rotimage.get_rect()
        rotrect.center = (self.xpos, self.ypos)
        screen.blit(self.rotimage, rotrect)

black = (0, 0, 0)
white = (255, 255,255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
colours = (black, white, red, green, blue)

pygame.init()

width = 800
height = 600
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("bouncy")

clock = pygame.time.Clock()
ballList = []
ballMarked = []
randNum = rand.randint(1, 10)

for i in range(randNum):
    ballList.append(ball())

done = False

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    for ball in ballList:
        ball.xpos += ball.spdx
        ball.ypos += ball.spdy

        if ball.xpos > width - (ball.length / 2) or ball.xpos < 0 + (ball.length / 2):
            ball.spdx = -ball.spdx
        if ball.ypos > height - (ball.length / 2) or ball.ypos < 0 + (ball.length / 2):
            ball.spdy = -ball.spdy

    for i in ballList:
        for j in ballList:
            if i == j:
                continue
            x = (i.xpos - j.xpos)**2
            y = (i.ypos - j.ypos)**2
            h = (x + y)**0.5
            if h - (i.length / 2) - (j.length / 2) <= 0:
                i.isAlive = False
                j.isAlive = False

    for ball in ballList:
        if ball.isAlive == False:
            ballList.remove(ball)

    screen.fill(white)
    for ball in ballList:
        ball.redraw(screen)
    pygame.display.flip()
    clock.tick(20)
