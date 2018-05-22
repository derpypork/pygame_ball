import sys, pygame, math
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

class player(object):
    playerImage = pygame.image.load("intro_ball.gif")
    def __init__(self):
        size = 80
        self.xpos = rand.randint(75,width - 75)
        self.ypos = rand.randint(75,height - 75)
        self spd = 10
        self.length = 75
        self.delta = 0
        self.image = pygame.transform.scale(self.image,(self.length,self.length))

    def updatepos(self,width,height):
        if self.xpos > width:
            self.xpos = 0
        if self.xpos < 0:
            self.xpos = width
        if self.ypos > height:
            self.ypos = 0
        if self.ypos < 0:
            self.ypos = height
        self.angle = self.angle + self.delta
        self.rotjunk = pygame.transform.rotate(self.junk, self.angle) 
        self.rotrec = self.rotjunk.get_rect() 
        self.rotrec.center = (self.xpos,self.ypos) 

    def processevent(self,event):
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.delta = 3
            if event.key == pygame.K_RIGHT:
                self.delta = -3
                
            if event.key == pygame.K_UP:
                self.sp=10
            if event.key == pygame.K_DOWN:
                self.sp=-10

            if event.key == pygame.K_SPACE:
                fire=True
       
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.delta=0
            if event.key == pygame.K_RIGHT:
                self.delta=0

            if event.key == pygame.K_UP:
                self.sp=0
            if event.key == pygame.K_DOWN:
                self.sp=0

            if event.key == pygame.K_SPACE:
                fire=False


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

playerImage = pygame.transform.rotate(ufo,-90)
ship = player(width,height,playerImage)

done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        else:
            ship.processevent(event)
    
    ship.updatepos(width,height)
        
    screen.fill(black)
    
    screen.blit(ship.rotjunk,ship.rotrec) 
        
    pygame.display.flip()
    clock.tick(20)