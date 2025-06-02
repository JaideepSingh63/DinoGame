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
BLACK=(0,0,0)
ground_y=230

font=pygame.font.SysFont(None,60)
#creating a function to reset the game 
def reset_game():
    global game_over,dino,cactus,cactus_speed,velocity_y,is_jumping
    dino=pygame.Rect(50,230,40,40)
    cactus=pygame.Rect(WIDTH,230,40,40)
    cactus_speed=random.randint(5,15)
    game_over = False
    velocity_y = 0
    is_jumping = False

reset_game()
clock=pygame.time.Clock()
gravity=1

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    
    if game_over:
        if (keys[pygame.K_r] or keys[pygame.K_UP]):
            reset_game()
# assigning keys to do some function like move right left up and down 
    if not game_over:
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
        if dino.colliderect(cactus):
            game_over=True

    win.fill(WHITE)                     # Clear screen
    pygame.draw.rect(win, GREEN, dino)
    pygame.draw.polygon(win, RED, [(cactus.x, cactus.y + cactus.height),(cactus.x + cactus.width // 2, cactus.y),(cactus.x + cactus.width, cactus.y + cactus.height)])
    #pygame.draw.rect(win, RED, cactus)
    if game_over:
        text=font.render("Game Over",True,BLACK)
        win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 30))
    pygame.display.update()            # Update screen
