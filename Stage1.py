import pygame
import sys

pygame.init()

WIDTH,HEIGHT=800,300
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Stage:1")

WHITE=(255,0,255)
RED=(255,0,0)
GREEN=(0,255,0)

dino1=pygame.Rect(50,230,40,40)
dino2=pygame.Rect(100,230,40,40)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    win.fill(WHITE)                     # Clear screen
    pygame.draw.rect(win, GREEN, dino1) # Draw dino
    pygame.draw.rect(win, RED, dino2) # Draw dino
    pygame.display.update()            # Update screen
