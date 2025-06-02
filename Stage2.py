import pygame
import sys

pygame.init()

WIDTH,HEIGHT=800,300
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Stage:2")

WHITE=(255,0,255)
RED=(255,0,0)
GREEN=(0,255,0)

dino1=pygame.Rect(50,230,40,40)
dino1_speed=5
clock=pygame.time.Clock()

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        dino1.x -= dino1_speed
    if keys[pygame.K_RIGHT]:
        dino1.x += dino1_speed
    if keys[pygame.K_UP]:
        dino1.y -= dino1_speed
    if keys[pygame.K_DOWN]:
        dino1.y += dino1_speed

    win.fill(WHITE)                     # Clear screen
    pygame.draw.rect(win, GREEN, dino1) # Draw dino
    pygame.display.update()            # Update screen
