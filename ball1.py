import sys, pygame
import random as rand

pygame.init()

a = rand.randint(-1, 255)
b = rand.randint(-1, 255)
c = rand.randint(-1, 255)

size = width, height = 500, 500
speed = [2, 2]
colour = a, b, c
WHITE = 255, 255, 255
BLUE =  (  0,   0, 255)

screen = pygame.display.set_mode(size)

ball = pygame.draw.circle(screen, colour, [60, 60], 60)
ballarea = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        ballarea = ballarea.move(speed)
        if ballarea.left < 0 or ballarea.right > width:
            speed[0] = -speed[0]
        if ballarea.top < 0 or ballarea.bottom > height:
            speed[1] = -speed[1]

    screen.fill(WHITE)
    screen.blit(ball, ballarea)
    pygame.display.flip()