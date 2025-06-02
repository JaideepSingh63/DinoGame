import pygame
import sys
import random

pygame.init()

WIDTH,HEIGHT=800,300
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Stage:4")

WHITE=(255,0,255)
RED=(255,0,0)
GREEN=(0,255,0)
ground_y=230

dino=pygame.Rect(50,230,40,40)
dino_speed=5
clock=pygame.time.Clock()

cactus=pygame.Rect(WIDTH,230,40,40)
cactus_speed=random.randint(5,15)

gravity=1
velocity_y=0
is_jumping= False

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
# assigning keys to do some function like move right left up and down 
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dino.x -= dino_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dino.x += dino_speed
    '''if keys[pygame.K_UP]:
        dino.y -= dino_speed
    if keys[pygame.K_DOWN]:
        dino.y += dino_speed'''
    #intiating the jump
    if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and not is_jumping:
        velocity_y=-15
        is_jumping=True
    
    velocity_y += gravity
    dino.y += velocity_y
    #rest
    if dino.y>=ground_y:
        dino.y=ground_y
        velocity_y=0
        is_jumping=False
    #Restrict the boundries
    if dino.x<0:
        dino.x=0
    if dino.x>WIDTH-dino.width:
        dino.x=WIDTH-dino.width
    if dino.y<0:
        dino.y=0
    if dino.y>HEIGHT-dino.height:
        dino.y=HEIGHT-dino.height
    #movement of obstacle
    cactus.x-=cactus_speed
    if cactus.right<0:
        cactus.x=WIDTH+100
        cactus_speed=random.randint(5,15)

    win.fill(WHITE)                     # Clear screen
    pygame.draw.rect(win, GREEN, dino) # Draw dino
    pygame.draw.rect(win, RED, cactus) # Draw dino
    pygame.display.update()            # Update screen
