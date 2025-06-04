import pygame
import sys
import random

pygame.init()
pygame.mixer.init()

background_image=pygame.image.load("asserts/background.jpg")
background_image=pygame.transform.scale(background_image,(1280,720))
WIDTH,HEIGHT=background_image.get_width(),background_image.get_height()
win=pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("Stage:9")

WHITE=(255,0,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLACK=(0,0,0)
ground_y=HEIGHT-245


font1=pygame.font.Font("asserts/pixelfont.ttf",70)
font2=pygame.font.Font("asserts/pixelfont.ttf",15)
stone_img=pygame.image.load("asserts/stone.png").convert_alpha()
stone_img=pygame.transform.scale(stone_img,(100,100))
running_img=[
    pygame.image.load("asserts/running1.png").convert_alpha(),
    pygame.image.load("asserts/running2.png").convert_alpha(),
    pygame.image.load("asserts/running3.png").convert_alpha(),
    pygame.image.load("asserts/running4.png").convert_alpha(),
    pygame.image.load("asserts/running5.png").convert_alpha(),
    pygame.image.load("asserts/running6.png").convert_alpha(),
    pygame.image.load("asserts/running7.png").convert_alpha(),
    pygame.image.load("asserts/running8.png").convert_alpha()
]

running_img=[pygame.transform.scale(frames,(150,150)) for frames in running_img]
current_frame=0
frame_delay=3
frame_counter=0


#creating a function to reset the game 
def reset_game():
    global game_over,dino,cactus,cactus_speed,velocity_y,is_jumping,score,max_speed,base_speed,distance
    dino=pygame.Rect(50,ground_y,60,100)
    #dino=dino.inflate(-10,-10)
    cactus=pygame.Rect(WIDTH +100,ground_y+70,60,100)
    #cactus=cactus.inflate(-10,-10)

    cactus_speed=5
    base_speed=7
    max_speed=25
    game_over = False
    velocity_y = 0
    score=0
    distance=0
    is_jumping = False

reset_game()
clock=pygame.time.Clock()
gravity=1
#background image 
bg_x=0
bg_speed=2

jump_sound=pygame.mixer.Sound("asserts/jump2.wav")
gameover_sound=pygame.mixer.Sound("asserts/gameover.wav")
speed_up_sound=pygame.mixer.Sound("asserts/speedup.mp3")
speed_up_played=False
running = True
gameoversound=False
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    keys = pygame.key.get_pressed()
    if game_over:
        if not gameoversound:
            gameover_sound.play()
            pygame.mixer.music.stop()
            gameoversound=True
        if (keys[pygame.K_r]):
            gameoversound=False
            reset_game()
# assigning keys to do some function like move right left up and down 
    if not game_over:

        frame_counter+=1
        if frame_counter>=frame_delay:
            frame_counter=0
            current_frame=(current_frame+1)% len(running_img)

        bg_x=bg_x-bg_speed
        if bg_x <= -background_image.get_width():
            bg_x=0
    
        
        #intiating the jump
        distance+=1
        if distance%400==0 and distance != 0 and not speed_up_played:
            speed_up_sound.play()
            speed_up_played=True
        elif distance % 400 !=0:
            speed_up_played=False
        
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and not is_jumping:
            velocity_y=-15
            is_jumping=True
            jump_sound.play()
        
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
        cactus_speed=base_speed+(distance//150)
        cactus.x-=cactus_speed

        if cactus.right<0:
            cactus.x=WIDTH+100
            score+=1
            cactus_speed=random.randint(5,15)
        if dino.colliderect(cactus):
            game_over=True

    win.fill(WHITE)                     # Clear screen
    win.blit(background_image ,(bg_x,0))
    win.blit(background_image ,(bg_x+background_image.get_width(),0))
    #pygame.draw.rect(win, GREEN, dino)
    win.blit(running_img[current_frame],(dino.x,dino.y))
    #pygame.draw.polygon(win, RED, [(cactus.x, cactus.y + cactus.height),(cactus.x + cactus.width // 2, cactus.y),(cactus.x + cactus.width, cactus.y + cactus.height)])
    #pygame.draw.rect(win, RED, cactus)
    win.blit(stone_img,(cactus.x,cactus.y))

    if game_over:
        text=font1.render("Game Over",True,BLACK)
        text1=font2.render("press 'r' to restart game",True,BLACK)
        win.blit(text1, (WIDTH / 2 - text1.get_width() / 2, HEIGHT / 3 - 30))
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 4.5 - 30))
    score_text=font2.render(f"Score:{int(score)} Distance:{int(distance)}",True,BLACK)
    win.blit(score_text,(10,10))
    pygame.display.update()            # Update screen
